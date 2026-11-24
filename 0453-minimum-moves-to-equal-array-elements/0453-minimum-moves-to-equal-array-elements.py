class Solution:
    def minMoves(self, nums: list[int]) -> int:
        s=min(nums)

        m=0
        for i in nums:
            m+=i-s
        return m