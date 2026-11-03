class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return true
        adjacencyMap = {i:[] for i in range(n)}

        for parent, child in edges:
            adjacencyMap[parent].append(child)
            adjacencyMap[child].append(parent)
        
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for child in adjacencyMap[node]:
                if child == prev:
                    continue
                if not dfs(child, node):
                    return False
            return True
        if not dfs(0, -1): return False
        return len(visited) == n