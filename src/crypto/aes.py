#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
AES对称加密，加密与解密；AES加密类。

使用第三库pycryptodome（安装后要将crypto改为首字母大写Crypto）加密与解密；
内建库binascii将二进制与ascii进行转化

@File    :   aes.py
@Time    :   2020/01/31 17:05:42
@Author  :   ZHOU 
"""

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class AESCrypto:
    """
    aes加密类。

    传入密钥，来实例化。
    ：prama key：16，24，32字节长度的key（对应128，192，256位AES加密算法）
    """
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    # 加密方法
    def encrypto(self, text):
        """
        AES加密方法。

        将text用AES-128（16字节）加密，使用key为128位，需要对应。
        key为属性，实例化时创建。
        返回用16进制ASCII字符表示。
        """
        cryptor = AES.new(self.key, self.mode, self.key)
        length = 16
        count = len(text)

        if (count % length) != 0:
            add = length - (count % length)
        else:
            add = 0
        
        text = text + (b'\0' * add) #不足补空格（\0）
        self.ciphertext = cryptor.encrypt(text) # 属性绑定，在之后可以用到，虽然之后没有了

        return b2a_hex(self.ciphertext) #将二进制转化为ASCII码16进制表示

    # 解密方法
    def decrypto(self, text):
        """
        AES解密方法。

        将text用AES-128算法解密。key为属性，实例化时创建。
        返回解密后的字符串。
        """
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))

        return plain_text.rstrip(b'\0')


# 测试
if __name__ == "__main__":
    ENCRYPTO_KEY = b"45c7809a825c424f"

    ase = AESCrypto(ENCRYPTO_KEY)

    s = ase.encrypto(b'123')
    print(s)

    a = ase.decrypto(s)
    print(a)

    assert a == b"123"