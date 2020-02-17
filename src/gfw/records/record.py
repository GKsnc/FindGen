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
from gfw.records.circulate import CirculateRecord

version=0x0000 # 流通规则版本

class Record(object):
    """
    商品流通记录（完整）。
    记录：版本+流通内容+认证内容。此类是包含全部，生成这样一条记录。
    这个类主要来实现认证内容；
    签名，公钥，只要能识别是谁发送就行了
    """

    def __init__(self, id, pri_key, pub_key):
        """
        :param id:商品id
        :param pri_key: 参与者私钥
        :param pub_key: 参与者公钥
        """
        self.id=id
        self.pri_key=pri_key
        self.pub_key=pub_key

    def new_record(self,circulate_flag):
        """
        生成一条记录。
        版本，流通记录，验证脚本。
        :param circulate_flag: 二进制数，流通标识
        """

        # TODO(ZHOU) 此商品ID之前所有的流通记录,先搜索，判断
        id_pre_crecord=list()


        self.new['version']=version
        self.new['crec']=CirculateRecord.new_circulate_record(self.id,circulate_flag,id_pre_crecord)
        self.new['pub_key']=self.pub_key
        self.new['sign']=self.sign(self.pri_key,self.new)

        return self.new
 
    # 签名验证机制
    def sign(self, priv_key, record):
        """
        签名记录
        :param priv_key: 私钥
        :param record: 需要签名的记录
        :return:
        """

        sign_data=self.serialize(record)
        sign=ecdsa.sign(sign_data,priv_key) 
        
        return sign


    def serialize(self, record):
        """
        #序列化记录。
        # :return: dict类型
        """
        k=dict()
        k['version']=record['version']
        k['id']=record['crec']['id']
        k['seq']=record['crec']['seq']
        k['circulate_flag']=record['crec']['circulate_flag']
        k['time']=record['crec']['time']
        k['pub_key']=record['pub_key']

        return k

    def vertify(self,record):
        """
        验证签名
        :param record:jilu
        """
        sign_data=self.serialize() # 这个不应该这样些，但就这样了，之后再完善
        ecdsa.verify(self.sign,sign_data,self.pub_key)