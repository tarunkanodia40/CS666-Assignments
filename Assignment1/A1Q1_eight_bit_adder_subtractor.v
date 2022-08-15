module eight_bit_adder_subtractor (Data0, Data1, mode, final_sum, final_carry_out, overflow);

    // Inputs
    input [7:0] Data0;
    input [7:0] Data1;
    input mode;

    // Outputs
    output wire [7:0] final_sum;
    output wire final_carry_out;
    output wire overflow;

    wire [7:0] Data1_in;

    assign Data1_in[0] = Data1[0] ^ (~ mode);
    assign Data1_in[1] = Data1[1] ^ (~ mode);
    assign Data1_in[2] = Data1[2] ^ (~ mode);
    assign Data1_in[3] = Data1[3] ^ (~ mode);
    assign Data1_in[4] = Data1[4] ^ (~ mode);
    assign Data1_in[5] = Data1[5] ^ (~ mode);
    assign Data1_in[6] = Data1[6] ^ (~ mode);
    assign Data1_in[7] = Data1[7] ^ (~ mode);

    wire add;
    assign add = 1;

    wire [7:0] carry;
    one_bit_adder_subtractor FAS0(Data0[0], Data1_in[0], ~mode, add, final_sum[0], carry[0]);
    one_bit_adder_subtractor FAS1(Data0[1], Data1_in[1], carry[0], add, final_sum[1], carry[1]);
    one_bit_adder_subtractor FAS2(Data0[2], Data1_in[2], carry[1], add, final_sum[2], carry[2]);
    one_bit_adder_subtractor FAS3(Data0[3], Data1_in[3], carry[2], add, final_sum[3], carry[3]);
    one_bit_adder_subtractor FAS4(Data0[4], Data1_in[4], carry[3], add, final_sum[4], carry[4]);
    one_bit_adder_subtractor FAS5(Data0[5], Data1_in[5], carry[4], add, final_sum[5], carry[5]);
    one_bit_adder_subtractor FAS6(Data0[6], Data1_in[6], carry[5], add, final_sum[6], carry[6]);
    one_bit_adder_subtractor FAS7(Data0[7], Data1_in[7], carry[6], add, final_sum[7], carry[7]);

    assign final_carry_out = carry[7];
    assign overflow = (Data0[0] ^ final_carry_out) & (Data1[0] ^ final_carry_out);

endmodule