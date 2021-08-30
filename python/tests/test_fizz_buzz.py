"""
------------------------------------------
        code ch 18 tests
------------------------------------------
"""
import pytest
from code_challenges.tree_fizz_buzz.tree_f_b import Node,Queue,k_tree,k_tree_fizz_buzz

def test_K_arry_tree_if_empty():
    with pytest.raises(Exception, match="K array tree is empty"):
        k_tree_fizz_buzz(k_tree())

def testk_arry_tree():

    copied_k_tree=k_tree()
    copied_k_tree.root = Node(5)
    copied_k_tree.root.children += [Node(45)]
    copied_k_tree.root.children += [Node(0)]
    copied_k_tree.root.children += [Node(9)]
    copied_k_tree.root.children += [Node(3)]
    copied_k_tree.root.children += [Node(1)]
    copied_k_tree.root.children += [Node(5)]
    copied_k_tree.root.children += [Node(11)]
    copied_k_tree.root.children += [Node(15)]
    copied_k_tree=k_tree_fizz_buzz(copied_k_tree).__str__()
    assert copied_k_tree=="['Buzz', 'FizzBuzz', 'FizzBuzz', 'Fizz', 'Fizz', '1', 'Buzz', '11', 'FizzBuzz']"
