class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for i in strs:
            my_dict[''.join(sorted(i))].append(i)
        return my_dict.values()


        # my_dict = {}
        # result = []
        # for i in strs:
        #     sorted_word = ''.join(sorted(i))
        #     if sorted_word not in my_dict:
        #         my_dict[sorted_word] = []
        #         my_dict[sorted_word].append(i)
        #     else:
        #         my_dict[sorted_word].append(i)
        # for i in my_dict.values():
        #     result.append(i)
        # return result


