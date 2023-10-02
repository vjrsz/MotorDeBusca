from collections import defaultdict


class Cache:
    def __init__(self):
        self.hashmap = self.new_dict()

    def insert(self, key, sub_key, value):
        if not self.hashmap[key]:
            self.hashmap[key] = self.new_dict()

        self.hashmap[key][sub_key] = value

    def get(self, key, sub_key=None):
        value = self.hashmap[key]

        if value and sub_key:
            return value[sub_key]

        return value

    @staticmethod
    def new_dict():
        return defaultdict(lambda: 0)
