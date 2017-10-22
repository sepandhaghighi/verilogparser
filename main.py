# -*- coding: utf-8 -*-
import re
from operator import xor
import itertools
output_dict={}
input_dict={}

def moduleExtractor(splitData):

    moduleSection=[]
    inputSection=[]
    wireSection=[]
    outputSection=[]
    for item in splitData:
        if (item.find("module")!=-1) and (item.find("endmodule")==-1):
            index_1 = item.find("(")
            index_2 = item.find(")")
            moduleSection=list(map(str.strip,item[index_1+1:index_2].replace("\n","").split(",")))
        if item.find("input")!=-1:
            inputSection=list(map(str.strip,item[8:].replace("\n","").split(",")))
        if item.find('wire')!=-1:
            wireSection = list(map(str.strip, item[7:].replace("\n", "").split(",")))
        if item.find('output')!=-1:
            outputSection = list(map(str.strip, item[9:].replace("\n", "").split(",")))


    return (moduleSection,inputSection,wireSection,outputSection)

def functionExtractor(splitData):
    for item in splitData:
        output_item=""
        input_vector=[]
        splited_item=item.strip().replace("\n","").split(" ")
        input_vector = list(map(str.strip,("").join(splited_item[2:])[1:-1].split(",")))
        output_item=input_vector.pop(0)
        if splited_item[0].upper()=="AND":
            output_dict[output_item]=andFunc(input_vector)
        elif splited_item[0].upper()=="OR":
            output_dict[output_item] = orFunc(input_vector)
        elif splited_item[0].upper()=="NAND":
            output_dict[output_item]=nandFunc(input_vector)
        elif splited_item[0].upper()=="NOR":
            output_dict[output_item] = norFunc(input_vector)
        elif splited_item[0].upper() == "XOR":
            output_dict[output_item] = xorFunc(input_vector)
        elif splited_item[0].upper() == "XNOR":
            output_dict[output_item] = xnorFunc(input_vector)
        elif splited_item[0].upper() == "BUF":
            output_dict[output_item] = bufFunc(input_vector[0])
        elif splited_item[0].upper() == "NOT":
            output_dict[output_item] = notFunc(input_vector[0])





def andFunc(inputVector):
    output=1
    tempLogic=1
    for i in inputVector:
        if i in output_dict.keys():
            tempLogic=output_dict[i]
        else:
            tempLogic=input_dict[i]
        if (tempLogic=="z" or tempLogic=="x") and output!=0:
            output="x"
            break
        elif tempLogic==0:
            output=0
            break
        else:
            output=output and tempLogic
    return output
def nandFunc(inputLogic):
    output=andFunc(inputLogic)
    if output==1:
        return 0
    elif output==0:
        return 1
    else:
        return "x"
def bufFunc(inputLogic):
    temp=inputLogic
    if temp=="z" or temp=="x":
        return "x"
    else:
        return temp
def notFunc(inputLogic):
    temp=inputLogic
    if temp=="z" or temp=="x":
        return "x"
    elif temp==1:
        return 0
    else:
        return 1
def xorFunc(inputVector):
    output=0
    tempLogic=0
    for i in inputVector:
        if i in output_dict.keys():
            tempLogic=output_dict[i]
        else:
            tempLogic=input_dict[i]
        if tempLogic=="z" or tempLogic=="x":
            output="x"
            break
        else:
            output=xor(output,tempLogic)
    return output

def xnorFunc(inputVector):
    output=xorFunc(inputVector)
    if output=="x":
        return output
    elif output==1:
        return 0
    else:
        return 1

def orFunc(inputVector):
    output=0
    tempLogic=0
    for i in inputVector:
        if i in output_dict.keys():
            tempLogic=output_dict[i]
        else:
            tempLogic=input_dict[i]
        if (tempLogic=="z" or tempLogic=="x") and output!=1:
            output="x"
            break
        elif tempLogic==1:
            output=1
            break
        else:
            output=output or tempLogic
    return output
def norFunc(inputVector):
    output=orFunc(inputVector)
    if output=="x":
        return output
    elif output==1:
        return 0
    else :
        return 1
def getVerilog(filename,input_data):
    try:
        global output_dict
        global input_dict
        file=open(filename,"r")
        data=file.read()
        splitData = data.strip().split(";")
        (module,inputArray,wireArray,outputArray)=moduleExtractor(splitData)
        input_dict={}
        if len(input_data)==len(inputArray):
            input_dict=dict(zip(inputArray,input_data))
        outputs=[]
        outputs.extend(wireArray)
        outputs.extend(outputArray)
        output_dict=dict(zip(outputs,len(outputs)*[0]))
        functionExtractor(splitData)
        print(input_dict,output_dict)



    except FileNotFoundError:
        print("Verilog File Not Found")



def test_maker(length):
    '''
    This function create all of possible case for logic test
    :param length: length of bit array
    :type length: int
    :return: all of possible cases as list
    '''
    return itertools.combinations_with_replacement([1,0,"z","x"],length)


if __name__=="__main__":
    test_benchmark=test_maker(2)
    for i in test_benchmark:
        getVerilog("test.v",i)