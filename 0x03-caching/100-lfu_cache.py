#!/usr/bin/python3
""" LFUCache """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache Class """

    def __init__(self):
        """ constructor """
        super().__init__()
        self.lfu_order = []
        self.frequency = {}

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
                self.lfu_order.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    min_value = min(self.frequency.values())
                    min_keys = [k for k in self.frequency
                                if self.frequency[k] == min_value]
                    for i in range(len(self.lfu_order)):
                        if self.lfu_order[i] in min_keys:
                            break
                    del self.cache_data[self.lfu_order[i]]
                    del self.frequency[self.lfu_order[i]]
                    print("DISCARD:", self.lfu_order[i])
                    self.lfu_order.pop(i)
                self.cache_data[key] = item
                self.frequency[key] = 1
            self.lfu_order.append(key)

    def get(self, key):
        """
        return the value of key in self.cache_data
        """
        if key in self.cache_data:
            self.lfu_order.remove(key)
            self.lfu_order.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
