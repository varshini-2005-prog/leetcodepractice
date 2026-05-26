from collections import Counter

class Solution:
    def totalFruit(self, fruits):
        left = 0
        count = Counter()
        max_len = 0

        for i in range(len(fruits)):

            count[fruits[i]] += 1

            while len(count) > 2:

                count[fruits[left]] -= 1

                if count[fruits[left]] == 0:
                    del count[fruits[left]]

                left += 1

            max_len = max(max_len, i - left + 1)

        return max_len