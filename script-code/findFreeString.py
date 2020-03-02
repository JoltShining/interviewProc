#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:2020-02-28
Describe:输入一个格式为a:3,b:2,c:5@a:2,b:1,c:4的字符串,@符号前为全量字符串,@符号后为子字符串,
找出全量字符减去子字符串后的剩余字符串
如上输出为:a:1,b:1,c:1
如果@符号后为空字符串,则输出整个字符串,输入A:1,b:2@     输出:A:1,b:2@
"""
import sys

def castStrToDict(tempStr):

    strDict = {}
    tempStrList = tempStr.split(',')
    # print(tempStrList)
    for item in tempStrList:

        strDict[item[0]] = item[2]

    return strDict

def castDictToStr(srcDict):

    temp = []
    obj = ""
    # print(srcDict)
    for k,v in srcDict.items():
        stringItem = k +':'+ v
        temp.append(stringItem)
    if len(temp) == 1:
        return temp[0]
    else:
        return ','.join(temp)


def findUnsedString(srcString,disString):


    for elem,num in disString.items():
        count = int(srcString[elem]) - int(num)
        if count == 0:
            del srcString[elem]
        else:
            srcString[elem] = str(count)
    if not srcString:
        return ''
    else:
        return castDictToStr(srcString)

def findFreeString(freeString,usedString):

    if usedString == "\n":
        return freeString + '@'

    srcString = castStrToDict(freeString)
    disString = castStrToDict(usedString)

    return findUnsedString(srcString,disString)

if __name__ == "__main__":

    for line in sys.stdin:
        # print(line)

        srcString = line.split('@')
        if len(srcString) == 1:
            print(srcString[0])
        else:
            srcString,disString = srcString[0],srcString[1]
            print(findFreeString(srcString, disString))



