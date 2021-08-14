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
