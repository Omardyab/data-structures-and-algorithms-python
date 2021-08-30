import pytest
from insertion_sort import *

@ pytest.mark.parametrize(
    "actual_list,expected_list",[
    ([8,0,29,82,6,30],[0, 6, 8, 29, 30, 82]),
    ([10,20,30,40,50],[10,20,30,40,50] ),
    ([100,-20,-10,4,54],[-20, -10, 4, 54, 100]),
    ([8,4,23,42,16,15],[4, 8, 15, 16, 23, 42]),
    ([0,9,-1,4,6,125],[-1, 0, 4, 6, 9, 125])
    ])

def test_insertion_sort(actual_list,expected_list):
   assert insertion_sort(actual_list)==expected_list
