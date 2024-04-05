class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        result = []
        s_list=list(s)
        temp=[]
        for i in range(len(s)):
            if target[i%len(target)] in s_list:
                temp.append(target[i%len(target)])
                s_list.remove(target[i%len(target)])
                if sorted(temp) == sorted(target):
                    result.append(temp)
                    temp=[]
        return len(result)



        # for i in range(len(s)):
        #     if s[i] in t_list:
        #         temp.append(s[i])
        #         t_list.remove(s[i])
        #         print(temp)
        #         if sorted(temp) == sorted(target):
        #             result.append(temp)
        #             temp=[]
        #             i=0
        #             t_list = list(target)
        # print(result)
        
        