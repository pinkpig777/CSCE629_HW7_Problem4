import heapq
graph = {
    1: [(2, 1), (11, 1), (10, 2)],
    2: [(1, 1), (3, 1), (21, 1)],
    3: [(2, 1), (4, 1), (8, 2)],
    4: [(3, 1), (5, 1)],
    5: [(4, 1), (6, 2), (7, 1), (22, 1)],
    6: [(5, 2), (7, 2)],
    7: [(5, 1), (6, 2), (8, 1)],
    8: [(3, 2), (7, 1), (9, 1)],
    9: [(8, 1), (10, 1), (19, 2)],
    10: [(1, 2), (9, 1), (11, 1)],
    11: [(1, 1), (10, 1), (12, 2), (17, 1)],
    12: [(11, 2), (13, 2)],
    13: [(12, 2), (14, 2), (21, 1)],
    14: [(13, 2), (15, 1), (16, 1), (20, 1)],
    15: [(14, 1)],
    16: [(14, 1), (17, 1)],
    17: [(11, 1), (16, 1), (18, 2)],
    18: [(17, 2), (19, 2)],
    19: [(9, 2), (18, 2)],
    20: [(21, 2), (22, 1)],
    21: [(13, 1), (20, 2), (22, 2)],
    22: [(20, 1), (21, 2)]
}


def dijkstra(graph, source):
    dist = {v: float('inf') for v in graph}
    dist[source] = 0
    Q = [(0, source)]

    while Q:
        d, u = heapq.heappop(Q)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(Q, (dist[v], v))
    return dist


if __name__ == "__main__":
    destinations = [6, 8, 9, 15, 16, 22]
    source_node = 1
    distances = dijkstra(graph, source_node)
    for node in sorted(destinations):
        print(
            f"Distance from node {source_node} to node {node} is {distances[node]}")
