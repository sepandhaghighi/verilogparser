// Verilog
// c17
// Ninputs 5
// Noutputs 2
// NtotalGates 6
// NAND2 6

module c17 (a,b,e,f,g);

input a,b;

output g;

wire e,f;

and  AND2_1  (e, a, b);
not  NOT1_1  (f, b);
or   OR2_2   (g, e, f);

endmodule
