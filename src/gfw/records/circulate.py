#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
流通记录。
record类用于规划这条记录的格式并使用。（偏向区块链）
CirculateRecord类用于规划这条记录生成规则。（偏向GFW模型）

@File    :   circulate_flag.py
@Time    :   2020/02/09 19:10:57
@Author  :   ZHOU 
"""

import time


class CirculateRecord(object):
    """
    流通记录类，是用来处理流通记录的。

    记录：版本+流通内容+认证内容；此类是流通内容部分。
    流通内容：商品ID，时间戳，序号，流通标识。
        商品ID：唯一标识商品的一串数字。
        时间戳：记录生成时间。
        序号：此商品ID流通的序号。（用于标识流通环节）
        流通标识：4bit，用于标识流通环节的具体内容。
    """
    def __init__(self, id, version):
        self.id = id #商品ID
        self.version = version

    def new_circulate_record(self, circulate_flag, pre_crec):
        """
        创建一条流通记录。

        :param id: 商品id
        :param circulate_flag: 流通标识（取值）
            生产(0000)：生产到销售(0001)：销售中(0010)：被购买(0011)：快递中(0100)：消费者手中(0101)：
        :param pre_rec:此商品ID之前的记录，list类型，记录是dict类型。
        """
        flag=self.valid_crec(pre_crec)
        new = dict()

        if flag is False:
            raise ValueError('商品流通值有误!')
        elif circulate_flag==b'0000':
            new['seq']=0
        else:
            new['seq']=sorted(pre_crec,key=dict.get('seq'))[-1]['seq']+1 # 对列表中字典进行排序,选择最后一个seq+1；bug如果之前没有记录会出错，不过那是特使的记录，在此不表
        
        new['id']=id
        new['circulate_flag']=circulate_flag
        new['time']=int(time.time())

        return new

    # v0 版本规则验证
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
