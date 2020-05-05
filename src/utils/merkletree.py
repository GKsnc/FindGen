#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
MerkleTree算法。
具体参考：https://www.cnblogs.com/fengzhiwu/p/5524324.html

@File    :   merkletree.py
@Time    :   2020/03/06 20:19:42
@Author  :   ZHOU 
"""

import hashlib


class MerkleTree(object):
    """
    - doc  Merkle tree
    """

    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError("data must be a bytes list")
        
        if not data:
            raise ValueError("记录不能为空！")

        self.data = data
        self.nodes = []
        self.root = None

    def new_tree(self):

        if len(self.data) % 2 != 0:
            self.data.append(self.data[-1])

        for d in self.data:
            # 暂时现不检查是否是字节类型
            node = MerkleNode(None, None, d)
            node.new_node()
            self.nodes.append(node)

        for i in range(int(len(self.data)/2)):
            new_level = []

            for j in range(0, len(self.nodes), 2):
                node = MerkleNode(self.nodes[j], self.nodes[j + 1], '')
                node.new_node()
                new_level.append(node)
            self.nodes = new_level

        self.root = self.nodes[0]


class MerkleNode(object):
    """
    - doc
    """

    def __init__(self, left, right, data):
        self.Left = left
        self.Right = right
        self.data = data # 暂时不检查data是否是字节类型

    def new_node(self):
        if not self.Left and not self.Right:
            hash_value = hashlib.sha256(self.data.encode()).hexdigest()
            self.data = hash_value
        else:
            prehash = self.Left.data + self.Right.data
            hash_value = hashlib.sha256(prehash.encode()).hexdigest()
            self.data = hash_value