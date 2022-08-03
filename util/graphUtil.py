import itertools
import pandas as pd
import networkx as nx


def getNodeOddDegrees(G):
    nodes_odd_degree = [v for v, d in G.degree if d % 2 == 1]
    return nodes_odd_degree


def getCombinations(G):
    List = getNodeOddDegrees(G)
    return len(list(itertools.combinations(List, 2)))


def gEulerize(G, weight_name):
    if G.order() == 0:
        raise nx.NetworkXPointlessConcept("Cannot Eulerize null graph")
    if not nx.is_connected(G):
        raise nx.NetworkXError("G is not connected")
    odd_degree_nodes = getNodeOddDegrees(G)
    G = nx.MultiGraph(G)
    if len(odd_degree_nodes) == 0:
        return G
    odd_deg_pairs_paths = []
    for m, n in itertools.combinations(odd_degree_nodes, 2):
        odd_deg_pairs_paths.append((m, {n: nx.shortest_path(G, source=m, target=n, weight=weight_name),
                                        'weight': nx.dijkstra_path_length(G, source=m, target=n, weight=weight_name)}))

    # odd_deg_pairs_paths = [
    #    (m, {n: nx.shortest_path(G, source=m, target=n, weight=weight_name),
    #         'weight': nx.dijkstra_path_length(G, source=m, target=n, weight=weight_name)})
    #    for m, n in itertools.combinations(odd_degree_nodes, 2)
    # ]
    print("Total Combinations of odd degree nodes:", len(odd_deg_pairs_paths))
    Gp = nx.Graph()
    for n, Ps in odd_deg_pairs_paths:
        p = []
        wt = None
        m = None
        for key in Ps.keys():
            if key != 'weight' and n != key:
                m = key
                p = Ps[key]
            elif key == 'weight':
                wt = Ps[key]
        Gp.add_edge(m, n, weight=1 / wt, path=p)

    best_matching = nx.Graph(list(nx.max_weight_matching(Gp, True)))
    newGraph = nx.MultiGraph(G)
    for m, n in best_matching.edges():
        path = Gp[m][n]["path"]
        newGraph.add_edges_from(nx.utils.pairwise(path))
    return newGraph

# 125751
