# L


# 多人协作云脑图

![logo](res/Logo.png)

[代码仓库](http://git.code.oa.com/v_jxinma/MindMap.git)

[TOC]

## 描述
**多人协作云脑图**

* 前端：[AngularJS](https://angularjs.org/)， [HTML5](https://en.wikipedia.org/wiki/HTML5)， [SVG](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics)
* 后端：[NodeJS](https://nodejs.org/en/)， [MongoDB](https://www.mongodb.com/download-center?jmp=nav)
* 交互：[Socket.io](http://socket.io/)，[Differential Synchronization](https://neil.fraser.name/writing/sync/)


## 部署
#### 依赖
* **NodeJS**（推荐版本 v6.2.2）
* NodeJS的模块管理工具 **npm**（推荐版本 v3.9.5）
* 数据库 **MongoDB**（推荐版本 v3.2.7）
* 其余依赖项详见项目目录下 **package.json** 文件


#### 数据库启动
* Windows
	1. （为方便使用Mongod，Mongo命令）将MongoDB bin目录添加到环境变量
	2. 安装MongoDB服务，设置存放位置和启动端口（只需要安装一次）
```console
$ mongod --dbpath %YOUR_DATABASE_LOCATION% --logpath %YOUR_LOG_FILE_LOCATION% --port 27018 --install
```
> Example:
> %YOUR_DATABASE_LOCATION% : D:\data\db
> %YOUR_LOG_FILE_LOCATION% : D:\data\log\mongodb.log
	3. 启动数据库Server（仅需在第一次启动或关闭数据库服务后启动）
```console
$ mongod
```

* Linux
	1. 安装之后可以使用默认配置启动服务
```console
$ mongod -f %YOUR_CONFIGUTATION_FILE_LOCATION%
```
> Example:
> %YOUR_CONFIGUTATION_FILE_LOCATION% : /etc/mongodb.conf


#### 项目启动
1. 安装项目所需的NodeJS模块
```console
$ npm install
```

2. 启动项目
```console
$ npm start
```

3. 停止项目
```console
$ (Ctrl + C)
```


## 使用
项目 URL 组成：
**http://HOST_NAME:PORT/projectevent?params=PARAMS**
> 说明：
> HOST_NAME : 主机名
> PORT : 项目占用的端口号
> PARAMS : TAPD生成的包含当前用户名及workspace_id的密文串（详情咨询AnyeChen）

> Example:
> http://10.125.48.28/projectevent?params=slSlqZ2miKBTrsHJoc%2FMUpKFp6PXo6aoxZWZkpyUW5tZY2Bna2WemmJa3w%3D%3D

可将其URL直接接入TAPD应用


## 配置说明
项目的配置文件位于 **MindMap/server/config/config.js**
* 项目启动端口号：
        "port": 80,

* 由于项目与TAPD对接，使用了**[TAPD Open API](http://open.tapd.oa.com/account)**。所以使用前需填写个人API账号信息：
		"tapdOpenApiHost": "",
    	"tapdOpenApiFormat": ".json",
    	"tapdOpenApiUsername": "",
    	"tapdOpenApiPassward": "",

* 所使用的数据库服务的地址：
		"mongodbServerUrl": ""


## 产品截图
个人脑图
![Screenshots_0.png](.\res\Screenshots_0.png)

迭代脑图
![Screenshots_1.png](.\res\Screenshots_1.png)

Wiki脑图
![Screenshots_2.png](.\res\Screenshots_2.png)


## 开发者
* [v_jxinma(马坚鑫)]()
* [v_cjli(李成江)]()
* [v_xryao(姚炫容)]()
* [v_nnanwang(王楠)]()
