#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
工作量证明，共识算法。

@File    :   pow.py
@Time    :   2020/02/28 13:53:39
@Author  :   ZHOU 
"""

import hashlib
from settings import maxNonce, targetBits
# from utils.merkletree import MerkleTree


class ProofOfWork:
    """
    工作量证明算法
    """

    def __init__(self, block, nonce=0):
        self.nonce = nonce

        if not isinstance(block, dict):
            raise TypeError

        self.block = block
        self.target = 1 << (256-targetBits)

    def hash_txs(self):
        """
        将block的transactions 信息hash加密, 并且用merkle tree来存储交易信息。
        :return:
        """

        tree = MerkleTree(self.block["Transactions"])
        tree.new_tree()

        return tree.root.data

    def prepare_data(self):
        """
        准备计算的数据
        :return:
        """

        timestamp = hex(self.block["TimeStamp"])[0]

        data = "".join([
            self.block["PrevBlockHash"],
            # TODO(ZHOU) self.hash_txs()   #Merkle树
            timestamp,
            hex(targetBits),
            hex(self.nonce)
        ])

        return data

    def run(self):
        print("Mining  a new block...")

        hash_v = ""
        while self.nonce < maxNonce:
            data = self.prepare_data()

            hash_v = hashlib.sha256(data.encode("utf-8")).hexdigest()

            print("-----> is mining ... %s" % hash_v)

            if int(hash_v, 16) <= self.target:
                break
            else:
                self.nonce += 1
        print("\n")

        return hash_v, self.nonce

    def validate(self):
        data = self.prepare_data()
        hash_v = hashlib.sha256(data.encode('utf-8')).hexdigest()

        print(int(hash_v, 16), self.target)

        if int(hash_v, 16) <= self.target:
            return True
        return False


# TODO(ZHOU) 适用gfw模型的共识算法；暂时先用这套算法
# pow也是可以的，但会产生不必要计算，比如生产商发布商品时，只要它满足一定的资质就可以发布商品，我们也能追踪到是他发布的，但如果它造假呢？
#怎么造假，假设给它发布区块的权利，商品数量不对，比如：将商品数量增多，而实际上并没有那么多，到最后会有一些商品ID是没有对应商品的
#先放放，这个问题，我先将最初版的程序做出来