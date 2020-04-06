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
from . import circulate

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
        :param id:商品id #这个改成记录编号？
        :param pri_key: 参与者私钥
        :param pub_key: 参与者公钥
        """
        self.id=id
        self.version=version
        self.pri_key=pri_key
        self.pub_key=pub_key

    def new_record(self,circulate_flag):
        """
        生成一条记录。
        版本，流通记录，验证脚本。
        :param circulate_flag: 二进制数，流通标识
        """

        # TODO(ZHOU) 此商品ID之前所有的流通记录,先搜索，判断；这件事，可以在初始化是，完成，或者空闲时间，完成，；这个功能实现在blockchain模块中
        id_pre_crecord=list()


        self.new=dict()
        crec=circulate.CirculateRecord(self.id,self.version)

        self.new['version']=version
        self.new['crec']=crec.new_circulate_record(circulate_flag,id_pre_crecord)
        self.new['pub_key']=self.pub_key
        self.new['sign']=self.sign(self.pri_key,self.new) # 签名时没有sign字段，运行函数后才生成

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
        r,s=ecdsa.sign(sign_data,priv_key) 
        signature = "".join([str(r), str(s)])
        
        return signature


    def serialize(self, record):
        """
        #序列化记录。
        # :return: 返回json
        """

        return json.dumps(record,sort_keys=True)

    def vertify(self,record):
        """
        验证签名。
        :param record:一条记录
        """
        sign_data=self.serialize() # 这个不应该这样些，但就这样了，之后再完善
        return ecdsa.verify(self.sign,sign_data,self.pub_key)


# 测试
if __name__=='__main__':
    # 生成公钥私钥对 
    rec=Record(0xe750c03ec430596c40000,55248630652735703223152638700518970040653913471915361658953299428523546807998,5647229235116611234207182631713135971966847906144383840806022238380289234910871917806701283430577159806922743362718786414358965919409008443583248119700767)
    a=rec.new_record(0x0)

# TODO(ZHOU) 公私钥对的使用,保存方式