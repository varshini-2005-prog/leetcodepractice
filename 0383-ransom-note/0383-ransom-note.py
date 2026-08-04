class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        d={}
        for i in m:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in r:
            if i not in d:
                return False
                break
            d[i]-=1
            if d[i]<0:
                return False
                break

        else:
           
            return True