#!/usr/bin/python3

import markdown
import json
import os
import time
from blog.config import CONF_PREFIX_PATH,STATIC_MD_PREFIX_PATH


# markdown字符转html
def md2html(str):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']
    return markdown.markdown(str,extensions=exts)


# 生成header
def generate_header(conf):
    html='''
    <div id="header">
        <button id='switch_btn'></button>
        <a href="%s" title="%s">
            <img src="%s"/>
        </a>
        <h1>%s</h1>
    </div>
    '''
    return html %(conf['link'],conf['icon_alt'],conf['icon_url'],conf['name'])


# 生成profle
def generate_profile(conf):
    html='''
    <a href="%s" title="%s">
        <img src="%s" alt="%s"/>
    </a>
    <span>%s</sapn>
    '''

    return html %(conf['link'],conf['link_title'],conf['icon_url'],conf['link_title'],conf['name'])


# 生成行级导航连接的li
def generate_row_links_li(conf):
    html='''
    <li>
        <a href="%s" title="%s">
            <img src="%s"/>
            <span>%s</span>
        </a>
    </li>
    '''

    return html %(conf['link'],conf['name'],conf['icon_url'],conf['name'])


# 生成行级导航连接
def generate_row_links(conf):
    str=''
    for x in conf:
        str+=generate_row_links_li(x)

    return str


# 生成列级导航连接的li
def generate_col_links_li(conf):
    html='''
    <li>
        <a href="%s" title="%s">
            <img src="%s"/>
        </a>
    </li>
    '''

    return html %(conf['link'],conf['name'],conf['icon_url'])


# 生成列级导航连接
def generate_col_links(conf):
    str=''
    for x in conf:
        str+=generate_col_links_li(x)
    
    return str


# 生成sidebar
def generate_sidebar(conf):
    profile=generate_profile(conf['profile'])
    row_links=generate_row_links(conf['row_links'])
    col_links=generate_col_links(conf['col_links'])
    
    html='''
    <nav id="sidebar">
        <div id="profile">
            %s
        </div>

        <ul id="row_links">
            %s
        </ul>

        <ul id="col_links">
            %s
        </ul>
    </nav>
    '''
    return html %(profile,row_links,col_links)


# 生成css
def generate_css(link):
    html='''
    <link rel="stylesheet" type="text/css" href="%s">
    '''

    return html %(link)


# 生成js
def generate_js(link):
    html='''
    <script src="%s"></script>
    '''
    
    return html %(link)


# 生成head
def generate_head(title,key_words,css_arr,js_arr):
    css_str=''
    for css in css_arr:
        css_str+=generate_css(css)
    
    js_str=''
    for js in js_arr:
        js_str+=generate_js(js)
    
    html='''
    <html>
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
    '''
    return html %(title,key_words,key_words,css_str,js_str)


# 生成main
def generate_main(content):
    html='''
    <div id="main">
		<div id="content" class="md">
			%s
		</div>
    '''
    return html %(content)


# 生成footer
def generate_footer(footer_html,css_arr,js_arr):
    css_str=''
    for css in css_arr:
        css_str+=generate_css(css)
    
    js_str=''
    for js in js_arr:
        js_str+=generate_js(js)

    html='''
            <footer>
                %s
            </footer>
        </div>
        %s
        %s
    </body>
    </html>
    '''
    return html %(footer_html,css_str,js_str)


# 生成完整的html
def generate_complete_html(page_conf,main_str=''):
    with open(os.path.join(CONF_PREFIX_PATH,'global.conf'),'r',encoding='utf-8') as fd:
        global_conf=json.load(fd)
    
    start_css_arr=global_conf['start_css_arr']+page_conf['start_css_arr']
    start_js_arr=global_conf['start_js_arr']+page_conf['start_js_arr']
    end_css_arr=global_conf['end_css_arr']+page_conf['end_css_arr']
    end_js_arr=global_conf['end_js_arr']+page_conf['end_js_arr']

    head=generate_head(page_conf['title'],page_conf['key_words'],start_css_arr,start_js_arr)
    with open(os.path.join(CONF_PREFIX_PATH,'header.conf'),'r',encoding='utf-8') as fd:
        conf=json.load(fd)
        header=generate_header(conf)

    with open(os.path.join(CONF_PREFIX_PATH,'sidebar.conf'),'r',encoding='utf-8') as fd:
        conf=json.load(fd)
        sidebar=generate_sidebar(conf)

    main=generate_main(main_str)

    footer=generate_footer(global_conf['footer'],end_css_arr,end_js_arr)
    return '%s %s %s %s %s' %(head,header,sidebar,main,footer)


def generate_li(str):
    return '''
    <li>
        %s
    </li>
    ''' %(str)


def generate_ul(li_arr,id=''):
    str=''
    for li in li_arr:
        str+=li
    
    if id=='':
        id_str=''
    else:
        id_str=" id='%s'" %(id)
    return '''
    <ul%s>
        %s
    </ul>
    ''' %(id_str,str)

# 根据tag数组生成ul
def generate_tag_ul(tag_info_arr):
    li_arr=[]
    for tag_info in tag_info_arr:
        li_content='''
        <button>%s(%s)</button>
        '''% (tag_info['name'],tag_info['count'])
        li_arr.append(generate_li(li_content))

    return generate_ul(li_arr,'tags_ul')


def get_dir_latest_file_mtime(dir_name,*ignore_name_arr):
    max_time = 0
    for item in os.listdir(dir_name):
        ignore=False
        for ignore_name in ignore_name_arr:
            if ignore_name==item:
                ignore=True
        if not ignore:
            file_path=os.path.join(dir_name,item)
            mtime=os.path.getmtime(file_path)
            if mtime > max_time:
                max_time=mtime
    return max_time
    
        
