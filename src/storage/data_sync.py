#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import redis


"""
不同主机的数据库数据同步

使用前电脑需要安装redis数据库
使用第三方库redis

@Time    :   2020/02/16 
@Author  :   Kang 

"""

class Sync:
    '''
    运行命令 Sync(master_ip) 后本机的redis数据库会自动向master_ip 主机同步数据
    '''
    #默认的主服务器端口
    master_port = 6379
    slave_port = 6379

    #可以通过参数改变参数，无参数则为默认
    def __init__(self,ip,master_port = None,slave_port = None):
        self.master_ip = ip
        self.port = master_port if master_port else self.master_ip
        self.slave_port = slave_port if slave_port else self.slave_port

        #建立连接
        self.slave = redis.StrictRedis(host='localhost',port=self.slave_port)
        self.master = redis.StrictRedis(host=self.master_ip,port=self.master_port)

        #主从复制
        self.slave.slaveof(host=self.master_ip,port=self.master_port)

#测试
# Sync('192.168.1.101')
