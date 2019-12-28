#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:2019-12-27
Describe:计算正整数number有多少种两个质数相加(HUAWEI测试机试题),未考虑算法复杂度
"""

import math,sys


# 判断是否为质数
def judge_is_prime_factor(number):

    if number < 2:
        return False
    if number == 2:
        return True
    count = int(math.sqrt(number)+1)     # 如果number不能被2到sqrt(number)整除,则为质数
    for i in range(2, count):
        if number % i == 0:
            return False
    else:
        return True


# 返回两个相加的质数列表[(a,b)]
def find_prime_factor_list(number):

    result_prime_factor = []
    for n in range(2,int(number/2)+1):
        if judge_is_prime_factor(n):
            if judge_is_prime_factor(number-n):
                result_prime_factor.append((n,number-n))

    return result_prime_factor


if __name__ == "__main__":

    test_number = []
    # 读取数字
    for line in sys.stdin:    #readline().strip())
        # print(line)
        a = line.split()
        # print(type(a))
        if a == ['0']:
            break
        for item in a:
            test_number.append(int(item))
    # test_number = [2,5,10,18,19,1000000]                 # 输入测试列表
    for item in test_number:
        print(len(find_prime_factor_list(item)))       # 根据返回的列表长度取所需的种数
    print("end")

