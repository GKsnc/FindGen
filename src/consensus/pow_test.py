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
from pow import ProofOfWork
from blockchain.block import Block


if __name__ == '__main__':
    b = Block()

    genesis_block = b.new_block({}, "")

    pow = ProofOfWork(genesis_block)
    pow.run()
