from general_pages import GeneralPages
from blog import const
import os
import sys

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        post_dir = os.path.join(const.PUBLIC_PATH, sys.argv[1])
        if len(sys.argv) == 2:
            GeneralPages.generate_by_dir(post_dir, post_dir)
        else:
            post_name = sys.argv[2]
            html_file_path = os.path.join(post_dir, post_name + '.html')
            with open(html_file_path, 'w+', encoding='utf-8') as fd:
                html_str = GeneralPages.generate_by_file(post_name, post_dir)
                fd.write(html_str)
            print("生成 %s 成功：%s" % (post_name, html_file_path))

    else:
        print('参数错误')
