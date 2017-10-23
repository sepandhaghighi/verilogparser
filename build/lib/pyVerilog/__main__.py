# -*- coding: utf-8 -*-
from .pyVerilog import *
import sys
import time
if __name__=="__main__":
    args=sys.argv
    filename=""
    if len(args)>2:
        timer_1=time.perf_counter()
        if args[2].upper()=="ALL":
            getVerilog(args[1],alltest=True)
        else:
            getVerilog(args[1],input_data=args[2].split(","),alltest=False)
        timer_2=time.perf_counter()
        print("Simulation Time : "+time_convert(str(timer_2-timer_1)))
    else:
        print("Bad pyVerilog Call")