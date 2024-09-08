class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = left = curr = 0
        for right in range(len(arr)):
            curr += arr[right]
            if (right - left + 1) >= k:
                if curr/k >= threshold:
                    ans += 1
                curr -= arr[left]
                left += 1

        return ans
                 

        