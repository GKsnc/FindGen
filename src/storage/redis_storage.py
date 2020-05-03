#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
区块信息的存储与查询。

使用前电脑需要安装redis数据库，使用第三方库redis。
redis只做存取目的。此类作为中间件，处理redis到blockchain。

@Time    :   2020/02/5
@Author  :   Kang

"""

import redis
import json

class Redis:
    # 设置连接属性
    host = '127.0.0.1'
    port = 6379
    # db = "findgen"  # 数据库名称
    db = '0'    # 数据库名称
    password = None

    # 连接数据库，可以传入参数设置连接属性，无参数传入则连接本机数据库
    def __init__(self, Host=None, Port=None, Db=None, Password=None):

        # 如果传入参数，则用传入的参数修改默认属性
        self.host = Host if Host else self.host
        self.port = Port if Port else self.port
        self.db = Db if Db else self.db
        self.password = Password if Password else self.password;

        # 连接数据库
        self.rds = redis.StrictRedis(host=self.host, port=self.port, password=self.password)


    # 将区块信息存入数据库,成功返回1，失败返回0
    def set(self,flag,info):  # flag可以唯一确定一个区块，info为区块信息
        """
        :param flag:区块hash
        :param info：区块
        """
        # info = json.load(info)
        try:
            self.rds.set(flag, info)
            return 1
        except:
            return 0

    # 获取指定key值的value值，value为json字符串
    def get(self, key):
        return self.rds.get(key)

    # 返回数据库中的所有key值
    def keys(self):
        return self.rds.keys()

    # 删除block区块
    def delete(self, block):
        self.rds.delete(block)

    # 将内存中的数据写入磁盘
    def save(self):
        self.rds.save()

    #将key对应的已编码的json字符串解析为字典对象返回
    def jget(self,key):
        #获取key对应的json字符串
        data = self.rds.get(key)
        #将key对应的son字符串解码为字典对象
        json_data = json.loads(data)
        #信息提取
        json_data = str(json_data)
        json_data = json_data.replace('[','')
        json_data = json_data.replace(']','')
        json_data = eval(json_data)
        return json_data

    #主从同步(非p2p),成功返回1，失败返回0
    def sync(self,ip = None,master_port = 6379 ):  #ip为主服务器ip
        if ip == None:
            return 0
        try:
            #主从复制
            self.rds.slaveof(host=ip,port=master_port)
            return 1
        except:
            return 0


# 测试
if __name__ == '__main__':
    # #打开文件
    # with open('..\\..\\sample_block.json','r') as f:
    #     txt = f.read()
    # # 连接数据库
    # con = Redis(Host='127.0.0.1',Db='0')
    # # print(con.keys())
    # if con.set('block1',txt):
    #     print(con.get('block1'))
    #     block = con.jget('block1')
    # # print(block["Records"]["crec"]["id"])
    # con.set('姓名','张三')
    # print(con.keys())
    # con.delete('姓名')
    # print(con.keys())
    # # print(con.sync(ip='127.0.0.1'))

    redis = Redis(Db='a')
    print(redis.db)
    # redis.set(1,1)
    redis.save()
    print(redis.keys())
