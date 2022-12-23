import networkx as nx

def read_network(path):
    G = nx.Graph()
    with open(path, 'r') as f:
        for row,line in enumerate(f.readlines()):
            for col,elem in enumerate(line.strip().split(',')):
                if elem != '-':
                    G.add_edge(row, col, w=int(elem))
    return G

from matplotlib import pyplot as plt

def draw_network(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, nx.get_edge_attributes(G, 'w'))
    plt.show()

def trim_network(G):
    saving = 0
    while True:
        try:
            cycle = nx.find_cycle(G)
            max_edge = max(cycle, key=lambda e: G.edges[e]['w'])
            saving += G.edges[max_edge]['w']
            G.remove_edge(*max_edge)
        except nx.NetworkXNoCycle:
            break
    print(f'saved {saving}')
