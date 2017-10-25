# -*- coding: utf-8 -*-
from .Verilog import *
import sys
import time
import doctest
if __name__=="__main__":
    args=sys.argv
    filename=""
    if len(args)>1:
        if args[1].upper()=="HELP":
            help_func()
            sys.exit()
        elif args[1].upper()=="TEST":
            doctest.testfile("test.py",verbose=True)

        timer_1 = time.perf_counter()
        if len(args)>2:
            if args[2].upper()=="ALL":
                verilog_parser(args[1],alltest=True)
            elif args[2].upper()=="RANDOM":
                if len(args)>3:
                    verilog_parser(args[1], alltest=True, random_flag=True,test_number=int(args[3]))
                else:
                    verilog_parser(args[1],alltest=True,random_flag=True)
            else:
                verilog_parser(args[1],input_data=args[2].split(","),alltest=False)
            timer_2=time.perf_counter()
            print("Simulation Time : "+time_convert(str(timer_2-timer_1)))
    else:
        help_func()