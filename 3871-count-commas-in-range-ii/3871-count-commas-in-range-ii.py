class Solution:
    def countCommas(self, n: int) -> int:
        m = n
        c = 0
        x = 1000
        
        while x <= m:
            c += m - x + 1
            x *= 1000
            
        return c