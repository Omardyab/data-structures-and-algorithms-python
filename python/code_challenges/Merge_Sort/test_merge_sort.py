from code_challenges.Merge_Sort.merge_sort import *
import pytest


@pytest.mark.parametrize(
    "unsorted_list,sorted_list",
   [
    ([8,0,29,82,6,30],[0, 6, 8, 29, 30, 82]),
    ([10,20,30,40,50],[10,20,30,40,50] ),
    ([100,-20,-10,4,54],[-20, -10, 4, 54, 100]),
    ([8,4,23,42,16,15],[4, 8, 15, 16, 23, 42]),
    ([0,9,-1,4,6,125],[-1, 0, 4, 6, 9, 125])
    ]
)
# def test_merge_sort(unsorted_list, sorted_list):
#     assert merge_sort(unsorted_list) == sorted_list

def test_sort(unsorted_list, sorted_list):
    temp = unsorted_list
    merge_sort(unsorted_list)
    assert temp == sorted_list
