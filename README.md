# LeetCode_Contest229
A coding contest on online coding platform<br/><br/>

Q1. You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.<br/>

Return the merged string.<br/><br/>
Q2. You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.<br/>
In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.<br/>
Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.<br />
<br/>
Each answer[i] is calculated considering the initial state of the boxes.<br/><br/>
Q3.You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.
You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:<br/>
    1) Choose one integer x from either the start or the end of the array nums.<br/>
    2) Add multipliers[i] * x to your score.<br/>
    3) Remove x from the array nums.<br/>
    
Return the maximum score after performing m operations.<br/><br />
Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]<br/>
Output: 102<br />
Explanation: An optimal solution is as follows:<br />
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.<br />
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.<br />
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.<br />
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.<br />
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. <br />
The total score is 50 + 15 - 9 + 4 + 42 = 102.<br /><br/>

Q4. You are given two strings, word1 and word2. You want to construct a string in the following manner:<br/>
    1) Choose some non-empty subsequence subsequence1 from word1.<br/>
    2) Choose some non-empty subsequence subsequence2 from word2.<br />
    3) Concatenate the subsequences: subsequence1 + subsequence2, to make the string. <br/>
Return the length of the longest palindrome that can be constructed in the described manner. If no palindromes can be constructed, return 0.<br/>
A subsequence of a string s is a string that can be made by deleting some (possibly none) characters from s without changing the order of the remaining characters.

A palindrome is a string that reads the same forward as well as backward.
