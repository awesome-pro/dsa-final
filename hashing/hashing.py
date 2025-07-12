# Implementing Hashing from scratch in Python

# class HashTable:
#     def __init__(self, size=100):
#         self.size = size
#         self.table = [None] * size

#     def hash_function(self, key):
#         return key % self.size
    
#     def insert(self, key, value):
#         index = self.hash_function(key)
#         self.table[index] = value

#     def get(self, key):
#         index = self.hash_function(key)
#         return self.table[index]
    
#     def remove(self, key):
#         index = self.hash_function(key)
#         self.table[index] = None

# # Time Complexity: O(1)
# # Space Complexity: O(n)
# hash_table = HashTable()
# hash_table.insert(1, "John")
# hash_table.insert(2, "Jane")
# print(hash_table.get(1))
# print(hash_table.get(2))
# hash_table.remove(1)

# Implementing Hashing with Chaining

# Time Complexity: O(1)
# Space Complexity: O(n)
class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return None
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

# Time Complexity: O(1)
# Space Complexity: O(n)
hash_table = HashTable()
hash_table.insert(1, "John")
