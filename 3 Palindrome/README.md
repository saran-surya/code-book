3 Palindrome

Given an input string word, split the string into exactly 3 palindromic
Working from left to right, choose the smallest split for the first substring that
Unevaluated still allows the remaining word to be split into 2 palindromes.
Submissions Similarly, choose the smallest second palindromic substring that leaves a
third palindromic substring.


If there is no way to split the word into exactly three palindromic substrings,
Graphs print "Impossible" (without quotes). Every character of the string needs to be

consumed.
Cases not allowed -

After finding 3 palindromes using above instructions, if any character of the
original string remains unconsumed.

No character may be shared in forming 3 palindromes.
+ Constraints

1 <= the length of input sting <= 1000

+ Input

First line contains the input string consisting of characters between [a-z].

+ Output

Print 3 substrings one on each line.
+ Time Limit
1

+ Examples


Example 1

Input

nayannamantenet

Output

nayan

naman

tenet

Explanation

The original string can be split into 3 palindromes as mentioned in the output.

However, if the input was nayanamantenet, then the answer would be
"Impossible".

Example 2

Input

aaaaa

Output

a

a

aaa

Explanation

The other ways to split the given string into 3 palindromes are as follows -
[a, aaa, al, [aaa, a, al, [aa, aa, al, etc.

Since we want to minimize the length of the first palindromic substring using
left to right processing, the correct way to split is [a, a, aaa].

Example 3
Input
aaaabaaaa
Output

a

aaabaaa

a
Explanation

The other ways to split the given string into 3 palindromes are as follows -
213

[aaaa, b, aaaal], [aa, aabaa, aal, etc.

Since we want to minimize the length of the first palindromic substring using
left to right processing, the correct way to split is [a, aaabaaa, al].
