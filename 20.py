class Solution:
    def isValid(self, s: str) -> bool:
        pairs={
            "}":"{","]":"[",")":"("
        }
        st=[]
        v=True
        for i in s:
            if i in pairs:
                if not st or st[-1]!=pairs[i]:
                    v=False
                    break
                else:
                    st.pop()
            else:
                st.append(i)

        if v and len(st)==0:
            return True
        else:
            return False