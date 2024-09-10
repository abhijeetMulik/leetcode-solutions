class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = ans = 0
        seen = defaultdict(int)
        for right, fruit in enumerate(fruits):
            seen[fruit] += 1
            if len(seen) > 2:
                while len(seen) > 2:
                    seen[fruits[left]] -= 1
                    if seen[fruits[left]] == 0:
                        del seen[fruits[left]]
                    left += 1
            
            ans = max(ans, right - left + 1)

        return ans
                
        