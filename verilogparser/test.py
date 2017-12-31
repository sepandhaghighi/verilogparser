# -*- coding: utf-8 -*-
'''
>>> from verilogparser import *
>>> import os
>>> import itertools
>>> import coverage
>>> import random
>>> cov=coverage.Coverage()
>>> cov.start()
>>> path=os.path.join(os.getcwd(),"Samples","c17.v")
>>> test_logics1()
BUF  1   1
NOT  1   0
BUF  0   0
NOT  0   1
BUF  x   x
NOT  x   x
BUF  z   x
NOT  z   x
>>> test_logics2()
OR  (1, 1)   1
NOR  (1, 1)   0
XOR  (1, 1)   0
XNOR  (1, 1)   1
AND  (1, 1)   1
NAND  (1, 1)   0
OR  (1, 0)   1
NOR  (1, 0)   0
XOR  (1, 0)   1
XNOR  (1, 0)   0
AND  (1, 0)   0
NAND  (1, 0)   1
OR  (1, 'x')   1
NOR  (1, 'x')   0
XOR  (1, 'x')   x
XNOR  (1, 'x')   x
AND  (1, 'x')   x
NAND  (1, 'x')   x
OR  (1, 'z')   1
NOR  (1, 'z')   0
XOR  (1, 'z')   x
XNOR  (1, 'z')   x
AND  (1, 'z')   x
NAND  (1, 'z')   x
OR  (0, 1)   1
NOR  (0, 1)   0
XOR  (0, 1)   1
XNOR  (0, 1)   0
AND  (0, 1)   0
NAND  (0, 1)   1
OR  (0, 0)   0
NOR  (0, 0)   1
XOR  (0, 0)   0
XNOR  (0, 0)   1
AND  (0, 0)   0
NAND  (0, 0)   1
OR  (0, 'x')   x
NOR  (0, 'x')   x
XOR  (0, 'x')   x
XNOR  (0, 'x')   x
AND  (0, 'x')   0
NAND  (0, 'x')   1
OR  (0, 'z')   x
NOR  (0, 'z')   x
XOR  (0, 'z')   x
XNOR  (0, 'z')   x
AND  (0, 'z')   0
NAND  (0, 'z')   1
OR  ('x', 1)   1
NOR  ('x', 1)   0
XOR  ('x', 1)   x
XNOR  ('x', 1)   x
AND  ('x', 1)   x
NAND  ('x', 1)   x
OR  ('x', 0)   x
NOR  ('x', 0)   x
XOR  ('x', 0)   x
XNOR  ('x', 0)   x
AND  ('x', 0)   0
NAND  ('x', 0)   1
OR  ('x', 'x')   x
NOR  ('x', 'x')   x
XOR  ('x', 'x')   x
XNOR  ('x', 'x')   x
AND  ('x', 'x')   x
NAND  ('x', 'x')   x
OR  ('x', 'z')   x
NOR  ('x', 'z')   x
XOR  ('x', 'z')   x
XNOR  ('x', 'z')   x
AND  ('x', 'z')   x
NAND  ('x', 'z')   x
OR  ('z', 1)   1
NOR  ('z', 1)   0
XOR  ('z', 1)   x
XNOR  ('z', 1)   x
AND  ('z', 1)   x
NAND  ('z', 1)   x
OR  ('z', 0)   x
NOR  ('z', 0)   x
XOR  ('z', 0)   x
XNOR  ('z', 0)   x
AND  ('z', 0)   0
NAND  ('z', 0)   1
OR  ('z', 'x')   x
NOR  ('z', 'x')   x
XOR  ('z', 'x')   x
XNOR  ('z', 'x')   x
AND  ('z', 'x')   x
NAND  ('z', 'x')   x
OR  ('z', 'z')   x
NOR  ('z', 'z')   x
XOR  ('z', 'z')   x
XNOR  ('z', 'z')   x
AND  ('z', 'z')   x
NAND  ('z', 'z')   x
>>> zero_insert("22")
'22'
>>> zero_insert("320")
'320'
>>> zero_insert("2")
'02'
>>> zero_insert(22)
Traceback (most recent call last):
        ...
TypeError: object of type 'int' has no len()
>>> time_convert(33)
'00 days, 00 hour, 00 minutes, 33 seconds 00 ms'
>>> time_convert(15000)
'00 days, 04 hour, 10 minutes, 00 seconds 00 ms'
>>> time_convert("sadasdasd")
Traceback (most recent call last):
        ...
ValueError: invalid literal for int() with base 10: 'sadasdasd'
>>> line()
'******************************'
>>> list(test_maker(2))
[(1, 1), (1, 0), (0, 1), (0, 0)]
>>> verilog_parser(path,input_data=[1,1,1,1,1],alltest=False,print_status=False)
INPUT VECTOR :
<BLANKLINE>
[('N1', 1), ('N2', 1), ('N3', 1), ('N6', 1), ('N7', 1)]
NODES :
<BLANKLINE>
[('N10', 0), ('N11', 0), ('N16', 1), ('N19', 1), ('N22', 1), ('N23', 0)]
<BLANKLINE>
******************************
>>> module_detail(path)
          ___ _____
  _____  <  //__  /    _   __
 / ___/  / /   / /    | | / /
/ /__   / /   / /   _ | |/ /
\___/  /_/   /_/   (_)|___/
<BLANKLINE>
<BLANKLINE>
******************************
Input Size : 5
******************************
Wire Size : 4
******************************
Output Size : 2
******************************
AND : 0
******************************
OR : 0
******************************
NAND : 6
******************************
NOR : 0
******************************
XOR : 0
******************************
XNOR : 0
******************************
BUF : 0
******************************
NOT : 0
******************************
>>> help_func()
                    _  _
__   __  ___  _ __ (_)| |  ___    __ _  _ __    __ _  _ __  ___   ___  _ __
\ \ / / / _ \| '__|| || | / _ \  / _` || '_ \  / _` || '__|/ __| / _ \| '__|
 \ V / |  __/| |   | || || (_) || (_| || |_) || (_| || |   \__ \|  __/| |
  \_/   \___||_|   |_||_| \___/  \__, || .__/  \__,_||_|   |___/ \___||_|
                                 |___/ |_|
<BLANKLINE>
         ___      ____   _____
__   __ / _ \    |___ \ |___ /
\ \ / /| | | |     __) |  |_ \
 \ V / | |_| | _  / __/  ___) |
  \_/   \___/ (_)|_____||____/
<BLANKLINE>
<BLANKLINE>
 ____           ____      _   _                _      _         _      _
| __ )  _   _  / ___|    | | | |  __ _   __ _ | |__  (_)  __ _ | |__  (_)
|  _ \ | | | | \___ \    | |_| | / _` | / _` || '_ \ | | / _` || '_ \ | |
| |_) || |_| |  ___) | _ |  _  || (_| || (_| || | | || || (_| || | | || |
|____/  \__, | |____/ (_)|_| |_| \__,_| \__, ||_| |_||_| \__, ||_| |_||_|
        |___/                           |___/            |___/
<BLANKLINE>
Help :
<BLANKLINE>
     - file.v all --> (test all cases)
<BLANKLINE>
     - file.v random test_number(optional) --> (test random cases)
<BLANKLINE>
     - file.v input test vector --> (test case Example : python -m verilogparser test.v input 1,1,1)
<BLANKLINE>
     - file.v detail --> (module details)
     - file.v deductive --> (deductive analysis)
     - file.v time timeslot --> (delay analysis Example : python -m verilogparser test.v input 1,1,1 time 12)
Help :
<BLANKLINE>
     - file.v all --> (test all cases)
<BLANKLINE>
     - file.v random test_number(optional) --> (test random cases)
<BLANKLINE>
     - file.v input test vector --> (test case Example : python -m verilogparser test.v input 1,1,1)
<BLANKLINE>
     - file.v detail --> (module details)
     - file.v deductive --> (deductive analysis)
     - file.v time timeslot --> (delay analysis Example : python -m verilogparser test.v input 1,1,1 time 12)
>>> path=os.path.join(os.getcwd(),"Samples","deducttest2.v")
>>> verilog_parser(path,input_data=[1,1],alltest=False,random_flag=False,test_number=100,xz_flag=False,print_status=False,deductive_mode=True,time_mode=False,time_slot=0)
INPUT VECTOR :
<BLANKLINE>
[('a', 1), ('b', 1)]
<BLANKLINE>
NODES :
<BLANKLINE>
[('FANOUT1(b)_0', ['b_0', 'FANOUT1(b)_0']), ('FANOUT2(b)_0', ['b_0', 'FANOUT2(b)_0']), ('a', ['a_0']), ('b', ['b_0']), ('e', ['FANOUT2(b)_0', 'a_0', 'b_0', 'e_0']), ('f', ['b_0', 'FANOUT1(b)_0', 'f_1']), ('g', ['FANOUT2(b)_0', 'a_0', 'e_0', 'g_0'])]
<BLANKLINE>
******************************
INPUT VECTOR :
<BLANKLINE>
[('a', 1), ('b', 1)]
<BLANKLINE>
NODES :
<BLANKLINE>
[('e', 1), ('f', 0), ('g', 1)]
<BLANKLINE>
******************************
>>> path=os.path.join(os.getcwd(),"Samples","deducttest3.v")
>>> verilog_parser(path,input_data=[0,1],alltest=False,random_flag=False,test_number=100,xz_flag=False,print_status=False,deductive_mode=True,time_mode=False,time_slot=0)
INPUT VECTOR :
<BLANKLINE>
[('a', 0), ('b', 1)]
<BLANKLINE>
NODES :
<BLANKLINE>
[('FANOUT1(a)_1', ['a_1', 'FANOUT1(a)_1']), ('FANOUT1(b)_0', ['b_0', 'FANOUT1(b)_0']), ('FANOUT2(a)_1', ['a_1', 'FANOUT2(a)_1']), ('FANOUT2(b)_0', ['b_0', 'FANOUT2(b)_0']), ('FANOUT3(a)_1', ['a_1', 'FANOUT3(a)_1']), ('FANOUT3(b)_0', ['b_0', 'FANOUT3(b)_0']), ('FANOUT4(b)_0', ['b_0', 'FANOUT4(b)_0']), ('a', ['a_1']), ('b', ['b_0']), ('e', ['a_1', 'FANOUT3(a)_1', 'e_1']), ('f', ['b_0', 'FANOUT3(b)_0', 'f_1']), ('g', ['FANOUT3(b)_0', 'FANOUT3(a)_1', 'f_1', 'a_1', 'b_0', 'e_1', 'g_0']), ('h', ['FANOUT2(b)_0', 'b_0', 'h_0']), ('i', ['a_1', 'FANOUT1(a)_1', 'b_0', 'FANOUT1(b)_0', 'i_0'])]
<BLANKLINE>
******************************
INPUT VECTOR :
<BLANKLINE>
[('a', 0), ('b', 1)]
<BLANKLINE>
NODES :
<BLANKLINE>
[('e', 0), ('f', 0), ('g', 1), ('h', 1), ('i', 1)]
<BLANKLINE>
******************************
>>> path=os.path.join(os.getcwd(),"Samples","deducttest.v")
>>> verilog_parser(path,input_data=[1,1],alltest=False,random_flag=False,test_number=100,xz_flag=False,print_status=False,deductive_mode=False,time_mode=True,time_slot=10)
INPUT VECTOR :
<BLANKLINE>
[('a', [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), ('b', [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])]
<BLANKLINE>
NODES :
<BLANKLINE>
[('e', ['x', 'x', 'x', 0, 0, 0, 0, 0, 0, 0]), ('f', ['x', 'x', 'x', 1, 1, 1, 1, 1, 1, 1]), ('g', ['x', 'x', 'x', 'x', 1, 1, 1, 1, 1, 1]), ('h', ['x', 'x', 'x', 'x', 'x', 1, 1, 1, 1, 1]), ('i', ['x', 'x', 'x', 'x', 'x', 'x', 'x', 0, 0, 0]), ('j', ['x', 'x', 0, 0, 0, 0, 0, 0, 0, 0]), ('k', ['x', 'x', 'x', 1, 1, 1, 1, 1, 1, 1]), ('l', ['x', 'x', 'x', 0, 0, 0, 0, 0, 0, 0])]
<BLANKLINE>
******************************
>>> random.seed(2)
>>> verilog_parser(path,input_data=[1,1],alltest=False,random_flag=True,test_number=100,xz_flag=False,print_status=False,deductive_mode=False,time_mode=True,time_slot=10)
INPUT VECTOR :
<BLANKLINE>
[('a', [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), ('b', [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])]
<BLANKLINE>
NODES :
<BLANKLINE>
[('e', ['x', 'x', 'x', 0, 0, 0, 0, 0, 0, 0]), ('f', ['x', 'x', 'x', 1, 1, 1, 1, 1, 1, 1]), ('g', ['x', 'x', 'x', 'x', 1, 1, 1, 1, 1, 1]), ('h', ['x', 'x', 'x', 'x', 'x', 1, 1, 1, 1, 1]), ('i', ['x', 'x', 'x', 'x', 'x', 'x', 'x', 0, 0, 0]), ('j', ['x', 'x', 0, 0, 0, 0, 0, 0, 0, 0]), ('k', ['x', 'x', 'x', 1, 1, 1, 1, 1, 1, 1]), ('l', ['x', 'x', 'x', 0, 0, 0, 0, 0, 0, 0])]
<BLANKLINE>
******************************
>>> cov.stop()
>>> cov.save()

'''