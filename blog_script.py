# /usr/bin/python3
import os
import sys
import platform

if(platform.system() =="Windows"):
    SCRIPT_PREFIX = 'python ./python/'
else:
    SCRIPT_PREFIX = 'python3 ./python/'

def exec_recomend():
    os.system(SCRIPT_PREFIX + 'special_pages/recommend.py')


def exec_archive():
    os.system(SCRIPT_PREFIX + 'special_pages/archive.py')


def exec_tag():
    os.system(SCRIPT_PREFIX + 'special_pages/tag.py')


def exec_page():
    os.system(SCRIPT_PREFIX + 'page.py')


def exec_general_pages():
    os.system(SCRIPT_PREFIX + 'general_pages.py')


def exec_rss():
    os.system(SCRIPT_PREFIX + 'rss.py')


def exec_sitemap():
    os.system(SCRIPT_PREFIX + 'sitemap.py')

def exec_incremental_posts():
    os.system(SCRIPT_PREFIX + 'posts.py')
    os.system(SCRIPT_PREFIX + 'post_json.py')
    exec_archive()
    exec_tag()
    exec_page()
    exec_rss()
    exec_sitemap()

def exec_all_posts():
    os.system(SCRIPT_PREFIX + 'posts.py -all')
    os.system(SCRIPT_PREFIX + 'post_json.py')
    exec_archive()
    exec_tag()
    exec_page()
    exec_rss()
    exec_sitemap()


def exec_dir_posts(dir_name, post_name = None):
    if post_name is None:
        os.system(SCRIPT_PREFIX + 'dir_posts.py ' + dir_name)
    else:
        os.system(SCRIPT_PREFIX + 'dir_posts.py '+ dir_name + ' ' + post_name)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'recommend':
            exec_recomend()
        elif sys.argv[1] == 'post':
            if len(sys.argv) >= 3 and sys.argv[2] == '-all':
                exec_all_posts()
            else:
                exec_incremental_posts()
        elif sys.argv[1] == 'general':
            exec_general_pages()
        else:
            dir_name = sys.argv[1]
            if len(sys.argv) == 2:
                exec_dir_posts(dir_name)
            else:
                post_name = sys.argv[2]
                exec_dir_posts(dir_name, post_name)
    else:
        print('参数个数不够')