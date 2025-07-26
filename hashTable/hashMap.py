class SimpleHashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return sum(int(char) for char in key if char.isdigit()) % 10
    
    def put(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                print(f"{index}: {bucket[i]}")
            else:
                print("Element of key: {key} Not Found")

    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.remove((k, v))
            else:
                print("Element Not Found")

    def print_hash_map(self):
        print("Printing HashMap...")
        for i, buck in enumerate(self.buckets):
            print(f"{i}: {buck}")

hash_map = SimpleHashMap(10)
hash_map.put('18', 'Lutfu')
hash_map.put('20', 'Abdul')
hash_map.put('14', 'Marzouq')
hash_map.put('10', 'Anas')
hash_map.put('7', 'Zaid')
hash_map.get('12')
# hash_map.remove('18')
print(hash_map.print_hash_map())