class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        ans = [-inf, inf]
        high = -inf
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0)) #value, row, row_index
            high = max(high, nums[i][0])
        
        while heap:
            low, row, row_index = heapq.heappop(heap)

            if (ans[1] - ans[0]) > (high - low):
                ans = [low, high]
            
            if row_index + 1 == len(nums[row]):
                return ans
            else:
                next_element = nums[row][row_index + 1]
                heapq.heappush(heap, (next_element, row, row_index + 1))
                high = max(high, next_element)



        