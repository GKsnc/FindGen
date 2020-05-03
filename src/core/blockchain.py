#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
区块链中区块链部分。

包括区块链的存取,对区块链的操作,区块上链.

@File    :   blockchain.py
@Time    :   2020/02/11 15:03:53
@Author  :   ZHOU 
"""

import json
from block import Block
from storage.redis_storage import Redis
from consensus.pow import ProofOfWork


class BlockChain:
    """
    区块链。
    核心，对区块链的存取，查询等操作。
    """
    def __init__(self):
        # 首先存储块在内存中
        # 然后再存储在redis
        # self.blocks = []

        self.blocks = Redis()
        self.current_hash = None # TODO 当前hash

    def add_block(self, new_block):
        """
        添加block到链上
        :param new_block:
        :return:
        """
        # 使用区块的hash作为key
        # redis中L是最后一个区块的hash的key
        pow = ProofOfWork(new_block, new_block["Nonce"])
        if pow.validate(): # TODO(ZHOU) 了解如何验证合法性(validate)
            # self.blocks.append(new_block)
            if not self.blocks.get(new_block["Hash"]): # 不能有相同hash加入
                self.blocks.set(new_block["Hash"], new_block)
                self.blocks.set("L", new_block["Hash"])

    def get_block(self, block_hash):
        block = self.blocks.get(block_hash)
        if block:
            return eval(block.decode)

        else:
            return "区块不存在"
    
    def find_urc(self):
        """
        查找所有的未完成的记录（urc）。
        :return urc:类json格式
        """
        urc=dict()
        finished_urc=dict()
        while True:
            try:
                last_block = next(self.iterator())
            except StopIteration:
                genesis_hash = self.blocks.get(self.current_hash).decode()
                last_block = eval(genesis_hash)

                coinbase_tx = last_block["Transactions"]
                for tx in coinbase_tx:

                    rc_json = json.loads(tx.decode())

                    urc[rc_json["ID"]] = []

                    for out in rc_json["Vout"]:
                        if not spent_tx[rc_json["ID"]]:
                            urc[rc_json["ID"]].append(out)

                break     # 程序退出边界条件

            for rc in last_block["Records"]:
                rc_json = json.loads(rc.decode())
                urc[rc_json["goods_id"]] = []
                urc[rc_json["ID"]].append(rc_json['crec'])       

        return urc

    def iterator(self):
        # 创世区块的迭代？
        if not self.current_hash:
            self.current_hash = self.blocks.get("L")

        last_block = self.blocks.get(self.current_hash).decode() #为什么要decode？

        if eval(last_block)["PrevBlockHash"]: # 这个eval会有漏洞吗，需注意一下
            self.current_hash = eval(last_block)["PrevBlockHash"]
            yield eval(last_block)

    def find_rc(self, gid):
        """
        根据商品id找到交易信息
        :param gid:商品id
        :return:
        """
        while True:
            try:
                block = next(self.iterator())
            except StopIteration:
                genesis_hash = self.blocks.get(self.current_hash).decode()
                last_block = eval(genesis_hash)

                coinbase_rc = last_block["Records"]
                for rc in coinbase_rc:
                    rc_obj = json.loads(rc.decode()) # 出现了，json的load，那么所有这些都用json
                    if rc_obj["id"] == gid:
                        return rc
                break

            for rc in block["Records"]:
                rc_obj = json.loads(rc.decode())

                if rc_obj["id"] == gid:
                    return rc

            return "未找到交易信息"


    # def get_height(self):
    #     last_hash = self.blocks.get("l")
    #     last_block = self.blocks.get(last_hash).decode()

    #     return eval(last_block)["Height"]


    # def all_hashes(self):

    #     return [b for b in self.blocks.keys() if b != 'l']

    # def mine_block(self, transactions):

    #     """
    #     根据链上的最后一个区块的hash值，生成一个新的block
    #     :param transactions:
    #     :return:
    #     """
    #     lash_hash = self.blocks.get("l").decode()
    #     height = self.get_height()
    #     b = Block()
    #     new_block = b.new_block(transactions, lash_hash, height + 1)
    #     return new_block

    # def sign_transaction(self, tx):
    #     """
    #     交易信息加密
    #     :return:
    #     """
    #     pass

    # def verify_transaction(self, tx):
    #     """
    #     交易信息解密
    #     :return:
    #     """
    #     pass

    # def print_blockchain(self):
    #     """
    #     输出blockchain

    #     :return:
    #     """
    #     # for b in self.blocks:
    #     #     print(b)

    #     blocks = []

    #     for b in self.blocks.keys():

    #         if b.decode() != 'l':
    #             v = self.blocks.get(b).decode()
    #             blocks.append(eval(v))
    #     return blocks
