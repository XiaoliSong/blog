import os
import time
import json
from blog import const
from blog.html import Html

RSS_FILE_PATH = 'rss.xml'


def generate_rss_item(title, link, description, pubDate):
    title = Html.generate_element_by_str('title', title)
    link = Html.generate_element_by_str('link', link)
    description = Html.generate_element_by_str('description', description)
    pubDate = Html.generate_element_by_str('pubDate', pubDate)
    guid = Html.generate_element_by_str('guid', link)
    item = title + link + description + pubDate + guid
    item = Html.generate_element_by_str('item', item)
    return item


def generate_rss():
    with open(const.POST_JSON_FILE_PATH, 'r', encoding='utf-8') as fd:
        posts = json.load(fd)['posts'][0:const.POST_CNT_PER_PAGE]
    item_str = ''
    for post in posts:
        title = post['title']
        link = post['link']
        description_file_name = os.path.join(const.POST_DIR_PATH, post['id'],
                                             const.POST_PREFACE_FILE_PATH)
        with open(description_file_name, 'r', encoding='utf-8') as fd:
            description = Html.from_markdown_str(fd.read())
        pubDate = post['datetime']
        item_str += generate_rss_item(title, link, description, pubDate)

    title = Html.generate_element_by_str('title', const.BLOG_NAME)
    link = Html.generate_element_by_str('link', const.DOMAIN_ROOT_URL_PREFIX)
    description = Html.generate_element_by_str('description',
                                               const.BLOG_DESCRIPTION)
    atom_link = Html.generate_sp_element(
        'atom:link',
        href=const.DOMAIN_ROOT_URL_PREFIX + '/' + RSS_FILE_PATH,
        rel='self')
    language = Html.generate_element_by_str('language', const.LANGUAGE)
    lastBuildDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    lastBuildDate = Html.generate_element_by_str('lastBuildDate',
                                                 lastBuildDate)
    channel = Html.generate_element_by_strs(
        'channel',
        [title, link, description, atom_link, language, lastBuildDate])

    return '''<rss xmlns:atom="http://www.w3.org/2005/Atom" version="2.0">
    %s
    %s
</rss>
''' % (channel, item_str)


def generate_rss_file():
    rss_file_name = os.path.join(const.PUBLIC_PATH, RSS_FILE_PATH)
    with open(rss_file_name, 'w+', encoding='utf-8') as fd:
        fd.write(generate_rss())
    print("生成 RSS 成功：%s" % (rss_file_name))


if __name__ == "__main__":
    generate_rss_file()