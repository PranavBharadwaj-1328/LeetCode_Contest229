# LeetCode_Contest229
A coding contest on online coding platform<br/><br/>
Q3.You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.
You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:<br/>
    1) Choose one integer x from either the start or the end of the array nums.<br/>
    2) Add multipliers[i] * x to your score.<br/>
    3) Remove x from the array nums.<br/><br/>
    
Return the maximum score after performing m operations.<br/><br />
Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]<br/>
Output: 102<br />
Explanation: An optimal solution is as follows:<br />
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.<br />
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.<br />
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.<br />
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.<br />
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. <br />
The total score is 50 + 15 - 9 + 4 + 42 = 102.<br />
