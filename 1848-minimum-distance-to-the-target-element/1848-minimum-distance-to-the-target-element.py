class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_dist = 10000   

        for i in range(len(nums)):
            if nums[i]==target:
                dist=abs(i-start)
                if dist<min_dist:
                    min_dist=dist
        return min_dist