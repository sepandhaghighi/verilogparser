# -*- coding: utf-8 -*-
from functools import reduce

def andFuncD(inputVector,inputVectorD,nodeName,Output):
    '''
    And Function Deductive Logic
    :param inputVector: input logic vector
    :param inputVectorD: input  stuck-at-fault vector
    :param nodeName: output node name
    :param Output: output node value
    :return: list of stuck-at-fault
    '''
    S=[]
    result={}
    inputVectorDTemp=list(inputVectorD)
    for index,item in enumerate(inputVector):
        if item==0:
            S.append(inputVectorDTemp.pop(inputVectorDTemp.index(inputVectorD[index])))
    if len(S)==0:
        result=list(reduce(set.union,list(map(set,inputVectorDTemp))))
        result.append(nodeName+"_0")
    else:
        result = set(reduce(set.intersection, list(map(set, S))))
        if len(inputVectorDTemp) != 0:
            result=result.difference(set(reduce(set.union,list(map(set,inputVectorDTemp)))))
        result = list(result)
        result.append(nodeName+"_1")
    return result


def nandFuncD(inputVector,inputVectorD,nodeName,Output):
    '''
    Nand Function Deductive Logic
    :param inputVector: input logic vector
    :param inputVectorD: input  stuck-at-fault vector
    :param nodeName: output node name
    :param Output: output node value
    :return: list of stuck-at-fault
    '''
    S=[]
    result={}
    inputVectorDTemp=list(inputVectorD)
    for index,item in enumerate(inputVector):
        if item==0:
            S.append(inputVectorDTemp.pop(inputVectorDTemp.index(inputVectorD[index])))
    if len(S)==0:
        result=list(reduce(set.union,list(map(set,inputVectorDTemp))))
        result.append(nodeName+"_1")
    else:
        result = set(reduce(set.intersection, list(map(set, S))))
        if len(inputVectorDTemp)!=0:
            result=result.difference(set(reduce(set.union,list(map(set,inputVectorDTemp)))))
        result=list(result)
        result.append(nodeName+"_0")
    return result


def orFuncD(inputVector,inputVectorD,nodeName,Output):
    '''
    Or Function Deductive Logic
    :param inputVector: input logic vector
    :param inputVectorD: input  stuck-at-fault vector
    :param nodeName: output node name
    :param Output: output node value
    :return: list of stuck-at-fault
    '''
    S=[]
    result={}
    inputVectorDTemp=list(inputVectorD)
    for index,item in enumerate(inputVector):
        if item==1:
            S.append(inputVectorDTemp.pop(inputVectorDTemp.index(inputVectorD[index])))
    if len(S)==0:
        result=list(reduce(set.union,list(map(set,inputVectorDTemp))))
        result.append(nodeName+"_1")
    else:
        result = set(reduce(set.intersection, list(map(set, S))))
        if len(inputVectorDTemp) != 0:
            result=result.difference(set(reduce(set.union,list(map(set,inputVectorDTemp)))))
        result = list(result)
        result.append(nodeName+"_0")
    return result

def norFuncD(inputVector,inputVectorD,nodeName,Output):
    '''
    Nor Function Deductive Logic
    :param inputVector: input logic vector
    :param inputVectorD: input  stuck-at-fault vector
    :param nodeName: output node name
    :param Output: output node value
    :return: list of stuck-at-fault
    '''
    S=[]
    result={}
    inputVectorDTemp=list(inputVectorD)
    for index,item in enumerate(inputVector):
        if item==1:
            S.append(inputVectorDTemp.pop(inputVectorDTemp.index(inputVectorD[index])))
    if len(S)==0:
        result=list(reduce(set.union,list(map(set,inputVectorDTemp))))
        result.append(nodeName+"_0")
    else:
        result = set(reduce(set.intersection, list(map(set, S))))
        if len(inputVectorDTemp) != 0:
            result=result.difference(set(reduce(set.union,list(map(set,inputVectorDTemp)))))
        result = list(result)
        result.append(nodeName+"_1")
    return result

def xorFuncD(inputVector,inputVectorD,nodeName,Output):
    '''
    Xor Function Deductive Logic
    :param inputVector: input logic vector
    :param inputVectorD: input  stuck-at-fault vector
    :param nodeName: output node name
    :param Output: output node value
    :return: list of stuck-at-fault
    '''
    result={}
    inputVectorDTemp=list(inputVectorD)
    union_set=set(reduce(set.union,list(map(set,inputVectorDTemp))))
    intersection_set=set(reduce(set.intersection,list(map(set,inputVectorDTemp))))
    result=list(union_set.difference(intersection_set))
    result.append(nodeName+"_"+str(1-Output))
    return result

def bufFuncD(inputVector,inputVectorD,nodeName,Output):
    '''
    buf Function Deductive Logic
    :param inputVector: input logic vector
    :param inputVectorD: input  stuck-at-fault vector
    :param nodeName: output node name
    :param Output: output node value
    :return: list of stuck-at-fault
    '''
    result=[]
    result.extend(inputVectorD[0])
    result.append(nodeName+"_"+str(1-Output))
    return result
