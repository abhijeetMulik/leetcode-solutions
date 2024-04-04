class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = []
        for word in words:
            temp = list(chars)
            # print('word is:', word)
            tmp = []
            for w in word:
                # tmp = []
                if w in temp:
                    tmp.append(w)
                    temp.remove(w)
                else:
                    tmp.clear()
                    break
                # print(tmp)
            result.append(''.join(tmp))
        return len(''.join(result))
                    
            
        