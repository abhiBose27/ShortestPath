import math


# dijkstra algo but checks for negative paths
# returns null if there is a negative path or if there is no path
# from src to dest
# in the case of a road network these cases can be ignored
def adj_list_with_weights(n, edges):
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        (a, b, w) = edge
        adj_list[a].append([b, w])
    return adj_list


def adj_matrix_with_weights(n, edges):
    adj_list = [[-1 for _ in range(n)] for _ in range(n)]
    for edge in edges:
        (a, b, w) = edge
        adj_list[a][b] = w
    return adj_list


def DFS(src, dist, adj, visited, pred):
    global negative_cycle
    visited[src] = True
    for el in adj[src]:
        weight: int = el[1]
        next_node: int = el[0]
        if visited[next_node] and dist[src] + weight < dist[next_node]:
            negative_cycle = True
        elif dist[src] + weight < dist[next_node]:
            pred[next_node] = src
            dist[next_node] = dist[src] + weight

            DFS(next_node, dist, adj, visited.copy(), pred)


def shortest_path(n, edges, src, dst):
    tmp = dst
    global negative_cycle

    dist = [math.inf] * n
    dist[src] = 0
    visited = [False] * n
    adj = adj_list_with_weights(n, edges)
    negative_cycle = False
    pred = [None] * n
    DFS(src, dist, adj, visited, pred)
    if negative_cycle:
        return None
    if dist[dst] == math.inf:
        return None
    res = []
    while dst != src:
        res.insert(0, dst)
        dst = pred[dst]
    res.insert(0, src)
    return res, dist[tmp]
