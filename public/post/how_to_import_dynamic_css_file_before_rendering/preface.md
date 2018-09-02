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
