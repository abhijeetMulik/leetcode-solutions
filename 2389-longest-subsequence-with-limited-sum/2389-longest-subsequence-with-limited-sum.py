class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for q in queries:
            count = 0
            for n in nums:
                if q >= n:
                    q -= n
                    count += 1
                else:
                    break
            ans.append(count)

        return ans
