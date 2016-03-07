from matplotlib import pyplot as plt
import networkx as nx
from numpy import array

def weighted_graph_with_edge_labels():
    #create an empty graph
    G = nx.Graph()
    
    #add three edges
    G.add_edge('A','B');
    # G.add_edge('B','C');
    G.add_edge('C','A');
    G.add_edge('D','A');
    G.add_edge('E','A');

    # G['A']['B']['weight'] = 10
    # # G['B']['C']['weight'] = 14
    # G['C']['A']['weight'] = 25
    # G['D']['A']['weight'] = 50
    # G['E']['A']['weight'] = 700

    # position the nodes by Force Layout
    pos = {'A': array([  3,   2]), 'C': array([ 3,  1]), 'B': array([-0.80901706,  0.58778518]), 'E': array([-0.80901694, -0.58778536]), 'D': array([ 0.30901712, -0.95105648])}
    print pos
    
    #position the nodes according the output
    # from the spring/force layout algorithm
    nx.draw(G,pos)

    #show the created graph
    plt.show()
    # #shorter edge length indicates higher weight

    # edge_weight=dict([((u,v,),int(d['weight'])) for u,v,d in G.edges(data=True)])

    # nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_weight)
    # nx.draw_networkx_nodes(G,pos)
    # nx.draw_networkx_edges(G,pos)
    # nx.draw_networkx_labels(G,pos)
    # plt.axis('on')
    # plt.show()

weighted_graph_with_edge_labels()