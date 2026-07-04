class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """
        DFS: O(V + E), O(V + E)
        1. Build adjacency list: city -> list of its (neighbor, distance)
        2. Start DFS from city 1, track a visited set
        3. At each city, iterate all its roads
        4. For each road, update the answer with min(res, dist)
        5. If neighbor not visited, mark visited and recurse into it
        6. Return the min distance found across all visited roads
        """
        adj = defaultdict(list)     # auto create empty [] for any new key
        for source, dest, dist in roads:
            # bidirectional road
            adj[source].append((dest, dist))
            adj[dest].append((source, dist))
        
        res = float('inf')
        visited = set()
        
        def dfs(city):
            visited.add(city)
            # let dfs() reassign the outer res variable, not create a new local one
            nonlocal res

            for neighbor, dist in adj[city]:
                res = min(res, dist)
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(1)
        return res