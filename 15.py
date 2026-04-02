class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        res=[]
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]!=nums[j]:
                    for k in range(j+1,n):
                        if nums[j]!=nums[k]:
                            if nums[i]+nums[j]+nums[k]==0:
                                res.append([nums[i],nums[j],nums[k]])
        return set(res)