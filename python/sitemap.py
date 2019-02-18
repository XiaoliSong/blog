import os
import time
import json
from blog.html import Html
from blog import const

SITE_MAP_FILE_PATH = 'sitemap.xml'

# html页面文件
STATIC_HTML_ARR = [
    "40x.html",
    "50x.html",
    "about.html",
    "archive.html",
    "friends.html",
    "index.html",
    "recommend.html",
    "search.html",
    "tag.html",
    "works.html",
]

# html页面文件夹
HTML_DIR_ARR = ["page"]


def _generate_url(loc, lastmod, changefreq, priority):
    return '''
    <url>
        <loc>%s</loc>
        <lastmod>%s</lastmod>
        <changefreq>%s</changefreq>
        <priority>%s</priority>
    </url>
''' % (loc, lastmod, changefreq, priority)


def generate_sitemap():
    urlset_str = ''

    for static_html in STATIC_HTML_ARR:
        file_path = os.path.join(const.PUBLIC_PATH, static_html)
        mtime = os.path.getmtime(file_path)
        lastmod = time.strftime('%Y-%m-%d', time.localtime(mtime))
        loc = const.DOMAIN_ROOT_URL_PREFIX + '/' + static_html
        changefreq = 'hourly'
        priority = '1.0'
        urlset_str += _generate_url(loc, lastmod, changefreq, priority)

    for dir_name in HTML_DIR_ARR:
        real_dir = os.path.join(const.PUBLIC_PATH, dir_name)
        for item in os.listdir(real_dir):
            if item.endswith('.html'):
                file_path = os.path.join(real_dir, item)
                mtime = os.path.getmtime(file_path)
                lastmod = time.strftime('%Y-%m-%d', time.localtime(mtime))
                loc = const.DOMAIN_ROOT_URL_PREFIX + '/' + dir_name + '/' + item
                changefreq = 'hourly'
                priority = '0.9'
                urlset_str += _generate_url(loc, lastmod, changefreq, priority)

    with open(const.POST_JSON_FILE_PATH, 'r', encoding='utf-8') as fd:
        posts = json.load(fd)['posts']
        for post in posts:
            lastmod = post['update_datetime'][0:post['update_datetime'].index(' ')]
            loc = const.DOMAIN_ROOT_URL_PREFIX + post['link']
            changefreq = 'daily'
            priority = '0.9'
            urlset_str += _generate_url(loc, lastmod, changefreq, priority)

    urlset = Html.generate_element_by_str(
        'urlset',
        urlset_str,
        xmlns="http://www.google.com/schemas/sitemap/0.9")
    sitemap_str = '''<?xml version="1.0" encoding="utf-8"?>%s''' % (urlset)
    return Html.prettify(sitemap_str)


def generate_sitemap_file():
    file_name = os.path.join(const.PUBLIC_PATH, SITE_MAP_FILE_PATH)
    with open(file_name, 'w+', encoding='utf-8') as fd:
        fd.write(generate_sitemap())
    print("生成 sitemap 成功：%s" % (file_name))


if __name__ == "__main__":
    generate_sitemap_file()