import os
import time
import json
from blog.config import ROOT_URL_PREFIX,ROOT_PATH,POST_JSON_PATH

URL_PREFIX="https://www.li1996.cn"
STATIC_HTML_ARR=[
    "40x.html",
    "50x.html",
    "about.html",
    "archive.html",
    "friends.html",
    "index.html",
    "recommend.html",
    "search.html",
    "tag.html",
    "works.html",
]

HTML_DIR_ARR=[
    "page"
]

def generate_url(loc,lastmod,changefreq,priority):
    return'''
    <url>
        <loc>%s</loc>
        <lastmod>%s</lastmod>
        <changefreq>%s</changefreq>
        <priority>%s</priority>
    </url>
''' %(loc,lastmod,changefreq,priority)


def generate_sitemap():
    urls_str=''
    for static_html in STATIC_HTML_ARR:
        file_path=os.path.join(ROOT_PATH,static_html)
        mtime=os.path.getmtime(file_path)
        lastmod=time.strftime('%Y-%m-%d',time.localtime(mtime))
        loc=ROOT_URL_PREFIX+'/'+static_html
        changefreq='hourly'
        priority='1.0'
        urls_str+=generate_url(loc,lastmod,changefreq,priority)
    
    for dir_name in HTML_DIR_ARR:
        real_dir=os.path.join(ROOT_PATH,dir_name)
        for item in os.listdir(real_dir):
            if item.endswith('.html'):
                file_path=os.path.join(real_dir,item)
                mtime=os.path.getmtime(file_path)
                lastmod=time.strftime('%Y-%m-%d',time.localtime(mtime))
                loc=ROOT_URL_PREFIX+'/'+dir_name+'/'+item
                changefreq='hourly'
                priority='0.9'
                urls_str+=generate_url(loc,lastmod,changefreq,priority)
    
    with open(POST_JSON_PATH,'r',encoding='utf-8') as fd:
        posts=json.load(fd)['posts']
        for post in posts:
            lastmod=post['datetime'][0:post['datetime'].index(' ')]
            loc=ROOT_URL_PREFIX+post['link']
            changefreq='daily'
            priority='0.9'
            urls_str+=generate_url(loc,lastmod,changefreq,priority)

    sitemap_str='''<?xml version="1.0" encoding="utf-8"?>
 <urlset xmlns="http://www.google.com/schemas/sitemap/0.9">
%s
 </urlset>
''' %(urls_str)
    file_name=os.path.join(ROOT_PATH,'sitemap.xml')
    with open(file_name,'w+',encoding='utf-8') as fd:
        fd.write(sitemap_str)
    print("生成sitemap成功：%s" %(file_name))


if __name__=="__main__":
    generate_sitemap()
