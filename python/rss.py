import os
import time
import json
from blog.config import ROOT_URL_PREFIX,ROOT_PATH,POST_JSON_PATH,POST_PREFIX_PAHT,POST_CNT_PER_PAGE,POST_PREFACE_NAME,RSS_FILE_PATH
from blog.config import LANGUAGE,BLOG_NAME,BLOG_DESCRIPTION,ROOT_URL_PREFIX
from blog.helper import md2html

def generate_rss_item(title,link,description,pubDate):
    return '''<item>
    <title>
        %s
    </tile>
    <link>
        %s
    </link>
    <description>
        %s
    </description>
    <pubDate>
        %s
    </pubDate>
    <guid>
        %s
    </guid>
</item>''' % (title,link,description,pubDate,link)


def generate_rss():
    with open(POST_JSON_PATH,'r',encoding='utf-8') as fd:
        posts=json.load(fd)['posts'][0:POST_CNT_PER_PAGE]
    item_str=''
    for post in posts:
        title=post['title']
        link=post['link']
        description_file_name=os.path.join(POST_PREFIX_PAHT,post['id'],POST_PREFACE_NAME)
        with open(description_file_name,'r',encoding='utf-8') as fd:
            description=md2html(fd.read())
        pubDate=post['datetime']
        item_str+=generate_rss_item(title,link,description,pubDate)

    last_build_date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    rss_str='''<rss xmlns:atom="http://www.w3.org/2005/Atom" version="2.0">
    <channel>
        <title>%s</title>
        <link>%s</link>
        <description>%s</description>
        <atom:link href="%s" rel="self"/>
        <language>%s</language>
        <lastBuildDate>%s</lastBuildDate>
    </channel>
    %s
</rss>
''' % (BLOG_NAME,ROOT_URL_PREFIX,BLOG_DESCRIPTION,ROOT_URL_PREFIX+'/'+RSS_FILE_PATH,LANGUAGE,last_build_date,item_str)

    rss_file_name=os.path.join(ROOT_PATH,RSS_FILE_PATH)
    with open(rss_file_name,'w+',encoding='utf-8') as fd:
        fd.write(rss_str)
    print("生成RSS成功：%s" %(rss_file_name))


if __name__=="__main__":
    generate_rss()