# Creating circular references
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Creating circular references
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node1

# Setting references to None
node1 = None
node2 = None
node3 = None

# Even though we've set the references to None,
# the objects are still in memory because of the circular references.

# Triggering garbage collection
import gc
gc.collect()

# After garbage collection, the circularly referenced objects are deleted from memory.
