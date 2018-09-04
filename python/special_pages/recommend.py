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

RECOMMEND_FILE_PATH_PREFIX = 'recommend'
RECOMMEND_JSON_FILE_PATH = os.path.join(const.PUBLIC_PATH, 'recommend.json')



def generate_recommend_page():
    with open(RECOMMEND_JSON_FILE_PATH, 'r', encoding='utf-8') as fd:
        posts = json.load(fd)['posts']
    tag_info_arr, tag_posts_arr = special_pages.util.generate_tag_data(posts)

    h1 = Html.generate_element_by_str('h1', '推荐')
    tag_ul = special_pages.util.generate_tag_ul(tag_info_arr)
    tag_contents_ul = special_pages.util.generate_tag_contents_ul(tag_posts_arr)
    main_content = ' '.join([h1, tag_ul, tag_contents_ul])
    conf_file_path = os.path.join(const.SPECAIL_PAGES_DIR_PATH,
                                  RECOMMEND_FILE_PATH_PREFIX + '.conf')
    with open(conf_file_path, 'r', encoding='utf-8') as fd:
        page_conf = json.load(fd)
    return Page.generate_complete_html(page_conf, main_content)


def generate_recommend_page_file():
    html_file_path = os.path.join(const.PUBLIC_PATH,
                                  RECOMMEND_FILE_PATH_PREFIX + '.html')
    with open(html_file_path, 'w+', encoding='utf-8') as fd:
        html_str = generate_recommend_page()
        fd.write(html_str)
    print("生成 %s 成功：%s" % (RECOMMEND_FILE_PATH_PREFIX, html_file_path))


if __name__ == "__main__":
    generate_recommend_page_file()
