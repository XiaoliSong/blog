#!/usr/bin/python3
from os import path
import json
import sys
from blog.helper import generate_main,generate_complete_html
from blog.config import CONF_PREFIX_PATH,STATIC_MD_PREFIX_PATH
from blog.helper import generate_li,generate_ul,generate_tag_ul


# 根据tag内容数组生成ul
def generate_tag_contents_ul(tag_contents):
    li_arr=[]
    for tag,info_arr in tag_contents.items():
        sub_li_arr=[]
        for info in info_arr:
            sub_li_content='''
            <a href="%s" title="%s">%s</a>
            ''' %(info['link'],info['name'],info['name'])
            sub_li_arr.append(generate_li(sub_li_content))

        sub_ul=generate_ul(sub_li_arr)

        li_content='''
        <h2>%s</h2>
        %s
        ''' %(tag,sub_ul)
        li_arr.append(generate_li(li_content))   
    return generate_ul(li_arr,'tag_contents_ul')


def generate_recommend_content_main(json_data):
    tags=[]
    tag_contents={}
    for link,detail in json_data.items():
        link_tags=detail['tags']
        info={
            'link':link,
            'name':detail['name']
        }
        for link_tag in link_tags:
            if link_tag not in tags:
                tags.append(link_tag)
            if link_tag not in tag_contents:
                tag_contents[link_tag]=[info]
            else:
                tag_contents[link_tag].append(info)
    tag_counts={}
    for tag in tags:
        tag_counts[tag]=len(tag_contents[tag])
    tag_ul_html=generate_tag_ul(tag_counts)
    tag_contents_ul_html=generate_tag_contents_ul(tag_contents)
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
