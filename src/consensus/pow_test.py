#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
# 描述

@File    :   pow_test.py
@Time    :   2020/02/28 14:15:29
@Author  :   ZHOU 
"""

import sys
sys.path.append("src")
from consensus.pow import ProofOfWork
from core.block import Block


if __name__ == '__main__':
    b = Block('0x0')

    genesis_block = b.new_block(['0x0'])

    pow = ProofOfWork(genesis_block[1])
    pow.run()
