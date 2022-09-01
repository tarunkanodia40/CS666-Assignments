module sbox_top;

    // Inputs
    reg [3:0] x_case;
    reg [3:0] x_combinational;

    // Outputs
    wire [3:0] result_case;
    wire [3:0] result_combinational;

    // Instantiation of 8-bit adder subtractor 
    sbox_case SBOX_CASE (x_case, result_case);
    sbox_combinational SBOX_COMBINATIONAL (x_combinational, result_combinational);

    initial
    begin
        x_case = 'h0; x_combinational = 'h0; #1 $display("<%2d>: x = %h, Sbox_case(x) = %h\n", $time, x_case, result_case);  $display("<%2d>: x = %h, Sbox_combinational(x) = %h\n", $time, x_combinational, result_combinational);
        #5 x_case = 'h1; x_combinational = 'h1; #1 $display("<%2d>: x = %h, Sbox_case(x) = %h\n", $time, x_case, result_case);  $display("<%2d>: x = %h, Sbox_combinational(x) = %h\n", $time, x_combinational, result_combinational);
        #5 x_case = 'h2; x_combinational = 'h2; #1 $display("<%2d>: x = %h, Sbox_case(x) = %h\n", $time, x_case, result_case);  $display("<%2d>: x = %h, Sbox_combinational(x) = %h\n", $time, x_combinational, result_combinational);
        #5 x_case = 'h3; x_combinational = 'h3; #1 $display("<%2d>: x = %h, Sbox_case(x) = %h\n", $time, x_case, result_case);  $display("<%2d>: x = %h, Sbox_combinational(x) = %h\n", $time, x_combinational, result_combinational);
        #5 x_case = 'h4; x_combinational = 'h4; #1 $display("<%2d>: x = %h, Sbox_case(x) = %h\n", $time, x_case, result_case);  $display("<%2d>: x = %h, Sbox_combinational(x) = %h\n", $time, x_combinational, result_combinational);
        #5 x_case = 'h5; x_combinational = 'h5; #1 $display("<%2d>: x = %h, Sbox_case(x) = %h\n", $time, x_case, result_case);  $display("<%2d>: x = %h, Sbox_combinational(x) = %h\n", $time, x_combinational, result_combinational);
        #5 x_case = 'h6; x_combinational = 'h6; #1 $display("<%2d>: x = %h, Sbox_case(x) = %h\n", $time, x_case, result_case);  $display("<%2d>: x = %h, Sbox_combinational(x) = %h\n", $time, x_combinational, result_combinational);
        #5 x_case = 'h7; x_combinational = 'h7; #1 $display("<%2d>: x = %h, Sbox_case(x) = %h\n", $time, x_case, result_case);  $display("<%2d>: x = %h, Sbox_combinational(x) = %h\n", $time, x_combinational, result_combinational);
        #5 x_case = 'h8; x_combinational = 'h8; #1 $display("<%2d>: x = %h, Sbox_case(x) = %h\n", $time, x_case, result_case);  $display("<%2d>: x = %h, Sbox_combinational(x) = %h\n", $time, x_combinational, result_combinational);
        #5 x_case = 'h9; x_combinational = 'h9; #1 $display("<%2d>: x = %h, Sbox_case(x) = %h\n", $time, x_case, result_case);  $display("<%2d>: x = %h, Sbox_combinational(x) = %h\n", $time, x_combinational, result_combinational);
        #5 x_case = 'hA; x_combinational = 'hA; #1 $display("<%2d>: x = %h, Sbox_case(x) = %h\n", $time, x_case, result_case);  $display("<%2d>: x = %h, Sbox_combinational(x) = %h\n", $time, x_combinational, result_combinational);
        #5 x_case = 'hB; x_combinational = 'hB; #1 $display("<%2d>: x = %h, Sbox_case(x) = %h\n", $time, x_case, result_case);  $display("<%2d>: x = %h, Sbox_combinational(x) = %h\n", $time, x_combinational, result_combinational);
        #5 x_case = 'hC; x_combinational = 'hC; #1 $display("<%2d>: x = %h, Sbox_case(x) = %h\n", $time, x_case, result_case);  $display("<%2d>: x = %h, Sbox_combinational(x) = %h\n", $time, x_combinational, result_combinational);
        #5 x_case = 'hD; x_combinational = 'hD; #1 $display("<%2d>: x = %h, Sbox_case(x) = %h\n", $time, x_case, result_case);  $display("<%2d>: x = %h, Sbox_combinational(x) = %h\n", $time, x_combinational, result_combinational);
        #5 x_case = 'hE; x_combinational = 'hE; #1 $display("<%2d>: x = %h, Sbox_case(x) = %h\n", $time, x_case, result_case);  $display("<%2d>: x = %h, Sbox_combinational(x) = %h\n", $time, x_combinational, result_combinational);
        #5 x_case = 'hF; x_combinational = 'hF; #1 $display("<%2d>: x = %h, Sbox_case(x) = %h\n", $time, x_case, result_case);  $display("<%2d>: x = %h, Sbox_combinational(x) = %h\n", $time, x_combinational, result_combinational);
    end

endmodule
 
