module eight_bit_adder_subtractor_top;

    // Inputs
    reg signed [7:0] Data0;
    reg signed [7:0] Data1;
    reg mode;

    // Outputs
    wire signed [7:0] final_sum;
    wire final_carry_out;
    wire overflow;

    // Instantiation of 8-bit adder subtractor 
    eight_bit_adder_subtractor ADDER_SUBTRACTOR (Data0, Data1, mode, final_sum, final_carry_out, overflow);

    initial
    begin
        $monitor("<%2d>: Data0 = %4d, Data1 = %4d, mode = %b, final_sum = %4d, final_carry_out = %b, overflow = %b\n", $time, Data0, Data1, mode, final_sum, final_carry_out, overflow);
    end

    initial
    begin
        Data0 = 2; Data1 = 1; mode = 1;
        #5 Data0 = 2; Data1 = 1; mode = 0;
        #5 Data0 = 15; Data1 = 10; mode = 1; 
        #5 Data0 = 15; Data1 = 10; mode = 0; 
        #5 Data0 = 10; Data1 = 15; mode = 0; 
        #5 Data0 = -10; Data1 = 15; mode = 0; 
        #5 Data0 = 127; Data1 = 129; mode = 1;
        #5 Data0 = 127; Data1 = 127; mode = 1;
        #5 Data0 = 128; Data1 = 128; mode = 1;
        #5 Data0 = 128; Data1 = 128; mode = 0;
        #5 Data0 = -128; Data1 = -128; mode = 1;
        #5 Data0 = 101; Data1 = -101; mode = 0;
        #5 Data0 = 63; Data1 = 65; mode = 1;
        #5 Data0 = 63; Data1 = 64; mode = 1;
        #5 Data0 = 126; Data1 = 2; mode = 1;
    end

endmodule
 
