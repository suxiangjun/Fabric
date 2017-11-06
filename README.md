## 项目名称：类 Fabric

*本软件只在python3环境下运行。*

#### 实现功能

- 运行程序列出主机组或者主机列表
- 选择指定主机或主机组

- 选择让主机或者主机组执行命令或者向其传输文件（上传/下载）

- 充分使用多线程或多进程

- 不同主机的用户名密码、端口可以不同

#### 程序架构

```php+HTML
|
├──Fabric                #服务端
│      │──bin                       
│      │   ├──fabric.py      #  类 Fabric执行程序   
│      │   └──__init__.py
│      │──core               #  主程序文件        
│      │   ├──main.py         
│      │   └──__init__.py
│      └──data               # 数据存储的地方
│      │    ├──password.bak  # 存所有主机的基本数据
│      │	├──password.dat
│      │    └──password.dir
│      │──downloads          # 下载文件存放路径
│      │──log                # 日志目录
│      │    └──Fabric.log  
│      │──uploads            # 上传文件存放路径  
│        
│──README
```

`使用说明：`             q 返回上一层 

​		                 b 退出程序

[博客地址]: http://www.cnblogs.com/xiangjun555

