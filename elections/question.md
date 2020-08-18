Elections

Elections are going on, and there are two candidates A and B, contesting
Private Testcase with each other. There is a queue of voters and in this queue some of
Submissions them are supporters of A and some of them are supporters of B. Many of
them are neutral. The fate of the election will be decided on which side the
neutral voters vote. Supporters of A and supporters of B make attempt to
win the votes of neutral voters.

1. The voter queue is denoted by three characters, viz {-, A, B}. The -
denotes neutral candidate, A denotes supporter of candidate A and B
denotes supporter of candidate B.


2. Supporters of A can only move towards the left side of the queue.
3. Supporters of B can only move towards the right side of the queue.

4. Since time is critical, supporters of both A and B will move
simultaneously.

5. They both will try and influence the neutral voters by moving in their
direction in the queue. If supporter of A reaches the neutral voter before
supporter of B reaches him, then that neutral voter will become a
supporter of candidate A.

6. Similarly, if supporter of B reaches the neutral voter before supporter of
A reaches him, then that neutral voter will become a supporter of
candidate B.

7. Finally, if both reach at the same time, the voter will remain neutral. A
neutral vote cannot decide the outcome of the election.

8. If finally, the queue has more votes for candidate A, then A wins the
election. If B has more votes, then B wins that election. If both have equal
votes, then it will be a coalition government.

Refer Examples section for understanding the dynamics of how the
supporters influence the neutral voters.

Constraints

1 <= length of queue <= 10° 5

Input

First line contains an integer which is length of queue of voters.
Second line contains characters {-, A, B}, in which denotes

- A = voter who is supporter of candidate A

- B = voter who is supporter of candidate B

- \- = neutral voter

Output

Print candidate with maximum number of votes. If they have equal
number of votes, print “Coalition government".

Time Limit


1

Examples
Example 1
Input

14
--AB--AB---A--
Output

A
Explanation:

For starting positions where there is no opposition from supporter of B,
supporter of A can promote in left side of the queue. The voting queue will
then look like below:

AAAB--AB---A--

From 4th place (in voting queue) B supporter is moving towards the right

side, simultaneously 7th placed A supporter is also moving towards the
left side. Then the voting queue will look like below:

AAABBAAB---A--

From eth place B supporter is moving towards the right side,

simultaneously qath placed A supporter is also moving towards the left
side. Then the voting queue will look like below:

AAABBAABB-AA--

Since supporters of both A and B will reach the 10th voter at the same
time, 10* voter will remain neutral.

Since supporter of A at qath place cannot move towards right, last 2
voters will not be influenced and remain neutral. Then the voting queue
will look like below:

AAABBAABB-AA--

Since all voter have now cast their votes, election results can now be
declared.

So final resultis: AAA BBAABB-AA--
A has 7 votes, B has 4 votes hence, A wins the election.
Example 2

Input

Explanation:

Since supporter of A at 15t place cannot move towards right, last 3 voters
will not be influenced and will remain neutral. Then the voting queue will
look like below:

A---

Since all voter have now cast their votes, election results can now be
declared.

So final result is: A - - -

A has 1 vote, B has 0 votes hence, A wins the election.
Example 3

Input

5

A--B

Output

Coalition government

Explanation:

Since supporter of A at 1t place cannot move towards right, supporter of

B at 54 cannot move towards left, middle 3 voters will not be influenced
and will remain neutral. Then the voting queue will look like below:

A---B
So final result is: A---B
A has 1 vote, B has 1 vote hence, output will be “Coalition government".
