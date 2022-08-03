import time

import numpy as np
import datetime as dt
import plotly.graph_objects as go


def plot_path(lat, long):
    fig = go.Figure(go.Scattermapbox(
        name="Path",
        mode="lines",
        lon=long,
        lat=lat,
        marker={'size': 10},
        line=dict(width=4.5, color='red')))

    lat_center = np.mean(lat)
    long_center = np.mean(long)
    fig.update_layout(mapbox_style="stamen-terrain",
                      mapbox_center_lat=30, mapbox_center_lon=-80)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},
                      mapbox={
                          'center': {'lat': lat_center,
                                     'lon': long_center},
                          'zoom': 13})
    fig.show()


def stats_preRun(G):
    print('Number of edges in original graph: {}'.format(len(G.edges())))
    print('Number of nodes in original graph: {}\n'.format(len(G.nodes())))


def stats(G, eulerizedGraph, euler_circuit, weight_name):
    total_cost_of_circuit = 0
    total_cost_of_origMap = 0
    for u, v, k in euler_circuit:
        dic = eulerizedGraph.get_edge_data(u, v)
        total_cost_of_circuit += dic[0][weight_name]
    for edge in G.edges():
        dic = G.get_edge_data(edge[0], edge[1])
        total_cost_of_origMap += dic[0][weight_name]

    print("========================")

    print('Number of edges in circuit: {}'.format(len(euler_circuit)))

    print('Number of edges traversed more than once: {}\n'.format(len(euler_circuit) - len(G.edges())))

    print("SOME STATS")
    if weight_name == 'travel_time':
        print("Cost of Original Map:", time.strftime("%H:%M:%S", time.gmtime(total_cost_of_origMap)))
        print("Cost of eulerian circuit:", time.strftime("%H:%M:%S", time.gmtime(total_cost_of_circuit)))
    if weight_name == 'length':
        print('Length of path: {0:.2f} m'.format(total_cost_of_circuit))
        print('Length of the original map: {0:.2f} m'.format(total_cost_of_origMap))
        print('Length spent retracing edges: {0:.2f} m'.format(total_cost_of_circuit - total_cost_of_origMap))
        if total_cost_of_origMap != 0:
            percent = ((1 - total_cost_of_circuit / total_cost_of_origMap) * - 100)
        else:
            percent = 0
        print('Percent of mileage retraced: {0:.2f}% \n'.format(percent))

    print("=======================")
