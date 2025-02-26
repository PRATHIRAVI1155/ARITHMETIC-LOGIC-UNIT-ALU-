# ARITHMETIC-LOGIC-UNIT-ALU-

COMPANY NAME : CODTECH IT SOLUTIONS

 NAME : PRATHIKSHA R

 INTERN ID : CT08RWF

 DOMAIN : VLSI

DURATION : 4 WEEKS

MENTOR : NEELA SANTHOSH KUMAR

### **ALU Task 1: Overview and Explanation**  

The **Arithmetic Logic Unit (ALU)** is a fundamental component of digital systems, responsible for performing arithmetic and logical operations in a processor. In **ALU Task 1**, the objective is to design a simple **8-bit ALU** using Verilog and test its functionality through a testbench. This ALU executes basic operations such as addition, subtraction, bitwise logic, and shift operations.  

The ALU takes two **8-bit inputs (A and B)** and an **operation code (opcode)** that determines which function to perform. The result is produced based on the selected operation. The operations supported by this ALU include:  

1. **Addition (A + B)**: Adds two numbers and produces the sum.  
2. **Subtraction (A - B)**: Subtracts B from A to get the difference.  
3. **Bitwise AND (A & B)**: Performs a logical AND operation on each bit.  
4. **Bitwise OR (A | B)**: Performs a logical OR operation on each bit.  
5. **Bitwise XOR (A ^ B)**: Performs a logical XOR operation.  
6. **Left Shift (A << 1)**: Shifts bits of A one position to the left.  
7. **Right Shift (A >> 1)**: Shifts bits of A one position to the right.  
8. **Pass A**: Directly passes the value of A to the output.  

To implement this ALU, **Verilog** is used to define its functionality with a case statement that selects the correct operation based on the opcode input.  

To test the ALU, a **testbench** is created that provides different values for A, B, and the opcode while observing the results. The testbench runs a simulation where different operations are executed sequentially, and the output is displayed.  

For example, if **A = 15 and B = 10**, the ALU would generate the following results for each operation:  
- Addition: 25  
- Subtraction: 5  
- AND: 10  
- OR: 15  
- XOR: 5  
- Left Shift: 30  
- Right Shift: 7  
- Pass A: 15  

The output of the simulation confirms that the ALU is functioning correctly.  

Further improvements to this ALU could include expanding its capabilities to support **multiplication, division,** and **comparison operations.** Additionally, **status flags** like zero flag, carry flag, and overflow flag can be introduced for advanced functionality.  

This task serves as an essential introduction to digital logic design and processor operations, making it a foundational step in learning **computer architecture and FPGA-based systems.**



