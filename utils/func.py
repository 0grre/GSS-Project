# coding: utf-8

import markdown2

def md_to_html(get_MD, n, give_HTML):

    f = open(get_MD + "/" + n, "r")
    page_rendered = markdown2.markdown(f.read())
    n = n[:-3]
    page_rendered_file = open(give_HTML + "/" + n + ".html", "w")
    head = """<!doctype html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link href="./assets/css/style.css" rel="stylesheet" media="all" type="text/css"> 
        <title>""" + n + """</title>
    </head>
    <body>"""
    footer = """</body>
    </html>"""
    page_rendered_file.write(head+page_rendered+footer)
    page_rendered_file.close()
