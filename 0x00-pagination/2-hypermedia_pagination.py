#!/usr/bin/env python3
""" Simple Helper Function """
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """ A function named index_range that takes two integer
    arguments page and page_size.
    Returns a tuple of size two containing a start index and an end index """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Simple Pagination """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        data = self.dataset()
        start, end = index_range(page, page_size)
        if start > len(data) or end >= len(data):
            return []
        return data[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, int]:
        """ A method that takes the same arguments (and defaults)
        as get_page and returns a dictionary """
        data = self.get_page(page, page_size)
        total = (len(data) + page_size - 1)
        if page < total:
            nex = page + 1
        else:
            nex = None
        if page > 1:
            prev = page - 1
        else:
            prev = None

        result = {
                "page_size": page_size,
                "page": page,
                "data": data,
                "next_page": nex,
                "prev_page": prev,
                "total_pages": total
                }

        return result

