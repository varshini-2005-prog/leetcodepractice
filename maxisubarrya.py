class Solution(object):
    def maxSubArray(self, nums):
       
        mx=nums[0]
        c=nums[0]

        for i in range(1,len(nums)):
            c=max(nums[i],c+nums[i])
            mx=max(mx,c)
        return mx