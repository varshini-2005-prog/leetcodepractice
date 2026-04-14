class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = float('inf')

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):

                    if nums[i] == nums[j] and nums[j] == nums[k]:
                        dist = abs(i-j) + abs(j-k) + abs(k-i)
                        ans = min(ans, dist)

        if ans == float('inf'):
            return -1
        else:
            return ans