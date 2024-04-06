class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        max_count, cnt, left = 0, 0, 0
        for i in range(len(s)):
            cnt+=1 if s[i] in vowels else 0
            if i-left+1>k:
                cnt-=1 if s[left] in vowels else 0
                left+=1
            max_count=max(max_count, cnt)
        return max_count



# times out
        # for i in range(len(s)+1-k):
        #     count=0
        #     for j in s[i:i+k]:
        #         if j in vowels:
        #             count +=1
        #     max_count = max(max_count, count)
        # return max_count
        