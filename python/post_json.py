#!/usr/bin/python3

import os
import json
import functools
from blog.util import get_post_datetime
from blog import const


def post_time_cmp_func(x, y):
    if x['datetime'] < y['datetime']:
        return -1
    elif x['datetime'] > y['datetime']:
        return 1
    else:
        return 0


def generate_post_json():
    post_arr = []
    for post_dir_item in os.listdir(const.POST_DIR_PATH):
        post_dir = os.path.join(const.POST_DIR_PATH, post_dir_item)
        if (os.path.isdir(post_dir)):
            conf_file_name = os.path.join(post_dir, const.POST_CONF_FILE_PATH)
            with open(conf_file_name, 'r', encoding='utf-8') as fd:
                post_conf = json.load(fd)
                datetime = get_post_datetime(post_dir_item)
                link = const.POST_URL_PREFIX + post_dir_item + '/index.html'
                post_arr.append({
                    'id': post_dir_item,
                    'title': post_conf['title'],
                    'tags': post_conf['tags'],
                    'datetime': datetime,
                    'link': link
                })
    post_arr = sorted(
        post_arr, key=functools.cmp_to_key(post_time_cmp_func), reverse=True)
    post_json = {'posts': post_arr}
    return json.dumps(post_json)


def generate_post_json_file():
    with open(const.POST_JSON_FILE_PATH, 'w+', encoding='utf-8') as fd:
        fd.write(generate_post_json())

    print('生成 post_json 成功' + const.POST_JSON_FILE_PATH)


if __name__ == "__main__":
    generate_post_json_file()
