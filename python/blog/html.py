#!/usr/bin/python3
import markdown
from bs4 import BeautifulSoup


class Html:
    @classmethod
    def __get_attr_str(cls, **attr_dict):
        attr_str = ''
        for key, value in attr_dict.items():
            if key == 'class_name':
                attr_str = attr_str + ' class="' + value + '"'
            else:
                attr_str = attr_str + ' ' + key + '="' + value + '"'
        return attr_str

    @classmethod
    def from_markdown_str(cls, markdown_str):
        '''convert markdown string to html string
        Args:
            markdown_str: A string in markdown style
        Returns:
            A string after converting
        '''
        exts = [
            'markdown.extensions.extra', 'markdown.extensions.codehilite',
            'markdown.extensions.tables', 'markdown.extensions.toc'
        ]
        return markdown.markdown(markdown_str, extensions=exts)

    @classmethod
    def generate_element_by_str(cls, tag_name, content_str='', **attr_dict):
        attr_str = cls.__get_attr_str(**attr_dict)
        return '''<%s%s>%s</%s>
        ''' % (tag_name, attr_str, content_str, tag_name)

    @classmethod
    def generate_element_by_strs(cls, tag_name, content_strs=[], **attr_dict):
        content_str = ' '.join(content_strs)
        return cls.generate_element_by_str(tag_name, content_str, **attr_dict)

    @classmethod
    def generate_sp_element(cls, tag_name, **attr_dict):
        attr_str = cls.__get_attr_str(**attr_dict)
        return '''
        <%s%s />
        ''' % (tag_name, attr_str)

    @classmethod
    def generate_css(cls, url):
        return cls.generate_sp_element(
            'link', rel="stylesheet", type="text/css", href=url)

    @classmethod
    def generate_js(cls, url):
        return cls.generate_element_by_str('script', '', src=url)

    @classmethod
    def prettify(cls, html_str):
        soup = BeautifulSoup(html_str, 'html.parser')
        return soup.prettify()
