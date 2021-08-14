# Trees
<!-- Short summary or background information -->
        Tree is a node-based data structure
        Tree can have any number of children (next values) k
        a linked list is a special case of Tree, K=1
        In Binary tree K=2
        
## Challenge
<!-- Description of the challenge -->
    Node

    Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

    Binary Tree

    Create a Binary Tree class
    Define a method for each of the depth first traversals:
    pre order
    in order
    post order which returns an array of the values, ordered appropriately.


    Binary Search Tree

        Create a Binary Search Tree class
        This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
    Binary Search Tree

        Time: O(log(N))
        Space:O(1)

    Binary Tree
        Time: O(N)
        Space:O(1)

## API
<!-- Description of each method publicly available in each of your trees -->
    Add
        Arguments: value
        Return: nothing
        Adds a new node with that value in the correct location in the binary search tree.

    Contains

        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.
