#!/usr/bin/env python3
""" A LFU caching system Class """

from base_caching import BaseCaching
from collections import OrderedDict, Counter


class LFUCache(BaseCaching):
    """ A class LFUCache that inherits from BaseCaching
    and is a caching system """

    def __init__(self):
        """ Calling base with super() """
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = Counter()

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
                min_freq = min(self.frequency.values())
                least_freq_keys = []
                for k, v in self.frequency.items():
                    if v == min_freq:
                        least_freq_keys.append(k)
                least_recent_key = least_freq_keys[0]
                if len(least_freq_keys) > 1:
                    least_recent_key = next(iter(self.cache_data))
                print(f"DISCARD: {least_recent_key}")
                self.cache_data.pop(least_recent_key)
                del self.frequency[least_recent_key]

            self.cache_data[key] = item
            self.frequency[key] += 1

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.frequency[key] += 1
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        else:
            return None
