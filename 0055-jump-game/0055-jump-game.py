class Solution:
    def canJump(self, nums):
        max_reach = 0
        
        for i in range(len(nums)):
            
            if i > max_reach:
                return False
            
            if i + nums[i] > max_reach:
                max_reach = i + nums[i]
        
        return True