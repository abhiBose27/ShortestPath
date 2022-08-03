def adj_list_with_weights(n, edges):
    adj_list = [[] for i in range(n)]
    for edge in edges:
        (a, b, c) = edge
        adj_list[a].append([b, c])
    return adj_list


def adj_list(n, edges):
    adj_list = [[] for i in range(n)]
    for edge in edges:
        (a, b) = edge
        adj_list[a].append(b)
        adj_list[b].append(a)
    return adj_list


def odd_degree(n, edge):
    adj = adj_list(n, edge)
    for edge in adj:
        if len(edge) % 2 == 0:
            return False
    return True


def is_eulerian(n, edge):
    if not edge:
        return True
    if not is_edge_connected(n, edge):
        return False
    adj = [[] for i in range(n)]
    for (a, b, _) in edge:
        adj[a].append(b)
        adj[b].append(a)

    for el in adj:
        if len(el) % 2 == 1:
            return False
    return True


def is_edge_connected(n, edges):
    adj = [[] for i in range(n)]
    for (a, b, _) in edges:
        adj[a].append(b)
        adj[b].append(a)

    def DFSUtil(temp, v, visited):
        visited[v] = True

        temp.append(v)

        for i in adj[v]:
            if not visited[i]:
                temp = DFSUtil(temp, i, visited)
        return temp

    def connectedComponents():
        visited = []
        cc = []
        for i in range(n):
            visited.append(False)
        for v in range(n):
            if not visited[v]:
                temp = []
                cc.append(DFSUtil(temp, v, visited))
        return cc

    res = connectedComponents()
    cont1 = 1
    cont2 = -1
    for x in res:
        cont1 = len(x)
        if cont1 != 1:
            if cont2 > 1:
                return False
            cont2 = cont1
        elif cont1 != 1 and cont2 > 1:
            return False
    return True


def find_eulerian_cycle(n, edges):
    if len(edges) == 0:
        return []
    cycle = [edges[0][0]]  # start somewhere
    while True:
        rest = []
        for (a, b, _) in edges:
            if cycle[-1] == a:
                cycle.append(b)
            elif cycle[-1] == b:
                cycle.append(a)
            else:
                rest.append((a, b, 0))
        if not rest:
            assert cycle[0] == cycle[-1]
            return cycle[0:-1]
        edges = rest
        if cycle[0] == cycle[-1]:
            # Rotate the cycle so that the last state
            # has some outgoing edge in EDGES.
            for (a, b, _) in edges:
                if a in cycle:
                    idx = cycle.index(a)
                    cycle = cycle[idx:-1] + cycle[0:idx + 1]
                    break
    return cycle
