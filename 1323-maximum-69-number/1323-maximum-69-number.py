class Solution:
    def maximum69Number (self, num: int) -> int:
        n = str(num)
        max_ele = num
        for i in range(len(n)):
            tmp = 0
            if n[i] == '9':
                tmp = '6'
            else:
                tmp = '9'

            tmp = n[:i] + tmp + n[i+1:]
            max_ele = max(max_ele, int(tmp))
        
        return max_ele

        