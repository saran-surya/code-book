
# Path Through Graph

#### Feel free to raise pull requests for edge cases and performance issues, I have this code running a while loop and a for loop running until the square-root of the number to find the maximum factor, and almost breaking the loop in O(1) itself,

You are given two natural numbers. Imagine these natural numbers as nodes
Private Testcase on a graph. On this graph, a number is connected to its largest factor other
Submissions than itself. You have to find the shortest path between them and print the
number of edges on that path.

If the two numbers do not have any common factor, then construct a path

through 1. For better understanding refer to the examples below:

Example 1: Input numbers: 2 4
The numbers are directly connected as follows on the graph. 2 is the largest
factor of 4, other than itself.

Graphs :
We can also see that there is only on edge between them.
4<->2
Hence the number of edges in shortest path is 1.
Output: 1

Example 2: Input numbers: 18 19

The graph for number 18 and 19 will look like this. Here we have 4 edges in
the path.

18 <--> 9 <--> 3 <--> 1 <--> 19

Output: 4

Example 3: Input numbers: 9 9

The number of edges in shortest path is zero since the numbers correspond

to the same node.
Output: 0

= Constraints

O0<M,N<=10%9

= Input

Single line containing two space separated integers M, N

= Output

Number of edges in the shortest path.

= Time Limit


Examples

Example 1

Input

15689 28

Output

5

Explanation :

The graph for number 15689 and 28 will look like this.

Since we know that largest factor of 15689 other than itself is 541.
Since 541 is a prime number, it’s largest factor other than itself is 1.
For number 28, it’s largest factor other than itself is 14.

Largest factor of 14, other than itself is 7.

Since 7 is a prime number, it’s largest factor other than itself is 1.
So, the graph will look like this:

15689 <--> 541 <--> 1 <--> 7 <--> 14 <--> 28

Since there are 5 edges in this graph, output will be 5.

Example 2

Input

164

Output

2

Explanation :

The graph for number 16 and 4 will look like this.

Since we know that largest factor of 16 other than itself is 8.

Largest factor of 8 other than itself is 4. That’s the other input number, so we
will stop here.

So, the graph will look like this:

16<-->8<-->4
