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

    # 首先要先下载整个区块链，p2p(或者说检查完整性？)


    # 网络相关的一些配置 p2p


    # 然后实例化区块链
    findgen_chain=BlockChain() # 区块链的一些参数，也在这一步完成，版本之类的

    # 以上，初始化完成

    # 系统行为
    # 查询，上链，验证(包括在各个需要的地方)

    # 完整下载区块，进行查询
    # 查询一件商品的流通情况
    # 方法一：遍历整个区块链，根据商品ID依次查找(速度慢，且不能重复利用查找结果)
    # 方法二：找出所有的类utxo(gfw的未完成商品) urc，unfinished record,未完成记录
    # 这里先等等，区块链的操作
    # json，redis，区块链，python之间是什么，二进制？字符串？列表？字典？json？

    # 查询的准备
    urc=findgen_chain.find_urc()
    # print(urc['goods_id'])

    #TODO(ZHOU) 上链与验证


    # 用户行为(有很多，先看系统行为吧)
    # 按照设计的模型，谁都能发布吗，需要什么，如何公开，


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


# 一些问题：
# 连接到本机上的redis，安全性，还有redis的安装问题 TODO(ZHOU)，存储在redis是没有加密的吗？需要加密吗？不需要，区块链设计就解决了这个问题