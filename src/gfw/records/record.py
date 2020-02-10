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
    这个类主要来实现认证内容
    """

    def __init__(self, id, crec):
        """
        :param id: 商品id（哈希？）
        :param crec： 流通记录,CirculateRecord类
        """
        self.version=version
        self.id = id
        self.crec = crec


    # TODO(ZHOU) 签名验证机制，这个认证机制有包括gfw规则验证吗？


    # TODO(ZHOU) 返回一条完整的记录
    def get_record(self):
        pass

# 测试
if __name__=='__main__':
    # TODO(ZHOU) 生成一条记录


# TODO(ZHOU) 将商品ID的记录都找出来(之后在建立这个基础上，有一系列功能)