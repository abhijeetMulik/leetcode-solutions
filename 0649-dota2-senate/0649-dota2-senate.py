class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        R, D = deque(), deque()

        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)

        while R and D:
            dTurn = D.popleft()
            rTurn = R.popleft()

            if dTurn < rTurn:
                D.append(dTurn + len(senate))
            else:
                R.append(rTurn + len(senate))
        

        return 'Radiant' if R else 'Dire'