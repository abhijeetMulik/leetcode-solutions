class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_ele = max(costs)
        count = [0] * (max_ele + 1)
        ans = 0

        for c in costs:
            count[c] += 1
        
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        sorted_op = [0] * len(costs)
        for c in reversed(costs):
            sorted_op[count[c] - 1] = c
            count[c] -= 1
        
        for s in sorted_op:
            if coins < s:
                break
            ans += 1
            coins -= s

        return ans