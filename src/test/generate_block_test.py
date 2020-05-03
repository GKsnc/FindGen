#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
测试生成区块。

@File    :   generate_block_test.py
@Time    :   2020/02/19 15:51:30
@Author  :   ZHOU 
"""

import sys
sys.path.append("src")
import json
from core.adress import Participant
from gfw.goodsid import IdWorker
from gfw.records import Records


# 生成区块测试v1
def testv1():
    """
    区块生成流程。

    生产者:生成参与者地址->商品地址生成->记录生成->生成区块(共识算法参与)->上链(区块链,redis,通信等问题)
    """
    producer=adress.Participant() # 生产者实例化
    producer.new_keypair() # 生产者公私钥对生成
    
    pgid_worker=goodsid.IdWorker(69012345678912,0)
    goods_1=pgid_worker.get_id() # 生成一个商品ID

    rec=record.Records(goods_1,producer.private_key,producer.pub_key) # 实例化记录处理程序
    r_1=rec.new_record(0x0) # 生成一条记录
    recs=[]
    recs.append(r_1)

    blo=block.Block() #实例化区块生成程序
    blo_1=blo.new_block(recs,'0') # 生成区块

    bolockchain=BlockChain() # 实例化区块链
    bolockchain.add_block(blo_1) # 添加区块到区块链中

# 生成区块测试v2
# 0427 开始最后的“大”更新
def main():
    """
    生成区块。
    第一步，需要有参与方；三方，生产者，交易方，被交易方。
    第二步，商品；由生产者生成商品ID，并发布出去。
    第三步，交易；交易方与被交易方交易商品，生成记录，广播出去。
    第四步，“矿工”发布区块；接受到的记录，挖矿，发布区块。（挖矿前，验证区块）
    第五步，接收区块，验证。
    """

    # 生产者，生成公私钥对 
    producer = Participant() # 实例化
    producer.new_keypair() # 生成公私钥对
    producer.get_adress() # 生成地址
    producer.save_to_file() # 保存私钥
    # producer.load_to_file() # 读取私钥，构建地址
    # TODO base58;私钥，公钥，地址的编码
    # 私钥编码;base58算法错了;看下那个仓库的base58

    # 商品发布（上链）
    # 生产商（者）发布商品；传入ENA码，签名，直接发布？
    # 发布可以直接发布，但接受时是要验证的，比如验证是否有这个企业，这个企业是否可以生产发布等等
    # 为什么不在上链的时候做验证？这需要第三方的参与，未来更新
    idworker = IdWorker(69012345678912) # ENA码的绑定待优化
    ids = idworker.get_ids(10) # 生成10个商品id

    records = Records(producer.priv_key,producer.pub_key) # 实例化
    for i in ids:
        record = records.new_record(i,'0x000f',producer.address) # 生成记录
        # print(record)
        # 广播（验证）；等等，不用广播，我是生产者，直接发布区块就可以了
    # 发布区块

    
    # 在这里，有另一个问题，那就是惩罚机制；与之对应的是奖励机制；这里要么和比特币一样，用虚拟货币，要么，先不管了，之后再考虑吧

    # 交易，发布也没有特别严格的验证；
    # 有地址后，直接发给地址，然后发布就行

    # 收揽的记录，形成区块，发布出去。为了防止，内容有误，自然的先验证，在添加到区块，最后发布出去，

    # 接受到区块后，进行验证。

    # 接受与发布，这里没有写的太详细，是因为想待网络模块完成后，进一步编写。

    # 查找区块，显示商品ID的交易记录

    # 结束
    

if __name__ == "__main__":
    main()