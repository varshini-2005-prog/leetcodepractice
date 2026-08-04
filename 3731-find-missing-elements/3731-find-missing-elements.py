class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s=min(nums)
        l=max(nums)
        ans=[]
        for i in range(s,l+1):
            if i not in nums:
                ans.append(i)
        return ans