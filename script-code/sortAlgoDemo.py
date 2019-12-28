#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:2019-12-14
Describe:algo example
"""


# insert sort by rec
def ins_sort_rec(seq,i):
    if i == 0: return
    ins_sort_rec(seq, i - 1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1

def ins_sort(seq):
    for i in range(len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1


def sel_sort_rec(seq, i):
    if i == 0: return
    max_j = i
    for j in range(i):
        if seq[j] > seq[max_j]: max_j = j
    seq[i], seq[max_j] = seq[max_j], seq[i]
    sel_sort_rec(seq, i-1)


def sel_sort(seq):
    for i in range(len(seq)-1,0,-1):
        max_j = i
        for j in range(i):
            if seq[j] > seq[max_j]: max_j = j
        seq[i], seq[max_j] = seq[max_j],seq[i]


def cover(board,lab=1, top=0,left=0, side=None):
    if side is None: side = len(board)

    # side length of subboard
    s = side // 2

    # offsets for outer/inner squares of subboards
    offsets = (0, -1),(side-1, 0)

    for dy_outer,dy_inner in offsets:
        for dx_outer,dx_inner in offsets:
            # if the outer cotner is not set...
            if not board[top+dy_outer][left+dx_outer]:
                board[top+s+dy_inner][left+s+dx_inner] = lab

    # next label
    lab += 1
    if s > 1:
        for dy in [0,s]:
            for dx in [0,s]:
                lab = cover(board,lab,top+dy,left+dx,s)
    # return the next available label
    return lab


if __name__ == "__main__":
    seq = [1,3,9,4,6,7,2,1,8]
    print("seq is {}".format(seq))
    print("递归插入排序调用结果:{},sep:{}".format(ins_sort_rec(seq,8),seq))
    seq = [1, 3, 9, 4, 6, 7, 2, 1, 11]
    print("插入排序调用结果:{},seq:{}".format(ins_sort(seq),seq))
    seq = [1, 5, 9, 4, 6, 7, 2, 1, 8]
    print("递归选择调用排序结果:{},seq:{}".format(sel_sort_rec(seq,8),seq))
    seq = [1, 3, 9, 4, 6, 7, 2, 1, 8]
    print("选择排序的结果是:{},seq:{}".format(sel_sort(seq),seq))

    board = [[0]*8 for i in range(8)]
    board[7][7] = -1
    cover(board)
    for row in board:
        print((" %2i"*8) % tuple(row))


