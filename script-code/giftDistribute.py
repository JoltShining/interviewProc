#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:2019-12-28
Describe:公司有n个人,进行礼物公平分配,每个人不能拿到自己的礼物(富途测试机试题)
Other:未考虑复杂度
"""
import random


def gift_distribute(giftList):
    """
    :param giftList: 序号对应自己的礼物编号
    :return: 随机礼物列表,值对应自己抽取的是几号的礼物,
    giftList[0]=9,0号抽取的是9号的礼物
    """
    random.shuffle(giftList)      # random.shuffle(list)返回值为None,直接在原序列随机
    # print(giftList)
    for item in giftList:
        # if item  == None:
        #    break
        if giftList.index(item) == item:        # 如果抽取的自己的礼物,重新随机序列
            print(item)
            gift_distribute(giftList)
        else:
            return  giftList                           # 都抽取的是其他人的礼物,返回这个seq
    # else:
        # return giftList


if __name__ == "__main__":

    giftList = list(range(20))
    print("礼物编号:{}".format(giftList))
    print("抽取编号:{}".format(gift_distribute(giftList)))

