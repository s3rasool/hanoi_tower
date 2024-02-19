# Towers of Hanoi Problem

This problem involves the Towers of Hanoi, a classic mathematical puzzle. The problem is relevant for novice programmers as it provides an opportunity to explore recursive function methods.

## Problem Statement:

In this problem, we have three pegs labeled A, B, and C, connected vertically to the ground. Disks of different radii are placed on peg A, with the largest disk at the bottom and the smallest at the top. Each disk is either on the ground or on a larger disk.

The goal is to move all the disks from peg A to peg B with the help of peg C, following specific rules. A disk cannot be placed on a smaller disk, and only one disk can be moved at a time.

The recursive approach for solving this problem is implemented in the function `hanoi(from, to, help, n)`, where `n` represents the number of disks to be moved from peg 'from' to peg 'to' with the assistance of peg 'help'. The recursive steps involve moving `n-1` disks from 'from' to 'help', moving the largest disk from 'from' to 'to', and then moving the `n-1` disks from 'help' to 'to'.



For a better understanding of the Towers of Hanoi problem and its recursive solution, refer to the following image:

![Tower of Hanoi](Ex_Pic.png)

## Mathematical Proof:

We can prove that the minimum number of moves required to transfer all disks from peg A to peg B is given by the formula \(2^n - 1\), where \(n\) is the number of disks. The recursive relation is expressed as \(T_n = 2 \times T_{n-1} + 1\), where \(T_n\) is the minimum number of moves for \(n\) disks.

By mathematical induction, it can be shown that \(T_n = 2^n - 1\). Additionally, it is demonstrated that any method with fewer moves is not possible.

## Additional Notes:

For the input \(n\), representing the number of disks on peg A, the program outputs the sequence of moves required to achieve the goal. Each move is displayed as a line in the format: `i from to`, where `i` is the step number.

### Example:

*Input:*
3

*Output:*
1 A B

2 A C

3 B C

4 A B

5 C A

6 C B

7 A B
