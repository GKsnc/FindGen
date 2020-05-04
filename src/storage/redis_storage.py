#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
区块信息的存储与查询。

使用前电脑需要安装redis数据库，使用第三方库redis。
程序中遍历区块链所产生的数据，也存放到redis中。（不同数据库）

@Time    :   2020/02/5
@Author  :   Kang

"""

import redis
import json

class Redis(object):
    # 设置连接属性
    host = 'localhost'
    port = 6379
    password = None

    # 默认连接0号数据库，有其他需求创建新的实例。
    def __init__(self, Host=None, db=0, Port=None, Password=None):
        # 如果传入参数，则用传入的参数修改默认属性
        self.host = Host if Host else self.host
        self.port = Port if Port else self.port
        self.password = Password if Password else self.password;
        # 连接数据库
        try:
            self.rds = redis.StrictRedis(host=self.host, port=self.port,db=db, password=self.password,decode_responses=True)
        except:
            pass # 连接失败的报错提示,看下redis会报什么错

    # 将区块信息存入数据库,成功返回1，失败返回0
    def set(self,flag,info):  # flag可以唯一确定一个区块，info为区块信息
        """
        :param flag:区块hash
        :param info：区块(json,字符)
        """
        # info = json.load(info)
        try:
            self.rds.set(flag, info)
            return 1
        except:
            raise ValueError('区块存入失败！')
    
    def jset(self,flag,info):
        '''
        :param flag:区块hash
        :param info：区块(python数据对象)
        '''
        info = json.dumps(info)
        try:
            self.rds.set(flag, info)
            return 1
        except:
            raise ValueError('区块存入失败！')

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
        '''
        存入是json字符串，返回解析为python对象的区块。
        '''
        #获取key对应的json字符串
        data = self.rds.get(key)
        #将key对应的son字符串解码为字典对象
        json_data = json.loads(data)
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
    redis = Redis()
    redis.set(1,1)
    redis.set(2,2)
    print(redis.get(1))
    print(redis.keys())
    #打开文件
    # with open('..\\..\\sample_block.json','r') as f:
    #     txt = f.read()
    # # 连接数据库
    # con = Redis(Host='127.0.0.1')
    # print(con.keys())
    # if con.set('block1',txt):
    #     print(con.get('block1'))
    #     block = con.jget('block1')
    # # print(block["Records"]["crec"]["id"])
    # con.set('姓名','张三')
    # print(con.keys())
    # con.delete('姓名')
    # print(con.keys())
    # # print(con.sync(ip='127.0.0.1'))
