## 全局配置文件

### 说明
全局配置文件作用于在每个生成的html文件，有以下几个文件
* global.conf
* header.conf
* 

### global.conf

用于配置共有的css、js文件、footer底部的html

* start_css_arr
	* html页面放在head的css文件数组
* start_js_arr
	* html页面放在head的js文件数组
* end_css_arr
	* html页面放在末尾body前的css文件数组
* end_js_arr
	* html页面放在末尾body前的js文件名数组
* footer
	* 加载在底部的html字符串

如：
```
{
    "start_css_arr":[
        "./css/global.css",
        "./css/md.css"
    ],
    "start_js_arr":[],
    "end_css_arr":[],
    "end_js_arr":["./js/global.js"],
    "footer":"Xl的博客 - <a href='http://li1996.cn' title='Xl的博客'>li1996.cn </a>"
}
```


### header.conf
用于配置共有的header部分
```
{
    "name":"Xl的博客",
    "link":"/about/",
    "icon_url":"http://blog-1252791686.cosbj.myqcloud.com/icon/logo.png",
    "icon_alt":"关于"
}
```

### sidebar.conf
用于配置共有的sidebar部分

如：
```
{
    "profile":{
        "name":"Xl的博客",
        "link":"/",
        "link_title":"Xl的博客",
        "icon_url":"http://blog-1252791686.cosbj.myqcloud.com/icon/logo.png"
    },
    "row_links":[
        {"name":"首页","link":"/index.html","icon_url":"http://blog-1252791686.cosbj.myqcloud.com/icon/home.png"},
        {"name":"归档","link":"/archives.html","icon_url":"http://blog-1252791686.cosbj.myqcloud.com/icon/archives.png"},
        {"name":"标签","link":"/tags.html","icon_url":"http://blog-1252791686.cosbj.myqcloud.com/icon/tags.png"},
        {"name":"作品","link":"/works.html","icon_url":"http://blog-1252791686.cosbj.myqcloud.com/icon/works.png"},
        {"name":"推荐","link":"/recommend.html","icon_url":"http://blog-1252791686.cosbj.myqcloud.com/icon/recommend.png"},
        {"name":"关于","link":"/about.html","icon_url":"http://blog-1252791686.cosbj.myqcloud.com/icon/about.png"},
        {"name":"友链","link":"/friends.html","icon_url":"http://blog-1252791686.cosbj.myqcloud.com/icon/friends.png"}
    ],
    "col_links":[
        {"name":"GitHub","link":"https://github.com/XiaoliSong/","icon_url":"http://blog-1252791686.cosbj.myqcloud.com/icon/github.png"},
        {"name":"Search","link":"/search.html","icon_url":"http://blog-1252791686.cosbj.myqcloud.com/icon/search.png"}
    ]
}
```

### page.conf
分页导航的配置，也就是/page/(index)/index.html的页面配置

```
{
    "title":"Xl的博客",
    "key_words":"Xl的博客",
    "start_css_arr":["./css/article.css","./css/page.css"],
    "start_js_arr":[],
    "end_css_arr":[],
    "end_js_arr":[]
}
```

## 一般页面配置文件

### 说明

可配置信息有：
* title
	* html页面的title
* key_words
	* html页面的key_words
* start_css_arr
	* html页面放在head的css文件数组
* start_js_arr
	* html页面放在head的js文件数组
* end_css_arr
	* html页面放在末尾body前的css文件数组
* end_js_arr
	* html页面放在末尾body前的js文件名数组

### 当前已有文件说明：
* works.conf
	* works.html的页面配置
* about.conf
	* about.html的页面配置
* friends.conf
	* friends.html的页面配置
* search.conf
	* friends.html的页面配置
* archive.conf
	* archive.html的页面配置
* tag.conf
	* tag.html的页面配置
* recommend.conf
	* recommend.html的页面配置
### conf文件例子 
'''
{
    "title":"关于 - Xl的博客",
    "key_words":"关于,Xl的博客",
    "start_css_arr":[],
    "start_js_arr":[],
    "end_css_arr":[],
    "end_js_arr":[]
}
'''

## 注意事项：
css和js文件名最好为绝对路径