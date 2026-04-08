class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        n=len(nums)
        left=nums[:(n+1)//2]
        right=nums[(n+1)//2:]
        left=left[::-1]
        right=right[::-1]

        j=0
        for i in range(n):
            if i%2==0:
                nums[i]=left[j]
            else:
                nums[i]=right[j]
                j+=1
        return nums