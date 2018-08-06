#!/usr/bin/python3
from os import path
import json
import sys
from blog.helper import generate_main,generate_complete_html
from blog.config import CONF_PREFIX_PATH,STATIC_MD_PREFIX_PATH
from blog.helper import generate_li,generate_ul,generate_tag_ul


# 根据tag内容数组生成ul
def generate_tag_contents_ul(tag_posts_arr):
    li_arr=[]
    for tag_posts in tag_posts_arr:
        sub_li_arr=[]
        tag=tag_posts['name']
        posts=tag_posts['posts']
        for post in posts:
            sub_li_content='''
            <a href="%s" title="%s">%s</a>
            ''' %(post['link'],post['title'],post['title'])
            sub_li_arr.append(generate_li(sub_li_content))

        sub_ul=generate_ul(sub_li_arr)
        li_content='''
        <h2>%s</h2>
        %s
        ''' %(tag,sub_ul)
        li_arr.append(generate_li(li_content)) 
    return generate_ul(li_arr,'tag_contents_ul')


def generate_recommend_content_main(json_data):
    tag_arr=[]
    tag_posts={}
    for post in json_data['posts']:
        for tag in post['tags']:
            if tag not in tag_arr:
                tag_arr.append(tag)
            if tag not in tag_posts:
                tag_posts[tag]=[post]
            else:
                tag_posts[tag].append(post)

    tag_info_arr=[]
    tag_posts_arr=[]        
    for tag in tag_arr:
        tag_info_arr.append({
            'name':tag,
            'count':len(tag_posts[tag])
        })
        tag_posts_arr.append({
            'name':tag,
            'posts':tag_posts[tag]
        })

    tag_ul_html=generate_tag_ul(tag_info_arr)
    tag_contents_ul_html=generate_tag_contents_ul(tag_posts_arr)
    return '''
    <h1>推荐</h1>
    %s
    %s
    ''' %(tag_ul_html,tag_contents_ul_html)


if __name__=="__main__":
    name='recommend'
    with open(path.join(STATIC_MD_PREFIX_PATH,name+'.json'),'r',encoding='utf-8') as fd:
        json_data=json.load(fd)
        main=generate_recommend_content_main(json_data)
        with open(path.join(CONF_PREFIX_PATH,name+'.conf'),'r',encoding='utf-8') as fd:
            page_conf=json.load(fd)
            html=generate_complete_html(page_conf,main)
            with open(path.join(STATIC_MD_PREFIX_PATH,name+'.html'),'w+',encoding='utf-8') as fd:
                print('生成成功，输出文件：'+path.join(STATIC_MD_PREFIX_PATH,name+'.html'))
                fd.write(html)
