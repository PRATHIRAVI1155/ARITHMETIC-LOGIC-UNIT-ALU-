!apt-get install -y iverilog
  
%%writefile alu.v
module ALU (
    input [3:0] A, B,      
    input [2:0] ALU_Sel,   
    output reg [3:0] Result 
);
    
    always @(*) begin
        case (ALU_Sel)
            3'b000: Result = A + B;   // Addition
            3'b001: Result = A - B;   // Subtraction
            3'b010: Result = A & B;   // AND operation
            3'b011: Result = A | B;   // OR operation
            3'b100: Result = ~A;      // NOT operation (only A is used)
            default: Result = 4'b0000; // Default case
        endcase
    end
endmodule

%%writefile alu_tb.v
module ALU_tb;
    reg [3:0] A, B;
    reg [2:0] ALU_Sel;
    wire [3:0] Result;
    
    ALU uut (
        .A(A), 
        .B(B), 
        .ALU_Sel(ALU_Sel), 
        .Result(Result)
    );
    
    initial begin
        $monitor("A=%b, B=%b, ALU_Sel=%b, Result=%b", A, B, ALU_Sel, Result);
        
        A = 4'b0101; B = 4'b0011; 
        ALU_Sel = 3'b000; #10; // Addition
        ALU_Sel = 3'b001; #10; // Subtraction
        ALU_Sel = 3'b010; #10; // AND operation
        ALU_Sel = 3'b011; #10; // OR operation
        ALU_Sel = 3'b100; #10; // NOT operation
        
        $stop;
    end
endmodule

!iverilog -o alu_test alu.v alu_tb.v
!vvp alu_test
