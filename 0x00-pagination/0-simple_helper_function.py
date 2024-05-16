#!/usr/bin/env python3
""" Simple helper function
"""

def index_range(page, page_size):
    start_idx = 0
    end_idx = 0
    for _ in range(page):
        start_idx = end_idx
        end_idx += page_size
    return(start_idx, end_idx)


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)