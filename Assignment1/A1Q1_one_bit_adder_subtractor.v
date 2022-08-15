module one_bit_adder_subtractor (i0, i1, carry_in, mode, Sum, carry_out);
    
    // Inputs
    input i0, i1, carry_in, mode;

    // Outputs
    output wire Sum, carry_out;

    // Combinational logic for the module
    assign Sum = i0 ^ i1 ^ carry_in;
    assign carry_out = ((mode & ((i0 & i1) | (i0 & carry_in) | (i1 & carry_in))) | (~mode & (~i0 & (i1 ^ carry_in)))) | (i1 & carry_in);

endmodule