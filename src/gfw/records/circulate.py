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
    流通记录。
    记录：版本+流通内容+认证内容；此类是流通内容部分。
    流通内容：商品ID，时间戳，序号，流通标识。
        商品ID：唯一标识商品的一串数字。
        时间戳：记录生成时间。
        序号：此商品ID流通的序号。（用于标识流通环节）
        流通标识：4bit，用于标识流通环节的具体内容。
    """
    def __init__(self,id,circulate_flag):
        """
        :param id: 商品id
        :param circulate_flag: 流通标识（取值）
            生产：生产到销售：销售中：被购买：快递中：消费者手中：
        """
        self.id=id
        self.circulate_flag=circulate_flag

    def new_circulate_record(self，seq = 0):
        """
        创建一条流通记录。
        """
        self.time=time.time()
        self.seq=seq # TODO(ZHOU) 序号如何生成，序号代表；这得从头遍历，找到此ID之前有没有，才能生成这个序号啊
