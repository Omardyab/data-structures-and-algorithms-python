from code_challenges.linked_list_insertions.linked_list_insertions  import *

import pytest

""" test for all code challnages are here"""

"""
---------------------------------------------
 tests for code ch 6 tests => go line 38
---------------------------------------------
tests for code ch 8 tests => go line 89
---------------------------------------------
tests for code ch 11 tests => go line 134
---------------------------------------------
tests for code ch 12 tests => go line 166
---------------------------------------------
tests for code ch 13 tests => go line 228
---------------------------------------------
tests for code ch 16 tests => go line 261
---------------------------------------------
"""

"""
------------------------------------------
        code ch 6 tests
------------------------------------------
"""


""" testing linked list insertions (code ch 6)
    [x]Can successfully add a node to the end of the linked list
    [x] Can successfully add multiple nodes to the end of a linked list
    [x] Can successfully insert a node before a node located in the middle of a linked list
    [x] Can successfully insert a node before the first node of a linked list
    [x] Can successfully insert after a node in the middle of the linked list
    [x] Can successfully insert a node after the last node of the linked list
"""
def test_append():
    myll1=Linkedlist()
    myll1.insert(1)
    myll1.append(20)
    assert myll1.head.next.value==20

def test_linked_multiple_append():
    myll2=Linkedlist()
    myll2.append(3)
    myll2.append(2)
    myll2.append(1)
    assert str(myll2)== f'(3) -> (2) -> (1)-> None'

def test_insert_before_mid():
    myll4=Linkedlist()
    myll4.append(22)
    myll4.append(44)
    myll4.append(66)
    myll4.insert_before(44,33)
    assert myll4.head.next.value==33

def test_insert_after():
    myll5=Linkedlist()
    myll5.append(44)
    myll5.append(55)
    myll5.append(77)
    myll5.insert_after(55,66)
    assert myll5.head.next.next.value==66

def test_linked_insert_after_last():
    myll6=Linkedlist()
    myll6.append(3)
    myll6.append(2)
    myll6.append(1)
    myll6.insert_after(1,0)
    assert str(myll6) == f'(3) -> (2) -> (1) -> (0)-> None'

def test_linked_insert_before_first():
    myll7=Linkedlist()
    myll7.append(4)
    myll7.append(3)
    myll7.append(1)
    myll7.insert_before(1,2)
    print(myll7)
    assert str(myll7) == f'(4) -> (3) -> (2) -> (1)-> None'

"""
------------------------------------------
        code ch 8 tests
------------------------------------------
"""
from code_challenges.linked_list_zip.linked_list_zip  import *

def test_linked_list_zip_1():
    ll1 =Linkedlist()
    ll1.insert(7)
    ll1.insert(5)
    ll1.insert(3)
    ll1.insert(1)
    ll2=Linkedlist()
    ll2.insert(8)
    ll2.insert(6)
    ll2.insert(4)
    ll2.insert(2)
    new=linked_list_zip(ll1,ll2)
    assert new==f"(1) -> (2) -> (3) -> (4) -> (5) -> (6) -> (7) -> (8)-> None"

def test_linked_list_zip_2():
    ll1 =Linkedlist()
    ll1.insert(7)
    ll1.insert(5)
    ll1.insert(3)
    ll2=Linkedlist()
    ll2.insert(8)
    ll2.insert(6)
    ll2.insert(4)
    ll2.insert(2)
    new=linked_list_zip(ll1,ll2)
    assert new==f"(3) -> (2) -> (5) -> (4) -> (7) -> (8)-> None"

def test_linked_list_zip_3():
    ll1 =Linkedlist()
    ll1.insert(7)
    ll1.insert(5)
    ll1.insert(3)
    ll2=Linkedlist()
    ll2.insert(8)
    ll2.insert(6)
    new=linked_list_zip(ll1,ll2)
    assert new==f"(3) -> (6) -> (5) -> (8) -> (7)-> None"

"""
------------------------------------------
        code ch 11 tests
------------------------------------------
"""
from code_challenges.stack_queue_pseudo.stack_queue_pseudo import *

def test_q_enqueue_one_element():
    queue = Pseudo_Queue()
    queue.enqueue(1)
    assert str(queue) == f'[{1}] | None'

def test_q_multi_element():
    queue = Pseudo_Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    assert str(queue) == f'[4] | [3] | [2] | [1] | None'

def test_dequeue_one_element():
    queue = Pseudo_Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert 1==queue.dequeue()

def test_dequeue_raise_exception():

    queue = Pseudo_Queue()
    with pytest.raises(Exception, match="empty queue dequeuing "):
        queue.dequeue()

"""
------------------------------------------
        code ch 12 tests
------------------------------------------
"""
from code_challenges.stack_queue_animal_shelter.stack_queue_animal_shelter import *


def test_animal_shelter_enqueue_dog():
    animal_queue = AnimalShelter()
    assert animal_queue.enqueue(Dog("Husky")) == "your animal is now added to the shelter"


def test_animal_shelter_enqueue_cat():
    animal_queue = AnimalShelter()
    assert animal_queue.enqueue(Cat("Lucy")) == "your animal is now added to the shelter"

def test_animal_shelter_dequeue_catanddog():
    animal_queue = AnimalShelter()
    animal_queue.enqueue(Cat('Lucy'))
    animal_queue.enqueue(Dog('Husky'))
    animal_queue.enqueue(Dog('Tiger'))
    animal_queue.enqueue(Cat('Kitty'))
    assert animal_queue.dequeue('cat')=="Lucy"
    assert animal_queue.dequeue('dog')=="Husky"
    assert str(animal_queue)==f"[Tiger] <= [Kitty] <= None"

def test_animal_shelter_dequeue_allcats():
    animal_queue = AnimalShelter()
    animal_queue.enqueue(Cat('Lucy'))
    animal_queue.enqueue(Dog('Husky'))
    animal_queue.enqueue(Dog('Tiger'))
    animal_queue.enqueue(Cat('Kitty'))
    assert animal_queue.dequeue('cat')=="Lucy"
    assert animal_queue.dequeue('cat')=="Kitty"
    assert str(animal_queue)==f"[Husky] <= [Tiger] <= None"


def test_animal_shelter_dequeue_alldogs():
    animal_queue = AnimalShelter()
    animal_queue.enqueue(Cat('Lucy'))
    animal_queue.enqueue(Dog('Husky'))
    animal_queue.enqueue(Dog('Tiger'))
    animal_queue.enqueue(Cat('Kitty'))
    assert animal_queue.dequeue('dog')=="Husky"
    assert animal_queue.dequeue('dog')=="Tiger"
    assert str(animal_queue)==f"[Lucy] <= [Kitty] <= None"

def test_animal_shelter_dequeue_nothing():
    animal_queue = AnimalShelter()
    animal_queue.enqueue(Cat('Lucy'))
    animal_queue.enqueue(Dog('Husky'))
    animal_queue.enqueue(Dog('Tiger'))
    animal_queue.enqueue(Cat('Kitty'))
    animal_queue.dequeue()
    assert str(animal_queue)==f"[Lucy] <= [Husky] <= [Tiger] <= [Kitty] <= None"

def test_animal_shelter_dequeue_from_empty_shelter():
    animal_queue = AnimalShelter()
    with pytest.raises(Exception, match="Your shelter is empty"):
        animal_queue.dequeue("cat")

"""
------------------------------------------
        code ch 13 tests
------------------------------------------
"""
from code_challenges.stack_queue_brackets.stack_queue_brackets import brackets_validator

def test_brackets_match():
    assert brackets_validator("{}[Omar]{}")==True

def test_brackets_nomatch():
    assert not brackets_validator('[{linear regression })')==True

def test_only_one_bracket():
   assert not brackets_validator('[')==True

def test_empty():
    assert not brackets_validator('')==False

def test_no_brackets():
    assert brackets_validator('Dario')==True

def test_two_diff_brackets():
    assert not brackets_validator('{]')==True

"""
------------------------------------------
        code ch 15 tests
------------------------------------------
"""
""" Write tests to prove the following functionality:
    Can successfully instantiate an empty tree
    Can successfully instantiate a tree with a single root node
    Can successfully add a left child and right child to a single root node
    Can successfully return a collection from a preorder traversal
    Can successfully return a collection from an inorder traversal
    Can successfully return a collection from a postorder traversal """

from code_challenges.trees.trees import *


def test_instantiate_empty_tree():
    assert BinaryTree(Node()).root.value== None

def test_instantiate_a_single_root_node_tree():
    assert BinaryTree(Node(2)).root.value== 2

def test_add_left_right_child():
    bt = BinaryTree()
    bt.root = Node("A")
    bt.root.right = Node("R")
    bt.root.left = Node("L")
    assert bt.root.value=="A"
    assert bt.root.right.value=="R"
    assert bt.root.left.value=="L"

def test_instantiate_a_pre_order_tree():
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    assert bt.pre_order() == [2, 7, 2, 6, 5, 11, 5, 9, 4]

def test_instantiate_a_post_order_tree():
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    assert bt.post_order() == [2, 5, 11, 6, 7, 4, 9, 5, 2]

def test_instantiate_an_in_order_tree():
    btree=BinaryTree()
    btree.root=Node(12)
    btree.root.left=Node(15)
    btree.root.right=Node(54)
    btree.root.left.left=Node(55)
    btree.root.right.right=Node(25)
    assert btree.in_order() == [55, 15, 12, 54, 25]

"""
------------------------------------------
        code ch 16 tests
------------------------------------------
"""
from code_challenges.trees_max.treesmax import *

def test_max():
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    assert bt.max()==11

def test_max_false():
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    assert bt.max()!=9

def test_max_none():
    bt = BinaryTree()
    assert bt.max() == None


"""
------------------------------------------
        code ch 18 tests
------------------------------------------
"""
# import pytest
# from code_challenges.tree_fizz_buzz.tree_f_b import *

# @pytest.fixture
# def k_tree():
#     node = Node(2)
#     node.children += [Node(7)]
#     node.children += [Node(5)]
#     node.children[0].children += [Node(2)]
#     node.children[0].children += [Node(4)]
#     node.children[1].children += [Node(9)]
#     node.children[1].children += [Node(8)]
#     node.children[0].children[1].children += [Node(6)]
#     node.children[0].children[1].children += [Node(10)]
#     node.children[0].children[1].children += [Node(18)]
#     node.children[0].children[1].children += [Node(15)]
#     node.children[1].children[1].children += [Node(30)]

#     k_tree = Tree(node)
#     return k_tree

# def test_fizz_buzz(k_tree):
#     assert breadth_first(fizz_buzz_tree(k_tree)) == [
#         '2', '7', 'Buzz', '2', '4', 'Fizz', '8', 'Fizz', 'Buzz', 'Fizz', 'FizzBuzz', 'FizzBuzz']


# def test_fizz_buzz_empty_tree():
#     k_tree = Tree()
#     assert breadth_first(fizz_buzz_tree(k_tree)) == breadth_first(k_tree)

=======


