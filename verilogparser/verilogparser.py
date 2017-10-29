# -*- coding: utf-8 -*-
import re
from .logics import *
import itertools
from functools import partial
import multiprocessing as mu
from art import tprint
import random
import time
func_array=[]
import gc
import os
version="0.11"
def test_logics2():
    test_table = itertools.product([1, 0, "x", "z"], repeat=2)
    for item in test_table:
        print("OR ",item," ",orFunc(item))
        print("NOR ",item," ", norFunc(item))
        print("XOR ",item," ", xorFunc(item))
        print("XNOR ",item," ", xnorFunc(item))
        print("AND ",item," ", andFunc(item))
        print("NAND ",item," ", nandFunc(item))
def test_logics1():
    test_table = [1, 0, "x", "z"]
    for item in test_table:
        print("BUF ",item," ", bufFunc(item))
        print("NOT ",item," ", notFunc(item))
def help_func():
    '''
    Print Help Page
    :return: None
    '''
    tprint("verilogparser")
    tprint("v"+version)
    tprint("By S.Haghighi")
    print("Help : \n")
    print("     - file.v all --> (test all cases)\n")
    print("     - file.v random test_number(optional) --> (test random cases)\n")
    print("     - file.v input test vector --> (test case Example : python -m verilog test.v input 1,1,1)\n")
    print("     - file.v detail --> (module details)")
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

def time_convert(input_time):
    '''
    This function convert input_string from sec to DD,HH,MM,SS Format
    :param input_string: input time string  in sec
    :type input_string:str
    :return: converted time as string
    '''
    input_sec=int(input_time)
    input_ms=int((input_time-input_sec)*1000)
    input_minute=input_sec//60
    input_sec=int(input_sec-input_minute*60)
    input_hour=input_minute//60
    input_minute=int(input_minute-input_hour*60)
    input_day=int(input_hour//24)
    input_hour=int(input_hour-input_day*24)
    return zero_insert(str(input_day))+" days, "+zero_insert(str(input_hour))+" hour, "+zero_insert(str(input_minute))+" minutes, "+zero_insert(str(input_sec))+" seconds "+zero_insert(str(input_ms))+" ms"


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
            index_1 = item.find(" ")
            inputSection=list(map(str.strip,item[index_1+1:].replace("\n","").split(",")))
        if item.find('wire')!=-1:
            index_1 = item.find(" ")
            wireSection = list(map(str.strip, item[index_1+1:].replace("\n", "").split(",")))
        if item.find('output')!=-1:
            index_1 = item.find(" ")
            outputSection = list(map(str.strip, item[index_1+1:].replace("\n", "").split(",")))


    return (moduleSection,inputSection,wireSection,outputSection)

def readData(inp,output_dict,input_dict):
    if inp in output_dict.keys():
        tempLogic = output_dict[inp]
    else:
        tempLogic = input_dict[inp]
    return tempLogic

def functionExtractor(splitData):
    global func_array
    func_array=[]
    gate_counter = [0, 0, 0, 0, 0, 0, 0, 0]
    for item in splitData:
        output_item=""
        input_vector=[]
        index_1=item.find("(")
        index_2=item.find(")")
        splited_item=item.strip().replace("\n","").split(" ")
        input_vector = list(map(str.strip,item[index_1+1:index_2].replace("\n","").split(",")))
        output_item=input_vector.pop(0)
        if splited_item[0].upper()=="AND":
            gate_counter[0]=gate_counter[0]+1
            func_array.append([andFunc,input_vector,output_item])
        elif splited_item[0].upper()=="OR":
            gate_counter[1] = gate_counter[1] + 1
            func_array.append([orFunc, input_vector, output_item])
        elif splited_item[0].upper()=="NAND":
            gate_counter[2] = gate_counter[2] + 1
            func_array.append([nandFunc, input_vector, output_item])
        elif splited_item[0].upper()=="NOR":
            gate_counter[3] = gate_counter[3] + 1
            func_array.append([norFunc, input_vector, output_item])
        elif splited_item[0].upper() == "XOR":
            gate_counter[4] = gate_counter[4] + 1
            func_array.append([xorFunc, input_vector, output_item])
        elif splited_item[0].upper() == "XNOR":
            gate_counter[5] = gate_counter[5] + 1
            func_array.append([xnorFunc, input_vector, output_item])
        elif splited_item[0].upper() == "BUF":
            gate_counter[6] = gate_counter[6] + 1
            func_array.append([bufFunc, input_vector, output_item])
        elif splited_item[0].upper() == "NOT":
            gate_counter[7] = gate_counter[7] + 1
            func_array.append([notFunc, input_vector, output_item])
    return gate_counter
def print_result(output_dict,input_dict,file):
    sorted_out_vector=str(sorted(output_dict.items()))
    sorted_in_vector=str(sorted(input_dict.items()))
    print("INPUT VECTOR : \n")
    print(sorted_in_vector+"\n")
    file.write("INPUT VECTOR : \n" + sorted_in_vector + "\n")
    print("NODES : \n")
    print(sorted_out_vector+"\n")
    file.write("NODES : \n" + sorted_out_vector + "\n")
    file.write(line() + "\n")
    print(line())

def get_result(output_dict,input_dict):
    global func_array
    mapFunc=partial(readData,output_dict=output_dict,input_dict=input_dict)
    for item in func_array:
        input_data = list(map(mapFunc, item[1]))
        output_dict[item[2]]=item[0](input_data)
    return  output_dict
def module_detail(filename):
    try:
        if filename==None:
            raise  Exception("[Error] Invalid Input File!!")
        file = open(filename, "r")
        data = file.read()
        splitData = data.strip().split(";")
        (module, inputArray, wireArray, outputArray) = moduleExtractor(splitData)
        tprint(os.path.basename(filename),font="slant")
        print(line())
        print("Input Size : "+str(len(inputArray)))
        print(line())
        print("Wire Size : " + str(len(wireArray)))
        print(line())
        print("Output Size : " + str(len(outputArray)))
        print(line())
        gate_counter = functionExtractor(splitData)
        gate_names=["AND","OR","NAND","NOR","XOR","XNOR","BUF","NOT"]
        gate_dict=dict(zip(gate_names,gate_counter))
        for gate in gate_names:
            print(gate+" : "+str(gate_dict[gate]))
            print(line())
        gc.collect()
    except FileNotFoundError:
        print("[Error] Verilog File Not Found")
    except Exception as e:
        print(str(e))

def verilog_parser(filename,input_data=None,alltest=False,random_flag=False,test_number=100,xz_flag=False,print_status=True):
    try:
        timer_1 = time.perf_counter()
        if filename==None:
            raise  Exception("[Error] Invalid Input File!!")
        file=open(filename,"r")
        data=file.read()
        splitData = data.strip().split(";")
        (module,inputArray,wireArray,outputArray)=moduleExtractor(splitData)
        input_dict={}
        test_table=[]
        output_file=open(os.path.basename(filename).split(".")[0]+".log","w")
        gate_counter=functionExtractor(splitData)
        if alltest==True:
            test_table=test_maker(len(inputArray),random_flag=random_flag,test_number=test_number,xz_flag=xz_flag)
        else:
            if input_data==None:
                raise Exception("[Error] Bad Input Array!")
            test_table.append(input_data)
        for case in test_table:
            if len(case)==len(inputArray):
                input_dict=dict(zip(inputArray,case))
            else:
                raise Exception("[Error] Bad Input Vector (This Logic Inputs : "+str(len(inputArray))+")")
            outputs=[]
            outputs.extend(wireArray)
            outputs.extend(outputArray)
            output_dict=dict(zip(outputs,len(outputs)*["x"]))
            result=get_result(output_dict,input_dict)
            print_result(result,input_dict,output_file)
        output_file.close()
        timer_2 = time.perf_counter()
        if print_status==True:
            print("Simulation Time : " + time_convert(timer_2 - timer_1))
        gc.collect()
    except FileNotFoundError:
        print("[Error] Verilog File Not Found")
        print("Simulation Faild!")
    except Exception as e:
        print(str(e))


def shuffeler(length,xz_flag,test_number):
    basis=[1,0]
    generator=[]
    table_length=2**length
    if xz_flag==True:
        basis=[1, 0,"x","z"]
        table_length=4**length
    for i in range(length):
        random.shuffle(basis)
        generator.append(basis)
    table=itertools.product(*generator)
    return itertools.islice(table,min(test_number,table_length))

def test_maker(length,random_flag=False,test_number=100,xz_flag=False):
    '''
    This function create all of possible case for logic test
    :param length: length of bit array
    :type length: int
    :return: all of possible cases as list
    '''
    try:

        if xz_flag==False:
            table=itertools.product([1,0], repeat=length)
        else:
            table = itertools.product([1, 0,"x","z"], repeat=length)
        if random_flag==False:
            return table
        else:
            return shuffeler(length,xz_flag,test_number)
    except ValueError:
        return shuffeler(length,xz_flag,test_number)

