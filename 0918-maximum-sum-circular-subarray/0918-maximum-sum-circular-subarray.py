class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=sum(nums)

        c_m=nums[0]
        m_s=nums[0]
        c_mi=nums[0]
        mi_s=nums[0]

        for i in nums[1:]:
            c_m=max(i,c_m+i)
            m_s=max(m_s,c_m)

            c_mi=min(i,c_mi+i)
            mi_s=min(mi_s,c_mi)

        if m_s<0:
            return m_s
        return max(m_s,total-mi_s)
