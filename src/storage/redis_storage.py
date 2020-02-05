#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
区块信息的存储，传入区块信息后，存入数据库

使用前电脑需要安装redis数据库
使用第三方库redis

@Time    :   2020/02/5 
@Author  :   Kang 

"""

import redis

class Redis:

    #设置连接属性
    host = 'localhost'
    port = 6379
    db = 0      #数据库名称

    #连接数据库，可以传入参数设置连接属性，无参数传入则连接本机数据库
    def __init__(self,Host = None,Port = None,Db=None):

        #如果传入参数，则用传入的参数修改默认属性
        self.host = Host if Host else self.host
        self.port = Port if Port else self.port
        self.db = Db if Db else self.db

        #连接数据库
        try:
            self.rds = redis.StrictRedis(host=self.host, port=self.port, db=self.db)
        except:
            exit(-1)

    #将区块信息存入数据库
    def set(self,block,info):   #block为key值，info为value值，info是一个字典类型
        try:
            self.rds.hmset(block, info)
        except Exception as e:
            print(e)

    #获取指定key值得value值，value为字典类型
    def get(self,block,*keys):
        return self.rds.hmget(block,keys)

    #返回数据库中的所有key值
    def keys(self):
        return self.rds.keys()

    #返回key值为block的哈希对象中的字段值
    def hkeys(self,block):
        return self.rds.hkeys(block)

    #删除block区块
    def delete(self,block):
        self.rds.delete(block)

    #修改block区块中的filed的值，修改为value
    def modify(self,block,field,value):
        self.rds.hset(block,field,value)

    #将内存中的数据写入磁盘
    def save(self):
        self.rds.save()

#测试
if __name__ == '__main__':
    info = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'sender': "8527147fe1f5426f9dd545de4b27ee00",
    'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
    'amount': 5,
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    }

    r = Redis() #获取连接
    r.set('block01',info)   #写入区块信息
    print(r.get('block01','index','proof')) #查询‘block01’区块中的‘index’和‘proof’字段的信息

    r.modify('block01','amount','6')    #修改‘block01’区块中的‘amount’字段为‘6’
    print(r.get('block01','amount'))    

    print(r.keys())
    r.delete('block01') #删除区块
    print(r.keys())

    