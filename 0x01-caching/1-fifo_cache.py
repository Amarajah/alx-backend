#!/usr/bin/python3
"""fifo_cache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """fifo class"""
    def __init__(self):
        """init"""
        super().__init__()

    def put(self, key, item):
        """Cache a key-value pair"""
        if key is None or item is None:
            return

        """If the cache is full, remove the first item (FIFO)"""
        if len(self.cache_data) >= self.MAX_ITEMS:
            """Get the first item's key and pop it from the cache"""
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f"DISCARD: {first_key}\n")

        """Add the new item to the cache"""
        self.cache_data[key] = item

    def get(self, key):
        """return key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
