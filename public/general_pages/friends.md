# 友链

* [奇舞团](https://75team.com/post/list)
* [十年踪迹的博客](https://www.h5jun.com/)
* [Jerry Qu的小站](https://imququ.com/)
* [酷壳 CoolShell](https://coolshell.cn/)
* [Charles Zhang (张铁蕾)](http://zhangtielei.com/)

如需要互相添加友情链接，请在下面评论。

<div id="gitalk-container"></div>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/gitalk@1/dist/gitalk.css">
<script src="https://cdn.jsdelivr.net/npm/gitalk@1/dist/gitalk.min.js"></script>
<script>
    const gitalk = new Gitalk({
    clientID: 'a5d425df08c92b74a417',
    clientSecret: '2c0840d0cb71a72d3ce8094d55094e5c260ffc15',
    repo: 'XiaoliSong.github.io.git_talk',
    owner: 'XiaoliSong',
    admin:  ['XiaoliSong'],
    id: location.pathname,      // Ensure uniqueness and length less than 50
    distractionFreeMode: false  // Facebook-like distraction free mode
    })
    gitalk.render('gitalk-container')
</script>