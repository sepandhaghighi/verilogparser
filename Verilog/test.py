# -*- coding: utf-8 -*-
'''
>>> from verilog import *
>>> import os
>>> import itertools
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
>>> time_convert('33')
'00 days, 00 hour, 00 minutes, 33 seconds'
>>> time_convert("15000")
'00 days, 04 hour, 10 minutes, 00 seconds'
>>> time_convert("sadasdasd")
Traceback (most recent call last):
        ...
ValueError: could not convert string to float: 'sadasdasd'
>>> line()
'******************************'
>>> list(test_maker(2))
[(1, 1), (1, 0), (0, 1), (0, 0)]
>>> verilog_parser(path,input_data=[1,1,1,1,1],alltest=False)
INPUT VECTOR :
<BLANKLINE>
[('N1', 1), ('N2', 1), ('N3', 1), ('N6', 1), ('N7', 1)]
NODES :
<BLANKLINE>
[('N10', 0), ('N11', 0), ('N16', 1), ('N19', 1), ('N22', 1), ('N23', 0)]
******************************

'''