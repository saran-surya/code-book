# Unlocker

## I have Followed a Naive approach for this problem feel free to raise pull requests for Performance issues and time complexity issues :)

== Problem Description

A locker is comprised of one or more layers. Each layer can be rotated only in
one direction. Odd numbered layers rotate in anti-clockwise direction (left to
right), and even numbered layers rotate in clockwise direction (right to left).

You are given a locker, in the form of a matrix. The matrix will be rectangular
in shape. The outer most layer of this matrix is layer1. In context of the
diagram below, the numbers painted in red are layer1 and the inner numbers
constitute layer2. Bigger matrices will have more layers.

One rotation defined as a given number moving in the neighbouring spot i.e.
one spot left for clockwise rotation and one spot right for anti-clockwise
rotation.

Number of rotations for each layer required to unlock the locker will be
provided as input. Print the final unlocked matrix as output.

Layer 4 = Bright Red

Layer 2=Black

 
Clockwise Antisclockwise

Rotations

Constraints

1<M,N <= 300

0 <= Numbers in matrix < 100

1 <= Number of rotations <= 1049

M%2=0 && N%2=0

Input

First line contains two space separated integer M and N which denotes the
number of rows and number of columns, respectively

Next M lines contain N space separated integers depicting the locked matrix

Last line contains L space separated integers, where L is the number of
layers. Each number on this line denotes the number of rotations for every
layer from 1 to L

Output

Print unlocked matrix

= Time Limit

2

Examples
Example 1
Input

1 2
3 4
2

Output

4 3
2 1
Explanation:

There is only one layer. So, we have to rotate it in anti-clockwise direction with
2 rotations.


Example 2
Input
4 4
1 2 3 4
2 3 4 5
2 4 5 6
2 3 4 5
2 2
Output
3 4 5 6
2 5 4 5
1 4 3 4
2 2 2 3

Explanation:

Here we have to rotate layer1 in anti-clockwise direction with 2 rotations, and
layer2 clockwise with 2 rotations.
