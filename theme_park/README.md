T-REX is a ferocious animal which used to live 10,000 years ago. Scientists successfully created few smilodons in an experimental DNA research. A park is established and those T-rexes are kept in a cage for visitors.

This park consists of Grasslands(G), Mountains(M) and Waterbodies(W) and it has three gates (situated in grasslands only). Below is a sample layout.

Sample Layout
Before opening the park, club authority decides to calculate Safety index of the park. The procedure of the calculation is described below. Please help them to calculate.

Safety Index calculation

Assume a person stands on grassland(x) and a T-rex escapes from the cage situated on grassland(y). If the person can escape from any of those three gates before the T-rex is able to catch him, then the grassland(x) is called safe else it is unsafe. A person and a T-rex both take 1 second to move from one area to another adjacent area(top, bottom, left or right) but a person can move only over grasslands though T-rex can move over grasslands and mountains.

If any grassland is unreachable for the T-rex(maybe it is unreachable for any person also), to increase safe index value Club Authority use to mark those grasslands as safe land. Explained below




For the above layout, there is only one gate at (4,6)

Y is the position of T-rex’s cage

X is not safe area

Z is a safe area as is it not possible for T-rex to reach z

Safety index=(total grassland areas which are safe*100)/total grassland area

 

Constraints

3<= R,C <= 10^3

Gates are situated on grasslands only and at the edge of the park

The cage is also situated in grassland only

The position of the cage and the position of three gates are different

Input Description:
The first line of the input contains two space-separated integers R and C, denoting the size of the park (R*C) The second line contains eight space-separated integers where First two integers represent the position of the first gate 3rd and 4th integers represent the position of second gate 5th and 6th integers represent the position of third gate respectively The last two integers represent the position of the cage Next R lines, each contains space separated C number of characters. These R lines represent the park layout.

Output Description:
Safety Index accurate up to two decimal places using Half-up Rounding method

Sample Input :
4 4
1 1 2 1 3 1 1 3
G G G G
G W W M
G G W W
M G M M
Sample Output :
75.00