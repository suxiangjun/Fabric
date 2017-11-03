#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author = "susu"

import shelve,os
d = shelve .open('shelve_test')  # 打开一个文件
d["上海"] = {"192.168.5.128":{
            "user":"root",
            "port":22,
            "password":"123456",
            "other":"阿里云"
            },
            "192.168.5.129":{
            "user":"root",
            "port": 22,
            "password":"123456",
            "other": "腾讯云"
            }
}
d["北京"] = {"192.168.1.123":{
            "user":"root",
            "port":22,
            "password":"123456",
            "other": "SEO"
            },
            "192.168.1.124":{
            "user":"root",
            "port": 22,
            "password":"123456",
            "other": "竞价"
            }
}
d.close()
# f = shelve .open('shelve_test')
# f["haha"]=[1,2,3]
# f.close()
# # f = shelve.open('shelve_test')
# f = shelve.open('shelve_test')
# def a(*args):
#     data = f["北京"]
#     data[args[0]] = {"user": args[1], "port": args[2], "password": args[3]}
#     f["北京"] = data
#     for i in f:
#         print(f[i])
# a("192.168.5.128","root",22,"123456")
#
#
# # num = 1
# # for i in f:
# #     print(f[i],type(i))
# #     print("{}.{}".format(num, i))
# #     num +=1

import paramiko
# print("\33[31m#\33[0mwqeq")
#
f = shelve.open('shelve_test')
for i in f:
    print(f[i])