# -*- coding: utf-8 -*-
from .pyVerilog import *
import sys
if __name__=="__main__":
    args=sys.argv
    filename=""
    if len(args)>2:
        if args[2].upper()=="ALL":
            getVerilog(args[1],alltest=True)
        else:
            getVerilog(args[1],input_data=list(args[2]),alltest=False)
    else:
        print("Bad pyVerilog Call")