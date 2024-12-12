class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n, m = len(nums1), len(nums2)
        for i in range(n):
            left = i
            right = m - 1
            while left <= right:
                mid = (left + right) // 2
                if nums2[mid] >= nums1[i]:
                    left = mid + 1
                else:
                    right = mid - 1
            ans = max(ans, right - i)
        
        return ans

            

        