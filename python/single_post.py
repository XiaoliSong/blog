#!/usr/bin/python3
from os import path
import json
import sys
import time
from blog.helper import generate_main,generate_complete_html,md2html
from blog.config import POST_PREFIX_PAHT,POST_CONF_NAME,POST_MD_NAME
from blog.helper import generate_li,generate_ul,generate_tag_ul,get_dir_latest_file_mtime

def generate_post_end(tags):
    str=''
    for tag in tags:
        tag_str='''
        <a href="/tag.html?tag=%s">#%s</a>
        ''' %(tag,tag)
        str+=tag_str

    html='''
    <div class="post_end">
		--END--
		<div class="post_tags">
			标签：
			%s
		</div>
	</div>
    '''
    return html %(str)


def generate_post_main(title,date,id,text,tags):
    post_end=generate_post_end(tags)
    return'''
    <article class='post'>
        <div class='post_meta'>
            <div class='post_meta_date'>%s</div>
            <div class='post_commet_cnt'><a href="#SOHUCS"><span id="sourceId::%s" class="cy_cmt_count"></span><span> 评论</span></a></div>
        </div>
        <h1><a>%s</a></h1>
        %s
    </article>
    %s
    <div id="SOHUCS" sid="%s" ></div>
    <script id="cy_cmt_num" src="https://changyan.sohu.com/upload/plugins/plugins.list.count.js?clientId=cytyIIWkH"></script>
    ''' %(date,id,title,text,post_end,id)


def generate_single_post(post_link_name):
    dir_name=path.join(POST_PREFIX_PAHT,post_link_name)
    conf_file_name=path.join(dir_name,POST_CONF_NAME)
    with open(conf_file_name,'r',encoding='utf-8') as fd:
        post_conf=json.load(fd)
        md_file_name=path.join(dir_name,POST_MD_NAME)
        with open(md_file_name,'r',encoding='utf-8') as fd:
            text=md2html(fd.read())
            t=get_dir_latest_file_mtime(dir_name,'index.html')
            date=time.strftime('%Y-%m-%d',time.localtime(t))
            main=generate_post_main(post_conf['title'],date,post_link_name,text,post_conf['tags'])
            html_file_name=path.join(dir_name,'index.html')
            with open(html_file_name,'w+',encoding='utf-8') as fd:
                html=generate_complete_html(post_conf,main)
                print('生成成功，输出文件：'+html_file_name)
                fd.write(html)

if __name__=="__main__":
    if(len(sys.argv)!=2):
        print('参数错误，参数如下：')
        print('post目录名')
        exit()
    
    post_link_name=sys.argv[1]
    generate_single_post(post_link_name)

