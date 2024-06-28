class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            return digit_sum

        count = defaultdict(int)
        ans = -1

        for num in nums:
            digit_sum = get_digit_sum(num)
            if digit_sum in count:
                ans = max(ans, count[digit_sum] + num)
            count[digit_sum] = max(count[digit_sum], num)
        # print(count)
        
        return ans
        