class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        mx=0
        for i in range(len(colors)):
            for j in range(n-1,-1,-1):
                if colors[i]!=colors[j]:
                    if j-i>mx:
                        mx=j-i
        return mx