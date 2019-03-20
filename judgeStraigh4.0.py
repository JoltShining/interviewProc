#!/usr/bin/python36
# judgeStraigh3.0
#Author :  Shining
#Date   :   2019-03-19
'''
随机抽取的五张牌是否为顺子   -------->done
添加大小王为癞子             ------->done
可判别是否同花顺             -------->done
后续考虑随机生成任意张牌，并符合扑克牌规则（四种花色，大小王）4.0--------->done
判断任意个数为顺子（>3?）（判断器抽象为类）5.0
'''
import random

class Poker:

    def __init__(self,point,suit):
        self.point = point
        self.suit = suit

    def __repr__(self):
        return '({},{})'.format(self.suit,self.point)
    

def judgeStraigh(objlist):
    flag = 0
    listofpoint = [obj.point for obj in objlist]
    listofsuit = [obj.suit for obj in objlist]          
    if len(set(listofpoint)) < 5:
        flag = 0
    else:
        translist = listofpoint[:]
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
                flag = 1
            else:
                flag = 0
        if 'litGhost' in translist and 'bigGhost' in translist:
            translist = [ item for item in translist if type(item) == int]
            sortedlist = sorted(translist,reverse = True)
            subsum = 0
            for i in range(len(sortedlist)-1):
                subsum += (sortedlist[i] - sortedlist[i+1])
            if subsum in [2,3,4]:
                flag = 1
            else:
                flag = 0
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
               if len(set(listofsuit)) == 1:
                   flag = 2
               else:
                    flag =1
           else:
               flag = 0
    return flag
#随机抽取五张扑克牌
def extractPoker(count):
    originpoker = set()
    originpoint = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    originsuit = ['Heart','spade','Diamond','Club']
    extractpoker = []
    for point in originpoint:
        for suit in originsuit:
            originpoker.add((point,suit))
    for i in range(count):
        poker = random.choice(list(originpoker))
        extractpoker.append(poker)
        originpoker.remove(poker)
    return extractpoker

if __name__ == '__main__':
    
    count = 0
    time = 1
    while True:
        count += 1
        pokerobj = []
        listofpoker = extractPoker(5)
        for poker in listofpoker:
            pokerobj.append(Poker(poker[0],poker[1]))
            
        flag = judgeStraigh(pokerobj)
        if flag == 0:
            print('{} 不是一个顺子...'.format(pokerobj))
        elif flag == 1:
            print('{} 是一个顺子,但不是同花顺。'.format(pokerobj))
            print('顺子的概率是万分之{}.'.format(time/count*10000))
            time += 1
            continue
        elif flag == 2:
            print('{} 是一个同花顺，恭喜您！'.format(pokerobj))
            print('同花顺的概率是万分之{}.'.format(1/count*10000))
            break
        else:
            print('不可预料的情况发生了？？？')

       
                

