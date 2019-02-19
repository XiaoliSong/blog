import json
from blog import const

with open(
        const.POST_JSON_FILE_PATH, 'r', encoding='utf-8') as post_fd, open(
            const.RECOMMEND_JSON_FILE_PATH, 'r',
            encoding='utf-8') as recommend_fd, open(
                const.SEARCH_JSON_FILE_PATH, 'w+', encoding='utf-8') as res_fd:
    res_dict = {}
    posts = json.load(post_fd)['posts']
    post_dict = {x['link']: x for x in posts}
    for k, v in post_dict.items():
        res_dict[k] = {'title': v['title'], 'tags': v['tags']}

    posts = json.load(recommend_fd)['posts']
    post_dict = {x['link']: x for x in posts}
    for k, v in post_dict.items():
        res_dict[k] = {'title': v['title'], 'tags': v['tags']}

    res_fd.write(json.dumps(res_dict, indent=4, separators=(',', ':')))
