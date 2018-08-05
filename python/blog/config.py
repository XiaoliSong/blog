from os import path

ROOT_PATH=path.abspath(path.join(path.dirname(__file__), "../../"))

CONF_PREFIX_PATH=path.abspath(path.join(path.dirname(__file__), "../../conf"))
STATIC_MD_PREFIX_PATH=path.abspath(path.join(path.dirname(__file__), "../../"))
POST_PREFIX_PAHT=path.abspath(path.join(path.dirname(__file__), "../../post"))
POST_URL_PREFIX='/post/'
POST_CONF_NAME='post.conf'
POST_MD_NAME='post.md'
POST_PREFACE_NAME='preface.md'
PAGE_PREFIX_PAHT=path.abspath(path.join(path.dirname(__file__), "../../page"))

POST_JSON_PATH=path.abspath(path.join(path.dirname(__file__), "../../post.json"))
RECOMMEND_JSON_PATH=path.abspath(path.join(path.dirname(__file__), "../../recommend.json"))

POST_CNT_PER_PAGE=3
