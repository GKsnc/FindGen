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
import time
from storage.redis_storage import Redis
from consensus.pow import ProofOfWork


class BlockChain(object):
    """
    区块链。
    核心，对区块链的存取，查询等操作。
    """
    def __init__(self):
        # 首先存储块在内存中
        # 然后再存储在redis
        # self.blocks = []

        # self.blocks = Redis()
        # self.current_hash = self.blocks.get('L') # TODO 当前hash
        self.__initial_blockchain()

    def __initial_blockchain(self):
        '''
        初始化区块链。
        没有，则创建。
        有，则进行同步与读取。
        '''
        # 由于网络模块尚未完成，同步，读取；未来更新
        # 读取数据库，进行判断，是否有区块链
        # 创世区块的创建
        self.blocks = Redis()
        # 判断是否有最后一个区块，没有则开始创建区块
        # 因为数据库中存储的是区块，不一定有L
        # 所以得判断，是否有区块链，
        # 可以用创世区块
        # 如果数据库为空则创世区块？
        # 创世区块编入到程序内
        if self.blocks.rds.exists('L'):
            self.current_hash = self.blocks.get('L')
            return True
        elif self.blocks.rds.keys():
            self.blocks.rds.flushdb() # 清空当前（0号）数据库；这里待网络模块完成，再做更改

        self.__genesis_block()
        self.current_hash = self.blocks.get('L')
        # 网络同步
        # 数据库什么都没有
        # 则，开始读取创世区块，并开始运行网络模块
        # 此处也需要认证
        # TODO 网络模块完成后，此处必须改变；存在隐患
        # 比如直接读取创世区块
        
        # redis存取的是区块链，如果网络同步后，建立键值对，需要hash作为键
    
    # 创世区块
    # 当一切都完成后，固定创世区块，这个方法也将删除，目前做测试使用
    def __genesis_block(self):
        '''
        创世区块。
        完成后，将区块，硬编码进程序。
        '''
        genesis_block = {
            "Version" : '0x0', # 16进制int
            "TimeStamp": int(time.time()), # int
            "MerkleRoot":'0x0',
            "Records": list(), # 数组
            "PrevBlockHash": '0x0', # 字符
            "Nonce": 0
        }
        genesis_block['Records'].append('0')
        pow = ProofOfWork(genesis_block)
        b_hash, nonce = pow.run()
        genesis_block["Nonce"] = nonce
        self.add_block(b_hash,genesis_block)

    def add_block(self, b_hash, new_block):
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
            if not self.blocks.get(b_hash): # 不能有相同hash加入
                if isinstance(new_block,str):
                    self.blocks.set(b_hash, new_block)
                else:
                    self.blocks.jset(b_hash, new_block)
                self.blocks.set("L", b_hash)

    def get_block(self, block_hash):
        block = self.blocks.jget(block_hash)
        if block:
            return block

        else:
            return "区块不存在"
    
    def find_urc(self):
        """
        查找所有的未完成的记录（urc）。
        :return urc:返回包含所有商品ID的字典。
        """
        urc=dict()
        finished_urc=dict()
        while True:
            try:
                last_block = next(self.iterator())
            except: # 此处依靠创世区块来编写
                # genesis_hash = self.blocks.get(self.current_hash).decode()
                # last_block = eval(genesis_hash)

                # coinbase_tx = last_block["Transactions"]
                # for tx in coinbase_tx:

                #     rc_json = json.loads(tx.decode())

                #     urc[rc_json["ID"]] = []

                #     for out in rc_json["Vout"]:
                #         if not spent_tx[rc_json["ID"]]:
                #             urc[rc_json["ID"]].append(out)
                break     # 程序退出边界条件

            if self.current_hash == '0x0':
                break # 这里处理的不是很好，之后视创世区块改变

            for rc in last_block["Records"]:
                rc_json = json.loads(rc)
                urc[rc_json['crec']["goods_id"]] = []
                urc[rc_json['crec']["goods_id"]].append(rc_json['crec'])

        return urc # TODO 存储到数据库中，缓存，未来更新

    def iterator(self):
        # 创世区块的迭代？
        if not self.current_hash:
            self.current_hash = self.blocks.get("L")
        

        try:
            last_block = self.blocks.jget(self.current_hash)
        except:
            raise StopIteration

        if last_block["PrevBlockHash"]:
            self.current_hash = last_block["PrevBlockHash"]
            yield last_block

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

    def print_blockchain(self):
        """
        输出blockchain

        :return:
        """
        # for b in self.blocks:
        #     print(b)

        blocks = []

        for b in self.blocks.keys():
            print(b)
            if b != 'L':
                v = self.blocks.get(b)
                blocks.append(v)
        return blocks

    def block2json_dump(self,block_hash):
        block = self.get_block(block_hash)
        # block['Records'] = json.loads(block['Records'])
        block['Records'] = list(map(json.loads,block['Records']))
        with open('block.json','w') as f:
            print('\n区块写入文件...\n')
            json.dump(block,f,indent=4,separators=(',',':'))


if __name__ == "__main__":
    bc_test = BlockChain()
