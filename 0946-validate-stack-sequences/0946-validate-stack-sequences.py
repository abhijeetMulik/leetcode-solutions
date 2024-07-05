class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        ans = deque()
        j = 0
        for i in range(len(pushed)):
            ans.appendleft(pushed[i])        
            while ans and ans[0] == popped[j]:
                ans.popleft()
                j += 1
        return not ans