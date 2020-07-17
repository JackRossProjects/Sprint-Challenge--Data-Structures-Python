#### Task 1. Implement a Ring Buffer Data Structure
'''
A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is 
full and a new element is inserted, the oldest element in the ring buffer is 
overwritten with the newest element. This kind of data structure is very useful 
for use cases such as storing logs and history information, where you typically 
want to store information up until it reaches a certain age, after which you don't 
care about it anymore and don't mind seeing it overwritten by newer data.

Implement this behavior in the RingBuffer class. RingBuffer has two methods, `append` and `get`. The `append` method adds the given element to the buffer. The `get` method returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.

For example:
```python
buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']
```
'''

# Ring Buffer
# 1.) Fixed size
# 2.) When full, new element added, the oldest is overwritten

class RingBuffer:
    # Guessing capacity is the max len of items in the array
    def __init__(self,capacity):
        self.capacity = capacity
        self.data = []

    class FullBuffer:
        # Full buffer class
        def append(self, item):
            # Append an element overwriting the oldest one.
            self.data[self.cur] = item
            self.cur = (self.cur+1) % self.capacity
        def get(self):
            # return list of elements
            return self.data[:self.cur]+self.data[self.cur:]

    def append(self,item):
        # append an element at the end of the buffer
        self.data.append(item)
        if len(self.data) == self.capacity:
            self.cur = 0
            # Permanently change self's class from non-full to full
            self.__class__ = self.FullBuffer
    def get(self):
        # return a list of elements from the oldest to the newest. """
        return self.data