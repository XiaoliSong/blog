import os
import time
from blog import const
from blog.html import Html


def get_dir_latest_file_mtime(dir_name,*ignore_name_arr):
    max_time = 0
    for item in os.listdir(dir_name):
        ignore=False
        for ignore_name in ignore_name_arr:
            if ignore_name==item:
                ignore=True
        if not ignore:
            file_path=os.path.join(dir_name,item)
            mtime=os.path.getmtime(file_path)
            if mtime > max_time:
                max_time=mtime
    return max_time

def get_post_datetime(post_id):
    post_dir_name = os.path.join(const.POST_DIR_PATH, post_id)
    post_t = get_dir_latest_file_mtime(post_dir_name, 'index.html')
    post_datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(post_t))
    return post_datetime

def get_post_date(post_id):
    post_dir_name = os.path.join(const.POST_DIR_PATH, post_id)
    post_t = get_dir_latest_file_mtime(post_dir_name, 'index.html')
    post_date = time.strftime('%Y-%m-%d',time.localtime(post_t))
    return post_date

def datetime2date(datetime):
    return datetime[0: datetime.index(' ')]


def get_sohucs_comment_cnt_js():
    return Html.generate_element_by_str(
        'script',
        id="cy_cmt_num",
        src=
        "https://changyan.sohu.com/upload/plugins/plugins.list.count.js?clientId=cytyIIWkH"
    )
