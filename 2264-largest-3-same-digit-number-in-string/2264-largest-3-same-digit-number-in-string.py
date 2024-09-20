class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        left = 0
        curr = []
        for right in range(len(num)):
            curr.append(num[right])
            if len(curr) >= 3:
                if len(set(curr)) == 1:
                    ans = max(ans, ''.join(curr))
                curr.remove(num[left])
                left += 1

        return ans
        