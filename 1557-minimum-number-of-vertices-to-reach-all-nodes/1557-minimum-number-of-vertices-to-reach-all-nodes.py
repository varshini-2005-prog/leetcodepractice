class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ind=[0]*(n+1)
        for u,v in edges:
            ind[v]+=1
        ans=[]
        for i in range(n):
            if ind[i]==0:
                ans.append(i)
        return ans 