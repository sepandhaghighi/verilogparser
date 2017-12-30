// Verilog
// c17
// Ninputs 5
// Noutputs 2
// NtotalGates 6
// NAND2 6

module c17 (a,b);

input a,b;

wire e,f;

output g;

and #3 AND2_1 (e,a,b);
not #4 NOT1_1 (f,b);
or #7  OR2_1  (g,f,e);



endmodule
