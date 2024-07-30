class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        n = len(asteroids)
        heapq.heapify(asteroids)
        for i in range(n):
            asteroid = heapq.heappop(asteroids)
            if asteroid <= mass:
                mass += asteroid
            else:
                return False
        return True

        