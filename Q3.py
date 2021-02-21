def maxScore(nums,multipliers):
    if(len(multipliers) == 0):
        return 0
    else:
        return max(nums[0]*multipliers[0]+maxScore(nums[1:],multipliers[1:]),nums[len(nums)-1]*multipliers[0]+maxScore(nums[:-1],multipliers[1:]))

