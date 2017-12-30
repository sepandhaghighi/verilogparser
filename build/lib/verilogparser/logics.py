# -*- coding: utf-8 -*-
from operator import xor
def andFunc(inputVector):
    '''
    And Function
    :param inputVector: input vector
    :type inputVector:list
    :return: ["x",0,1]
    '''
    output=1
    if 0 in inputVector:
        output=0
    elif ("z" in inputVector) or ("x" in inputVector):
        output="x"
    else:
        output=1
    return output
def nandFunc(inputVector):
    '''
    Nand Function
    :param inputVector: input vector
    :type inpuVector : list
    :return: ["x",0,1]
    '''
    output=andFunc(inputVector)
    if output==1:
        return 0
    elif output==0:
        return 1
    else:
        return "x"
def bufFunc(inputLogic):
    '''
    Buf Function
    :param inputLogic: 0,"z","x",1
    :type inpuVector : str,int
    :return: ["x",0,1]
    '''
    temp=inputLogic
    if "z" in temp or "x" in temp:
        return "x"
    else:
        return temp[0]
def notFunc(inputLogic):
    '''
    Not Function
    :param inputLogic: 0,"z","x",1
    :type inpuVector : str,int
    :return: ["x",0,1]
    '''
    temp=inputLogic
    if "z" in temp or "x" in temp:
        return "x"
    elif 1 in temp:
        return 0
    else:
        return 1
def xorFunc(inputVector):
    '''
    Xor Function
    :param inputVector: input vector
    :type inpuVector : list
    :return: ["x",0,1]
    '''
    output=0
    for i in inputVector:
        if i=="z" or i=="x":
            output="x"
            break
        else:
            output=xor(output,i)
    return output

def xnorFunc(inputVector):
    '''
    Xnor Function
    :param inputVector: input vector
    :type inpuVector : list
    :return: ["x",0,1]
    '''
    output=xorFunc(inputVector)
    if output=="x":
        return output
    elif output==1:
        return 0
    else:
        return 1

def orFunc(inputVector):
    '''
    Or Function
    :param inputVector: input vector
    :type inpuVector : list
    :return: ["x",0,1]
    '''
    output=0
    if 1 in inputVector:
        output=1
    elif ("z" in inputVector) or ("x" in inputVector):
        output="x"
    else:
        output=0
    return output
def norFunc(inputVector):
    '''
    Nor Function
    :param inputVector: input vector
    :type inpuVector : list
    :return: ["x",0,1]
    '''
    output=orFunc(inputVector)
    if output=="x":
        return output
    elif output==1:
        return 0
    else :
        return 1