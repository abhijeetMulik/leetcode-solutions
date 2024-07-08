class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D, R = deque(), deque()
        senate = list(senate)

        for i, n in enumerate(senate):
            if n == "R":
                R.append(i)
            else:
                D.append(i)
        
        while D and R:
            dTurn = D.popleft()
            rTurn = R.popleft()

            if rTurn < dTurn:
                R.append(rTurn + len(senate))
            else:
                D.append(dTurn + len(senate))
        
        return "Radiant" if R else "Dire"
