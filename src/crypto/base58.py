#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
base58

@File    :   base58.py
@Time    :   2020/03/18 21:33:08
@Author  :   ZHOU 
"""


Base58Alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58decode(data):
    """
    base58 解码
    :param data:
    :return:
    """
    result = 0

    for d in data:
        charIndex = Base58Alphabet.find(d)
        result = result * len(Base58Alphabet)
        result = result + charIndex

    decoded = hex(result)

    # if data[0] == Base58Alphabet[0]:
    #     decoded = str(0x0) + decoded

    return decoded


def base58encode(data):

    result = []
    # 首先将字符串转换成十六进制数
    x = int(data, 16)
    base = 58

    zero = 0

    while x != zero:
        x, mod = divmod(x, base)
        result.append(Base58Alphabet[mod])

    # if data[0] == str(0x0):
    #     result.append(Base58Alphabet[0])

    # 利用自己实现的reverse算法，当然实际工作中直接调用python标准库中的函数
    return "".join(reverse(result))


def reverse(res):
    """
    反转列表
    :param res:
    :return:
    """

    if len(res) <= 1:
        return res

    length_half = int(len(res) / 2)
    length = len(res) - 1

    for i in range(length_half):
        tmp = res[i]
        res[i] = res[length-i]
        res[length-i] = tmp

    return res
