# -*- coding: utf-8 -*-
import re
from .logics import *
import itertools
output_dict={}
input_dict={}


def zero_insert(input_string):
    '''
    This function get a string as input if input is one digit add a zero
    :param input_string: input digit az string
    :type input_string:str
    :return: modified output as str
    >>> zero_insert("22")
    >>> '22'
    '''
    if len(input_string)==1:
        return "0"+input_string
    return input_string

def time_convert(input_string):
    '''
    This function convert input_string from sec to DD,HH,MM,SS Format
    :param input_string: input time string  in sec
    :type input_string:str
    :return: converted time as string
    '''
    input_sec=float(input_string)
    input_minute=input_sec//60
    input_sec=int(input_sec-input_minute*60)
    input_hour=input_minute//60
    input_minute=int(input_minute-input_hour*60)
    input_day=int(input_hour//24)
    input_hour=int(input_hour-input_day*24)
    return zero_insert(str(input_day))+" days, "+zero_insert(str(input_hour))+" hour, "+zero_insert(str(input_minute))+" minutes, "+zero_insert(str(input_sec))+" seconds"


def line(char="*",number=30):
    return (char*number)

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
        if splited_item[0].upper()=="AND":
            input_data = list(map(readData, input_vector))
            output_dict[output_item]=andFunc(input_data)
        elif splited_item[0].upper()=="OR":
            input_data = list(map(readData, input_vector))
            output_dict[output_item] = orFunc(input_data)
        elif splited_item[0].upper()=="NAND":
            input_data = list(map(readData, input_vector))
            output_dict[output_item]=nandFunc(input_data)
        elif splited_item[0].upper()=="NOR":
            input_data = list(map(readData, input_vector))
            output_dict[output_item] = norFunc(input_data)
        elif splited_item[0].upper() == "XOR":
            input_data = list(map(readData, input_vector))
            output_dict[output_item] = xorFunc(input_data)
        elif splited_item[0].upper() == "XNOR":
            input_data = list(map(readData, input_vector))
            output_dict[output_item] = xnorFunc(input_data)
        elif splited_item[0].upper() == "BUF":
            input_data = list(map(readData, input_vector))
            output_dict[output_item] = bufFunc(input_data[0])
        elif splited_item[0].upper() == "NOT":
            input_data = list(map(readData, input_vector))
            output_dict[output_item] = notFunc(input_data[0])

def getVerilog(filename,input_data=None,alltest=False):
    try:
        global output_dict
        global input_dict
        file=open(filename,"r")
        data=file.read()
        splitData = data.strip().split(";")
        (module,inputArray,wireArray,outputArray)=moduleExtractor(splitData)
        input_dict={}
        test_table=[]
        output_file=open(filename.split(".")[0]+".log","w")
        if alltest==True:
            test_table=test_maker(len(inputArray))
        else:
            test_table.append(input_data)
        for case in test_table:
            if len(case)==len(inputArray):
                input_dict=dict(zip(inputArray,case))
            else:
                raise Exception("[Error] Bad Input Vector")
            outputs=[]
            outputs.extend(wireArray)
            outputs.extend(outputArray)
            output_dict=dict(zip(outputs,len(outputs)*[0]))
            functionExtractor(splitData)
            print("INPUT VECTOR : \n")
            print(input_dict)
            output_file.write("INPUT VECTOR : \n"+str(input_dict)+"\n")
            print("NODES : \n")
            print(output_dict)
            output_file.write("NODES : \n"+str(output_dict)+"\n")
            output_file.write(line()+"\n")
            print(line())
        output_file.close()
    except FileNotFoundError:
        print("[Error] Verilog File Not Found")
    except Exception as e:
        print(str(e))



def test_maker(length):
    '''
    This function create all of possible case for logic test
    :param length: length of bit array
    :type length: int
    :return: all of possible cases as list
    '''
    return itertools.product([1,0,"z","x"], repeat=length)


if __name__=="__main__":
    getVerilog("test.v",input_data=[1,1],alltest=False)