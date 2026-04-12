
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c=defaultdict(int)

        l=0
        mx=0
        res=0

        for i in range(len(s)):
            c[s[i]]+=1
            mx=max(mx,c[s[i]])

            while (i-l+1)-mx>k:
                c[s[l]]-=1
                l+=1
        res=max(res,i-l+1)
        return res