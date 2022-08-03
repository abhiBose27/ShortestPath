
def eulerCircuitToRoute(euler_circuit):
    route = []
    for edge in euler_circuit:
        route.append(edge[0])
    route.append(euler_circuit[0][0])
    return route


def pointsToCoord(G, route):
    long = []
    lat = []
    for i in route:
        long.append(G.nodes[i]['x'])
        lat.append(G.nodes[i]['y'])
    return long, lat
