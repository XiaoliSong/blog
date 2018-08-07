# 部署流程

采用docker的nginx容器，支持ssl

## docker 安装

见docker官网

## nginx容器启动

### 拉取nginx镜像

```
docker pull nginx
```

### 启动容器
```
docker run -itd --name blog -p 80:80 -p 443:443 -v ~/docker-project/blog/:/usr/share/nginx/html/ nginx /bin/bash
```

容器名为blog，注意端口映射80和443，文件夹映射，默认启动/bin/bash，nginx没有启动

## 进入容器配置

### 进入容器
```
docker exec -it blog /bin/bash
```

### 获取证书

参考：https://certbot.eff.org/lets-encrypt/debianstretch-nginx

#### 修改源
内容为sources.list的内容（debian stretch的源）
```
cat >/etc/apt/sources.list
```

修改sources.list文件后，执行：
```
apt-get update
```

然后：
```
apt-get install python-certbot-nginx -t stretch-backports
certbot --authenticator webroot --installer nginx
certbot certonly --authenticator standalone --pre-hook "nginx -s stop" --post-hook "nginx"
```

中途可能需要填写域名和邮箱，最好可能提示无法配置nginx.conf，所以需要手动修改nginx的配置，记住证书位置

### 修改/etc/nginx/default.conf

default.conf 需要修改的地方
* ssl证书位置
* server_name

```
cat >/etc/nginx/default.conf
```

### 自动更新ssl证书


```
cat >run.sh
```

```
bash run.sh &
```

### 启动nginx服务

```
service nginx restart
```