class Solution:
    def generateMatrix(self, n):
        mat = [[0]*n for _ in range(n)]
        l, r = 0, n-1
        t, b = 0, n-1
        m = 1
        
        while m <= n*n:
    
            for i in range(l, r+1):
                mat[t][i] = m
                m += 1
            t += 1

            for i in range(t, b+1):
                mat[i][r] = m
                m += 1
            r -= 1

            if t <= b:
                for i in range(r, l-1, -1):
                    mat[b][i] = m
                    m += 1
                b -= 1

            if l <= r: 
                for i in range(b, t-1, -1):
                    mat[i][l] = m
                    m += 1
                l += 1

        return mat