class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c_m=nums[0]
        c_mi=nums[0]

        mx=nums[0]
        for i in nums[1:]:
            if i<0:
                c_m,c_mi=c_mi,c_m
            c_m=max(i,c_m*i)
            c_mi=min(i,c_mi*i)
            mx=max(mx,c_m)
        return mx