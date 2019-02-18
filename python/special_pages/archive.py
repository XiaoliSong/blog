if __name__ == "__main__":
    import sys
    import os
    sys.path.append(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import json
import os
import blog.util
from blog.html import Html
from blog import const
from blog.page import Page
import special_pages.util

ARCHIVE_FILE_PATH_PREFIX = 'archive'


def generate_archive_data():
    with open(const.POST_JSON_FILE_PATH, 'r', encoding='utf-8') as fd:
        posts = json.load(fd)['posts']

    tag_arr = []
    tag_posts = {}
    for post in posts:
        date = post['create_datetime'][0:post['create_datetime'].index(' ')]
        tag = date[0:date.rfind('-')].replace('-', '年') + '月'
        if tag not in tag_arr:
            tag_arr.append(tag)
        if tag not in tag_posts:
            tag_posts[tag] = [post]
        else:
            tag_posts[tag].append(post)
    tag_posts_arr = []
    for tag in tag_arr:
        tag_posts_arr.append({
            'name': tag, 
            'posts': tag_posts[tag]
        })
    return tag_posts_arr


def generate_archive_page():
    h1 = Html.generate_element_by_str('h1', '归档')
    tag_posts_arr = generate_archive_data()
    tag_contents_ul = special_pages.util.generate_tag_contents_ul(
        tag_posts_arr)
    main_content = ' '.join([h1, tag_contents_ul])
    conf_file_path = os.path.join(const.SPECAIL_PAGES_DIR_PATH,
                                  ARCHIVE_FILE_PATH_PREFIX + '.conf')
    with open(conf_file_path, 'r', encoding='utf-8') as fd:
        page_conf = json.load(fd)
    return Page.generate_complete_html(page_conf, main_content)


def generate_archive_page_file():
    html_file_path = os.path.join(const.PUBLIC_PATH,
                                  ARCHIVE_FILE_PATH_PREFIX + '.html')
    with open(html_file_path, 'w+', encoding='utf-8') as fd:
        html_str = generate_archive_page()
        fd.write(html_str)
    print("生成 %s 成功：%s" % (ARCHIVE_FILE_PATH_PREFIX, html_file_path))


if __name__ == "__main__":
    generate_archive_page_file()
