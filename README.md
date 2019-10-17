# graph-property-statistics

Implementation of a randomization test regarding the hierarchical directionality of graph connections.

## About

The script implements a randomization statistical test. Consider a fully connected graph with directed edges.
We can consider the connections among three nodes (A,B,C) as hierarchical, if an A->B and a B->C
connection implies an A->C connection (if A is dominant over B, and B is dominant over C, then
A is dominant over C). Using this concept we can calculate a hierarchy index (H) for any directed graph.
The script calculates the H index of an input graph (given by a connection matrix) and returns a p value, which is an estimate of the probability that the H index of a completely random graph is at least as large
as the H index of the input (one-sided significance of hierarchy).

## Software / libraries
- Python: numpy, matplotlib, graphviz

## Results (examples for randomized, originally completely hierarchical, graphs)

Different shades of blue indicate the overall dominance of nodes (proportion of outgoing edges).

![results](https://github.com/peterszabo77/graph-property-statistics/blob/master/images/results.png)
