# Tarea 1 Rodrigo López Murguía, A01742780
# Decidi implementar las clases desde 0, utilizando las listas incluidas en python para simular estructuras de datos (Stack, Queue, Hash)
# Al final, se encuentran los test cases que decidí implementar para demostrar el funcionamiento
# Para el hash table, le pedí a gemini que me diera ideas base para la implementación de la hash table (propuso los buckets), pero yo lo simplifiqué al programar.


# Stack
class Stack:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def get(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def __str__(self):
        get = self.get()
        if get is not None:
            return f"Stack With {len(self.items)} item(s), last item is {get}"
        return "Empty Stack"

# Queue
class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

    def get(self):
        if len(self.items) == 0:
            return None
        return self.items[0]

    def __str__(self):
        get = self.get()
        if get is not None:
            return f"Queue with {len(self.items)} items, front item is {get}"
        return "Empty Queue"

# Simple Hash Table
class Hash:
    def __init__(self, size = 50):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def add(self, key, value):
        bucket_index = hash(key) % self.size
        bucket = self.buckets[bucket_index]

        # If it is already in a bucket, just update, or else just add it
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        index = hash(key) % self.size
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = hash(key) % self.size
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return v
        return None

    def __str__(self):
        active_buckets = []
        for bucket in self.buckets:
            if len(bucket) > 0:
                active_buckets.append(len(bucket))
        return f"Hash has {len(active_buckets)} active bucket(s), with {active_buckets} items."


## Test zone

# Test Stack
print("\n\nTesting Stack")
stack = Stack()
stack.add("A")
stack.add("B")
stack.add("C")
stack.add("D")

print(stack)
stack.pop()
stack.pop()
print(stack)

# Test Queue
print("\n\nTesting Queue")
q = Queue()
q.add("Persona 1")
q.add("Persona 2")
q.add("Persona 3")
q.add("Persona 4")
print(q)
q.pop()
q.pop()
print(q)

# Test Hash
print("\n\nTesting Hash")
h = Hash()
h.add("a01742780", "Rocco López")
h.add("a01742781", "Joel Peraza")
h.add("a01742782", "Daniel Tarriba")
h.add("a01742783", "Luis Lopez")
h.add("a01742784", "Rodrigo Ahumada")
print(h)

matricula = "a01742780"
print(h.get(matricula), "has id", matricula)

print("Deleting a01742782 Daniel Tarriba")
h.delete("a01742782")
print(h)