graph = {
    'A': ['B', 'C'],
    'B': ['D','E'],
    "C": ['G'],
    'D': [],
    'E': ['F'],
    'G': [],
    'F':[]
}

def DFS(currentNode, destination, graph, maxDepth, curList):
    print("Checking for destination", currentNode)
    curList.append(currentNode)
    if currentNode == destination:
        return True
    if maxDepth <= 0:
        return False
    for node in graph[currentNode]:
        if DFS(node, destination, graph, maxDepth - 1, curList):
            return True
    curList.pop()  # Backtrack if no path is found at this depth
    return False

def iterativeDDFS(currentNode, destination, graph, maxDepth):
    for i in range(maxDepth):
        print(f"\n--- Iteration with depth level {i} ---")
        curList = []
        if DFS(currentNode, destination, graph, i, curList):
            print("Yes, path exists")
            print(curList)
            return True
        print(f"Completed level {i}, no path found at this depth.\n")
    print("Path is not available")
    return False

# Calling the function
iterativeDDFS('A', 'E', graph, 4)

"""
Output :-
--- Iteration with depth level 0 ---
Checking for destination A
Completed level 0, no path found at this depth.


--- Iteration with depth level 1 ---
Checking for destination A
Checking for destination B
Checking for destination C
Completed level 1, no path found at this depth.


--- Iteration with depth level 2 ---
Checking for destination A
Checking for destination B
Checking for destination D
Checking for destination E
Yes, path exists
['A', 'B', 'D', 'E']
True
"""
