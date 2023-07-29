#!/usr/bin/python3
"""class BasicCache that inherits
from BaseCaching and is a caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""
    def __init__(self):
        """Initialize using the init method"""
        super().__init__()

    def put(self, key, item):
        """takes a key and an item as arguments."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return value linked to key."""
        if key is None:
            return None
        return self.cache_data.get(key, None)
