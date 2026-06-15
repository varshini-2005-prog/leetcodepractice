import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r=int(math.sqrt(num))

        if r*r == num:
            return True
        else:
            return False