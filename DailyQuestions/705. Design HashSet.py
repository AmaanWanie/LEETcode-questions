class MyHashSet:

    def __init__(self):
        self.hm = {}

    def add(self, key: int) -> None:
        self.hm[key] = None  

    def remove(self, key: int) -> None:
        self.hm.pop(key, None)  

    def contains(self, key: int) -> bool:
        return key in self.hm  
