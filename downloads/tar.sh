#!/bin/bash
#write by suxiangjun 2016.1213 
time=`date +%Y%m%d`
dump=/usr/local/mysql/bin/mysqldump
read -p "请输入你的网站名：" n
read -p "打包文件发送的地址: " p
read -p "需要备份数据库吗？y/n(默认为n) " z
tar1(){
if [ -z $x.sql ];then
exit
else
tar -zpcvf "$n""$time".tar.gz .
fi
}
case $z in
	Y|y)read -p "请输入数据库名: " x && $dump -uroot -p $x>$x.sql&&echo "已备份数据库"&& tar1;;
	N|n)tar -zpcvf "$n""$time".tar.gz . ;;
	*)tar -zpcvf "$n""$time".tar.gz . ;;
esac
sleep 3
scp "$n""$time".tar.gz $p:/home
