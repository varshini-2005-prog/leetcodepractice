class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=Counter(nums)
        mx=0
        for i in nums:
            if i+1 in n:
                mx=max(mx,n[i]+n[i+1])
        return mx