class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # empty dict
        # left and right pointers
        self.left = Node(0, 0)             # most used
        self.right = Node(0, 0)            # last used
        self.right.prev = self.left
        self.left.next = self.right



    def changepointers(self, node): # call it on a get query. 
        node.prev.next = node.next
        node.next.prev = node.prev

        temp2 = self.left.next
        self.left.next = node
        node.next = temp2
        node.prev = self.left 
        temp2.prev = node

    def addnew(self, node):

        #check if exceeding capacity
        if len(self.cache) > self.capacity:
            toremove = self.right.prev
            del self.cache[toremove.key]
            # now remove form pointer
            tempprev = self.right.prev.prev
            self.right.prev = self.right.prev.prev
            tempprev.next = self.right


        lefttemp = self.left.next
        self.left.next = node
        node.next = lefttemp
        node.prev = self.left
        lefttemp.prev = node
        

    def get(self, key: int) -> int:
        if key in self.cache: 
            # before returning, adjust the pointers. make this most recent. 
            self.changepointers(self.cache[key])
            return self.cache[key].value
        return -1 # if not exist

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.changepointers(self.cache[key])
            return

        # if putting in a new. check if we are at limit. 
        self.cache[key] = Node(key, value)  # made a new node
        self.addnew(self.cache[key])
              
