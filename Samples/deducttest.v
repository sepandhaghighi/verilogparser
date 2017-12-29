// Verilog
// c17
// Ninputs 5
// Noutputs 2
// NtotalGates 6
// NAND2 6

module c17 (a,b,e,f,g,h,i,j,k,l);

input a,b;

output e,f,g,h,i,j,k,l;


nand #3 NAND2_1  (e, a, b);
or #3   OR2_1    (f,a,b);
and #4  AND2_1   (g,a,b);
buf #5  BUF1_1   (h,a);
not #7  NOT1_1   (i,a);
xor #2  XOR2_1   (j,a,b);
xnor #3 XNOR2_1  (k,b,a);
nor  #3 NOR2_1   (l,a,b);

endmodule
