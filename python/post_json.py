#!/usr/bin/python3

import os
import json
import functools
from blog.util import get_post_md5, get_now_datetime
from blog import const


def post_time_cmp_func(x, y):
    if x['create_datetime'] < y['create_datetime']:
        return -1
    elif x['create_datetime'] > y['create_datetime']:
        return 1
    else:
        return 0


def generate_post_json():
    with open(const.POST_JSON_FILE_PATH, 'r', encoding='utf-8') as fd:
        old_posts = json.load(fd)['posts']
        old_post_dict = {post['id']: post for post in old_posts}
    post_arr = []
    for post_id in os.listdir(const.POST_DIR_PATH):
        post_dir = os.path.join(const.POST_DIR_PATH, post_id)
        if (os.path.isdir(post_dir)):
            conf_file_name = os.path.join(post_dir, const.POST_CONF_FILE_PATH)
            with open(conf_file_name, 'r', encoding='utf-8') as fd:
                post_conf = json.load(fd)
                md5 = get_post_md5(post_id)
                link = const.POST_URL_PREFIX + post_id + '/index.html'
                post = {
                    'id': post_id,
                    'title': post_conf['title'],
                    'tags': post_conf['tags'],
                    'md5': md5,
                    'link': link
                }

                if post_id not in old_post_dict:
                    create_datetime = get_now_datetime()
                    update_datetime = create_datetime
                else:
                    create_datetime = old_post_dict[post_id]['create_datetime']
                    update_datetime = old_post_dict[post_id]['update_datetime']
                    if md5 != old_post_dict[post_id]['md5']:
                        update_datetime = get_now_datetime()
                post['create_datetime'] = create_datetime
                post['update_datetime'] = update_datetime
                post_arr.append(post)
    post_arr = sorted(
        post_arr, key=functools.cmp_to_key(post_time_cmp_func), reverse=True)
    post_json = {'posts': post_arr}
    return json.dumps(post_json, indent=4, separators=(',', ':'))


def generate_post_json_file():
    data = generate_post_json()
    with open(const.POST_JSON_FILE_PATH, 'w+', encoding='utf-8') as fd:
        fd.write(data)

    print('生成 post_json 成功' + const.POST_JSON_FILE_PATH)


if __name__ == "__main__":
    generate_post_json_file()
