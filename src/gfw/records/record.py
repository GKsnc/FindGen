#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
生成商品流通记录。
记录：版本+流通内容+认证内容。

@File    :   records.py
@Time    :   2020/02/07 20:42:36
@Author  :   ZHOU 
"""

import hashlib
import json
from fastecdsa import ecdsa


version=0x # 流通规则版本

class Record(object):
    """
    商品流通记录（完整）。
    记录：版本+流通内容+认证内容。此类是包含全部，生成这样一条记录。
    这个类主要来实现认证内容；
    签名，公钥，只要能识别是谁发送就行了
    """

    def __init__(self, id, crec,pri_key,pub_key):
        """
        :param id: 商品id（哈希？）
        :param crec： 流通记录,CirculateRecord类
        """
        self.version=version
        self.id = id # 这个存在的必要
        self.crec = crec
        self.pri_key=pri_key # TODO(ZHOU) 这个先这样，之后完善，因为太多了
        self.pub_key=pub_key

    # TODO(ZHOU) 公钥私钥怎么录入，self录入
    # TODO(ZHOU) 签名验证机制，这个认证机制有包括gfw规则验证吗？
     def sign(self, priv_key, record):
        """
        签名记录
        :param priv_key: 私钥
        :param record: 需要签名的记录
        :return:
        """
        #TODO(ZHOU)是否需要之前所有记录 :param prev_txs: 之前的所有交易 
        sign_data=self.serialize()
        sign=ecdsa.sign(sign_data,priv_key) # TODO(ZHOU) 待测试
        self.sign=sign

    def vertify(self,record):
        """
        验证签名
        :param record:jilu
        """
        sign_data=self.serialize() # 这个不应该这样些，但就这样了，之后再完善
        ecdsa.verify(self.sign,sign_data,self.pub_key) # TODO(ZHOU) 待测试

    def serialize(self):
        """
        序列化记录。
        :return: json类型
        """
        k=dict()
        k['version']=self.version
        k['id']=self.crec.id
        k['circulate_flag']=self.crec.circulate_flag
        k['timestamp']=self.crec.time
        k['pub_key']=self.pub_key


    # TODO(ZHOU) 返回一条完整的记录
    def get_record(self):
        pass

# 测试
if __name__=='__main__':
    # TODO(ZHOU) 生成一条记录


# TODO(ZHOU) 将商品ID的记录都找出来(之后在建立这个基础上，有一系列功能)