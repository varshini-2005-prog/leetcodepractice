class Solution(object):
    def majorityElement(self, nums):
        
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for k,v in d.items():
            if v>len(nums)//2:
                return k