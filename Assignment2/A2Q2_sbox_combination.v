module sbox_combinational(x_combinational, result_combinational);

    // Define inputs
    input [3:0] x_combinational;

    // Define Outputs
    output wire [3:0] result_combinational;

    assign result_combinational[0] = (~x_combinational[3] & ~x_combinational[2] & x_combinational[0]) | (~x_combinational[3] & x_combinational[1] & x_combinational[0]) | (x_combinational[3] & ~x_combinational[2] & ~x_combinational[0]) | (x_combinational[3] & x_combinational[1] & ~x_combinational[0]) | (~x_combinational[3] & x_combinational[2] & ~x_combinational[1] & ~x_combinational[0]) | (x_combinational[3] & x_combinational[2] & ~x_combinational[1] & x_combinational[0]);

    assign result_combinational[1] = (~x_combinational[3] & ~x_combinational[2] & x_combinational[1]) | (~x_combinational[3] & x_combinational[1] & ~x_combinational[0]) | (~x_combinational[2] & x_combinational[1] & ~x_combinational[0]) | (x_combinational[3] & ~x_combinational[2] & ~x_combinational[1]) | (x_combinational[3] & x_combinational[2] & x_combinational[0]);

    assign result_combinational[2] = (~x_combinational[3] & ~x_combinational[2] & ~x_combinational[1]) | (~x_combinational[2] & ~x_combinational[1] & x_combinational[0]) | (~x_combinational[2] & x_combinational[1] & ~x_combinational[0]) | (x_combinational[3] & x_combinational[2] & ~x_combinational[1]) | (~x_combinational[3] & x_combinational[2] & x_combinational[1] & x_combinational[0]);

    assign result_combinational[3] = (~x_combinational[3] & ~x_combinational[1] & ~x_combinational[0]) | (~x_combinational[3] & x_combinational[1] & x_combinational[0]) | (~x_combinational[3] & x_combinational[2] & ~x_combinational[0]) | (x_combinational[3] & ~x_combinational[2] & x_combinational[0]) | (x_combinational[3] & ~x_combinational[2] & x_combinational[1]);

endmodule