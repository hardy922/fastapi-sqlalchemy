### 环境部署

##### python环境：3.9

Linux： [https://www.python.org/ftp/python/3.9.16/Python-3.9.16.tgz](https://)

windows：[`https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe`](https://)

##### **项目依赖**

执行命令： `pip3 install -r requirements.txt`

### 项目启动


##### api服务启动

执行命令： `python3 app.py -p 5002 -l info `

命令帮助： python3 app.py --help

-p  :端口号

-r  :是否自动重载，默认禁止,如需重载则使用 --reload

-l  :日志级别，有： debug, info, warning ,error


api服务启动后，可访问服务开启的IP和端口号+docs来访问swagger接口文档，如： http://127.0.0.1:5002/docs


##### 定时任务启动

1. 定时任务服务demo在tasks
2. 异步任务worker启动：python3 -m celery -A tasks worker -l info
3. 定时服务启动：python3 -m celery -A tasks beat



### 说明

文中出现的pip3 ，python3，是指系统配置的python环境软链接名称，如果配置的是pip和python，则使用pip install xxx， pyhon main.py xxx
