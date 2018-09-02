import os
import json
from blog.html import Html
from blog import const
from blog import util
from blog.page import Page


def generate_post_end(tags):
    tag_a_arr = []
    for tag in tags:
        a_href = '/tag.html?tag=' + tag
        a_content = '#' + tag
        a = Html.generate_element_by_str(
            'a', a_content, href=a_href, title=tag)
        tag_a_arr.append(a)
    tag_str = ' '.join(tag_a_arr)
    post_tags = Html.generate_element_by_str(
        'div', '标签：' + tag_str, class_name='post_tags')

    return Html.generate_element_by_str(
        'div', '<br />--END--<br />' + post_tags, class_name='post_end')


def generate_post_meta(date, id):
    post_meta_date = Html.generate_element_by_str(
        'div', date, class_name='post_meta_date')
    post_commet_cnt_a_span1 = Html.generate_element_by_str(
        'span', id="sourceId::" + id, class_name="cy_cmt_count")
    post_commet_cnt_a_span2 = Html.generate_element_by_str('span', ' 评论')
    post_commet_cnt_a = Html.generate_element_by_strs(
        'a', [post_commet_cnt_a_span1, post_commet_cnt_a_span2],
        href="#SOHUCS")
    post_commet_cnt = Html.generate_element_by_str(
        'div', post_commet_cnt_a, class_name='post_commet_cnt')
    return Html.generate_element_by_strs(
        'div', [post_meta_date, post_commet_cnt], class_name='post_meta')


def generate_post_article(title, date, id, text):
    post_meta = generate_post_meta(date, id)
    h1_a = Html.generate_element_by_str('a', title, href='#', title=title)
    h1 = Html.generate_element_by_str('h1', h1_a)
    return Html.generate_element_by_strs(
        'article', [post_meta, h1, text], class_name='post')

def generate_post_main(title, date, id, text, tags):
    article = generate_post_article(title, date, id, text)
    post_end = generate_post_end(tags)

    sohucs = Html.generate_element_by_str('div', id="SOHUCS", sid=id)
    sohucs_script = util.get_sohucs_comment_cnt_js()
    main_arr = [article, post_end, sohucs, sohucs_script]
    return ' '.join(main_arr)


def generate_post(post_id):
    post_dir_name = os.path.join(const.POST_DIR_PATH, post_id)
    conf_file_name = os.path.join(post_dir_name, const.POST_CONF_FILE_PATH)
    with open(conf_file_name, 'r', encoding='utf-8') as fd:
        post_conf = json.load(fd)
        md_file_name = os.path.join(post_dir_name, const.POST_MD_FILE_PATH)
        with open(md_file_name, 'r', encoding='utf-8') as fd:
            text = Html.from_markdown_str(fd.read())
            date = util.get_post_date(post_id)
            main = generate_post_main(post_conf['title'], date, post_id, text,
                                      post_conf['tags'])
            return Page.generate_complete_html(post_conf, main)


def generate_post_file(post_id):
    post_dir_name = os.path.join(const.POST_DIR_PATH, post_id)
    html_file_name = os.path.join(post_dir_name, 'index.html')
    with open(html_file_name, 'w+', encoding='utf-8') as fd:
        fd.write(generate_post(post_id))
    print("生成帖子 %s  成功：%s" % (post_id, html_file_name))


def generate_all_posts_file():
    cnt = 0
    for dir_name in os.listdir(const.POST_DIR_PATH):
        post_id = os.path.join(const.POST_DIR_PATH, dir_name)
        if (os.path.isdir(post_id)):
            generate_post_file(post_id)
            cnt += 1
    print("生成全部帖子成功，共：" + str(cnt) + "个")
