from django.shortcuts import render

from . import util

from markdown2 import Markdown

import random


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def convert_md_to_html(page_title):
    md_content = util.get_entry(page_title)
    markdowner = Markdown()
    if md_content is None:
        return None
    else:
        return markdowner.convert(md_content)


def entry(request, title):
    url_etry = convert_md_to_html(title)
    if url_etry is None:
        return render(
            request, "encyclopedia/error.html", {"message": "Entry does not exist"}
        )
    else:
        return render(
            request,
            "encyclopedia/entry.html",
            {"title": title, "content": url_etry}
        )

def search(request):
    if request.method == "POST":
        page_title = request.POST['q']
        page_body = convert_md_to_html(page_title)
        if page_body is not None:
            return render(request, "encyclopedia/entry.html", {
                "page_title": page_title,
                "page_body": page_body
            })
        else:
            allEntries = util.list_entries()
            recommendetion = []
            for entry in allEntries:
                if page_title.lower() in entry.lower():
                    recommendetion.append(entry)
            if recommendetion:
                return render(request, "encyclopedia/search.html",{
                   "recommendation": recommendetion
                })
        
            return render(request, "encyclopedia/error.html", {
                "message": "No entries with this name!"
            })
    
def new_page(request):
     if request.method == "GET":
        return render(request, "encyclopedia/new.html")
     else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Page already exist"
            })
        else:
            util.save_entry(title, content)
            html_content = convert_md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
               "title": title,
               "content": html_content
            })

def edit(request):
    if request.method == 'POST':
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })
    
def save_edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
               "title": title,
               "content": html_content
            })
    
def random_btn(request):
    allEntries = util.list_entries()
    random_entry = random.choice(allEntries)
    html_content = convert_md_to_html(random_entry)
    return render(request, "encyclopedia/entry.html", {
               "title": random_entry,
               "content": html_content
            })