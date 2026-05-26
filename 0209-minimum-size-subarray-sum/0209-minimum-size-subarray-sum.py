class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
            c=0
            m=float('inf')
            l=0
             
            if target in nums:
                return 1
            for i in range(len(nums)):
                c+=nums[i]
                while c>=target:
                    m=min(m,i-l+1)
                    c-=nums[l]
                    l+=1
                        
            if m!=float('inf'):
                return m
            else:
                return 0         