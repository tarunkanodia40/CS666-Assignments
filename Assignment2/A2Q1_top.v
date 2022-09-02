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
        $monitor("<%2d>: Number = %4d, Prime = %4d, GCD = %4d, Modulo-Inverse = %4d", $time, number, prime, gcd, inverse);
    end

    initial
    begin
        reset = 0;
        forever begin
            #5
            clk = ~clk;
        end
    end

    initial
    begin
        reset = 1;
        clk = 0;
        number = 10;
        prime = 53;
        #1 reset=0;
        #50
        reset = 1;
        clk = 0;
        number = 200;
        prime = 67;
        #1 reset=0;
        #200
        $finish;
    end

endmodule
 
