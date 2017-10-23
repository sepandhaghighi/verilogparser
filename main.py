# -*- coding: utf-8 -*-
import re
from logics import *
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

def readData(inp):
    if inp in output_dict.keys():
        tempLogic = output_dict[inp]
    else:
        tempLogic = input_dict[inp]
    return tempLogic

def functionExtractor(splitData):
    for item in splitData:
        output_item=""
        input_vector=[]
        splited_item=item.strip().replace("\n","").split(" ")
        input_vector = list(map(str.strip,("").join(splited_item[2:])[1:-1].split(",")))
        output_item=input_vector.pop(0)
        input_data=list(map(readData,input_vector))
        if splited_item[0].upper()=="AND":
            output_dict[output_item]=andFunc(input_data)
        elif splited_item[0].upper()=="OR":
            output_dict[output_item] = orFunc(input_data)
        elif splited_item[0].upper()=="NAND":
            output_dict[output_item]=nandFunc(input_data)
        elif splited_item[0].upper()=="NOR":
            output_dict[output_item] = norFunc(input_data)
        elif splited_item[0].upper() == "XOR":
            output_dict[output_item] = xorFunc(input_data)
        elif splited_item[0].upper() == "XNOR":
            output_dict[output_item] = xnorFunc(input_data)
        elif splited_item[0].upper() == "BUF":
            output_dict[output_item] = bufFunc(input_data[0])
        elif splited_item[0].upper() == "NOT":
            output_dict[output_item] = notFunc(input_data[0])

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
    return itertools.product([1,0,"z","x"], repeat=length)


if __name__=="__main__":
    test_benchmark=test_maker(2)
    for i in test_benchmark:
        getVerilog("test.v",i)