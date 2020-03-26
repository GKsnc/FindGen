#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
测试区块链

@File    :   blockchain_test.py
@Time    :   2020/03/22 14:45:53
@Author  :   ZHOU 
"""

# here put the import lib
import sys
sys.path.append("src")
from core.blockchain import BlockChain


def main()：
    findgen_chain=BlockChain() #连接到本机上的redis，安全性，还有redis的安装问题 TODO(ZHOU)，存储在redis是没有加密的吗？需要加密吗？不需要，区块链设计就解决了这个问题

    # 添加区块上链
    # findgen_chain.add_block(block) #数据结构见block模块，传输使用json；区块是怎么存储在redis中的

    # 区块长什么样，redis中区块，
    # 就存储成样本区块那样就行了，明文也不要紧

    # 创世区块长什么样

    # 币基交易？就是指区块中的Records字段吗？

    # 一个类似于utxo（未消费的交易输出），GFW模型也需要，未结束的商品，围绕这个结构，这个结构就是GFW的核心了
    # 参考utxo，来设计
    # 记录结构的设计，区块链中记录的结构 ginu
    # utxo设计
    # 商品只有一条线，直接指向那个区块或者记录编号（记录的hash）不好吗，不是
    # 第一步找到所有商品的未完成输出（找的话，就直接利用标识了前一个记录的标识来找），第二步，使用商品发布新的区块（验证，一条条向前验证，成功就接受区块
    # 结束