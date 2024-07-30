class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        n = len(asteroids)
        asteroids.sort()
        # heapq.heapify(asteroids)
        for i in range(n):
            # asteroid = heapq.heappop(asteroids)
            if asteroids[i] <= mass:
                mass += asteroids[i]
            else:
                return False
        return True

        