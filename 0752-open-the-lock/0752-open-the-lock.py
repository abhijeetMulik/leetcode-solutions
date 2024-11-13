class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def combinations(node):
            ans = []
            for i in range(4):
                x = node[i]
                for j in [1, -1]:
                    change = (int(x) + j) % 10
                    update = node[:i] + str(change) + node[i + 1:]
                    ans.append(update)
            return ans

        if '0000' in deadends:
            return -1
        
        queue = deque([('0000', 0)]) # target, turns
        seen = set(deadends)
        seen.add('0000')

        while queue:
            node, turns = queue.popleft()

            if node == target:
                return turns
            
            for c in combinations(node):
                if c not in seen:
                    seen.add(c)
                    queue.append((c, turns + 1))
        
        return -1
            
        