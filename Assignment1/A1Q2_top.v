module lfsr_top;

    reg [15:0] seed;
    reg reset;
    wire[15:0] state;

    reg clk;

    LFSR L(state, seed, clk,reset);

    initial
    begin
        $monitor("<%6d>: Seed = %b, State = %b, Reset = %1d\n", $time, seed, state, reset);
    end

    initial
    begin
        #50
        reset = 1;
        #50
        reset = 0;
    end
    initial
    begin
    	clk = 0;
    	reset = 0;
    	seed = 13;
    	forever begin
    		#1
    		clk = ~clk;
    	end
    end


endmodule
 
