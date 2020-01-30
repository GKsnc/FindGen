#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
哈希函数。
常见哈希算法可在python内建模块hashlib找到，包括MD5，SHA1等。

@File    :   hash.py
@Time    :   2020/01/30 19:54:14
@Author  :   ZHOU 
"""

import hashlib


def hash_pub_key(pub_key):
    """
    对公钥pub_key二次哈希（sha256+ripemd160）返回二次哈希后的值Public Key Hash（比特币术语）
    """

    if not isinstance(pub_key, (bytes, bytearray, str)):
        raise TypeError("pub 类型错误，需要str 或者bytes类型！")

    if isinstance(pub_key, str):
        pub_key = pub_key.encode("utf-8")

    # sha256 hash
    pub_sha256 = hashlib.sha256(pub_key).hexdigest()

    # ripemd160
    obj = hashlib.new("ripemd160", pub_sha256.encode('utf-8'))
    ripemd160_value = obj.hexdigest()

    return ripemd160_value

if __name__=='__main__':
    print(hash_pub_key("12345"))
