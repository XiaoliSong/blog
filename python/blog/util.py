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
    ''' %(const.GIT_TALK_CLIENT_ID, const.GIT_TALK_CLIENT_SECRET, const.GIT_TALK_REPO, const.GIT_TALK_OWNER, const.GIT_TALK_ADMIN)
