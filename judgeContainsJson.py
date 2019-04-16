'''
example 1:
input param1:{'d':2}
input param2:[{'a':1,'b':{'c':1,'d':2}},{'f':1}]

return:True

example2:
input param1:{'d':2,'f':2}
input param2:[{'a':1,'b':{'c':1,'d':2}},{'f':1}]

return False
'''

def listAllJson(tempList,result = None):
    '''
    遍历list中的字典项，转换成元组，添加进集合，并返回集合
    '''

    if result:                 #判断是否递归中调用，递归中调用则保存之前已经处理的字典项
        result = result
    else:
        result = set()         #非递归调用或者递归调用时无字典项加入result集合，则初始化result为空集合
    
    flag = False
    if isinstance(tempList,list):    #传入项为list，则遍历list
        
        for item in tempList:
            if isinstance(item,dict): 
                for elem in item:
                    if not isinstance(item[elem],dict):  #非嵌套字典，key,value作为元组直接加入result
                        result.add((elem,item[elem]))
                        flag = True
                    else:
                        if flag:                         #标志位修改 则表示递归之前有元素加入result，需要将该信息传入
                            listAllJson(item[elem],result)
    else:                                                #主要是递归调用中，传入项为dict，则遍历字典
        for elem in tempList:
            #if isinstance(item,dict):
                #for elem in item:
            if not isinstance(tempList[elem],dict):     #非嵌套字典，key,value作为元组直接加入result  
                result.add((elem,tempList[elem]))
                flag = True
            else:                                       #继续遍历嵌套字典
                if flag:
                    listAllJson(tempList[elem],result)
    return result
    
def judgeJson(objectDict,tempJson):

    '''
    判断objectDict是否包含在tempJson中
    '''

    objectSet = set(objectDict.items())             #将输入单层字典转换为集合
    print(objectSet)
    return objectSet.issubset(listAllJson(tempJson)) #判断objectSet是否是listAllJSon返回集合的子集

    

if __name__ == '__main__':

    temp = [{'a':1,'b':{'c':1,'d':2}},{'f':1}]
    input1 = {'d':2}
    input2 = {'d':2,'f':2}
    print(listAllJson(temp))
    print(judgeJson(input1,temp))
    print(judgeJson(input2,temp))
    
    
    
