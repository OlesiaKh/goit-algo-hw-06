import networkx as nx

# Створення графа
G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F'), ('E', 'G'), ('F', 'G')])

# Реалізація алгоритму DFS
def dfs(graph, start, visited=None, path=None, parent=None):
    if visited is None:
        visited = set()
        path = []
    if start not in visited:
        visited.add(start)
        if parent is not None:
            path.append((parent, start))
        for next in graph.neighbors(start):
            if next not in visited:
                dfs(graph, next, visited, path, start)
    return path

# Реалізація алгоритму BFS
def bfs(graph, start):
    visited, queue = set(), [start]
    path = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph.neighbors(vertex):
                if neighbor not in visited:
                    queue.append(neighbor)
                    path.append((vertex, neighbor))
    return path

# Виконання DFS та BFS
dfs_path = dfs(G, "A")
bfs_path = bfs(G, "A")
print(f"DFS path: {dfs_path}")
print(f"BFS path: {bfs_path}")

# Використання вбудованих функцій networkx для DFS та BFS
dfs_path = list(nx.dfs_edges(G, source="A"))
bfs_path = list(nx.bfs_edges(G, source="A"))
print(f"DFS path (networkx): {dfs_path}")
print(f"BFS path (networkx): {bfs_path}")



# Загальні висновки:
# Алгоритми DFS і BFS успішно відтворюють основні принципи пошуку в графах.
# Результати демонструють ефективність і коректність реалізації алгоритмів як вручну, так і за допомогою вбудованих функцій NetworkX.
# Пошук у глибину (DFS) більше підходить для задач, де важливо відвідати якнайглибші вершини, тоді як пошук у ширину (BFS) краще підходить для задач,
#  де важливо знайти найкоротший шлях до вершини.