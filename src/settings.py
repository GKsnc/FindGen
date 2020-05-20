#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
pow共识算法相关设置。

@File    :   settings.py
@Time    :   2020/02/28 14:18:43
@Author  :   ZHOU 
"""


maxNonce = 1 << 63 - 1 # 最大nonce
targetBits = 4 # 目标（4个0，生成的区块hash首位为0）