// Verilog
// c17
// Ninputs 5
// Noutputs 2
// NtotalGates 6
// NAND2 6

module c17 (a,b,e);

input a,b;

output e;


nand #4 NAND2_1  (e, a, b);


endmodule
