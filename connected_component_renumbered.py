# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:34:17 2020

@author: Administrator
"""

import networkx as nx

def BinarySearch(alist,tn,n):
    left=0
    right=n-1
    while left<=right:
        middle=int((left+right)/2)
        if alist[middle]==tn:
            return middle
        if tn>=alist[middle]:
            left=middle+1
        else:
            right=middle-1
    return -1

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

max_len_cc=max(len_cc)
max_cc_index = len_cc.index(max_len_cc)
max_cc = cc[max_cc_index]
print(max_len_cc)
largest_cc = G.subgraph(max_cc)  # subgraph of largest connected component
l_max_cc = list(map(int, max_cc))
l_max_cc.sort()

# renumber = [0] * max_len_cc
# for i in range(max_len_cc):
#     renumber[i] = l_max_cc[i]
cnt = 0
with open('largest_connected_component_renumbered.txt', 'w+') as lcc:
    for edge in largest_cc.edges:
        # lcc.write(l_max_cc.index(edge[0]))
        # lcc.write(' ')
        # lcc.write(l_max_cc.index(edge[1]))
        # lcc.write('\n')
        cnt += 1
        lcc.write(str(BinarySearch(l_max_cc, int(edge[0]), max_len_cc)) + ' ' + str(BinarySearch(l_max_cc, int(edge[1]), max_len_cc)) + '\n')
        if cnt == 10000:
            print('di')
            cnt = 0


# len_cc.pop(0)
# secmax_cc_index = len_cc.index(max(len_cc))
# print(len_cc[secmax_cc_index])

