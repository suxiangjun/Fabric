# # #!/usr/bin/env python
# # #-*- coding:utf-8 -*-
# # __author = "susu"
# #
# import shelve,os,re
# # d = shelve .open('shelve_test')  # 打开一个文件
# # d["上海"] = {"192.168.5.128":{
# #             "user":"root",
# #             "port":22,
# #             "password":"123456",
# #             "other":"阿里云"
# #             },
# #             "192.168.5.129":{
# #             "user":"root",
# #             "port": 22,
# #             "password":"123456",
# #             "other": "腾讯云"
# #             }
# # }
# # d["北京"] = {"192.168.1.123":{
# #             "user":"root",
# #             "port":22,
# #             "password":"123456",
# #             "other": "SEO"
# #             },
# #             "192.168.1.124":{
# #             "user":"root",
# #             "port": 22,
# #             "password":"123456",
# #             "other": "竞价"
# #             }
# # }
# # d.close()
# # # f = shelve .open('shelve_test')
# # # f["haha"]=[1,2,3]
# # # f.close()
# # # # f = shelve.open('shelve_test')
# # # f = shelve.open('shelve_test')
# # # def a(*args):
# # #     data = f["北京"]
# # #     data[args[0]] = {"user": args[1], "port": args[2], "password": args[3]}
# # #     f["北京"] = data
# # #     for i in f:
# # #         print(f[i])
# # # a("192.168.5.128","root",22,"123456")
# # #
# # #
# # # # num = 1
# # # # for i in f:
# # # #     print(f[i],type(i))
# # # #     print("{}.{}".format(num, i))
# # # #     num +=1
# #
# # import paramiko
# # # print("\33[31m#\33[0mwqeq")
# # #
# # f = shelve.open('shelve_test')
# # for i in f:
# #     print(f[i])
# import paramiko
# #
# # ssh = paramiko.SSHClient()
# # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # ssh.connect(hostname="192.168.5.129", port=22, username="root", password="123456")
# # while True:
# #     cmd = input("#").strip()
# #     if cmd == 0:
# #         continue
# #     elif cmd == "q":
# #         break
# #     stdin, stdout, stderr = ssh.exec_command(cmd)
# #     print(stdout.read().decode())
# #     print(stderr.read().decode())
# from multiprocessing import Process  # 导入进程模块
# import time
# import shelve,os
# basedir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# d = shelve .open(os.path.join(basedir,"data/password"))  # 打开一个文件
# d["上海"] = {"192.168.5.128":{
#             "user":"root",
#             "port":22,
#             "password":"123456",
#             "other":"阿里云"
#             },
#             "192.168.5.129":{
#             "user":"root",
#             "port": 22,
#             "password":"123456",
#             "other": "腾讯云"
#             }
# }
# d["北京"] = {"192.168.1.123":{
#             "user":"root",
#             "port":22,
#             "password":"123456",
#             "other": "SEO"
#             },
#             "192.168.1.124":{
#             "user":"root",
#             "port": 22,
#             "password":"123456",
#             "other": "竞价"
#             }
# }
# d.close()
a={1:2,2:2,3:2}
del a[2]
print(a)
