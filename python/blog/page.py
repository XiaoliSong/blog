import os
import json
from blog import const
from blog.component import Component
from blog.html import Html


class Page:
    @classmethod
    def __check_make_page_info(cls, page_info):
        if 'title' not in page_info:
            page_info['title'] = const.BLOG_NAME
        if 'key_words' not in page_info:
            page_info['key_words'] = const.BLOG_NAME
        if 'description' not in page_info:
            page_info['description'] = const.BLOG_DESCRIPTION
        if 'start_css_arr' not in page_info:
            page_info['start_css_arr'] = []
        if 'start_js_arr' not in page_info:
            page_info['start_js_arr'] = []
        if 'end_css_arr' not in page_info:
            page_info['end_css_arr'] = []
        if 'end_js_arr' not in page_info:
            page_info['end_js_arr'] = []
        return page_info

    @classmethod
    def __generate_head(cls, title, key_words, description, css_arr, js_arr):
        '''
        '''
        css_str = ''
        for css in css_arr:
            css_str += Html.generate_css(css)

        js_str = ''
        for js in js_arr:
            js_str += Html.generate_js(js)

        return '''<html>
            <head>
            <title>%s</title>
            <meta name="keywords" content="%s">
            <meta name="description" content="%s">
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1,maximum-scale=1,user-scalable=no">
            %s
            %s
            </head>
        <body>
        ''' % (title, key_words, description, css_str, js_str)

    @classmethod
    def __generate_main(cls, main_content):
        return '''
        <div id="main">
            <div id="content" class="md">
                %s
            </div>
        ''' % (main_content)

    # 生成footer
    @classmethod
    def __generate_footer(cls, footer_html, css_arr, js_arr):
        css_str = ''
        for css in css_arr:
            css_str += Html.generate_css(css)

        js_str = ''
        for js in js_arr:
            js_str += Html.generate_js(js)

        return '''
                <footer>
                    %s
                </footer>
            </div>
            %s
            %s
        </body>
        </html>
        ''' % (footer_html, css_str, js_str)

    @classmethod
    def generate_complete_html(cls, page_info, main_content=''):
        page_info = cls.__check_make_page_info(page_info)

        with open(const.GLOBAL_CONF_FILE_PATH, 'r', encoding='utf-8') as fd:
            global_conf = json.load(fd)

        start_css_arr = global_conf['start_css_arr'] + \
            page_info['start_css_arr']
        start_js_arr = global_conf['start_js_arr'] + page_info['start_js_arr']
        end_css_arr = global_conf['end_css_arr'] + page_info['end_css_arr']
        end_js_arr = global_conf['end_js_arr'] + page_info['end_js_arr']

        head = cls.__generate_head(page_info['title'], page_info['key_words'],
                                   page_info['description'], start_css_arr,
                                   start_js_arr)

        with open(const.HEADER_CONF_FILE_PATH, 'r', encoding='utf-8') as fd:
            conf = json.load(fd)
            header = Component.generate_header(conf)

        with open(const.SIDEBAR_CONF_FILE_PATH, 'r', encoding='utf-8') as fd:
            conf = json.load(fd)
            sidebar = Component.generate_sidebar(conf)

        main = cls.__generate_main(main_content)

        footer = cls.__generate_footer(global_conf['footer'], end_css_arr,
                                       end_js_arr)
        html_str = ' '.join([head, header, sidebar, main, footer])
        return Html.prettify(html_str)
