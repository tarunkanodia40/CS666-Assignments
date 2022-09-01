module sbox_case(x_case, result_case);

    // Define inputs
    input [3:0] x_case;

    // Define Outputs
    output reg [3:0] result_case;

    always @(x_case) begin
        case(x_case) 
            'h0: result_case = 'hC;
            'h1: result_case = 'h5;
            'h2: result_case = 'h6;
            'h3: result_case = 'hB;
            'h4: result_case = 'h9;
            'h5: result_case = 'h0;
            'h6: result_case = 'hA;
            'h7: result_case = 'hD;
            'h8: result_case = 'h3;
            'h9: result_case = 'hE;
            'hA: result_case = 'hF;
            'hB: result_case = 'h8;
            'hC: result_case = 'h4;
            'hD: result_case = 'h7;
            'hE: result_case = 'h1;
            'hF: result_case = 'h2;
        endcase
    end

endmodule