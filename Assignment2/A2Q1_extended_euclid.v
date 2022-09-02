module modinv(clk, reset, number, prime, finished, gcd, inverse);

    input [31:0] number, prime;
    input wire clk,reset;

    output reg[31:0] gcd, inverse;
    output reg finished;

    parameter [2:0] IDLE = 3'b001, COMPUTING = 3'b010, COMPUTED = 3'b100;
    reg [2:0] state, state_next;

    integer a, b, c, q, p, r;
    integer a_next, b_next, p_next, r_next;

    always @ (posedge clk, posedge reset)
    begin
        if (reset == 1)
            begin
                state <= IDLE;
                a <= 0;
                b <= 0;
                p <= 0;
                r <= 0;
            end
        else
            begin              
                state <= state_next;
                a     <= a_next;
                b     <= b_next;
                p     <= p_next;
                r     <= r_next;
            end
    end

    always @*
    begin
        finished <= 0;

        case (state)
            IDLE:
                begin
                    a_next <= number;
                    b_next <= prime;
                    p_next <= 1;
                    r_next <= 0;
                    state_next <= COMPUTING;
                end
            COMPUTING:
                begin
                    c = a % b;
                    q = a / b;
                    a_next = b;
                    b_next = c;
                    r_next = p - q * r;
                    p_next = r;

                    if (b_next == 0)
                        begin
                            state_next <= COMPUTED;
                        end
                    else
                        begin
                            state_next <= COMPUTING;
                        end
                end
            COMPUTED:
                begin
                    gcd <= a;
                    inverse <= (p + prime) % prime;
                    finished <= 1;
                end
        endcase
    end

endmodule