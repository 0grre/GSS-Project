import datetime
import os

from Class.Author import Author
from Class.Index import Index
from yattag import Doc, indent
from json import load

with open('config.json', 'r') as config_file:
    config = load(config_file)

author = Author(config.get('name'), config.get('mail'), config.get('phone'), config.get('avatar'))
index = Index(config.get('charset'), config.get('lang'), config.get('description'), config.get('title'))
d = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")


def head_builder(i):
    doc, tag, text = Doc().tagtext()
    doc.asis('<!DOCTYPE html>')
    doc.asis('<html>')
    with tag('head'):
        doc.stag('meta', charset=index.charset)
        doc.stag('meta', lang=index.lang)
        doc.stag('meta', name="description", content=index.description)
        with tag('script', src="https://kit.fontawesome.com/d4acc78081.js", crossorigin="anonymous"):
            text("")
        with tag('title'):
            text(index.title)
        doc.stag('link', rel="icon", href="favicon.ico")
        for stylesheet in config.get('stylesheets'):
            if i != 1:
                doc.stag('link', rel="stylesheet", href="../" + stylesheet, media="all", type="text/css")
            else:
                doc.stag('link', rel="stylesheet", href=stylesheet, media="all", type="text/css")
    doc.asis('<body>')

    return indent(doc.getvalue())


def header_builder(i):
    doc, tag, text = Doc().tagtext()
    with tag('header'):
        with tag('div', id="header-filter"):
            text("")
        with tag('div', id="header-picture"):
            if i != 1:
                doc.stag('img', id="picture", src="../" + author.avatar)
            else:
                doc.stag('img', id="picture", src=author.avatar)
            with tag('h1', id="name"):
                text(author.name)
            with tag('h1', id="title"):
                text(index.title)
    return indent(doc.getvalue())


def container_start():
    doc, tag, text = Doc().tagtext()
    doc.asis('<div class=container>')
    doc.asis('<div class=article>')

    return indent(doc.getvalue())


def container_end():
    doc, tag, text = Doc().tagtext()

    with tag('div', klass="end"):
        with tag('h4'):
            text("Auteur : " + author.name)
        with tag('h5'):
            text("Mis en ligne le : " + d)
    doc.asis('</div>')
    with tag('a', href="../index.html"):
        with tag('button'):
            text('HOME')
    doc.asis('</div>')
    return indent(doc.getvalue())


def links_builder():
    list_articles = os.listdir('articles')
    doc, tag, text = Doc().tagtext()
    with tag('h1'):
        text("Liste des articles")
    with tag('div', klass="container"):
        with tag('div', klass="list"):
            for article in list_articles:
                with tag('a', href="articles/"+article):
                    title = article[:-5]
                    text(title)

    return indent(doc.getvalue())


def footer_builder(i):
    doc, tag, text = Doc().tagtext()
    with tag('footer'):
        with tag('ul'):
            for icon, url in config.get('links').items():
                if url != "":
                    with tag('a', href=url):
                        with tag('i', klass="fab fa-" + icon):
                            text("")
    for script in config.get("scripts"):
        if i != 1:
            with tag('script', src="../" + script):
                text("")
        else:
            with tag('script', src=script):
                text("")

    doc.asis('</body>')
    doc.asis('</html>')
    return indent(doc.getvalue())
