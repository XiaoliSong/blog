import os
import json
from blog.page import Page
from blog.html import Html
from blog import const


class GeneralPages:
    @classmethod
    def generate_by_file(cls,
                         file_prefix,
                         file_dir_name=const.GENERAL_PAGES_DIR_PATH):
        md_file_path = os.path.join(file_dir_name, str(file_prefix) + '.md')
        with open(md_file_path, 'r', encoding='utf-8') as fd:
            main = Html.from_markdown_str(fd.read())
        cond_file_path = os.path.join(file_dir_name,
                                      str(file_prefix) + '.conf')
        with open(cond_file_path, 'r', encoding='utf-8') as fd:
            page_info = json.load(fd)
        return Page.generate_complete_html(page_info, main)

    @classmethod
    def generate_by_dir(cls, source_dir, target_dir):
        cnt = 0
        for dir_item in os.listdir(source_dir):
            if (dir_item.endswith('.conf')):
                file_prefix = dir_item.replace('.conf', '')
                html_file_path = os.path.join(target_dir,
                                              file_prefix + '.html')
                with open(html_file_path, 'w+', encoding='utf-8') as fd:
                    html_str = GeneralPages.generate_by_file(
                        file_prefix=file_prefix, file_dir_name=source_dir)
                    fd.write(html_str)
                cnt += 1
                print("生成 %s 成功：%s" % (file_prefix, html_file_path))
        print("生成 GeneralPage 成功，共 %d 个" % cnt)


if __name__ == "__main__":
    GeneralPages.generate_by_dir(const.GENERAL_PAGES_DIR_PATH,
                                 const.PUBLIC_PATH)
