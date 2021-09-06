from quick_sort import *
import pytest


@pytest.mark.parametrize(
    "unsorted,sorted",
    [
        ([], []),
        ([0, -18, 12, -8],[-18, -8, 0, 12]),
        ([100,-200,300,-400] , [-400, -200, 100, 300]),
        ([2, 3, 20, 7, 50, 0,-30], [-30, 0, 2, 3, 7, 20, 50]),
    ],
)
def test_quick_sort(unsorted, sorted):
    Quick_Sort(unsorted, 0, len(unsorted)-1)
    assert unsorted == sorted
