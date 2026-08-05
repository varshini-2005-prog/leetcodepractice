class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l=0
        s=set(nums)
        for i in s:
            if i-1 not in s:
                c=i
                le=1
                while c+1 in s:
                    c+=1
                    le+=1
                if le>l:
                    l=le
        return l