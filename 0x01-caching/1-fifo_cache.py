#!/usr/bin/env python3
""" A FIFO caching system Class """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ A class BasicCache that inherits from BaseCaching
    and is a caching system """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = list(self.cache_data.keys())[0]
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
