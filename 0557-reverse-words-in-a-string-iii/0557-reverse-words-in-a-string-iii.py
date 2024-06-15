class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        a = s.split(" ")
        for i in a:
            res.append(i[::-1])
        return " ".join(res)




        # res = []
        # tmp = ''
        # for i in s[::-1]:
        #     # print(i)
        #     tmp += i
        #     if i == ' ':
        #         res.append(tmp)
        #         # print(tmp)
        #         tmp =''
        # res.append(tmp+' ')    
        # res = res[::-1]
        # res[-1] = res[-1].strip()
        # return ''.join(res)
        