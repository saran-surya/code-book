### please feel free to raise pull requests for performance issues, and edge cases :)

String Merge

You are provided with a large string and one or more small strings. You need
Private Testcase to find if the large string can be formed by combining all the small strings. You
Submissions can interchange characters of small strings internally and you can combine
small strings in any order. Print "YES" if it is possible, otherwise print "NO".
enevaluated Noite: All strings contain lower case alphabets only.
Feedback Form + Constraints
1 <= length of large string <= 500000
1 <= length of small string <= 1000
1 <=N <= 500
+ Input

First line contains the large string
Second line contains an integer N denoting total number of small strings
Next N lines contain strings smaller than large string

+ Output

Print single line with YES or NO
+ Time Limit

1
+ Examples

Example 1

Input

dogisaloyalanimal

5

a

alloy
is
god
lamina

Output
YES

Explanation :

Large string is "dogisaloyalanimal". There are 5 small strings - 'a’, "alloy", "is",
"god", "lamina". We can do following operations on small strings:

1. Interchange characters of “alloy” to form “loyal”.
2. Interchange characters of "god" to form "dog".

3. Interchange characters of "lamina" to form “animal”.

So, we formed new set of small strings - "a’, "loyal", "is", "dog", "animal". Now
combine small strings in the below order:

"dog" + "is" + "g" + "loyal" + "animal"
We got it combined as "dogisaloyalanimal". This is same as large string
provided. So, the output is "YES".

Example 2
Input

thisisgood
4

god

is

so

hit

Output
NO

Explanation:

Large string is "thisisgood". There are 4 small strings - "god", "is", "so", "hit". We
cannot form the large string by combining small strings even after
interchanging its characters internally. So, the output is "NO".