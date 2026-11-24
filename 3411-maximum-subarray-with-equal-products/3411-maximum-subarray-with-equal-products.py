import math

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            product = 1
            hcf = 0
            lcm = 1

            for j in range(i, n):
                product = product * nums[j]

                hcf = math.gcd(hcf, nums[j])

                lcm = (lcm * nums[j]) // math.gcd(lcm, nums[j])

                if product == hcf * lcm:
                    ans = max(ans, j - i + 1)

        return ans