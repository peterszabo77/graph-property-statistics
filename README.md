# graph-property-statistics

Implementation of a randomization test regarding the hierarchical directionality of graph connections.

## About

The script implements a andomization statistical test. Consider a fully connected graph with directed edges.
We can consider the connections among three nodes (A,B,C) as hierarchical, if an A->B and a B->C
connection implies an A->C connection (if A is dominant over B, and B is dominant over C, then
A is dominant over C). Using this concept we can calculate a hierarchy index for any directed matrix.
The test returns a p value for an input graph, which is the probability that the hierarchy index of the input graph can be obtained for a graph with random connection directions.

## Software / libraries
- Python: numpy, matplotlib, graphviz

## Results (examples for randomized, originally completely hierarchical, graphs)

Different shades of blue indicate the overall dominance of nodes (proportion of outgoing edges).

![results](https://github.com/peterszabo77/graph-property-statistics/blob/master/images/results.png)
