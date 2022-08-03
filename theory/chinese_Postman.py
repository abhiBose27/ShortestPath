import math
import matplotlib.pyplot as plt

import dijkstra as djk
import eulerian
import networkx as nx
from networkx.drawing.nx_agraph import write_dot
# graph defined as a list of edges with weights

G = nx.MultiGraph()

edges = [(0, 1, 1), (0, 3, 1), (0, 4, 4), (1, 2, 2), (1, 4, 3), (2, 5, 1), (3, 4, 2), (4, 5, 2), (2,4, 5)]
for edge in edges:
    (a,b,w) = edge
    G.add_edge(a,b,length = w)
pos = nx.spring_layout(G)
edge_labels=dict([((u,v,),d['length'])
             for u,v,d in G.edges(data=True)])

nx.draw(G, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)

edge_labels=dict([((u,v,),d['length'])
             for u,v,d in G.edges(data=True)])
plt.show()
size = 6
print("edges are :", edges, "\n with size :", size)
adj = eulerian.adj_list_with_weights(6, edges)
# adj_matrix = djk.adj_matrix_with_weights(6, edges)
print("adjlist is : ", adj)

input("Press Enter to continue...")


def print_edges(edges):
    for edge in edges:
        (x, y, w) = edge
        print(x, " ", y, " ", w)


def odd_vertices(n, edges):
    li = [0] * n
    res = []
    for edge in edges:
        li[edge[0]] += 1
        li[edge[1]] += 1

    for i in range(n):
        if li[i] % 2 == 1:
            res.append(i)
    return res


odd_vert = odd_vertices(6, edges)
print("-------------------------------------")
print("odd degree vertices are ", odd_vert)
print("shortest path between 0 and 4 is (path, weight)", djk.shortest_path(6, edges, 0, 4))


def all_pairs(lst):
    if len(lst) < 2:
        yield []
        return
    if len(lst) % 2 == 1:
        # Handle odd length list
        for i in range(len(lst)):
            for result in all_pairs(lst[:i] + lst[i + 1:]):
                yield result
    else:
        a = lst[0]
        for i in range(1, len(lst)):
            pair = (a, lst[i])
            for rest in all_pairs(lst[1:i] + lst[i + 1:]):
                yield [pair] + rest


print("---------------------------")
print("all possible odd vertices pairs are")
for x in all_pairs(odd_vert):
    print(x)
print("---------------------------")


def add_edge(edges, a, b, w):
    edges.append((a, b, w))


def add_edges(list_of_paths, edges, n):
    adj = djk.adj_matrix_with_weights(n, edges)
    for path in list_of_paths:
        for i in range(len(path) - 1):
            add_edge(edges, path[i], path[i + 1], adj[path[i]][path[i + 1]]);


def eulirize(n, edges):
    odd_vert = odd_vertices(6, edges)
    min_sum = math.inf

    for li in all_pairs(odd_vert):
        tmp = []
        sum = 0
        for pair in li:
            dj = djk.shortest_path(n, edges, pair[0], pair[1])
            sum += dj[1]  # the weight of the path
            tmp.append(dj[0])  # append list of nodes that constitute path
        print("list of pairs", li, "total weight :", sum)

        if sum < min_sum:
            min_sum = sum
            res = tmp
    print("list of pairs with minimal weight", res)
    add_edges(res, edges, n)
    return edges


new_edges = eulirize(6, edges)
input("Press Enter to continue...")

print("after eurilizations, edges are ", new_edges)



input("Press Enter to continue...")




G = nx.MultiGraph()

for edge in new_edges:
    (a,b,w) = edge
    G.add_edge(a,b,length = w)
G.add_edge(0,1,length =3)


plt.show()
input("wait")
nx.draw_networkx_nodes(G, pos, node_color = 'r', node_size = 100, alpha = 1)
ax = plt.gca()
for e in G.edges:
    ax.annotate("",
                xy=pos[e[0]], xycoords='data',
                xytext=pos[e[1]], textcoords='data',
                arrowprops=dict(arrowstyle="->", color="0.5",
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])
                                ),
                                ),
                )
plt.axis('off')
plt.show()

print("check if graph has euler cycle :", eulerian.is_eulerian(size, new_edges))
cycle = eulerian.find_eulerian_cycle(size, new_edges)
print("cycle is ", cycle)


def Chinese_Postman(n, edges):
    new_edges = eulirize(n, edges)
    return eulerian.find_eulerian_cycle(size, new_edges)
