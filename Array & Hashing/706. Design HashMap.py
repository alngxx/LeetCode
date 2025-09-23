class MyHashMap:
    def __init__(self):
        # Each index represent a possible key (0 <= key, value <= 10^6)
        # All entries initialized = -1
        self.map = [-1] * 1000001
        # self.map = [-1, -1, -1, -1, ...]

    def put(self, key: int, value: int) -> None:
        # Set value at index [key]
        self.map[key] = value

    def get(self, key: int) -> int:
        # Retrives value store at index [key]
        # If no such key, it returns -1
        return self.map[key]

    def remove(self, key: int) -> None:
        # Removes the mapping by resetting it to -1
        self.map[key] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
