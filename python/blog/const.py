from os import path

LANGUAGE = 'zh-cn'
BLOG_NAME = 'Xiaoli Song'
BLOG_DESCRIPTION = 'Xiaoli Song,xiaolisong,Song Xiaoli,songxiaoli'
DOMAIN_ROOT_URL_PREFIX = "https://xiaolisong.github.io"
ROOT_URL_PREFIX = DOMAIN_ROOT_URL_PREFIX + "/blog/"
POST_URL_PREFIX = ROOT_URL_PREFIX + 'post/'

ROOT_PATH = path.abspath(path.join(path.dirname(__file__), "../../"))
CONF_DIR_PATH = path.abspath(path.join(ROOT_PATH, "conf"))
GLOBAL_CONF_FILE_PATH = path.abspath(path.join(CONF_DIR_PATH, 'global.conf'))
SIDEBAR_CONF_FILE_PATH = path.abspath(path.join(CONF_DIR_PATH, 'sidebar.conf'))
HEADER_CONF_FILE_PATH = path.abspath(path.join(CONF_DIR_PATH, 'header.conf'))

PUBLIC_PATH = path.abspath(path.join(path.dirname(__file__), "../../public/"))
POST_DIR_PATH = path.abspath(path.join(PUBLIC_PATH, "post"))

POST_CONF_FILE_PATH = 'post.conf'
POST_MD_FILE_PATH = 'post.md'
POST_PREFACE_FILE_PATH = 'preface.md'
PAGE_PREFIX_PATH = path.abspath(path.join(PUBLIC_PATH, "page"))

POST_JSON_FILE_PATH = path.abspath(path.join(PUBLIC_PATH, "post.json"))
RECOMMEND_JSON_FILE_PATH = path.abspath(
    path.join(PUBLIC_PATH, "recommend.json"))
SEARCH_JSON_FILE_PATH = path.abspath(
    path.join(PUBLIC_PATH, "search.json"))

GENERAL_PAGES_DIR_PATH = path.abspath(path.join(PUBLIC_PATH, 'general_pages'))
SPECAIL_PAGES_DIR_PATH = path.abspath(path.join(PUBLIC_PATH, 'special_pages'))

POST_CNT_PER_PAGE = 10

GIT_TALK_ENABLED = 1
GIT_TALK_CLIENT_ID = 'a5d425df08c92b74a417'
GIT_TALK_CLIENT_SECRET = '2c0840d0cb71a72d3ce8094d55094e5c260ffc15'
GIT_TALK_REPO = 'blog.git_talk'
GIT_TALK_OWNER = 'XiaoliSong'
GIT_TALK_ADMIN = ['XiaoliSong']
