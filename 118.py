class Solution(object):
    def generate(self, numRows):
        res = []
        
        for i in range(numRows):
            row = []
            n = 1
            for j in range(i + 1):
                row.append(n)
                n = n * (i - j) // (j + 1)
            res.append(row)
        
        return res
