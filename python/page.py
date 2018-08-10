#!/usr/bin/python3
import os
import json

from blog.helper import generate_main,generate_complete_html,md2html,generate_li
from blog.config import POST_JSON_PATH,POST_CNT_PER_PAGE,POST_PREFACE_NAME,PAGE_PREFIX_PAHT,POST_PREFIX_PAHT,CONF_PREFIX_PATH,ROOT_PATH


def generate_post_preface(info):
    preface_file_name=os.path.join(POST_PREFIX_PAHT,info['id'],POST_PREFACE_NAME)
    with open(preface_file_name,'r',encoding='utf-8') as fd:
        main=md2html(fd.read())
    date=info['datetime'][0:info['datetime'].index(' ')]
    html='''
    <article class='post'>
        <div class='post_meta'>
            <div class='post_meta_date'>%s</div>
            <div class='post_commet_cnt'><a href="%s#SOHUCS"><span id="sourceId::%s" class="cy_cmt_count"></span><span> 评论</span></a></div>
        </div>
        <h1><a href="%s" title="%s">%s</a></h1>
        %s
    </article>
    '''
    return html %(date,info['link'],info['id'],info['link'],info['title'],info['title'],main)


def generate_page(post_arr,index,has_former,has_next):
    html_str=''
    for post in post_arr:
        html_str+=generate_li(generate_post_preface(post))
    
    main='''
    <ul class="post_catlog">
    %s
    </ul>
    <script id="cy_cmt_num" src="https://changyan.sohu.com/upload/plugins/plugins.list.count.js?clientId=cytyIIWkH"></script>
    '''% (html_str)

    pagination_html='''
    <nav class="pagination">
    '''
    if has_former:
        pagination_html=pagination_html+'''
        <a href="/page/%d.html" class="former_link"><-上一页</a>
        '''% (index-1)
    else:
        pagination_html=pagination_html+'''
        <a href="#" class="former_link" visibility="hiddern"></a>
        '''
    if has_next:
        pagination_html=pagination_html+'''
        <a href="/page/%d.html" class="next_link">下一页-></a>
        '''% (index+1)
    else:
        pagination_html=pagination_html+'''
        <a href="#" class="next_link" visibility="hiddern"></a>
        '''
    pagination_html=pagination_html+'''
        <a href='/archive.html' class='center_link'>-归档-</a>
    </nav>
    '''
    main_html=main+pagination_html


    with open(os.path.join(CONF_PREFIX_PATH,'page.conf'),'r',encoding='utf-8') as fd:
        page_conf=json.load(fd)
        file_name=os.path.join(PAGE_PREFIX_PAHT,str(index)+'.html')
        with open(file_name,'w+',encoding='utf-8') as fd:
            html=generate_complete_html(page_conf,main_html)
            fd.write(html)
            print("生成page成功，页号：%d"%(index))
        
        # 生成首页
        if index==0:
            file_name=os.path.join(ROOT_PATH,'index.html')
            with open(file_name,'w+',encoding='utf-8') as fd:
                html=generate_complete_html(page_conf,main_html)
                fd.write(html)
                print("生成首页成功")
        


def generate_pages():
    with open(POST_JSON_PATH,'r',encoding='utf-8') as fd:
        posts=json.load(fd)['posts']
        posts_cnt=len(posts)
        cur_cnt=0
        index=0
        while cur_cnt<posts_cnt:
            if cur_cnt==0:
                has_former=False
            else:
                has_former=True
            cur_cnt+=POST_CNT_PER_PAGE
            if(cur_cnt<posts_cnt):
                has_next=True
            else:
                has_next=False
            generate_page(posts[(cur_cnt-POST_CNT_PER_PAGE):cur_cnt],index,has_former,has_next)
            index+=1
    print("生成全部page导航页面成功")


if __name__=="__main__":
    generate_pages()