class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)
        
        def compare(n1, n2):
            if n1+n2 > n2+n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))

        # if cannot use python sorted, although time complexity if O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if compare(nums[i], nums[j]) == 1:
        #             nums[i], nums[j] = nums[j], nums[i]



        return str(int(''.join(nums)))