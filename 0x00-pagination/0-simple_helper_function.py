#!/usr/bin/env python3
""" Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    ''''a function named index_range that takes two
    integer arguments page and page_size.

The function should return a tuple of size two containing
a start index and an end index corresponding to the range
of indexes to return in
a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
'''
    start_idx = 0
    end_idx = 0
    for _ in range(page):
        start_idx = end_idx
        end_idx += page_size
    return (start_idx, end_idx)


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
