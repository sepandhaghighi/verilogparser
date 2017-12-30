// Verilog
// c17
// Ninputs 5
// Noutputs 2
// NtotalGates 6
// NAND2 6

module c17 (a,b,e,f,g,h,i);

input a,b;

wire e,f;

output g,h,i;

and #3 AND2_1 (e,a,b);
not #4 NOT1_1 (f,b);
nor #7  OR2_1  (g,f,e);
or #8  OR2_2  (h,a,b);
xor #9 XOR2_1 (i,a,b);



endmodule
