from blog.html import Html
import blog.util


def generate_tag_data(posts):
    tag_arr = []
    tag_posts = {}
    for post in posts:
        for tag in post['tags']:
            if tag not in tag_arr:
                tag_arr.append(tag)
            if tag not in tag_posts:
                tag_posts[tag] = [post]
            else:
                tag_posts[tag].append(post)

    tag_info_arr = []
    tag_posts_arr = []
    for tag in tag_arr:
        tag_info_arr.append({'name': tag, 'count': len(tag_posts[tag])})
        tag_posts_arr.append({'name': tag, 'posts': tag_posts[tag]})

    return tag_info_arr, tag_posts_arr


def generate_tag_ul(tag_info_arr):
    li_arr = []
    for tag_info in tag_info_arr:
        button_content = tag_info['name'] + '(' + str(tag_info['count']) + ')'
        button = Html.generate_element_by_str('button', button_content)
        li = Html.generate_element_by_str('li', button)
        li_arr.append(li)
    return Html.generate_element_by_strs('ul', li_arr, id='tags_ul')


def generate_tag_contents_ul(tag_posts_arr):
    li_arr = []
    for tag_posts in tag_posts_arr:
        tag = tag_posts['name']
        h2 = Html.generate_element_by_str('h2', tag)

        sub_li_arr = []
        posts = tag_posts['posts']
        for post in posts:
            if 'create_datetime' in post:
                date = blog.util.datetime2date(post['create_datetime'])
                span = Html.generate_element_by_str('span', date)
                a_content = post['title'] + ' ' + span
            else:
                a_content = post['title']
            a = Html.generate_element_by_str(
                'a', a_content, href=post['link'], title=post['title'])
            sub_li = Html.generate_element_by_str('li', a)
            sub_li_arr.append(sub_li)
        sub_ul = Html.generate_element_by_strs('ul', sub_li_arr)
        li = Html.generate_element_by_strs('li', [h2, sub_ul])
        li_arr.append(li)
    return Html.generate_element_by_strs('ul', li_arr, id='tag_contents_ul')
