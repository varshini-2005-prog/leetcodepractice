class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res=[]
        for i in range(len(nums)):

            if nums[i]==target:
                res.append(i)
        if res==[]:
            return -1
        else:
            return res[0]