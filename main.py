# -*- coding: utf-8 -*-
import re



def moduleExtractor(data):
    splitData=data.strip().split(";")
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



def getVerilog(filename):
    try:
        file=open(filename,"r")
        data=file.read()
        print(moduleExtractor(data))
    except FileNotFoundError:
        print("Verilog File Not Found")




if __name__=="__main__":
    getVerilog("test.v")