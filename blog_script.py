# /usr/bin/python3
import os
import sys


SCRIPT_PREFIX = 'python ./python/'


def exec_recomend():
    os.system(SCRIPT_PREFIX + 'special_pages/recommend.py')

def exec_archive():
    os.system(SCRIPT_PREFIX + 'special_pages/archive.py')

def exec_tag():
    os.system(SCRIPT_PREFIX + 'special_pages/tag.py')

def exec_page():
    os.system(SCRIPT_PREFIX + 'page.py')

def exec_rss():
    os.system(SCRIPT_PREFIX + 'rss.py')

def exec_sitemap():
    os.system(SCRIPT_PREFIX + 'sitemap.py')


def exec_al_posts():
    os.system(SCRIPT_PREFIX + 'posts.py')
    os.system(SCRIPT_PREFIX + 'post_json.py')
    exec_archive()
    exec_tag()
    exec_page()
    exec_rss()
    exec_sitemap()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1]=='recommend':
            exec_recomend()
        elif sys.argv[1]=='post':
            exec_al_posts()
        else:
            print('参数错误')
    else:
        print('参数个数不够')