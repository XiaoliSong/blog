#!/usr/bin/python3
import os
import json
from blog.html import Html
from blog import util
from blog.post import generate_post_article
from blog.page import Page
from blog import const

PAGE_DIR_NAME = 'page'


def generate_post_item(info):
    date = util.datetime2date(info['create_datetime'])
    preface_file_name = os.path.join(const.POST_DIR_PATH, info['id'],
                                     const.POST_PREFACE_FILE_PATH)
    with open(preface_file_name, 'r', encoding='utf-8') as fd:
        text = Html.from_markdown_str(fd.read())
    return generate_post_article(info['title'], date, info['id'], text)


def generate_page_pagination(index, has_former, has_next):
    if has_former:
        href = const.ROOT_URL_PREFIX + PAGE_DIR_NAME + '/' + str(index -
                                                                 1) + '.html'
        former_a = Html.generate_element_by_str(
            'a', '<-上一页', href=href, class_name='former_link', title='<-上一页')
    else:
        former_a = Html.generate_element_by_str(
            'a', href='#', class_name='former_link', visibility='hiddern')

    if has_next:
        href = const.ROOT_URL_PREFIX + PAGE_DIR_NAME + '/' + str(index +
                                                                 1) + '.html'
        next_a = Html.generate_element_by_str(
            'a', '下一页->', href=href, class_name='former_link', title='下一页->')
    else:
        next_a = Html.generate_element_by_str(
            'a', href='#', class_name='next_link', visibility='hiddern')

    middle_a = Html.generate_element_by_str(
        'a', '-归档-', href='/archive.html', class_name='center_link')
    return Html.generate_element_by_strs(
        'nav', [former_a, next_a, middle_a], class_name='pagination')


def generate_page_file(post_arr, index, has_former, has_next):
    post_li_arr = []
    for post in post_arr:
        post_item = generate_post_item(post)
        li = Html.generate_element_by_str('li', post_item)
        post_li_arr.append(li)
    if len(post_li_arr) == 0:
        post_catlog = Html.generate_element_by_str(
            'ul', '当前暂无帖子', class_name='post_catlog')
    else:
        post_catlog = Html.generate_element_by_strs(
            'ul', post_li_arr, class_name='post_catlog')

    pagination = generate_page_pagination(index, has_former, has_next)
    main_html = ' '.join([post_catlog, pagination])

    page_conf = {
        "start_css_arr": [
            "https://blog-1252791686.cos.ap-beijing.myqcloud.com/css/article.css",
            "https://blog-1252791686.cos.ap-beijing.myqcloud.com/css/page.css"
        ],
        "description":
        "导航页, 第%d页" % (index)
    }
    page_file_name = os.path.join(const.PUBLIC_PATH, PAGE_DIR_NAME,
                                  str(index) + '.html')
    with open(page_file_name, 'w+', encoding='utf-8') as fd:
        html = Page.generate_complete_html(page_conf, main_html)
        fd.write(html)
        print("生成 page 成功，页号：%d" % (index))

    # 生成首页
    if index == 0:
        file_name = os.path.join(const.PUBLIC_PATH, 'index.html')
        with open(file_name, 'w+', encoding='utf-8') as fd:
            html = Page.generate_complete_html(page_conf, main_html)
            fd.write(html)
            print("生成 首页 成功")


def generate_all_pages_file():
    with open(const.POST_JSON_FILE_PATH, 'r', encoding='utf-8') as fd:
        posts = json.load(fd)['posts']
        posts_cnt = len(posts)
        if posts_cnt == 0:
            generate_page_file([], 0, False, False)
        else:
            left = 0
            index = 0
            while left < posts_cnt:
                if left == 0:
                    has_former = False
                else:
                    has_former = True
                right = left+ const.POST_CNT_PER_PAGE
                if (right < posts_cnt):
                    has_next = True
                else:
                    has_next = False
                generate_page_file(
                    posts[left:right], index,
                    has_former, has_next)
                left += const.POST_CNT_PER_PAGE
                index += 1
    print("生成 全部page导航页面 成功")


if __name__ == "__main__":
    generate_all_pages_file()