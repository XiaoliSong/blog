import os
import time
import hashlib
import json
from blog import const
from blog.html import Html


def get_file_md5(file_path):
    if not os.path.isfile(file_path):
        return ""
    m = hashlib.md5()
    with open(file_path, 'rb') as fd:
        while True:
            data = fd.read(4096)
            if len(data) == 0:
                break
            m.update(data)
    return m.hexdigest()


def get_post_md5(post_id):
    # 三个文件的md5值相加再md5
    data = ""
    file_dir = os.path.join(const.POST_DIR_PATH, post_id)
    for md5_item in [
            const.POST_CONF_FILE_PATH, const.POST_MD_FILE_PATH,
            const.POST_PREFACE_FILE_PATH
    ]:
        file_path = os.path.join(file_dir, md5_item)
        data = data + get_file_md5(file_path)
    return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()


def get_now_datetime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def datetime2date(datetime):
    return datetime[0:datetime.index(' ')]


def get_post_create_update_datetime(post_id):
    with open(const.POST_JSON_FILE_PATH, 'r', encoding='utf-8') as fd:
        old_posts = json.load(fd)['posts']
        old_post_dict = {post['id']: post for post in old_posts}
    if post_id in old_post_dict:
        post = old_post_dict[post_id]
        return post['create_datetime'], post['update_datetime']


def get_post_create_datetime(post_id):
    ct, ut = get_post_create_update_datetime(post_id)
    return ct


def get_post_create_date(post_id):
    return datetime2date(get_post_create_datetime(post_id))


def get_post_update_datetime(post_id):
    ct, ut = get_post_create_update_datetime(post_id)
    return ut


def get_post_update_date(post_id):
    return datetime2date(get_post_update_datetime(post_id))


def get_git_talk_html():
    if not const.GIT_TALK_ENABLED:
        return ''

    return '''
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/gitalk@1/dist/gitalk.css">
    <script src="https://cdn.jsdelivr.net/npm/gitalk@1/dist/gitalk.min.js"></script>
    <div id="gitalk-container"></div>
    <script>
        const gitalk = new Gitalk({
        clientID: '%s',
        clientSecret: '%s',
        repo: '%s',
        owner: '%s',
        admin: %s,
        id: location.pathname.substring(0,50),      // Ensure uniqueness and length less than 50
        distractionFreeMode: false  // Facebook-like distraction free mode
        })
        gitalk.render('gitalk-container')
    </script>
    ''' % (const.GIT_TALK_CLIENT_ID, const.GIT_TALK_CLIENT_SECRET,
           const.GIT_TALK_REPO, const.GIT_TALK_OWNER, const.GIT_TALK_ADMIN)
