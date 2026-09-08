class Solution:
    def countCommas(self, n: int) -> int:
        c=0
        for i in range(1,n+1):
            l=len(str(i))
            if l>=4 and l<=6:
                c+=1
            elif l>=7 and l<=6:
                c+=2
            elif l>=10:
                c+=3 
        return c