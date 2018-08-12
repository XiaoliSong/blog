[TOC]

## 页面渲染前加入动态的CSS的文件？

这是我自己的说法，可能不大对。主要描述的是这样的场景：
* css文件url的前缀可能经常变化（比如换对象存储的提供商、需要做迁移）
* 我们希望在渲染前完成css样式文件的加载

所以我的方案场景代码是这样的：
```
<!DOCTYPE html>
<html>
<head>
    <link class="remoteCss" rel="stylesheet" type="text/css" tempHref="/css/global.css">
</head>
<body>
    <div id="main">
</body>
</html>
```

希望，能够在页面渲染前完成样式文件的引入。css文件url前缀可能为http://baidu.com或者其他。目前我没有搜索到相关的解决方案。

## 排除的方案

有人可能会说，可以直接这样就行了。
```
<!DOCTYPE html>
<html>
<head>
    <link class="remote_css" rel="stylesheet" type="text/css" temp_href="/css/global.css">
    <script>
        const URL_PREFIX="http://www.baidu.com"
        css_arr=document.getElementsByClassName('remote_css');
        for(let i=0;i<css_arr.length;i++){
            css_arr[i].href=URL_PREFIX+css_arr[i].getAttribute("temp_href");
            /*
            或者往head动态加入节点，都是不可行的
            <link class="remote_css" rel="stylesheet" type="text/css" href="http://www.baidu.com/css/global.css">
            */
        }
    </script>
</head>
<body>
    <div id="main">
</body>
</html>
```

上面是可以动态加入CSS页面文件，但是不是在页面渲染前加载完成的。也就是会导致刚打开页面时，没有css样式就渲染了，等到样式文件加载完成重新渲染。

## 解决方案

首先，需要把js脚本放在head里面，保证渲染页面前先执行脚本。然后我们需要利用到css的import特性。

```
<!DOCTYPE html>
<html>
<head>
    <link class="remote_css" rel="stylesheet" type="text/css" temp_href="/css/global.css">
    <script>
        (function(){
            const URL_PREFIX="http://www.baidu.com";
            let css_arr=document.getElementsByClassName("remote_css");
            if(css_arr.length<0) return;

            let new_style=document.createElement('style');
            new_style.setAttribute("type","text/css");
            let new_css="";
            for(let i=0;i<css_arr.length;i++){
                new_css=new_css+"@import url('"+URL_PREFIX+css_arr[i].getAttribute("temp_href")+"');\n";
            }
            if(new_style.styleSheet){
                new_style.styleSheet.cssText=newCss;
            }
            else{
                new_style.appendChild(document.createTextNode(new_css));
            }
            document.getElementsByTagName('head')[0].appendChild(new_style);
        })();
    </script>
</head>
<body>
    <div id="main">
</body>
</html>
```