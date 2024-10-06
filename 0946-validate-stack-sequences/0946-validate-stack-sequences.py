class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        counter = 0
        for p in range(len(pushed)):
            stack.append(pushed[p])
            while stack and stack[-1] == popped[counter]:
                stack.pop()
                counter += 1
        print(stack)
        return not stack


        