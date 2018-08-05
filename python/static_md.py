#!/usr/bin/python3

from os import path
import json
import sys

from blog.helper import generate_main,md2html,generate_complete_html
from blog.config import CONF_PREFIX_PATH,STATIC_MD_PREFIX_PATH


def generate_generate_static_md_html(file_name_prefix):
    with open(path.join(STATIC_MD_PREFIX_PATH,file_name_prefix+'.md'),'r',encoding='utf-8') as fd:
        main=md2html(fd.read())

    with open(path.join(CONF_PREFIX_PATH,file_name_prefix+'.conf'),'r',encoding='utf-8') as fd:
        page_conf=json.load(fd)
    return generate_complete_html(page_conf,main)


if __name__=="__main__":
    if(len(sys.argv)<2):
        print('参数过少，参数如下：')
        print('infile_name_prefix, [outfile_name_prefix]')
        exit()

    infile_name_prefix=sys.argv[1]
    outfile_name_prefix=infile_name_prefix
    if(len(sys.argv)>=3):
        outfile_name_prefix=sys.argv[2]

    with open(path.join(STATIC_MD_PREFIX_PATH,outfile_name_prefix+'.html'),'w+',encoding='utf-8') as fd:
        html=generate_generate_static_md_html(infile_name_prefix)
        print('生成成功，输出文件：'+path.join(STATIC_MD_PREFIX_PATH,outfile_name_prefix+'.html'))
        fd.write(html)