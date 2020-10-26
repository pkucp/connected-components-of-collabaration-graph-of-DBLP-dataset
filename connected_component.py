# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:34:17 2020
@author: Administrator
"""

import networkx as nx


G = nx.Graph()
cc = []  # set of connected components
len_cc = []

with open('collaboration.txt', 'r') as f:
    for line in f:
        link = line.split()
        G.add_edge(link[0], link[1])

for c in nx.connected_components(G):
    cc.append(c)
    len_cc.append(len(c))

max_cc_index = len_cc.index(max(len_cc))
max_cc = cc[max_cc_index]
print(max(len_cc))
largest_cc = G.subgraph(max_cc)  # subgraph of largest connected component

with open('largest_connected_component.txt', 'w+') as lcc:
    for edge in largest_cc.edges:
        lcc.write(edge[0] + ' ' + edge[1] + '\n')

len_cc.pop(0)
secmax_cc_index = len_cc.index(max(len_cc))
print(len_cc[secmax_cc_index])
