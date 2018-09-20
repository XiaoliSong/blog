[TOC]

## 需求场景

开发后台的同学，经常需要写一些脚本定时启动运行，通常使用crontab来实现。有时候还有更加苛刻的需求：脚本不仅需要定时启动，而且还需要保证互斥
（同一时间只有一个进程在跑，上次的没结束则这次不启动）的要求，甚至还需要设置超时时间（当运行时间过长自动结束进程）和超时报警。那又该如何实现呢？答案是：crontab定时启动任务，flock保证互斥，timeout设置超时以及报警脚本

## crontab、flock、timeout的使用介绍

### crontab的使用

crontab是Linux自带的实现定时任务程序，只能实现分钟级的定时任务。具体参考[crontab 定时任务](https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/crontab.html)

需要注意的点：

* 实现每8分钟启动一次任务的实际执行情况是，从整点的0分钟开始每隔8分钟执行一次，所以56分钟时会执行一次且下次0分钟又会执行，其他小时、日应该也是类似。
* 脚本的路径应该使用绝对路径或者使用cd命令到绝对路径

### flock的使用

flock可以保证只有一个脚本单例执行。主要用的是互斥非阻塞模式，设置等待时间也有一定的用处，但我用的较少。

参考[使用flock命令确保脚本单例执行](https://blog.csdn.net/tenfyguo/article/details/51012527)

需要注意的点：

* flock的互斥文件最好使用绝对路径且以.lock结尾
* 使用flock之后会生成相应的文件，后面命令完成结束之后并不会自动清除掉

### timeout的使用

参考[timeout(1)-Linux man page](https://linux.die.net/man/1/timeout)

使用例子

```shell
# 超时发送-9信号，超时执行后面的脚本输出failed
timeout -s 9 5 sleep 20 || echo 'failed'
# 未超时执行后面的脚本输出success
timeout -s 9 10 sleep 5 && echo 'success'
```

需要注意的点
* timeout 正常结束的返回码是0
* timeout 超时kill结束的返回码是124

## 配合使用例子

首先定时执行的脚本task.sh如下：

```shell
echo 'start at：' `date`
# 大概3分钟
sleep 180
echo 'end at：' `date`
```

其次是超时报警通知脚本alarm.sh如下：

```
# 追加输出超时时间到alarm.log
echo 'timeout at：' `date` >>alarm.log
# 其他的报警措施，发邮件、短信....
```

由于上面的定时任务大概3分钟结束，所以我们的超时时间大于3分钟就行了（具体多少根据不同情况设置就行了），假设6分钟执行一次且互斥非阻塞，超时10分钟且超时执行报警脚本，则最终crontab文件如下
```
*/6 * * * * cd /data/projec && flock -xn ./task.lock -c 'timeout -9 600 sh task.sh || sh alarm.sh'
```

### 需要注意的点

如果task.sh启动了子进程进行处理，则需要在task.sh的末尾加上wait命令等待全部子进程完成才结束，否则timeout无效

```shell
cd /data/project
nohub python3 main.py >main.log 2>&1 &
wait
```