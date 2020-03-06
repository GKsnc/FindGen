#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
MerkleTree测试。

@File    :   merkletree_test.py
@Time    :   2020/03/06 20:22:07
@Author  :   ZHOU 
"""

from merkletree import MerkleNode, MerkleTree

if __name__ == "__main__":
    m1 = MerkleNode(None, None, b"Node1")
    m1.new_node()

    m2 = MerkleNode(None, None, b"Node2")
    m2.new_node()

    m3 = MerkleNode(None, None, b"Node3")
    m3.new_node()

    m4 = MerkleNode(None, None, b"Node3")
    m4.new_node()

    m5 = MerkleNode(m1, m2, b'')
    m5.new_node()

    print(m5.Left, m5.Right, m5.data)

    tree = MerkleTree([b'Node1', b'Node2', b'Node3']) # dict[0]的hash与dict[1]的hash，加一起再hash得到父节点结点，如此下去，得到树的根结点
    tree.new_tree()

    print(tree.root.data)
