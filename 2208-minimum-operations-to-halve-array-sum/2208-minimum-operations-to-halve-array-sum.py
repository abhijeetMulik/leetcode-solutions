class Solution:
    def halveArray(self, nums: List[int]) -> int:
        stop = sum(nums)/2
        nums = [-i for i in nums]
        heapq.heapify(nums)
        # print(nums)
        # print('inital total : ',total)
        count = 0
        while stop > 0:
            first = heapq.heappop(nums)
            firstHalf = first/2
            # print('first: ', first)
            # print('half: ', firstHalf)
            stop += firstHalf
            heapq.heappush(nums, firstHalf)
            count += 1

        return count
        