class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = {}
        for p in paths:
            cities[p[0]] = p[1]
        
        for v in cities.values():
            if v not in cities:
                return v


        