# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 08:10:03 2020

@author: Administrator
"""

def components(graph):
    component = []
    seen = set()
    for u in graph:
        if u in seen:
            continue
        current = walk(graph, u)
        seen.update(current)
        component.append(current)
    return component


def walk(graph, start, s=set()):
    nodes, current = set(), dict()
    current[start] = None
    nodes.add(start)
    while nodes:
        u = nodes.pop()
        for v in graph[u].difference(current, s):
            nodes.add(v)
            current[v] = u
    return current


graph = {
    'a': set('bc'),
    'b': set('d'),
    'c': set('bd'),
    'd': set(),
}
print(components(graph))
