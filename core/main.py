#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author = "susu"
import shelve,os,sys
import threading,time
import paramiko
basedir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d=shelve.open(os.path.join(basedir,"data/password"))
f=dict(d)
d.close()
#主机组类
class Group_Host(object):
    def __init__(self,name):
        self.name=name
        self.hosts=None
    def all_hosts(self):
        for i in self.hosts:
            print(i)
    def alter_hosts(self,*args):
        d = shelve.open(os.path.join(basedir,"data/password"))
        data=d[self.name]
        data[args[0]]={"user":args[1],"password":args[2], "port":args[3],"other":args[4]}
        d[self.name]=data
        d.close()

    @staticmethod
    def list_group_hosts(groupname):
        group_hosts = f[groupname]
        return group_hosts

    @staticmethod
    def del_hosts(hostname):
        d = shelve.open(os.path.join(basedir,"data/password"))
        data=d[Single_Host.is_exist(hostname)]
        del data[hostname]
        print("已成功删除【{}】主机".format(hostname))
        d[Single_Host.is_exist(hostname)]=data
        d.close()

#主机类
class Single_Host(object):
    def __init__(self,ip):
        self.ip=ip
        self.begin()
    def begin(self):
        for i in f:
            if self.ip in f[i]:
                self.group=i
                self.user=f[i][self.ip]["user"]
                self.port=f[i][self.ip]["port"]
                self.password=f[i][self.ip]["password"]
                break
    #执行命令
    def cmd_cmd(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.ip, port=self.port, username=self.user, password=self.password)
        while True:
            cmd=input("#").strip()
            if cmd==0:continue
            elif cmd=="q":break
            stdin, stdout, stderr = ssh.exec_command(cmd)
            print(stdout.read().decode())
            print(stderr.read().decode())
        ssh.close()
    #下载文件
    def cmd_get_put(self,cmd):
        try:
            if self.ip not in os.listdir(basedir+"/downloads"):
                os.mkdir(os.path.join(basedir,"downloads",self.ip))
            transport = paramiko.Transport(self.ip,self.port)
            transport.connect(username=self.user, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(transport)
            if cmd.startswith("put"):
                filename = cmd.split()[1]
                sftp.put(basedir+"/uploads/"+filename,cmd.split()[2]+"/"+filename)
                print("{}已成功上传到{}".format(filename,self.ip))
            elif cmd.startswith("get"):
                filename = cmd.split("/")[-1]
                sftp.get(cmd.split()[1], os.path.join(basedir,"downloads",self.ip,filename))
                print("已成功从{}下载{}".format(self.ip,filename))
            transport.close()
        except TimeoutError as e:
            print(self.ip,e)

    @staticmethod
    def is_exist(hostname):
        for i in f:
            if hostname in f[i]:
                return i
        else:
            return 0

    def interative(self):
        while True:
            choice3=input("1.执行命令\n2.上传/下载文件.\n>>")
            if choice3.isdigit():
                if choice3=="1":
                    self.cmd_cmd()
                elif choice3=="2":
                    print("get /url/filename #下载文件\nput filename /url/ #上传文件")
                    while True:
                        a = input(">>").strip()
                        if a.startswith("put") or a.startswith("get"):
                            self.cmd_get_put(a)
                        elif a=="q":break
                        elif a == "b":sys.exit()
                        else:
                            continue
            elif choice3== "q":
                break
            elif choice3== "b":
                sys.exit()
            else:
                print("输入错误")

#多台主机命令执行-线程函数
def cmd_cmd(ip,cmd):
    try:
        host_obj=Single_Host(ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host_obj.ip, port=host_obj.port, username=host_obj.user, password=host_obj.password)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print("########################{}##############################".format(host_obj.ip))
        print(stdout.read().decode())
        print(stderr.read().decode())
        ssh.close()
    except TimeoutError as e:
        print(ip,e)

#多台主机下载-线程函数
def cmd_g_p(ip,cmd):
    host_obj= Single_Host(ip)
    host_obj.cmd_get_put(cmd)

def run():
    while True:
        choice=input("1.单台主机管理\n2.主机批量管理\n3.新增主机\n4.删除主机\n>>")
        if choice=="1":
            hostname=input("服务器IP：")
            if hostname==0:continue
            if Single_Host.is_exist(hostname):
                h=Single_Host(hostname)
                h.interative()
                continue

        elif choice == "2":
            num = 1
            a = []
            for i in f:
                print("{}.{}".format(num, i))
                a.append(i)
                num += 1
            choice1 = input("选择主机组：")
            if int(choice1) <= len(a):
                while True:
                    choice2=input("1.查看{}组主机\n2.批量执行命令\n3.批量上传/下载文件\n>>".format(a[int(choice1) - 1]))
                    group_hosts=Group_Host.list_group_hosts(a[int(choice1) - 1])
                    all_hosts = [ip for ip in group_hosts]
                    if choice2.isdigit():
                        if choice2=="1":
                            for key in group_hosts:
                                print("{}    {}".format(key, group_hosts[key]["other"]))
                        elif choice2=="2":
                            while True:
                                cmd = input("\33[31m#\33[0m").strip()
                                if cmd == 0:
                                    continue
                                elif cmd == "q":
                                    break
                                elif cmd == "b":
                                    sys.exit()
                                for i in all_hosts:
                                    i = threading.Thread(target=cmd_cmd, args=(i,cmd,))
                                    i.start()
                                    i.join()
                        elif choice2=="3":
                            print("get /url/filename #下载文件\nput filename /url/ #上传文件")
                            while True:
                                cmd1 = input(">>").strip()
                                if cmd1.startswith("put") or cmd1.startswith("get"):
                                    p_obj_list = list()
                                    #生成线程处理请求
                                    for i in all_hosts:
                                        p=threading.Thread(target=cmd_g_p,args=(i,cmd1,))#产生一个线程实例
                                        p.start()
                                        p_obj_list.append(p)
                                    for p in p_obj_list:
                                        p.join()
                                elif cmd1 == "q":
                                    break
                                elif cmd1 == "b":
                                    sys.exit()
                                else:
                                    continue
                    elif choice2 == "q":
                        break
                    elif choice2 == "b":
                        sys.exit()

        elif choice == "3":
            newip=input("IP:").strip()
            if newip==0 or len(newip.split("."))!=4:
                print("格式错误，请重新输入")
                continue
            user=input("user:").strip()
            password=input("password:")
            while True:
                port=input("port:").strip()
                if port.isdigit():
                    port=int(port)
                    break
            other=input("备注:")
            num = 1
            a = []
            for i in f:
                print("{}.{}".format(num, i))
                a.append(i)
                num += 1
            group=input("选择分组：")
            if int(group) <= len(a):
                group_obj=Group_Host(a[int(group)- 1])
                group_obj.alter_hosts(newip,user,password,port,other)
                continue

        elif choice == "4":
            hostname=input("输入需要删除的主机IP：")
            if Single_Host.is_exist(hostname):
                Group_Host.del_hosts(hostname)
            else:
                print("主机不存在，无需删除")














