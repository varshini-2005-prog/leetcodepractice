class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        leftmax = 0
        rightmax = 0
        water = 0

        while i < j:

            if height[i] < height[j]:

                if height[i] >= leftmax:
                    leftmax = height[i]
                else:
                    water += leftmax - height[i]

                i += 1

            else:

                if height[j] >= rightmax:
                    rightmax = height[j]
                else:
                    water += rightmax - height[j]

                j -= 1

        return water