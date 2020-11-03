import markdown2
from utils.html_block import head_builder, footer_builder, container_start, container_end, header_builder, links_builder


def md_to_html(get_MD, n, give_HTML):
    i = 0
    f = open(get_MD + "/" + n, "r")
    page_rendered = markdown2.markdown(f.read())
    n = n[:-3]
    page_rendered_file = open(give_HTML + "/" + n + ".html", "w")

    head = head_builder(i)
    header = header_builder(i)
    article_start = container_start()
    article_end = container_end()
    footer = footer_builder()

    page_rendered_file.write(head + header + article_start + page_rendered + article_end + footer)
    page_rendered_file.close()


def index_builder():
    i = 1
    index_file = open('index.html', 'w')

    head = head_builder(i)
    header = header_builder(i)
    links = links_builder()
    footer = footer_builder()

    index_file.write(head + header + links + footer)
    index_file.close()
