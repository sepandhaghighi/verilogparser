// Verilog
// c17
// Ninputs 5
// Noutputs 2
// NtotalGates 6
// NAND2 6

module c17 (A,B,C,d,e,g,f,k,Z);

input A,B,C;

wire e,d,g,f,k;

output Z;

and    AND2_1 (d,A,B);
nand   NAND2_1 (e,B,C);
xor    XOR2_1  (f,C,B);
or     OR2_1  (g,d,e);
and    AND2_2 (k,g,f);
xor    XOR2_2 (Z,k,B)



endmodule
