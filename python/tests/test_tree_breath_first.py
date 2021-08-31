"""
------------------------------------------
        code ch 17 tests
------------------------------------------
"""
import pytest
from code_challenges.tree_breadth_first.treebreadth import *

def test_breadth_first_tree_if_empty():
    bt = Binary_Search_Tree()
    with pytest.raises(Exception, match="your tree is empty"):
        breadth_first(bt)


def test_breadth_first_add_two_nodes():
    t = Binary_Search_Tree()
    t.add(5)
    t.add(8)
    assert breadth_first(t) == [5,8]


def test_breadth_first_multi_nodes():
    nodes = [3, 2, 1, 0, 5, 7]
    t = Binary_Search_Tree()
    for node in nodes:
        t.add(node)
    assert breadth_first(t)==[3, 2, 5, 1, 7, 0]

