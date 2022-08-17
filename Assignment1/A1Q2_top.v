`include "A1Q2_D_FF.v"
`include "A1Q2_LFSR.v"
module lfsr_top;

    reg [15:0] seed;
    reg reset;
    wire[15:0] state;

    reg clk;

    LFSR L(state, seed, clk,reset);

    initial
    begin
        $monitor("<%d>: Seed = %b, State = %b, Reset = %d\n", $time, seed, state, reset);
    end

    initial
    begin
    	clk = 0;
    	reset=0;
    	seed=13;
    	forever begin
    		#1
    		clk = ~clk;
    	end
    end


endmodule
 