class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=Counter(t)
        d=Counter()
        res=""
        l=0
        for i in range(len(s)):
            d[s[i]]+=1
            while all(d[j]>=n[j] for j in n):
                if not res or i-l+1<len(res):
                    res=s[l:i+1]
                d[s[l]]-=1
                l+=1
        return res