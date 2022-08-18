module LFSR (state, seed, clk, reset);
	input [15:0] seed;
	input clk, reset;
	output wire[15:0] state;
	reg [15:0] cur_seed;
	reg [15:0] new_seed;
	reg first=1;

	D_FF D0(state[0], cur_seed[0], clk, reset);
	D_FF D1(state[1], cur_seed[1], clk, reset);
	D_FF D2(state[2], cur_seed[2], clk, reset);
	D_FF D3(state[3], cur_seed[3], clk, reset);
	D_FF D4(state[4], cur_seed[4], clk, reset);
	D_FF D5(state[5], cur_seed[5], clk, reset);
	D_FF D6(state[6], cur_seed[6], clk, reset);
	D_FF D7(state[7], cur_seed[7], clk, reset);
	D_FF D8(state[8], cur_seed[8], clk, reset);
	D_FF D9(state[9], cur_seed[9], clk, reset);
	D_FF D10(state[10], cur_seed[10], clk, reset);
	D_FF D11(state[11], cur_seed[11], clk, reset);
	D_FF D12(state[12], cur_seed[12], clk, reset);
	D_FF D13(state[13], cur_seed[13], clk, reset);
	D_FF D14(state[14], cur_seed[14], clk, reset);
	D_FF D15(state[15], cur_seed[15], clk, reset);

	reg[7:0] count = 0;
	reg to_finish = 0;

	always @(negedge clk) begin
		if (to_finish == 1) begin
			$finish;
		end

		if(reset || first) begin
			cur_seed <= seed;
			first <= 0;
		end else begin
			new_seed = {cur_seed[0], cur_seed[15], cur_seed[14] ^ cur_seed[0], cur_seed[13] ^ cur_seed[0], cur_seed[12], cur_seed[11] ^ cur_seed[0], cur_seed[10:1]};
			cur_seed = new_seed;

			if (cur_seed == seed && !first) begin
				to_finish = 1;
			end
		end

	end


endmodule