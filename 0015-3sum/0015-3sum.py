class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            k = len(nums) - 1
            j = i + 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    # tmp = sorted([nums[i], nums[j], nums[k]])
                    # if tmp not in ans:
                    # ans.append(tmp)
                    ans.add(tuple([nums[i], nums[j], nums[k]]))
                    k -= 1
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
        return ans



                