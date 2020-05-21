#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
测试区块链

@File    :   blockchain_test.py
@Time    :   2020/03/22 14:45:53
@Author  :   ZHOU 
"""

import sys
sys.path.append("src")
from core.blockchain import BlockChain
from core.adress import Participant

# 0427更新：这个函数，是为了理清楚整个流程
# 现在，由于一些结构的改变，回到上一个问题，如何生成一个区块
def test_1():

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
    #urc=findgen_chain.find_urc()
    # print(urc['goods_id'])

    # 上链与验证
    # 发布区块，需要一些条件，也就是要进行验证。
    # 矿工奖励？可以有
    # 验证，接受者验证区块，发送者也验证区块，在这里先只讨论区块的真实性，其他的之后考虑
    # 怎么验证，验证什么？
    # 流通记录，验证公钥签名匹配
    # 话说这算用户行为了吧
    # 那就从系统上来说，发布一个区块
    # block.verify()
    # findgen_chain.add_block(block)


    # 用户行为
    # 用户登录后，（系统查找地址，看看该地址有什么东西吗）
    # 地址，公钥，私钥三者的关系，也就是说记录并不是直接公钥，签名，这里是有个系统的
    '''
    私钥到字符串（如果显示出来，不仅仅是识别率不高，而且私钥太长。）base58
    公钥（公钥一般把byte数组是经过hex（16进制）的处理之后显示，不经过Base58的原因是： 公钥是用来验证私钥的签名，一般我们很少会看到公钥）
    压缩的公钥（椭圆曲线是对称的，知道了一半的信息就可以推导出来另外一半的信息了），因此只需要保存一般的公钥信息即可
    address=Base58(version+hash160(SHA-256(public key))+checksum)
    '''
    # 这些当然有用，但我目前最应该做的是地址是怎么用的
    # 看了一些，还是没有什么头绪
    # 最基本的创建，和基础的交易（流通）
    # 地址没有保存到区块链当中，因为没有必要，使用公钥就能解决，但还是需要地址，为了方便显示
    # 地址反算公钥？
    # 我们交易是发向一个地址，那么这个地址在区块链是怎么标识的？（用公钥得出地址后，遍历区块链查找；这个地址上的交易，所以区块链上还是会有地址？
    '''
    BOB把公钥的哈希值提供给ALICE。公钥哈希就是大家所熟知的编码过的比特币地址，编码采用的base58进行，里面包含了一个版本序号、哈希值以及一个用来校验错误的值。
    比特币地址可能通过任何介质传播，当然也包括单向的介质，这样可以切断发款人和收款人的联系，比特币地址还可以被进一步编码成其它的格式，比如包括”bitcoion：”的二维码地址。
    '''
    

    # 生产，流通，交易，验证 功能编写
    # 见系统说明文件

    # 注册就是直接生成私钥就行了，然后地址
    # buyer=Participant()
    # buyer.get_address()
    # print(buyer.address)
    # print(buyer.private_key)
    # print(buyer.pub_key)

    # 遍历区块，这里我的地址系统还没有加入系统；


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

# test_1是之前的测试用例,现在改为只用main这个测试用例
def main():
    findgen = BlockChain()
    
    # print(findgen.print_blockchain())
    while True:
        print(findgen.current_hash)
        try:
            block = next(findgen.iterator())
        except:
            break
        print(block,end='\n\n')

    # findgen.block2json_dump(findgen.blocks.get('L')) # 将最后一个区块导出到文件（json格式）

if __name__ == "__main__":
    main()