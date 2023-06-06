class HashTable:
    def __init__(self):
        self.table = {}

    def __contains__(self, key):
        return key in self.table

    def __len__(self):
        return len(self.table)
hash_table = HashTable()
hash_table.table = {"key1": 1, "key2": 2, "key3": 3}

print("key1" in hash_table)  # True
print("key4" in hash_table)  # False

print(len(hash_table))  # 3
