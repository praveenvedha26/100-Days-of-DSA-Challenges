# Problem 904: Fruit Into Baskets
# Difficulty: Medium
# Link: https://leetcode.com/problems/fruit-into-baskets/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def totalFruit(self, fruits: List[int]) -> int: 
        count = defaultdict(int)
        l=0
        total,maxi=0,0
        for r in range(len(fruits)):
            count[fruits[r]]+=1
            total+=1
            while (len(count)>2):
                f=fruits[l]
                count[f]-=1
                total-=1
                l+=1
                if not count[f]:
                    count.pop(f)
            maxi=max(total,maxi)
        return maxi