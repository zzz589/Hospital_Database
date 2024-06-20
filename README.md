# Hospital_Database

## 项目环境

- 编程语言：python3.12 `<br>`
- web 框架：python flask `<br>`
- 数据库：PostgreSQL `<br>`
- 操作系统：mac

运行方式

解压后在当前目录下执行命令

```
> python3 run.py
```

注：运行前需要先创建好 hospital 数据库.

需要配置好环境

docker 运行

`docker-compose up --build`

即可创建两个容器,一个是使用 postgresql 数据库,持久化容器在宿主机地址为/var/lib/postgresql/data

另一个是 python 容器,使用 flask 前端,将 5001 端口映射到宿主机的 5001 端口,

容器运行后使用宿主机访问http://127.0.0.1:5001即可

docker-compose 会让数据库自动初始化,创建好对应的表,数据将持久化储存
