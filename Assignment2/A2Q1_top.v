// Assumption: "b" will always be prime, as mentioned in the question. Otherwise modinv doesn't exist.
module modinv_top;
    reg clk,reset;
    reg [31:0] number;
    reg [31:0] prime;
    wire finished;
    wire[31:0] gcd;
    wire[31:0] inverse;

    modinv M(clk, reset, number, prime, finished, gcd, inverse);

    initial
    begin
        reset = 0;
        forever begin
            #1
            clk = ~clk;
        end
    end

    initial
    begin
        reset = 1;
        clk = 0;
        number = 10;
        prime = 53;
        #2 reset=0;
        #30 $display("<%4d> Number = %4d, Prime = %4d, Inverse = %4d", $time, number, prime, inverse);

        #20
        reset = 1;
        clk = 0;
        number = 200;
        prime = 67;
        #2 reset=0;
        #30 $display("<%4d> Number = %4d, Prime = %4d, Inverse = %4d", $time, number, prime, inverse);

        #20
        reset = 1;
        clk = 0;
        number = 999;
        prime = 5339;
        #2 reset = 0;
        #30 $display("<%4d> Number = %4d, Prime = %4d, Inverse = %4d", $time, number, prime, inverse);

        #20
        reset = 1;
        clk = 0;
        number = 4536;
        prime = 113;
        #2 reset = 0;
        #30 $display("<%4d> Number = %4d, Prime = %4d, Inverse = %4d", $time, number, prime, inverse);

        #20
        reset = 1;
        clk = 0;
        number = 993;
        prime = 1000000007;
        #2 reset = 0;
        #30 $display("<%4d> Number = %4d, Prime = %4d, Inverse = %4d", $time, number, prime, inverse);

        #20
        reset = 1;
        clk = 0;
        number = 123456789;
        prime = 7;
        #2 reset = 0;
        #30 $display("<%4d> Number = %4d, Prime = %4d, Inverse = %4d", $time, number, prime, inverse);
        
        #20
        reset = 1;
        clk = 0;
        number = 3156464;
        prime = 9679;
        #2 reset = 0;
        #30 $display("<%4d> Number = %4d, Prime = %4d, Inverse = %4d", $time, number, prime, inverse);
        
        #20
        reset = 1;
        clk = 0;
        number = 12235;
        prime = 2731;
        #2 reset = 0;
        #30 $display("<%4d> Number = %4d, Prime = %4d, Inverse = %4d", $time, number, prime, inverse);
        
        #2000
        $finish;
    end

endmodule
 
