class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lis = ['0'] * len(s)
        right = len(s)-1
        left = 0
        if len(s) == 1:
            return s
        while left <= right:
            if s[left].isalpha() and s[right].isalpha():
                lis[left], lis[right] = s[right], s[left]
                left += 1
                right -= 1
            if not s[left].isalpha():
                # print("not alpha left: ", s[left])
                lis[left] = s[left]
                left += 1
            if not s[right].isalpha():
                # print("not alpha right : ", s[right])
                lis[right] = s[right]
                right -= 1
        # print(lis)
        return "".join(lis)

        