# Factor of 3
#### Feel free to raise pull requests for edge cases and performance issues, Basically i am doing the process of permutations, and Atmost save time by reducing the unwanted permutaions, Still the Worst Case Complexity will remain the same as Calculating permutations for all elements.

=

Problem Description

Given an array arr, of size N, find whether it is possible to rearrange the
elements of array such that sum of no two adjacent elements is divisible by 3.

Constraints
1<=T<=10
2 <= N <= 1045

1 <= arr[i] <= 1045

Input

First line contains integer T denoting the number of testcases.
Each test cases consists of 2 lines as follows-

First line contains integer N denoting the size of the array.

Second line contains N space separated integers.

Output

For each test case print either "Yes" or "No" (without quotes) on new line.

= Time Limit

1

Examples
Example 1
Input

1

4

1233

Output

Yes

Explanation

Some of the rearrangements can be {2,1,3,3}, {3,3,1,2}, {2,3,3,1}, {1,3,3,2}....

We can see that there exist at least 1 combination {3,2,3,1} where sum of 2
adjacent number is not divisible by 3. Other combinations can be {1,3,2,3},
{2,3,1,3}.

Hence the output is Yes.

Example 2

Input

1

4

3619

Output

No

Explanation

All possible combination of {3,6,1,9} are

{1,3,6,9}, {1,3,9,6}, {1,6,9,3}, {1,6,3,9}, {1,9,3,6}, {1,9,6,3},
{6,1,3,9}, {6,1, 9,3}, {6,3,1,9}, {6,3,9,1}, {6,9,1,3}, {6,9,3, 1},
{3,1,6,9}, {3,1,9,6}, {3,9,1,6}, {3,9,6,1}, {3,6,1,9}, {3,6,9, 1},
{9,1,3,6}, {9,1,6,3}, {9,3,1,6}, {9,3,6,1}, {9,6,1,3}, {9,6,3, 1}.

Since none of these combinations satisfy the condition, the output is No.