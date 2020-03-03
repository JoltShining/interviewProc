#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:
Describe:删除字符串某一个重复子串,比如'aabbaabbbbb',删除子串'ab'
"""

def delSubStr(srcString,delStr):

    srcStrLen = len(srcString)
    delStrLen = len(delStr)
    srcStrList = [s for s in srcString]
    newStr = ''
    i = 0
    while i < srcStrLen:
        if srcString[i:i+delStrLen] == delStr:
            i += delStrLen
            continue
        else:
            newStr += srcString[i]
            i += 1

    return newStr

if __name__ == "__main__":

    srcStr = 'aabbababbbb'
    delStr = 'ab'
    clearStr = delSubStr(srcStr,delStr)
    print(clearStr)

