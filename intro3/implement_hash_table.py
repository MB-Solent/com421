class HashTable:

    def __init__(self, capacity):
        self.capacity = capacity
        bucket = []
        self.bucket_list = [[] for _ in range(self.capacity)]

    def get(self, key):
        bucket_id = self.calc_hash_code(key) % self.capacity
        for item in self.bucket_list[bucket_id]:
            if item[0] == key:
                return item[1]  # return value from tuple
        pass

    def put(self, key, value):
        bucket_id = self.calc_hash_code(key) % self.capacity
        self.bucket_list[bucket_id].append((key, value))

    def calc_hash_code(self, key):
        hash_code = 0
        for character in key:
            hash_code += ord(character)
        return hash_code

    def __str__(self):
        return self.bucket_list.__str__()


x = HashTable(10)

print(x)
x.put("test", 5)
print(x)

print(x.get("test"))
