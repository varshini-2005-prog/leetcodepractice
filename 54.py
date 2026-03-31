class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        l,r=0,len(mat[0])-1
        t,b=0,len(mat)-1
        arr=[]
        while l<=r and t<=b:
            for i in range(l,r+1):
                arr.append(mat[t][i])
            t+=1

            for i in range(t,b+1):
                arr.append(mat[i][r])
            r-=1

            if t<= b:
                for i in range(r,l-1,-1):
                    arr.append(mat[b][i])
                b-=1
            if l<= r:
                for i in range(b,t-1,-1):
                    arr.append(mat[i][l])
                l+=1
        return arr