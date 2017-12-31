# -*- coding: utf-8 -*-
from .logics import *
from .deductivelogic import  *
import itertools
from functools import partial
from art import tprint
import random
import time
func_array=[]
fanout_dict={}
import gc
import os
version="0.23"
def test_logics2():
    '''
    This function run testbench for OR,NOR,XOR,XNOR,AND,NAND
    :return:  None
    '''
    test_table = itertools.product([1, 0, "x", "z"], repeat=2)
    for item in test_table:
        print("OR ",item," ",orFunc(item))
        print("NOR ",item," ", norFunc(item))
        print("XOR ",item," ", xorFunc(item))
        print("XNOR ",item," ", xnorFunc(item))
        print("AND ",item," ", andFunc(item))
        print("NAND ",item," ", nandFunc(item))
def test_logics1():
    '''
    This function run testbench for BUF and NOT
    :return:  None
    '''
    test_table = [1, 0, "x", "z"]
    for item in test_table:
        print("BUF ",item," ", bufFunc([item]))
        print("NOT ",item," ", notFunc([item]))
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
    print("     - file.v input test vector --> (test case Example : python -m verilogparser test.v input 1,1,1)\n")
    print("     - file.v detail --> (module details)")
    print("     - file.v deductive --> (deductive analysis)")
    print("     - file.v time timeslot --> (delay analysis Example : python -m verilogparser test.v input 1,1,1 time 12)")

def fanout_dict_handler():
    '''
    This function remove one wire output from fanout_dict
    :return: None
    '''
    global fanout_dict
    for i in fanout_dict.keys():
        if fanout_dict[i]==1:
            fanout_dict[i]=0
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
    '''
    This function return line of chr
    :param char: line character
    :param number: number of character
    :return: line as str
    '''
    return (char*number)

def moduleExtractor(splitData):
    '''
    This function extract modules of verilog file
    :param splitData: splited data
    :return: (moduleSection,inputSection,wireSection,outputSection) as tuple
    '''

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
            item_strip=item.strip()
            index_1 = item_strip.find(" ")
            inputSection=list(map(str.strip,item_strip[index_1+1:].replace("\n","").split(",")))
        if item.find('wire')!=-1:
            item_strip = item.strip()
            index_1 = item_strip.find(" ")
            wireSection = list(map(str.strip, item_strip[index_1+1:].replace("\n", "").split(",")))
        if item.find('output')!=-1:
            item_strip = item.strip()
            index_1 = item_strip.find(" ")
            outputSection = list(map(str.strip, item_strip[index_1+1:].replace("\n", "").split(",")))

    return (inputSection,wireSection,outputSection)

def readData(inp,output_dict,input_dict):
    '''
    This function read data from input wire and output
    :param inp: input name
    :param output_dict: output dictionary
    :param input_dict: input dictionary
    :return: input value
    '''
    if inp in output_dict.keys():
        tempLogic = output_dict[inp]
    else:
        tempLogic = input_dict[inp]
    return tempLogic


def functionExtractor(splitData):
    '''
    This function extract functions from verilog file
    :param splitData: splited data
    :return: number of each gates as list
    '''
    global func_array
    global fanout_dict
    func_array=[]
    gate_counter = [0, 0, 0, 0, 0, 0, 0, 0]
    for item in splitData:
        output_item=""
        input_vector=[]
        delay=0
        index_1=item.find("(")
        index_2=item.find(")")
        splited_item=item.strip().replace("\n","").split(" ")
        input_vector = list(map(str.strip,item[index_1+1:index_2].replace("\n","").split(",")))
        output_item = input_vector.pop(0)
        for i in splited_item:
            if len(i)>1:
                if i[0]=="#":
                    delay=int(i[1:])
        if splited_item[0].upper()=="AND":
            for i in input_vector:
                fanout_dict[i] = fanout_dict[i] + 1
            gate_counter[0]=gate_counter[0]+1
            func_array.append([andFunc,input_vector,output_item,andFuncD,delay])
        elif splited_item[0].upper()=="OR":
            for i in input_vector:
                fanout_dict[i] = fanout_dict[i] + 1
            gate_counter[1] = gate_counter[1] + 1
            func_array.append([orFunc, input_vector, output_item,orFuncD,delay])
        elif splited_item[0].upper()=="NAND":
            for i in input_vector:
                fanout_dict[i] = fanout_dict[i] + 1
            gate_counter[2] = gate_counter[2] + 1
            func_array.append([nandFunc, input_vector, output_item,nandFuncD,delay])
        elif splited_item[0].upper()=="NOR":
            for i in input_vector:
                fanout_dict[i] = fanout_dict[i] + 1
            gate_counter[3] = gate_counter[3] + 1
            func_array.append([norFunc, input_vector, output_item,norFuncD,delay])
        elif splited_item[0].upper() == "XOR":
            for i in input_vector:
                fanout_dict[i] = fanout_dict[i] + 1
            gate_counter[4] = gate_counter[4] + 1
            func_array.append([xorFunc, input_vector, output_item,xorFuncD,delay])
        elif splited_item[0].upper() == "XNOR":
            for i in input_vector:
                fanout_dict[i] = fanout_dict[i] + 1
            gate_counter[5] = gate_counter[5] + 1
            func_array.append([xnorFunc, input_vector, output_item,xorFuncD,delay])
        elif splited_item[0].upper() == "BUF":
            for i in input_vector:
                fanout_dict[i] = fanout_dict[i] + 1
            gate_counter[6] = gate_counter[6] + 1
            func_array.append([bufFunc, input_vector, output_item,bufFuncD,delay])
        elif splited_item[0].upper() == "NOT":
            for i in input_vector:
                fanout_dict[i] = fanout_dict[i] + 1
            gate_counter[7] = gate_counter[7] + 1
            func_array.append([notFunc, input_vector, output_item,bufFuncD,delay])
    return gate_counter
def csv_init(input_array,wire_array,output_array,file):
    '''
    This function initiate csv out file
    :param input_array: input names
    :param wire_array: wire names
    :param output_array: output names
    :param file: csv file object
    :return: None
    '''
    input_keys = []
    input_keys.extend(input_array)
    input_keys.sort()
    output_keys = []
    output_keys.extend(output_array)
    output_keys.extend(wire_array)
    output_keys.sort()
    for inp in input_keys:
        file.write(inp+",")
    file.write(",,")
    for index,out in enumerate(output_keys):
        file.write(out)
        if index<len(output_keys):
            file.write(",")
    file.write("\n")
def csv_writer(output_dict,input_dict,file):
    '''
    This function write each line of csv file
    :param output_dict: output dictionary
    :param input_dict: input dictionary
    :param file: csv file object
    :return: None
    '''
    input_keys=list(input_dict.keys())
    input_keys.sort()
    output_keys=list(output_dict.keys())
    output_keys.sort()
    for inp in input_keys:
        file.write(str(input_dict[inp])+",")
    file.write(",,")
    for index,out in enumerate(output_keys):
        file.write(str(output_dict[out]))
        if index<len(output_keys):
            file.write(",")
    file.write("\n")

def csv_time_writer(output_dict,input_dict,file):
    '''
    This function write csv_file for time simulation
    :param output_dict: time simulation output dictionary
    :param input_dict: input dictionary
    :param file: csv_time file object
    :return:  None
    '''
    input_keys = list(input_dict.keys())
    input_keys.sort()
    output_keys = list(output_dict.keys())
    output_keys.sort()
    for inp in input_keys:
        file.write(str(inp)+",")
        file.write(",".join(list(map(str,input_dict[inp][:-1]))))
        file.write("\n")
    for out in output_keys:
        file.write(out)
        file.write(",")
        file.write(",".join(list(map(str,output_dict[out]))))
        file.write("\n")
    file.write("\n")

def csv_time_init(time_slot,file):
    '''
    This function initiate csv_file for time simulation
    :param time_slot: time slot for time simulation
    :param file: csv_time file object
    :return: None
    '''
    file.write("Input,")
    for i in range(time_slot):
        file.write("T"+str(i))
        if i<time_slot+1:
            file.write(",")
    file.write("\n")




def print_result(output_dict,input_dict,file):
    '''
    This function print and save result in file
    :param output_dict: output dictionary
    :param input_dict: input dictionar
    :param file: file
    :return: None
    '''
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

def get_result(output_dict,input_dict,deductive_dict):
    '''
    This function calculate resultof each gate
    :param output_dict:  output dictionary
    :param input_dict:  input dictionary
    :param deductive_dict:  dedeuctive dictionary
    :return: [output_dict,deductive_dict]  as list
    '''
    global func_array
    mapFunc=partial(readData,output_dict=output_dict,input_dict=input_dict)
    fanout_dict_handler()
    fanout_dict_temp=fanout_dict.copy()
    for key in input_dict.keys():
        deductive_dict[key]=[key+"_"+str(1-input_dict[key])]
    for item in func_array:
        fanout_added=[]
        input_data = list(map(mapFunc, item[1]))
        output_dict[item[2]] = item[0](input_data)
        for index,j in enumerate(item[1]):
            if fanout_dict_temp[j]>0:
                deductive_dict[j].append("FANOUT"+str(fanout_dict_temp[j])+"("+j+")_"+str(1-input_data[index]))
                fanout_added.append(j)
                fanout_dict_temp[j]=fanout_dict_temp[j]-1
        deductive_dict[item[2]]=item[3](input_data,list(map(lambda i:deductive_dict[i],item[1])),item[2],output_dict[item[2]])
        for i in fanout_added:
            fanout=deductive_dict[i][-1]
            deductive_dict[fanout]=deductive_dict[i]
            deductive_dict[i]=deductive_dict[i][:-1]
    return  [output_dict,deductive_dict]

def get_result_time(output_dict,input_dict,time_slot):
    '''
    This function calculate delay simulation for each input
    :param output_dict: output dictionary
    :param input_dict: input dictionary
    :param time_slot: observation timeslot
    :return: output dictionary
    '''
    global func_array
    output_dict_temp=output_dict.copy()
    mapFunc = partial(readData, output_dict=output_dict, input_dict=input_dict)
    for i in input_dict.keys():
        input_dict[i]=[input_dict[i]]
    for i in range(time_slot):
        for item in func_array:
            input_data = list(map(mapFunc, item[1]))
            delay=item[4]
            if delay<=i:
                output_dict_temp[item[2]].append(item[0](list(map(lambda x: x[i-delay],input_data))))
            else:
                pointer=item[2]
                output_dict_temp[pointer].append(output_dict_temp[item[2]][-1])
        for j in input_dict.keys():
            input_dict[j].append(input_dict[j][-1])
    for i in output_dict_temp.keys():
        output_dict_temp[i]=output_dict_temp[i][1:]
    return output_dict_temp


def module_detail(filename):
    '''
    This function show modules details
    :param filename: verilog file name
    :return: None
    '''
    try:
        if filename==None:
            raise  Exception("[Error] Invalid Input File!!")
        file = open(filename, "r")
        data = file.read()
        splitData = data.strip().split(";")
        (inputArray, wireArray, outputArray) = moduleExtractor(splitData)
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
    except Exception:
        print("Parsing Faild!")

def verilog_parser(filename,input_data=None,alltest=False,random_flag=False,test_number=100,xz_flag=False,print_status=True,deductive_mode=False,time_mode=False,time_slot=0):
    '''
    Main Function of program run simulation in different mode
    :param filename: verilog file name
    :param input_data: input data
    :param alltest: all test mode flag
    :param random_flag: random test flag
    :param test_number: number of test
    :param xz_flag: xz mode flag
    :param print_status: print simulation status
    :param deductive_mode: deductive simulation mode flag
    :param time_mode: delay simulation mode flag
    :param time_slot: time slot
    :return: None
    '''
    try:
        global fanout_dict
        timer_1 = time.perf_counter()
        fanout_keys=[]
        if filename==None:
            raise  Exception("[Error] Invalid Input File!!")
        file=open(filename,"r")
        data=file.read()
        splitData = data.strip().split(";")
        (inputArray,wireArray,outputArray)=moduleExtractor(splitData)
        fanout_keys.extend(wireArray)
        fanout_keys.extend(inputArray)
        fanout_dict=dict(zip(fanout_keys,len(fanout_keys)*[0]))
        input_dict={}
        test_table=[]
        output_file=open(os.path.basename(filename).split(".")[0]+".log","w")
        csv_file=open(os.path.basename(filename).split(".")[0]+".csv","w")
        csv_init(inputArray,wireArray,outputArray,csv_file)
        functionExtractor(splitData)
        if deductive_mode==True and time_mode==False:
            deductive_file=open(os.path.basename(filename).split(".")[0]+".ds","w")
        if time_mode==True:
            time_csv_file = open(os.path.basename(filename).split(".")[0] + "_time.csv", "w")
            csv_time_init(time_slot,time_csv_file)
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
            output_dict={k:["x"] for k in outputs}
            dedcutive_dict=dict(zip(outputs,len(outputs)*[[]]))
            if time_mode==True:
                result=get_result_time(output_dict,input_dict,time_slot)
                print_result(result, input_dict, output_file)
                csv_time_writer(result,input_dict,time_csv_file)
                #result = get_result(output_dict, input_dict, dedcutive_dict)
                #csv_writer(result[0], input_dict, csv_file)
                #print_result(result[0], input_dict, output_file)
            else:
                result = get_result(output_dict, input_dict, dedcutive_dict)
                if deductive_mode==True:
                    print_result(result[1],input_dict,deductive_file)
                csv_writer(result[0],input_dict,csv_file)
                print_result(result[0],input_dict,output_file)
        output_file.close()
        csv_file.close()
        if deductive_mode==True and time_mode==False:
            deductive_file.close()
        if time_mode==True:
            time_csv_file.close()
        timer_2 = time.perf_counter()
        if print_status==True:
            print("Simulation Time : " + time_convert(timer_2 - timer_1))
        gc.collect()
    except FileNotFoundError:
        print("[Error] Verilog File Not Found")
        print("Simulation Faild!")
    except Exception as e:
        print(str(e))


def shuffler(length,xz_flag,test_number):
    '''
    This function shuffle for random test
    :param length: length of test
    :param xz_flag: xz flag mode
    :param test_number: number of test
    :return: test vectors
    '''
    basis=[1,0]
    generator=[]
    table_length=2**length
    if xz_flag==True:
        basis=[1, 0,"x","z"]
        table_length=4**length
    for i in range(length):
        random.shuffle(basis)
        generator.append(basis)
        random.shuffle(generator)
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
            return shuffler(length,xz_flag,test_number)
    except ValueError:
        return shuffler(length,xz_flag,test_number)

