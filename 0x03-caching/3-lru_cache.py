#!/usr/bin/python3
""" LRUCache """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache Class """

    def __init__(self):
        """ constructor """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lru_order.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.lru_order[0]]
                    print("DISCARD:", self.lru_order[0])
                    self.lru_order.pop(0)
                self.cache_data[key] = item
            self.lru_order.append(key)

    def get(self, key):
        """
        return the value of key in self.cache_data
        """
        if key in self.cache_data:
            self.lru_order.remove(key)
            self.lru_order.append(key)
            return self.cache_data[key]
        return None
