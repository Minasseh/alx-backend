#!/usr/bin/env python3
""" A LRU caching system Class """

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ A class LRUCache that inherits from BaseCaching
    and is a caching system """

    def __init__(self):
        """ Calling base with super() """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
