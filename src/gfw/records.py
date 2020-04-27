#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
生成商品流通记录。
记录：记录头+流通记录。

@File    :   records.py
@Time    :   2020/02/07 20:42:36
@Author  :   ZHOU 
"""

import hashlib
import json
import time
from fastecdsa import ecdsa

version=0x0001 # 记录版本（流通规则）

class Records(object):
    """
    记录。
    记录：记录头+流通记录。详见仓库数据结构。
    """

    def __init__(self,pri_key, pub_key):
        """
        :param pri_key: 参与者私钥
        :param pub_key: 参与者公钥
        #TODO 使用公私钥地址等，统一使用一个对象（参与者）？类
        """
        self.version=version
        self.pri_key=pri_key
        self.pub_key=pub_key

    def new_record(self,id,circulate_flag,adress,precord=[]):
        """
        生成一条记录。
        :param id: 商品ID(单个),批量商品(TODO)
        :param circulate_flag: 16进制，流通标识详见README。
        :param adress: 标准地址.
        :param precord: 根据商品ID或交易标识（recid）查找的之前的记录。
        """
        record = dict()
        #生产记录
        if circulate_flag==0x000f:
            crec={
                'goods_id':id,
                'seq':0,
                'circulate_flag':circulate_flag,
                'time':int(time.time()),
                'adress':adress
                }
            record['crec']=crec
            record['version']=self.version
            record['pub_key']=self.pub_key
            record['recid']=hashlib.sha256(self.serialize(record)).hexdigest() # hash记录，成为交易标识
            record['sign']=self.sign(self.pri_key,record)
            return record
        
        # 交易记录
        crec = dict()
        crec['goods_id'] = id
        crec['seq'] = precord[-1]['crec']['seq']+1
        crec['circulate_flag'] = circulate_flag
        crec['time'] = int(time.time())
        crec['address'] = adress
        record['crec'] = crec
        record['version'] = self.version
        record['pub_key'] = self.pub_key
        record['recid'] = precord[-1]['recid']
        record['sign'] = self.sign(self.pri_key,record)
        
        return record

    # 创建流通记录
    def new_circulate_record(self, id,circulate_flag,adress,seq):
        """
        创建一条流通记录。

        :param id: 商品id
        :param circulate_flag: 流通标识
        :param pre_rec:此商品ID之前的记录，list类型，记录是dict类型。待定 TODO
        :param adress:标准地址
        :param seq:流通索引。
        """
        #生产记录
        if circulate_flag==0x000f:
            crec={
                'goods_id':id,
                'seq':0,
                'circulate_flag':circulate_flag,
                'time':int(time.time()),
                'adress':adress
                }
            return crec

        # 普通交易记录
        crec={
                'goods_id':id,
                'seq':seq,
                'circulate_flag':circulate_flag,
                'time':int(time.time()),
                'adress':adress
                }
        # 交易记录
        #flag=self.valid_crec(pre_crec) 验证
        #new['seq']=sorted(pre_crec,key=dict.get('seq'))[-1]['seq']+1 # 对列表中字典进行排序,选择最后一个seq+1；bug如果之前没有记录会出错，不过那是特使的记录，在此不表
        return crec
        
        return new
 
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

    def record_rule(self):
        """
        流通规则.
        #TODO(ZHOU) 自定义流通规则接口
        """
        pass

    # 全局流通规则验证
    def valid_crec(self,pre_crec):
        """
        GFW模型规则检查。
        v0版本：只有三个标识，顺序不变

        :param pre_crec: 之前的流通记录,包含多个dict的列表。
        """

        # 假设pre_crec为包含多个crec的列表
        for d in pre_crec:
            if d['circulate_flag']==b'0000' and d['seq']==b'0':
                continue
            elif d['circulate_flag']==b'0001' and d['seq']==b'1':
                continue
            elif d['circulate_flag']==b'0011' and d['seq']==b'2':
                continue

            # 不满足规则，这条记录就不符合规范
            return False

#TODO(ZHOU) 规则编写；初步的三条规则，进一步，需要什么，等需要什么，在编写。



# 测试
if __name__=='__main__':
    # 生成公钥私钥对 
    rec=Records(0xe750c03ec430596c40000,55248630652735703223152638700518970040653913471915361658953299428523546807998,5647229235116611234207182631713135971966847906144383840806022238380289234910871917806701283430577159806922743362718786414358965919409008443583248119700767)
    a=rec.new_record(0x0)

# TODO(ZHOU) 公私钥对的使用,保存方式