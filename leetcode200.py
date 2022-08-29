class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        
        
        def dfs(visited, graph, node):
            if node not in visited:
                # print(node)
                visited.add(node)
                for neighbor in graph[node]:
                    dfs(visited, graph, neighbor)

graph = {
    '1': ['1','2','3'],
    '2': ['1','2','3'],
    '3': ['1','2','3']
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '2')