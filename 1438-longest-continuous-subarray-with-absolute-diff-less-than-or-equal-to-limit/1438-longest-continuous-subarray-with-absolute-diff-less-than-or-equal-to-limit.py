class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc = deque()
        dec = deque()
        left = ans = 0

        for right in range(len(nums)):
            while inc and inc[-1] > nums[right]:
                inc.pop()
            while dec and dec[-1] < nums[right]:
                dec.pop()

            dec.append(nums[right])
            inc.append(nums[right])
            
            while dec[0] - inc[0] > limit:
                if nums[left] == dec[0]:
                    dec.popleft()
                if nums[left] == inc[0]:
                    inc.popleft()
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans
        