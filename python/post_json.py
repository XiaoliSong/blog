#!/usr/bin/python3

import os
import time
import json
import functools
from blog.helper import get_dir_latest_file_mtime
from blog.config import POST_PREFIX_PAHT,POST_CONF_NAME,POST_JSON_PATH

def post_cmp_func(x,y):
    if x['datetime']<y['datetime']:
        return -1
    elif x['datetime']>y['datetime']:
        return 1
    else:
        return 0


def generate_post_json():
    post_arr=[]
    for dir_name in os.listdir(POST_PREFIX_PAHT):
        path_dir_name=os.path.join(POST_PREFIX_PAHT,dir_name)
        if(os.path.isdir(path_dir_name)):
            conf_file_name=os.path.join(path_dir_name,POST_CONF_NAME)
            with open(conf_file_name,'r',encoding='utf-8') as fd:
                post_conf=json.load(fd)
                t=get_dir_latest_file_mtime(path_dir_name,'index.html')
                datetime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))
                link="/post/"+dir_name+'/index.html'
                post_arr.append({
                    'id':dir_name,
                    'title':post_conf['title'],
                    'tags':post_conf['tags'],
                    'datetime':datetime,
                    'link':link
                })
    post_arr=sorted(post_arr,key=functools.cmp_to_key(post_cmp_func),reverse=True)
    post_json={
        'posts':post_arr
    }
    json_str=json.dumps(post_json)

    with open(POST_JSON_PATH,'w+',encoding='utf-8') as fd:
        fd.write(json_str)
    
    print('成功生成post_json文件：'+POST_JSON_PATH)

if __name__=="__main__":
    generate_post_json()

