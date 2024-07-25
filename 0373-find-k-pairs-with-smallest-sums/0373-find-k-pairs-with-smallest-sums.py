class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []

        for i in range(min(len(nums2), k)):
            heapq.heappush(heap, (nums1[0] + nums2[i], 0, i))
        
        ans = []
        while heap and len(ans) < k:
            total, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1):
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))

        
        return ans
 

        