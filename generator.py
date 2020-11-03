# coding: utf-8
import os
import sys
from utils.func import md_to_html, index_builder

get_MD = sys.argv[1]
give_HTML = sys.argv[2]

if not os.path.exists(give_HTML):
    os.makedirs(give_HTML)

list_files_MD = os.listdir(get_MD)

list_files_MD = [md_to_html(get_MD, n, give_HTML) for n in list_files_MD if n.endswith(".md")]

index_builder()



