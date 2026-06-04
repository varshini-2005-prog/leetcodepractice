class Solution:
    def calculate(self, s: str) -> int:
        st = []
        p = ""
        num = ""

        pri = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2
        }

        for ch in s:
            if ch == " ":
                continue

            if ch.isdigit():
                num += ch
            else:
                p += num + " "
                num = ""

                while st and pri[st[-1]] >= pri[ch]:
                    p += st.pop() + " "

                st.append(ch)

        p += num + " "

        while st:
            p += st.pop() + " "

        st = []

        for token in p.split():

            if token.isdigit():
                st.append(int(token))

            else:
                b = st.pop()
                a = st.pop()

                if token == "+":
                    st.append(a + b)

                elif token == "-":
                    st.append(a - b)

                elif token == "*":
                    st.append(a * b)

                else:
                    st.append(int(a / b))   
        return st[-1]