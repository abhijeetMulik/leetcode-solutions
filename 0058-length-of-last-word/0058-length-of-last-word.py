class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        removeSpc = s.strip()
        result =""
        for i in range(len(removeSpc)-1, -1, -1):
            if removeSpc[i] ==" ":
                return len(result)
            result+=removeSpc[i]
        return len(result)
                
        # print(s.strip())

        