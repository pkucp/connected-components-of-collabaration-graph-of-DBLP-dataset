# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:34:17 2020

@author: Administrator
"""

import networkx as nx
# import matplotlib.pyplot as plt

# pointList = ['A','B','C','D','E','F','G']
# linkList = [('A','B'),('B','C'),('C','D'),('E','F'),('F','G'),]


def subgraph():
    G = nx.Graph()
    # 转化为图结构
    for node in pointList:
        G.add_node(node)

    for link in linkList:
        G.add_edge(link[0], link[1])

   # 画图
    plt.subplot(211)
    nx.draw_networkx(G, with_labels=True)
    color =['y','g']
    subplot = [223,224]
    # 打印连通子图
    for c in nx.connected_components(G):
       # 得到不连通的子集
        nodeSet = G.subgraph(c).nodes()
       # 绘制子图
        subgraph = G.subgraph(c)
        plt.subplot(subplot[0])  # 第二整行
        nx.draw_networkx(subgraph, with_labels=True,node_color=color[0])
        color.pop(0)
        subplot.pop(0)

    plt.show()
subgraph()