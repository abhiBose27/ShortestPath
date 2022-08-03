import argparse

import networkx as nx
import osmnx as ox
import datetime as dt

import util.convertUtil as cu
import util.graphUtil as gu
import util.plotGraph as pg

ox.__version__

boroughs = ["Ahuntsic-Cartierville", "Anjou", "Côte-des-Neiges–Notre-Dame-de-Grâce", "LaSalle",
            "Le Plateau-Mont-Royal", "Le Sud-Ouest", "L’Île-Bizard–Sainte-Geneviève", "Mercier–Hochelaga-Maisonneuve",
            "Montréal-Nord", "Outremont", "Pierrefonds-Roxboro", "Rivière-des-Prairies–Pointe-aux-Trembles",
            "Rosemont–La Petite-Patrie", "Saint-Laurent", "Saint-Léonard", "Verdun",
            "Villeray–Saint-Michel–Parc-Extension"]


def get_borough(city, country):
    print("Specified city:", city)
    # print("Specified country:", country)
    # print("Specified weight:", weight_name)
    # print("Getting map from Osmnx")
    G = ox.graph_from_place(city + ', ' + country, network_type="drive")
    # fig, ax = ox.plot_graph(G, node_color='b', node_zorder=3)

    # weight_name = 'length'
    # print("Added travel time and speed attributes")
    G = ox.add_edge_speeds(G)
    G = ox.add_edge_travel_times(G)
    G = ox.get_undirected(G)

    pg.stats_preRun(G)
    return gu.getCombinations(G)


def compare_totalCombinations():
    sum = 0
    for borough in boroughs:
        sum += get_borough(borough, "Canada")
    print("Getting odd pair combinations for Montreal............")
    total_comb = get_borough("Montreal", "Canada")
    print("Total odd pair Combinations for Montreal:", total_comb)
    print("Sum of odd pair combinations for each borough:", sum)
    print("Is odd pair Combinations for Montreal alone is higher than sum of odd pair combinations of boroughs of "
          "Montreal?", total_comb > sum)


def parse_argument():
    ps = argparse.ArgumentParser(description="Big demo.")
    ps.add_argument("--city",
                    type=str,
                    help="Specify city to search.")
    ps.add_argument("--country",
                    type=str,
                    help="Specify country to search.")
    ps.add_argument("--weight_name",
                    type=str,
                    help="Specify cost type.")
    args = ps.parse_args()
    if args.city is None:
        city = "Outremont"
        country = "Canada"
        weight_name = "travel_time"
        return city, country, weight_name
    return args.city, args.country, args.weight_name


def check_weight_name(str):
    if str != "travel_time" and str != "length":
        return False
    return True


def main():
    city, country, weight_name = parse_argument()
    if city is None or country is None or weight_name is None or not check_weight_name(weight_name):
        print("Please specify --city and --country")
        print("Example: --city Saint-Witz --country France --weight_name length")

    print("Specified city:", city)
    print("Specified country:", country)
    print("Specified weight:", weight_name)
    print("Getting map from Osmnx")
    G = ox.graph_from_place(city + ', ' + country, network_type="drive")
    fig, ax = ox.plot_graph(G, node_color='b', node_zorder=3)
    MultiDiGraph = G

    # weight_name = 'length'
    print("Added travel time and speed attributes")
    G = ox.add_edge_speeds(G)
    G = ox.add_edge_travel_times(G)
    G = ox.get_undirected(G)

    pg.stats_preRun(G)

    print("Eulerising the graph..........")
    eulerGraph = gu.gEulerize(G, weight_name)
    fig, ax = ox.plot_graph(eulerGraph, node_color='r', node_zorder=3)

    euler_circuit = list(nx.eulerian_circuit(eulerGraph, keys=True))
    pg.stats(G, eulerGraph, euler_circuit, weight_name)

    print("Getting the route.............")
    # Convert the euler circuit to a route
    route = cu.eulerCircuitToRoute(euler_circuit)
    long, lat = cu.pointsToCoord(eulerGraph, route)
    print("Plotting the route")
    pg.plot_path(lat, long)
    #ox.plot_graph_route(G, route, route_color='r')


if __name__ == '__main__':
    main()
