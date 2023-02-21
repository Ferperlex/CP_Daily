#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 12:18:59 2023

@author: fernandomacchiavellocauvi
"""

import sys

input = sys.stdin.readline


def maxint():
    return sys.maxsize * 2 + 1


def get_digit(number, n):
    return number // 10 ** n % 10


############ ---- Input Functions ---- ############
def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


# import time

if __name__ == "__main__":

    for _ in range(inp()):

        leng = inp()
        li = inlt()

        flag = True
        pre_i = 0
        r = [1]
        for j in range(1, leng):
            r.append(j + 1)
            if li[pre_i] == li[j]:
                r[pre_i], r[j] = r[j], r[pre_i]
            pre_i = j
        count = 1
        for l in r:
            if count == l:
                flag = False
                break
            count += 1

        if flag:
            print(*r)
        else:
            print(-1)
