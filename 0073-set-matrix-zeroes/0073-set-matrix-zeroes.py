class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(mat)
        c=len(mat[0])
        ze=[]
        zx=[]
        for i in range(r):
            for j in range(c):
                if mat[i][j]==0:
                    ze.append(i)
                    zx.append(j)

        for i in ze:
            for j in range(c):
                mat[i][j]=0
        for k in zx:
            for j in range(r):
                mat[j][k]=0
        return mat