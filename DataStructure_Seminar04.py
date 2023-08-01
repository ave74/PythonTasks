class HashTable:
 
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
 
    def create_buckets(self):
        return [[] for _ in range(self.size)]
 
    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))
 
    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_val
        else:
            return "Запись не обнаружена"
 
    def delete_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
 
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
 
hash_table = HashTable(4)
 
hash_table.set_val('+79005554433', 'Андрей')
hash_table.set_val('+79005554432', 'Алексей')
hash_table.set_val('+79005554432', 'Дарья1')
hash_table.set_val('+79005554433', 'Дарья2')
hash_table.set_val('+79005554434', 'Дарья3')
hash_table.set_val('+79005554435', 'Дарья4')
hash_table.set_val('+79005554436', 'Дарья5')
hash_table.set_val('+79005554437', 'Дарья6')
hash_table.set_val('+79005554438', 'Дарья7')
hash_table.set_val('+79005554439', 'Дарья8')
print(hash_table)
print()
 
hash_table.set_val('+79005554007', 'Bond')
print(hash_table)
print()
 
print(hash_table.get_val('+79005554007'))
print()
 
hash_table.delete_val('+79005554439')
print(hash_table)