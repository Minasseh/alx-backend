#!/usr/bin/env python3
""" A caching system Class """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ A class BasicCache that inherits from BaseCaching
    and is a caching system """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
