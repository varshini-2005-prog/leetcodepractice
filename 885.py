class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        r, c = rStart, cStart
        res.append([r, c])
        step = 1 
        
        while len(res) < rows * cols:
            for i in range(4): 
                for _ in range(step):
                    r += directions[i][0]
                    c += directions[i][1]
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                if i % 2 == 1:
                    step += 1
        return res