# Graphs
<!-- Short summary or background information -->

Graph is an abstract data type that is meant to implement the undirected graph and directed graph concepts from the field of graph theory within mathematics.

## Challenge
<!-- Description of the challenge -->
Implement your own Graph. The graph should be represented as an adjacency list.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
    - add node: time:O(1) space:O(1)
    - add edge: time:O(1) space:O(1)
    - get nodes: time:O(n) space:O(1)
    - get neighbors: time:O(n) space:O(1)
    - size time:O(n) space:O(1)

## API
<!-- Description of each method publicly available in your Graph -->
### add node

    Arguments: value
    Returns: The added node
    Add a node to the graph

### add edge

    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing
    Adds a new edge between two nodes in the graph
    If specified, assign a weight to the edge
    Both nodes should already be in the Graph

### get nodes

    Arguments: none
    Returns all of the nodes in the graph as a collection (set, list, or similar)
    get neighbors
    Arguments: node
    Returns a collection of edges connected to the given node
    Include the weight of the connection in the returned collection

### size

    Arguments: none
    Returns the total number of nodes in the graph
