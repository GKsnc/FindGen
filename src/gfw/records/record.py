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

    def verify(self, prev_rcs):
        """
        校验先前的所有输入是否合法。
        # TODO（ZHOU） 校验的实现
        :param prev_rcs: 之前的记录（具体指什么未知）
        :return:
        """

        if not prev_txs[vin.txid].ID:
            raise ValueError(
                "Error: previous transaction is not correct."
            )

        tx_copy = self.trimmed_copy()
        for inId, vin in enumerate(tx_copy.Vin):
            prev_tx = prev_txs[vin.txid]
            tx_copy.Vin[inId].signature = ""
            tx_copy.Vin[inId].pubkey = prev_tx.Vout[vin.vout].pub_key_hash

            sign_len = len(vin.signature)
            # x = vin.pubkey[:(sign_len/2)]
            # y = vin.pubkey[(sign_len/2):]
            #
            # raw_pub_key = ecdsa.verify()
            pass

        return True

    def sign(self, priv_key, prev_rcs):
        """
        签名记录。
        # TODO（ZHOU） 怎么签名，签名什么？

        :param priv_key: 私钥
        :param prev_rcs: 之前的所有记录 # TODO（ZHOU）这个东西怎么获取
        :return:
        """

        # TODO（ZHOU） 这个判断的实现
        if not prev_txs[vin.txid].ID:
            raise ValueError(
                    "Error: previous record is not correct."
                )

        tx_copy = self.trimmed_copy()
        for inId, vin in enumerate(tx_copy.Vin):
            prev_tx = prev_txs[vin.txid]
            tx_copy.Vin[inId].signature = ""
            tx_copy.Vin[inId].pubkey = prev_tx.Vout[vin.vout].pub_key_hash

            r, s = ecdsa.sign(tx_copy, priv_key)
            signature = "".join([str(r), str(s)])
            self.Vin[inId].signature = signature
            tx_copy.Vin[inId].pubkey = ""
