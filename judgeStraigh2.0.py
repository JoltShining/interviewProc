#!/usr/bin/python36
# judgeStraigh2.0
'''
添加大小王为癞子
后续可考虑花色，是否同花顺？
'''
from functools import reduce

def judgeStraigh(elemlist):
    #判断是否有重复扑克牌，有重复则不是顺子
    listofset = set(elemlist)           
    if len(listofset) < 5:
        return False
    else:
        #为了不改变传入的list，将传入的list复制给translist
        translist = elemlist[:]
        #将扑克牌JQKA转换为数字，以便于排序，判断是否是顺子
        if 'J' in translist:            
            translist[translist.index('J')] = 11
            #print(translist)
        if 'Q' in translist:
            translist[translist.index('Q')] = 12
            #print(translist)
        if 'K' in translist:
            translist[translist.index('K')] = 13
        # 是否考虑顺子A、2、3、4、5，如果考虑则在转换A的值需要再加条件
        # 包含JQK 任一元素转换为 14，否则转换为1，那么在判断不含大小鬼的时候也需要用相邻值减去和相加，和为4为顺子 否则不是
        if 'A' in translist:
            translist[translist.index('A')] = 14
         #如果大小鬼有一张在五张牌之中，那么剩余的四张数字牌逆序后，两两差值之和在【3,4】中则满足顺子的条件
        if ('litGhost'in translist and 'bigGhost' not in translist) \
        or ('bigGhost'in translist and 'litGhost' not in translist):
            translist = [ item for item in translist if type(item) == int]
            sortedlist = sorted(translist,reverse = True)
            subsum = 0
            for i in range(len(sortedlist)-1):
                subsum += (sortedlist[i] - sortedlist[i+1])
            if subsum in [3,4]:
                return True
            else:
                return False
        if 'litGhost' in translist and 'bigGhost' in translist:
            translist = [ item for item in translist if type(item) == int]
            sortedlist = sorted(translist,reverse = True)
            subsum = 0
            for i in range(len(sortedlist)-1):
                subsum += (sortedlist[i] - sortedlist[i+1])
            if subsum in [2,3,4]:
                return True
            else:
                return False
        # 没有大小鬼，则正常排序后，取首元素，在原始列表中找到首元素的索引，向后取5个元素（包含首元素）
        # 比较排序后列表与取出的列表是否一致，一致则是顺子，不一致则不是顺子
        else:
           sortedlist = sorted(translist)
            #print(sortedlist)
           originlist = [2,3,4,5,6,7,8,9,10,11,12,13,14]
           newStart = originlist.index(sortedlist[0])
           newlist =  originlist[newStart:newStart+5]
            #print(originlist.index(sortedlist[0]))
            #print(newlist)
            #print(translist)
           if sortedlist == newlist:
               return True
           else:
               return False
                

if __name__ == '__main__':
    a = [2,5,3,4,6]
    b = [9,7,10,'J',8]
    c = [10,'litGhost',"K","A",'J']
    d = [2,'Q',"K","A",'J']
    e = [9,'litGhost',10,'J','bigGhost']
    f = [6,'litGhost',10,'J','bigGhost']
    testlist = [a,b,c,d,e,f]
    for obj in testlist:
        if judgeStraigh(obj):
            print('{} 是顺子！'.format(obj))
        else:
            print('{} 不是顺子。。。'.format(obj))
       
                

