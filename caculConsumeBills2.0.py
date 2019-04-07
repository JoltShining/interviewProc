'''
DATE:2019-04-04
Author:Shining
Version:1.0
platform:py36
Theme:caculConsumeBills

计算每个人的花费，和需要付出的钱
输入格式为元组（日期，金额，款项，付款人，同消费1，同消费2）
输出每个人均分金额，以及谁付给谁多少
'''
import re

#读取TXT数据，并存入元组和列表
def readConsumeBills(consumeBill):

    
    
    consumptionBill = []
    datePat = r'\d+-\d+-\d+$'
    moneyPat = r'(\d+)+[\（ | \(]'
    billPatA = r'(\(+[^()\f\n\r\t\v]+\)+)+'
    billPatB = r'(\（+[^（）\f\n\r\t\v]+\）)+'
    with open(consumeBill,'r') as bills:
        for bill in bills:
            bill = bill.strip()
            #print(bill)
            if bill:
                date = re.findall(datePat,bill)
                money = re.findall(moneyPat,bill)
                #print(money)
                billA = re.findall(billPatA,bill)
                billB = re.findall(billPatB,bill)
                if date:
                    dateTuple = ()
                    date = (str(date[0]),)
                    dateTuple += date
                    #print(dateTuple)
                elif billA:
                    #print(billA)
                    consumptionBill += transformToTup(dateTuple,money,billA)
                elif billB:
                    #print(billB)
                    consumptionBill += transformToTup(dateTuple,money,billB)
                else:
                    print('出错了......')
                    break
    return consumptionBill



                                   
def transformToTup(date,money,bill):
    '''
    转换日期，金额，消费项，付款人，共同消费人为列表，元素为元组
    '''
    
    consumeList = []
    for i in range(len(bill)):
        consumerBill = ()
        consumerBill += date
        consumerBill += (int(money[i]),)
        for j in range(1,len(bill[i]),2):
            
            consumerBill += ((bill[i][j],))
        consumeList.append(consumerBill)
    return consumeList


def classfy(billList):

    xxfBill = []
    xxBill = []
    xufBill = []
    xiefBill = []
    result = []
    for item in billList:
        if len(item) == 6:
            xxfBill.append(item)
        elif '冯' not in item:
            xxBill.append(item)
        elif '谢' not in item:
            xufBill.append(item)
        elif '徐' not in item:
            xiefBill.append(item)
        else:
            return 0
    result.append(xxfBill)
    result.append(xxBill)
    result.append(xufBill)
    result.append(xiefBill)
    return result
            

def caculateBill(classfyList):
    
    payForList = []
    for elemlist in classfyList:
        entertainmentFee = 0
        sumOfThree = 0
        sumOfXu = 0
        sumOfXie = 0
        sumOfFeng = 0
        sumOfThree,sumOfXu,sumOfXie,sumOfFeng = calcSingleMoney(elemlist)
        payForList.append((sumOfThree,sumOfXu,sumOfXie,sumOfFeng))
    return payForList

def payForOther(billList):
    
    xieToFeng = 0
    xieToXu = 0
    xuToXie = 0
    xuToFeng = 0
    fengToXie = 0
    fengToXu = 0
    payforList = caculateBill(billList)
    strFormat = 'Bruce Shining Echo三人账单(花费总金额，Bruce付款金额，Shining付款金额，Echo付款金额)￥:{}'
    print(strFormat.format(payforList[0]))
    avrofthree = payforList[0][0]/3
    print('Bruce Shining and Echo 的三人账单平均花费金额为￥：{:.2f}'.format(avrofthree))
    #print('\n')
    print('='*len(strFormat)*2)
    print('1.Bruce Shining 两人账单(花费总金额，Bruce付款金额，Shining付款金额，Echo付款金额)￥:{}'.format(payforList[1]))
    print('2.Bruce Echo两人账单(花费总金额，Bruce付款金额，Shining付款金额，Echo付款金额)￥:{}'.format(payforList[2]))
    print('3.Shining Echo两人账单(花费总金额，Bruce付款金额，Shining付款金额，Echo付款金额)￥:{}'.format(payforList[3]))
    subAll = {}
    consumer = ('Bruce','Shining','Echo')
    for i in range(1,len(payforList[0])):
        subMoney = payforList[0][i] - avrofthree
        subAll[consumer[i-1]] = subMoney
        #print(subAll)
    acceptDict = {item[0]:item[1] for item in subAll.items() if item[1] > 0}
    #print(acceptDict)
    #print(acceptDict.keys())
    consumerSet = set(consumer)
    #print(consumerSet)
    consumeAccepter = set(acceptDict.keys())
    #print(consumeAccepter)
    payforer = consumerSet - consumeAccepter
    payforer = list(payforer)
    if len(payforer) == 0:
        return False
    elif len(payforer) == 1:
        if payforer[0] == 'Bruce':
            xuToXie += subAll['Shining']
            xuToFeng += subAll['Echo']
        elif payforer[0] == 'Shining':
            xieToXu += subAll['Bruce']
            xieToFeng += subAll['Echo']
        else:
            fengToXu += subAll['Bruce']
            fengToXie += subAll['Shining']
    else:
        if 'Bruce' in consumeAccepter:
            xieToXu += abs(subAll['Shining'])
            fengToXu += abs(subAll['Echo'])
        elif 'Shining' in consumeAccepter:
            xuToXie += abs(subAll['Bruce'])
            fengToXie += abs(subAll['Echo'])
        else:
            xuToFeng += abs(subAll['Bruce'])
            xieToFeng += abs(subAll['Shining'])
    xuXieBill = calcTwoMoney(payforList[1],'徐谢')
    xuFengBill = calcTwoMoney(payforList[2],'徐冯')
    xieFengBill = calcTwoMoney(payforList[3],'谢冯')
    #print('两个人的账单：：：：')
    #print(xuXieBill,xuFengBill,xieFengBill)
    xieGiveXu = xieToXu + xuXieBill['谢to徐'] - xuToXie - xuXieBill['徐to谢']
    xieGiveFeng = xieToFeng + xieFengBill['谢to徐'] - fengToXie - xieFengBill['冯to谢']
    xuGiveFeng = xuToFeng + xuFengBill['徐to冯'] - fengToXu - xuFengBill['冯to徐']
    if xieGiveXu > 0:
        xieGiveXu = xieGiveXu
        xuGiveXie = -xieGiveXu
    else:
        xuGiveXie = -xieGiveXu
        xieGiveXu = xieGiveXu
    if xieGiveFeng > 0:
        xieGiveFeng = xieGiveFeng
        fengGiveXie = -xieGiveFeng
    else:
        fengGiveXie = -xieGiveFeng
        xieGiveFeng = xieGiveFeng
    if xuGiveFeng > 0:
        xuGiveFeng = xuGiveFeng
        fengGiveXu = -xuGiveFeng
    else:
        xuGiveFeng = -xuGiveFeng
        fengGiveXu = xuGiveFeng
    
    return {'谢to冯':xieGiveFeng,'谢to徐':xieGiveXu,'徐to谢':xuGiveXie,'徐to冯':xuGiveFeng,'冯to谢':fengGiveXie,'冯to徐':fengGiveXu}
    
            
            
            
        
    

def countBill():
    eatFee = 0
    hotelFee = 0
    ticketFee = 0
    pass

def calcSingleMoney(billList):
    sumofAll = 0
    sumofXu =0
    sumofXie = 0
    sumofFeng = 0
    for bill in billList:
        sumofAll += bill[1]
        if bill[3] == '徐':
            sumofXu += bill[1]
        elif bill[3] == '谢':
            sumofXie += bill[1]    
        elif bill[3] == '冯':
            sumofFeng += bill[1]
    return sumofAll,sumofXu,sumofXie,sumofFeng

def calcTwoMoney(billList,billType):
    avrageTwo = billList[0] /  2
    xieToXu = 0
    xieToFeng = 0
    xuToXie = 0
    xuToFeng = 0
    fengToXie = 0
    fengToXu = 0
    subAll = {}
    consumer = ('Bruce','Shining','Echo')
    
    for i in range(1,len(billList)):
        if billList[i] == 0:
            continue
        else:
            subMoney = billList[i] - avrageTwo
            subAll[consumer[i-1]] = subMoney
        consumeAccepter = {item[0]:item[1] for item in subAll.items() if item[1] > 0}
        if billType == '徐谢':
            if 'Bruce' in consumeAccepter:
                xieToXu += subAll['Bruce']
            elif 'Shining' in consumeAccepter:
                xuToXie += subAll['Shining']
            else:
                pass
        elif billType == '徐冯':
            if 'Bruce' in consumeAccepter:
                fengToXu += subAll['Bruce']
            elif 'Echo' in consumeAccepter:
                xuToFeng += subAll['Echo']
            else:
                pass
        elif billType == '谢冯':
            if 'Shining' in consumeAccepter:
                fengToXie += subAll['Shining']
            elif 'Echo' in consumeAccepter:
                xieToFeng += subAll['Echo']
            else:
                pass
    return {'谢to徐':xieToXu,'谢to冯':xieToFeng,'徐to谢':xuToXie,'徐to冯':xuToFeng,'冯to徐':fengToXu,'冯to谢':fengToXie}
def calcThreeMoney(billList):
    pass

def balanceBill(totalAccount,payforDict):
    '''
    计算互相支付差额后每个人的花费
    返回Bruce消费金额，Shining消费金额，Echo消费金额
    '''
    for key,value in payforDict.items():
        if key == '谢to徐':
            xiePay = totalAccount[2] + value
        elif key == '谢to冯':
            xiePay = totalAccount[2] + value
        elif key == '徐to谢':
            xuPay = totalAccount[1] + value
        elif key == '徐to冯':
            xuPay = totalAccount[1] + value
        elif key == '冯to徐':
            fengPay = totalAccount[3] + value
        elif key == '冯to谢':
            fengPay = totalAccount[3] + value
    total = totalAccount[1] + totalAccount[2] + totalAccount[3]
    return (total,xuPay,xiePay,fengPay)

def payforPrint(payforDict):
    '''
    根据两人账单和三人账单打印付款结果
    '''
    for key,val in payforDict.items():
        if key == '谢to徐' and val > 0:
            print('Shining 需要付款人民币￥:{:.2f}元给 Bruce。'.format(val))
        elif key == '谢to冯' and val > 0:
            print('Shining 需要付款人民币￥:{:.2f}元给 Echo。'.format(val))
        elif key == '徐to谢' and val > 0:
            print('Bruce 需要付款人民币￥:{:.2f}元给 Shining。'.format(val))
        elif key == '徐to冯' and val > 0:
            print('Bruce 需要付款人民币￥:{:.2f}元给 Echo。'.format(val))
        elif key == '冯to徐' and val > 0:
            print('Echo 需要付款人民币￥:{:.2f}元给 Bruce。'.format(val))
        elif key == '冯to谢' and val > 0:
            print('Echo 需要付款人民币￥:{:.2f}元给 Shining。'.format(val))
    
        
    
        
        
        

if __name__ == '__main__':

    billList = readConsumeBills('C:\\Users\\PC\\Desktop\\travelConsumeBills.txt')
    consumeCount = len(billList)
    consumeXu = len([bill for bill in billList if bill[3] == '徐'])
    consumeXie = len([bill for bill in billList if bill[3] == '谢'])
    consumeFeng = len([bill for bill in billList if bill[3] == '冯'])
    totalAccount = calcSingleMoney(billList)
    print(totalAccount)
    sA = '1.本次湖南之行总计消费【{}】笔，共计金额人民币￥：{:.2f}元。'
    sB = '2.其中Bruce支付【{}】笔，共计金额人民币￥：{:.2f}元。'
    sC = '3.其中Shining支付【{}】笔，共计金额人民币￥：{:.2f}元。'
    sD = '4.其中Echo支付【{}】笔，共计金额人民币￥：{:.2f}元。'
    print(sA.format(consumeCount,totalAccount[0]))
    print(sB.format(consumeXu,totalAccount[1]))
    print(sC.format(consumeXie,totalAccount[2]))
    print(sD.format(consumeFeng,totalAccount[3]))   
    classBill = classfy(billList)    
    payforDict = payForOther(classBill)
    print('='*128)
    print('计算三人账单和两人账单后的付款字典为(+为付款，-为收款):{}.'.format(payforDict))
    payforPrint(payforDict)
    banlanceBill = balanceBill(totalAccount,payforDict)
    print('经过付收款平衡后，Bruce，Shining，Echo 湖南行花费为：-->\n')
    print('  1: Bruce 花费人民币￥：【{:.2f}】元'.format(banlanceBill[1]))
    print('  2: Shining 花费人民币￥：【{:.2f}】元'.format(banlanceBill[2]))
    print('  3: Echo 花费人民币￥：【{:.2f}】元'.format(banlanceBill[3]))
    
    
    
    #print(billList)
    #print(len(billList))
    #print(classBill)
    #print(len(classBill[0])+len(classBill[1])+len(classBill[2])+len(classBill[3]))
    
