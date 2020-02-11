#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
区块链中区块部分。
用于创建区块。

@File    :   block.py
@Time    :   2020/02/11 14:07:24
@Author  :   ZHOU 
"""

import time
import hashlib
import json
# from consensus.proof_of_work import ProofOfWork 共识算法
# from core.transactions.transaction import Transaction 记录，记录生成程序


version = 0x #区块版本号

class Block(object):
    """
    区块。

    block = {
        # 区块头
        "Version" : ""， # 四字节，区块头的版本号，用于跟踪版本和协议更新
        "PrevBlockHash" : "", # 记录了该区块的上一个区块的Hash地址
        "MerkleRoot" : "", # 记录了该区块中记录的merkle树根的哈希值
        "Timestamp": datetime.now(), # 记录了该区块的创建时间戳；
        "Height": "", # 块高
        "Nonce": "", # 记录了用于证明工作量的计算参数
        # 其他用于共识算法的参数，待定

        # 区块体
        "Records" : "", # 多个记录数据(多个record？)
    }
    """

    def __init__(self):
        self.block = dict()

    def new_block(self, records, prev_hash, height):
        """
        创建新区块。
        : records : 多个记录数据
        : pre_hash : 上一个区块的Hash地址
        : height : 块高
        : return : 返回区块
        """
        block = {
            "Version" : version,
            "TimeStamp": int(time.time()),
            "Records": records,
            "PrevBlockHash": prev_hash,
            "Nonce": 0,
            "Height": height
        }

        # 共识算法 # TODO(ZHOU) 共识算法
        # pow = ProofOfWork(block)

        # b_hash, nonce = pow.run()
        # block["Hash"] = b_hash
        # block["Nonce"] = nonce

        self.block = block
        return block

    def set_hash(self, block):
        """
        生成区块的hash
        """
        # 字典顺序要一致，不然hash值会不同
        block_string = json.dumps(block, sort_keys=True).encode()
        
        return hashlib.sha256(block_string).hexdigest()


# TODO(ZHOU) 创建一个区块，等记录生成程序完成
def new_genesis_block(coinbase):
   pass
# 币基交易（coinbase）的存在必要性