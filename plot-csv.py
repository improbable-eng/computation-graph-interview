import networkx as nx
import pandas as pd
import argparse
import matplotlib


matplotlib.use('TkAgg')

parser = argparse.ArgumentParser()
parser.add_argument("name", help="The name of the graph to load from the 'csv' directory")
args = parser.parse_args()

print("Plotting", args.name)

# load the data

path = "csv/"

nodes = pd.read_csv(f"{path}/{args.name}.nodes.csv").set_index("id")
edges = pd.read_csv(f"{path}/{args.name}.edges.csv")

# create the graph

G = nx.MultiDiGraph()
G.add_edges_from(edges.values)

# draw the graph

default_color = '#DDDDDD'
colors = [default_color] * len(nodes)
if 'color' in nodes.columns:
    color_dict = nodes['color'].fillna('#DDDDDD').to_dict()
    colors = [color_dict[id] for id in G.nodes]

pos = nx.kamada_kawai_layout(G)
# pos = nx.fruchterman_reingold_layout(G)

edge_labels = {}
for u,v,d in G.edges:
    num_edges = G.number_of_edges(u,v)
    if num_edges > 1:
        edge_labels[(u,v)] = num_edges

nx.draw_networkx_labels(
	G,
	pos,
	labels=nodes['name'].to_dict(),
	font_size=14
)

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

nx.draw(
    G,
    pos,
    node_color=colors,
    node_size=500,
    arrowsize=20
)

matplotlib.pyplot.show()
