import networkx as nx
import matplotlib.pyplot as plt
import csv
import pprint as pp
from math import log, e
import matplotlib as mpl 

# function to read from finalized_cewit_faculty.csv and make a dictionary from it.

def get_dep_fac_dict():
    with open('finalized_cewit_faculty.csv') as f:
        csv_content = csv.DictReader(f)
        dep_fac_dict = {}
        names = []
        iu_dep_list = []
        for row in csv_content:
            fn = row['Name'].split(',')[1].strip().lower()
            ln = row['Name'].split(',')[0].strip().lower()
            dep_fac_dict.setdefault(row['Department'].title(),[]).append((fn,ln))


    return dep_fac_dict


# first, we go to http://www.perbang.dk/rgbgradient/ to get a rgb gradient table with custom steps and start color and end color
# then, paste the color codes into a file, one hex string per line.
# the file looks like:
# E1D8B7
# D6D8B9
# CCD9BB
# C2D9BD
# B8DABF
# AEDAC1
# A4DBC3
# 9ADCC6

def get_gradien_color():
    with open('gradient_colors_faculty') as f:
        color_dict ={}
        colors = []
        for c in f.readlines():
            colors.append('#'+c.strip())
        colors.reverse()  # this reverse the colorbar
        for i in range(5,35):
            color_dict[i] = colors[i-5].strip()
    return color_dict, colors


dep_fac_dict = get_dep_fac_dict()
color_dict, C = get_gradien_color()

print C



# pp.pprint(color_dict)

# because there are too many departments/nodes in the graph, so we only keep the top 25 departments


for d in dep_fac_dict.keys():
    if len(dep_fac_dict[d]) < 5:
        dep_fac_dict.pop(d)








G = nx.Graph()


edge_width_list = []
for d in dep_fac_dict.keys():
    # if len(dep_fac_dict[d]) <= 4:
    #     width = 4
    # else:
    #     width = len(dep_fac_dict[d])
    width = len(dep_fac_dict[d])
    edge_tuple = ('CEWIT', d)
    edge_width_list.append((edge_tuple,width))



for tuple, width in edge_width_list:
    G.add_edge(tuple[0], tuple[1], weight = width/5)   # the weight determines the width of links between departments and CEWIT






node_labels = {}
node_sizes = {}
node_colors = {}
for d in dep_fac_dict.keys():
    node_labels[d] = d + '\n' + str(len(dep_fac_dict[d]))
    # node_sizes[d] = log(len(dep_fac_dict[d]),1.5) * 200   # use log() to decrease the difference between huge node and small node
    # if len(dep_fac_dict[d]) < 11:
    #     node_sizes[d] = 13 * 300
    if len(dep_fac_dict[d]) < 10:
        node_sizes[d] = 14 *250
    elif len(dep_fac_dict[d]) < 20:
        node_sizes[d] = 18 *250
    elif len(dep_fac_dict[d]) < 25:
        node_sizes[d] = 22 * 250
    else:
        node_sizes[d] = (len(dep_fac_dict[d])-2) * 250
    # node_colors[d] = '#E1D8B7'
    node_colors[d] = color_dict[len(dep_fac_dict[d])]

    # color_index.append(len(dep_fac_dict[d]))


node_labels['CEWIT'] = 'CEWIT'
node_sizes['CEWIT'] = 1500
node_colors['CEWIT'] = '#CD894E'

# print node_sizes.keys()
# print node_sizes.values()
# print node_labels.keys()
# print node_labels.values()
edges = G.edges()
weights = [G[u][v]['weight'] for u,v in edges]

plt.figure('Distribution of CEWIT Faculty Members-no caption',figsize=(16,8)) 

cm = mpl.colors.ListedColormap(C)

pos = nx.spring_layout(G, k=.9, scale = 2)

nx.draw(G, pos, linewidths = 0.5,labels = node_labels, font_size = 14, edges = edges, width = 4, nodelist = node_sizes.keys(), node_size = node_sizes.values(), font_family = 'Century Gothic', node_color=node_colors.values(), edge_color='#9adcc6',with_labels=True)

sm = plt.cm.ScalarMappable(cmap=cm, norm=plt.normalize(vmin=5, vmax=35))
sm._A = []
plt.colorbar(sm, shrink = 0.7, pad = 0.15, orientation = 'vertical', anchor = (-2,0.5),fraction = 0.1)



plt.show() # display