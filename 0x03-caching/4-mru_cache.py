#!/usr/bin/python3
""" MRUCache """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache Class """

    def __init__(self):
        """ constructor """
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.mru_order.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.mru_order[-1]]
                    print("DISCARD:", self.mru_order[-1])
                    self.mru_order.pop(-1)
                self.cache_data[key] = item
            self.mru_order.append(key)

    def get(self, key):
        """
        return the value of key in self.cache_data
        """
        if key in self.cache_data:
            self.mru_order.remove(key)
            self.mru_order.append(key)
            return self.cache_data[key]
        return None
