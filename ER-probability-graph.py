#!/usr/bin/env python
'''
implement a directed graph with a fixed probability, and plot the distribution
'''
import random
from citation_distribution import normalize_distri
from matplotlib import pyplot

P = 0.4
N = 1000

def graphWithProbability(probability, number_nodes):
    '''
    take probability and the number of the node,
    return a directed graph
    '''
    p = probability
    graph = dict([])
    nodes = range(number_nodes)
    for node in nodes:
        graph[node] = set([])
        values = nodes
        values.remove(node)
        for value in values:
            if random.random() < p:
                graph[node].add(value)
                
    return graph
    
if __name__ == '__main__':
    '''
    Take the probability and the number of the nodes,
    implement the graph, compute the normalized distribution(in-degree),
    then plot it
    '''
    pyplot.figure(figsize=(18,7))
    pyplot.suptitle('Distribution of in-degree of the graph implemented by probability')
    arrange = 250 # for subplot
    for p in range(1, 10, 2):
        arrange += 1
        nor_distri = normalize_distri(graphWithProbability(p/10.0, N))
        nor_distri.pop(0, None)
        keys = nor_distri.keys()
        values = nor_distri.values()
        plot = pyplot.subplot(arrange)
        plot.loglog(keys, values, 'o')
        plot.set_title('p:%s n:%s' %(p/10.0, N))
        plot.set_ylim(0.001, 0.1)
        
        
    for n in range(1000, 5100, 1000):
        arrange += 1
        nor_distri = normalize_distri(graphWithProbability(P, n))
        nor_distri.pop(0, None)
        keys = nor_distri.keys()
        values = nor_distri.values()
        plot = pyplot.subplot(arrange)
        plot.loglog(keys, values, 'o')
        plot.set_title('p:%s n:%s' %(P, n))
        plot.set_ylim(0.001, 0.1)
        
    pyplot.show()
            