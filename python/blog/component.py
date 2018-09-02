from blog.html import Html


class Component:
    @classmethod
    def __generate_row_links(cls, row_links):
        row_link_strs = []
        for row_link in row_links:
            img = Html.generate_sp_element(
                'img', src=row_link['icon_url'], alt=row_link['name'])
            span = Html.generate_element_by_str('span', row_link['name'])
            a = Html.generate_element_by_str(
                'a', img + span, href=row_link['link'])
            li = Html.generate_element_by_str('li', a)
            row_link_strs.append(li)
        return Html.generate_element_by_strs(
            'ul', row_link_strs, id="row_links")

    @classmethod
    def __generate_col_links(cls, col_links):
        col_link_strs = []
        for col_link in col_links:
            img = Html.generate_sp_element(
                'img', src=col_link['icon_url'], alt=col_link['name'])
            a = Html.generate_element_by_str('a', img, href=col_link['link'])
            li = Html.generate_element_by_str('li', a)
            col_link_strs.append(li)
        return Html.generate_element_by_strs(
            'ul', col_link_strs, id="col_links")

    @classmethod
    def __generate_profile(cls, profile):
        img = Html.generate_sp_element(
            'img', src=profile['icon_url'], alt=profile['link_title'])
        a = Html.generate_element_by_str(
            'a', img, href=profile['link'], title=profile['link_title'])
        span = Html.generate_element_by_str('span', profile['name'])
        return Html.generate_element_by_strs('div', [a, span], id='profile')

    @classmethod
    def generate_sidebar(cls, sidebar):
        profile = cls.__generate_profile(sidebar['profile'])
        row_links = cls.__generate_row_links(sidebar['row_links'])
        col_links = cls.__generate_col_links(sidebar['col_links'])
        return Html.generate_element_by_strs(
            'nav', [profile, row_links, col_links], id='sidebar')

    @classmethod
    def generate_header(cls, header):
        button = Html.generate_element_by_str('button', id='switch_btn')
        img = Html.generate_sp_element(
            'img', src=header['icon_url'], alt=header['icon_alt'])
        a = Html.generate_element_by_str(
            'a', img, href=header['link'], title=header['icon_alt'])
        h1 = Html.generate_element_by_str('h1', header['name'])
        return Html.generate_element_by_strs(
            'div', [button, a, h1], id="header")
