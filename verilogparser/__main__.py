# -*- coding: utf-8 -*-
from .verilogparser import *
import sys
import doctest
def map_int(item):
    if item=='1' or item=='0':
        return int(item)
    else:
        return item
if __name__=="__main__":
    args=sys.argv
    filename=None
    input_data=None
    for item in args:
        if item.find(".v")!=-1:
            filename=item
    xz_flag=False
    test_number=100
    all_mode=False
    random_mode=False
    upper_args=list(map(str.upper,args))
    if "TEST" in upper_args:
        doctest.testfile("test.py", optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
        sys.exit()
    if "INPUT" in upper_args:
        index=upper_args.index("INPUT")
        if len(upper_args)>index+1:
            input_data=list(map(map_int,list(args[index+1].split(","))))
    if "XZ" in upper_args:
        xz_flag=True
    if "RANDOM" in upper_args and (len(upper_args)>2):
        random_mode=True
        all_mode=True
        index = upper_args.index("RANDOM")
        try:
            if len(upper_args)>index+1:
                test_number=int(args[index+1])
        except ValueError:
            pass
    if ("ALL" in upper_args) and (len(upper_args)>2):
        all_mode=True
    if "HELP" in upper_args:
        help_func()
        sys.exit()
    if "DETAIL" in upper_args:
        module_detail(filename=filename)
        sys.exit()

    if all_mode==True:
        verilog_parser(filename,alltest=True,random_flag=random_mode,xz_flag=xz_flag,test_number=test_number)
    else:
        verilog_parser(filename,input_data=input_data)




