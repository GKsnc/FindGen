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
from consensus.pow import ProofOfWork
from gfw import records
from core.blockchain import BlockChain


version = '0x0' #区块版本号

class Block(BlockChain):
    """
    区块。
    详见仓库Readme和系统结构说明。
    """

    def __init__(self,current_hash):
        '''
        :param current_hash:区块链最后一个区块的hash
        '''
        self.block = dict()
        self.prev_hash = current_hash

    def new_block(self, records):
        """
        创建新区块。
        : records : 多个记录数据；数组；
        : pre_hash : 上一个区块的Hash地址；字符串；
        : height : 块高；已删除；
        : return : 返回区块与该区块的hash。
        """
        block = {
            "Version" : version, # 16进制int
            "TimeStamp": int(time.time()), # int
            "MerkleRoot":'0x0',
            "Records": records, # 数组
            "PrevBlockHash": self.prev_hash, # 字符
            "Nonce": 0,
            # "Height": height
        }

        # 共识算法
        pow = ProofOfWork(block)

        b_hash, nonce = pow.run()
        block["Nonce"] = nonce

        self.block = block
        return b_hash,block

    def set_hash(self, block):
        """
        生成区块的hash
        """
        # 字典顺序要一致，不然hash值会不同
        block_string = json.dumps(block, sort_keys=True).encode()
        
        return hashlib.sha256(block_string).hexdigest()

    def verify(self):
        for re in self.block['Records']:
            if not record.vertify(re):
                # 这里是报错，还是返回一个信息？
                return "商品流通记录错误！"


def new_genesis_block(coinbase):
   pass
# TODO 币基交易（coinbase）的存在必要性