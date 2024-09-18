class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        for s in strs:
            right = 0
            left = 0
            tmp = ""
            while right < len(s) and left < len(base):
                if s[right] != base[left]:
                    break
                else:
                    tmp += s[right]
                right += 1
                left += 1
            base = tmp
        return base
        

        