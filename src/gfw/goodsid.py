#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
生成商品地址（商品ID）。

利用雪花算法。划分包括时间戳，商品编码，序列号
商品编码52bit（13位十进制数,还未实现），秒级时间戳（32位），序列号（20bit)

@File    :   generate_id.py
@Time    :   2020/02/06 17:17:06
@Author  :   ZHOU 
"""

import time
import logging
import binascii


# 104位ID的划分
EAN_13_BITS = 52
SEQUENCE_BITS = 12

# 最大取值计算
MAX_EAN_13 = -1 ^ (-1 << EAN_13_BITS)  # 2**5-1 0b11111

# 移位偏移计算
EAN_13_SHIFT = SEQUENCE_BITS
TIMESTAMP_LEFT_SHIFT = SEQUENCE_BITS + EAN_13_BITS

# 序号循环掩码
SEQUENCE_MASK = -1 ^ (-1 << SEQUENCE_BITS)

# 元年时间戳
TWEPOCH = 1581059925 


logger = logging.getLogger('flask.app')


class IdWorker(object):
    """
    用于生成IDs
    """

    def __init__(self, EAN_13, sequence=0):
        """
        初始化
        :param EAN_13: EAN-13码
        :param sequence: 起始序号
        """
        # sanity check
        if EAN_13 > MAX_EAN_13 or EAN_13 < 0:
            raise ValueError('worker_id值越界')

        self.EAN_13 = EAN_13
        self.sequence = sequence

        self.last_timestamp = -1  # 上次计算的时间戳

    def _gen_timestamp(self):
        """
        生成整数时间戳
        :return:int timestamp
        """
        return int(time.time())

    def get_id(self):
        """
        获取新ID
        :return:
        """
        timestamp = self._gen_timestamp()

        # 时钟回拨
        if timestamp < self.last_timestamp:
            logging.error('clock is moving backwards. Rejecting requests until {}'.format(self.last_timestamp))
            raise InvalidSystemClock

        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & SEQUENCE_MASK
            if self.sequence == 0:
                timestamp = self._til_next_millis(self.last_timestamp)
        else:
            self.sequence = 0

        self.last_timestamp = timestamp

        new_id = ((timestamp - TWEPOCH) << TIMESTAMP_LEFT_SHIFT) | (self.EAN_13 << EAN_13_SHIFT) | self.sequence
        return new_id

    def _til_next_millis(self, last_timestamp):
        """
        等到下一毫秒
        """
        timestamp = self._gen_timestamp()
        while timestamp <= last_timestamp:
            timestamp = self._gen_timestamp()
        return timestamp


class InvalidSystemClock(Exception):
    """
    时钟回拨异常
    """
    pass

# 测试
if __name__ == '__main__':
    worker = IdWorker(69012345678912,0) 
    print(hex(worker.get_id())) # 16进制显示输出

# 商品ID是否混淆（哈希）？