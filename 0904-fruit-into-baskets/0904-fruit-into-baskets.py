class Solution:
    def totalFruit(self, fruits):

        count = Counter()

        l = 0
        m = 0

        for r in range(len(fruits)):

            count[fruits[r]] += 1

            while len(count) > 2:

                count[fruits[l]] -= 1

                if count[fruits[l]] == 0:
                    del count[fruits[l]]

                l += 1

            m = max(m, r - l + 1)

        return m