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
# 0427 最后的“大”更新
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
    

if __name__ == "__main__":
    main()