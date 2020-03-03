#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:20-03-02
Describe:输出字符串中最长不重复的部分
"""


def findMaxNoRptStr(srcStr):

    subStr = set()
    # maxStr = ''
    maxLength = 0
    strLength = len(srcStr)
    resStr = ''
    for i in range(strLength-1):
        subStr.add(srcStr[i])
        maxStr = srcStr[i]
        for j in range(i+1,strLength):
            if srcStr[j] in subStr:
                if len(resStr) < len(maxStr):
                    resStr = maxStr
                    maxLength = len(resStr)
                maxStr = ''
                subStr = set()
                break
            else:
                subStr.add(srcStr[j])
                setLength = len(subStr)
                maxStr += srcStr[j]
                if setLength > maxLength:
                    maxLength = setLength
                    resStr = maxStr
        else:
            if maxLength > len(resStr):
                resStr = maxStr
            break

    return resStr, maxLength


if __name__ == "__main__":

    testStringList = ['abc','aa','12aaa','abab','abbbccbacd','abbbddacbee','abcdabcd']
    for string in testStringList:
        maxStr, maxLgh = findMaxNoRptStr(string)
        print("最大的不重复字符串是:{},长度为:{}.".format(maxStr,maxLgh))

