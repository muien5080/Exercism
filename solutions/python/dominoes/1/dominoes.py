from collections import defaultdict

def can_chain(dominoes):
    if not dominoes:
        return []

    # Build graph with edge indices (to handle duplicates)
    graph = defaultdict(list)
    used = [False] * len(dominoes)

    for i, (a, b) in enumerate(dominoes):
        graph[a].append((b, i))
        graph[b].append((a, i))

    # Check all degrees are even
    for node in graph:
        if len(graph[node]) % 2 != 0:
            return None

    # DFS to check connectivity
    visited = set()

    def dfs(node):
        stack = [node]
        while stack:
            n = stack.pop()
            if n not in visited:
                visited.add(n)
                for nei, _ in graph[n]:
                    stack.append(nei)

    start = dominoes[0][0]
    dfs(start)

    if any(node not in visited for node in graph if graph[node]):
        return None

    # Hierholzer’s algorithm to build cycle
    stack = [start]
    path = []
    
    while stack:
        v = stack[-1]
        while graph[v] and used[graph[v][-1][1]]:
            graph[v].pop()

        if not graph[v]:
            path.append(stack.pop())
        else:
            u, i = graph[v].pop()
            if used[i]:
                continue
            used[i] = True
            stack.append(u)

    if len(path) != len(dominoes) + 1:
        return None

    # Convert node path → domino chain
    chain = []
    for i in range(len(path) - 1):
        chain.append((path[i], path[i+1]))

    return chain