from os import path

LANGUAGE = 'zh-cn'
BLOG_NAME = 'Xl的博客'
BLOG_DESCRIPTION = 'Xl的博客'
DOMAIN_ROOT_URL_PREFIX = "https://www.li1996.cn"
ROOT_URL_PREFIX = "/"
POST_URL_PREFIX = '/post/'

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
RECOMMEND_JSON_FILE_PATH = path.abspath(path.join(PUBLIC_PATH, "recommend.json"))

GENERAL_PAGES_DIR_PATH = path.abspath(path.join(PUBLIC_PATH, 'general_pages'))
SPECAIL_PAGES_DIR_PATH = path.abspath(path.join(PUBLIC_PATH, 'special_pages'))

POST_CNT_PER_PAGE = 10
