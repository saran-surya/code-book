#### Tennis Score
###### Please feel free to Raise pull Requests for this Question :)
A game of tennis (singles) is played. Regions of the court are named as

Private Testcase shown in the image.

The running score of each game is described in the manner: "0","15", "30", and

"40". If at least three points have been scored by each side and a player has
one more point than his opponent, the score of the game is advantage
("Advantage") for the player in the lead. (source: Wikipedia)


A set consists of a sequence of games played with service alternating
between games, ending when a player wins a set by winning at least six
games and at least two games more than the opponent. If one player has won
six games and the opponent five, an additional game is played. If the leading
player wins that game, the player wins the set 7-5. If the trailing player wins
the game (tying the set 6-6) a tie-break is played. A tie-break, allows one
player to win one more game and thus the set, to give a final set score of 7-6
or 6-7.


a2
H2
Oz o2
a3 4
NET le
Qi a2
o1 o1
Hi
O1


Aim is to toss the ball on the green part of the other side of the court. A set of
strings will be provided signifying where the tennis ball has been tossed on
the court. Assume that no player will hit the ball directly (i.e. without the ball
being tossed on his (green) side of the court).

For Example, a string Q4 Q1 Q3 01 will mean that server serves and the ball
hits the area Q4. Receiver returns and ball hits ground in area Q1, server hits
back again to area Q3 and then the receiver hits ‘long’ to area 01 and loses a
point. So the set output is 0-0 and the current game output will be 15-0.

Following are the rules of the game:
e Game always starts with Server on H1 side (lower side in the image)
e Serve changes after every game is won

¢ On'Serve' ball should hit on any 'Q' part of the other side. Hitting on 'H' part
will be considered a fault

e While serving, if the server makes a double fault (ball should fall on his
side or outside region twice), the server loses one point

e Points scored by the current server are mentioned first, for example if
server wins the first point score will be 15-0

e At the end of a set, a changeover happens i.e. players change sides of the
court.

e In case of game score 40-40, display "Deuce”. In case of Server's
Advantage, display "Advantage Server”.

In case of Receiver's Advantage, display "Advantage Receiver"

Number of sets played may not exceed 5

Incase asetis complete a set score of 7-5 will be denoted as:
7 0 (first player set score)
5 0 (second player set score)

Since the second set is about to start, a score of 0 0 is displayed. Please
read these scores vertically.

e When a new game is about to start, display 0 - O for new game. For
example:

0 0 (current game score)
Departure from Tennis rule:

e In real game of tennis a server is required to serve cross court. However, in
this problem the server can serve in any court {Q3, Q4} for server 1 and
{Q1, Q2} for server 2

e In real game of tennis a tie-break is counted in scores of 1, 2, 3, 4 instead
of 15, 30, 40 etc. However, in this problem a tie-break is won according to
regular rule i.e. by scoring points like in a regular game. For example, lets
say the score is 6-6. In regular tennis a tie break would follow, but in this
problem the 13th game will be played and scored using the same rules
applied for first 12 games. Whoever wins the 13th game, wins the set i.e.
either 7-6 or 6-7

e In a real game of tennis, a changeover (players switching court sides)

happens at the end of a set or after the first game is played in a new set.
However, in this problem changeover happens at the end of the set

Constraints

Number of space separated strings in input < 500

Input

One line containing a string representing the sequence where the ball drops,
separated by space

Output

First line containing the set score of all the sets of the Server (starting from
first and separated by space)

Second line containing the set score of all the sets of the Receiver (starting
from first and separated by space)

Third line containing the game score of the current game (separated by
space) or "Deuce" or "Advantage Receiver" or "Advantage Server", as may be
the case.

= Time Limit

1


Example 1
Input

Q1 Q1
Output

0
0
015

Explanation

Server serves and ball hits area Q1. He will not lose point because he is
serving. Again he serves and ball hits area Q1. Since, this is a double fault he
loses one point. Hence the game score is 0-15.

Example 2

Input

Q1 Q1 Q3 Q3 Q1 Q1 Q3 Q3 QI Q1 Q3 Q3
Output

0
0
Deuce

Explanation
- String Q1 Q1 indicates a double fault. The score becomes 0-15

- Next String Q3 indicates a valid serve. The second Q3 indicates that the
Receiver could not return the serve because it fell into his own half. This
makes the score 15-15.

- Similar sequence repeats for two more times, making the score 30-30, then
40-40 which is Deuce.

Example 3

Input

Q1 Q1 Q2 Q3 01 H2 H2 Q1 Q1 Q1 Q2
Output

1

00

Explanation

- Except points Q2 Q3 01 all other string indicates a double fault on part of the
server

- Q2 Q3 O1 earns the server one point
- Overall the server loses the game

- Now a new game begins and the current server becomes receiver and vice
versa

- The score is printed after the new game begins and the score is 0 0. Hence,
server score is 1 whereas the receiver score is 0
