import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Створення вагового графа
G = nx.Graph()
G.add_edge("A", "B", weight=5)
G.add_edge("B", "D", weight=3)
G.add_edge("D", "F", weight=4)
G.add_edge("F", "E", weight=2)
G.add_edge("E", "C", weight=6)
G.add_edge("B", "F", weight=5)
G.add_edge("F", "A", weight=1)
G.add_edge("E", "G", weight=3)
G.add_edge("C", "G", weight=2)
G.add_edge("D", "G", weight=4)

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths



shortest_paths = dijkstra(G, "A")
print(shortest_paths)


pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()


# висновок:
# Граф має складну структуру з декількома шляхами між вершинами.
# Алгоритм Дейкстри ефективно визначає найкоротші шляхи від початкової вершини "A" до всіх інших вершин, враховуючи ваги ребер. 
# Візуалізація допомагає краще зрозуміти топологію графа та важливість окремих ребер у знаходженні найкоротших шляхів.