class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(string):
            ans = []
            for right in range(len(string)):
                if string[right] == '#':
                    if len(ans) > 0:
                        ans.pop()
                else:
                    ans.append(string[right])
            return ans
                    
        # print(helper(s))
        # print(helper(t))
        return helper(s) == helper(t)
