class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = defaultdict(int)
        loss = defaultdict(int)

        for m in matches:
            if m[0] in loss:
                if m[0] in win:
                    del win[m[0]]
            else:
                win[m[0]] += 1
            loss[m[1]] += 1

            if m[1] in win:
                del win[m[1]]

        ans = []
        for key in loss.keys():
            if loss[key] == 1:
                ans.append(key)
        return sorted(list(win.keys())), sorted(ans)
        