class Solution:
    def getRow(self, row: int) -> List[int]:
        dp=[[1]]
        for i in range(1,row+1):
            p=[1]*(i+1)
            for j in range(1,i):
                p[j]=dp[i-1][j-1]+dp[i-1][j]
            dp.append(p)
        return dp[row]