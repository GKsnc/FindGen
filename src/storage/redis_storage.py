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
    host = 'localhost'
    port = 6379
    db = findgen  # 数据库名称
    password = None

    # 连接数据库，可以传入参数设置连接属性，无参数传入则连接本机数据库
    def __init__(self, Host=None, Port=None, Db=None, Password=None):

        # 如果传入参数，则用传入的参数修改默认属性
        self.host = Host if Host else self.host
        self.port = Port if Port else self.port
        self.db = Db if Db else self.db
        self.password = Password if Password else self.password;

        # 连接数据库
        self.rds = redis.StrictRedis(host=self.host, port=self.port, db=self.db, password=self.password)

    # 将区块信息存入数据库
    def set(self, block,info):  # block可以唯一确定一个区块，info为区块信息
        """
        :param block:区块hash
        :param info：区块
        """
        self.rds.set(block,info) # 返回值？

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

    # 清空数据库
    def clear(self):
        self.rds.flushall()

    #将key对应的已编码的json字符串解码为字典对象
    def jget(self,key):
        #获取key对应的json字符串
        data = self.rds.get(key)
        #将key对应的son字符串解码为字典对象
        json_data = json.loads(data)
        json_data = dict(json_data)
        #将列表json_data['Records']转化为字典
        json_data['Records'] = json_data.get('Records')[0]
        return json_data


# 测试
if __name__ == '__main__':
    #打开文件
    with open('..\\..\\sample_block.json','r') as f:
        txt = f.read()

    #连接数据库
    con = Redis('127.0.0.1',6379,0)
    #清空数据库
    con.clear()
    #将一个区块存入数据库
    con.set('block0',txt)
    #输出说有key值
    print(con.keys())
    #将key为'block0'的value值返回
    block = con.jget('block0')
    #查询信息
    print(block['Records']['crec']['id'])
    print(block['Version'])