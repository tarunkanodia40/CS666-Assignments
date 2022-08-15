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
        $monitor("<%d>: Data0 = %d, Data1 = %d, mode = %b, final_sum = %d, final_carry_out = %b, overflow = %b\n", $time, Data0, Data1, mode, final_sum, final_carry_out, overflow);
    end

    initial
    begin
        Data0 = 2; Data1 = 1; mode = 1;
        #5 Data0 = 2; Data1 = 1; mode = 0;
        #10 Data0 = 15; Data1 = 10; mode = 1; 
        #15 Data0 = 15; Data1 = 10; mode = 0; 
        #20 Data0 = 10; Data1 = 15; mode = 0; 
        #25 Data0 = -10; Data1 = 15; mode = 0; 
    end

endmodule
 