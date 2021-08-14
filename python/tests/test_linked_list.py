from code_challenges.linked_list_insertions.linked_list_insertions  import *

import pytest


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

