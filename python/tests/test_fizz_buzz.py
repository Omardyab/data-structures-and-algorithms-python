"""
------------------------------------------
        code ch 18 tests
------------------------------------------
"""
import pytest
from code_challenges.tree_fizz_buzz.tree_f_b import *

@pytest.fixture
def k_tree():
    node = Node(2)
    node.child += [Node(7)]
    node.child += [Node(5)]
    node.child[0].child += [Node(2)]
    node.child[0].child += [Node(4)]
    node.child[1].child += [Node(9)]
    node.child[1].child += [Node(8)]
    node.child[0].child[1].child += [Node(6)]
    node.child[0].child[1].child += [Node(10)]
    node.child[0].child[1].child += [Node(18)]
    node.child[0].child[1].child += [Node(15)]
    node.child[1].child[1].child += [Node(30)]

    k_tree = Tree(node)
    return k_tree

