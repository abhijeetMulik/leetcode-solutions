class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for i in range(len(nums))]
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result






        # prefix = [1 for i in range(len(nums))]
        # post = [1 for i in range(len(nums))]
        # result = [1 for i in range(len(nums))]

        # prefix[0] = nums[0]

        # for i in range(1, len(nums)):
        #     prefix[i] = nums[i]*prefix[i-1]
        
        # post[len(nums)-1] = nums[-1]

        # for i in range(len(nums)-2, -1, -1):
        #     post[i] = post[i+1] * nums[i]
        
        # print('pre',prefix)
        # print('post',post)
        
        # post = [1]+post+[1]
        # prefix = [1] + prefix + [1]
        
        # # result[0]=post[0]
        # result[-1] = prefix[-2]

        # for i in range(1,len(nums)+1):
        #     result[i-1] = (prefix[i-1]*post[i+1])
        
        # return result
        