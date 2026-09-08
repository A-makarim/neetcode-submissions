class Node:
    def __init__(self):
        self.children = {}   # can be a max of 26
        self.end = False # does the word end here?


class PrefixTree:
    def __init__(self):
        self.root = Node() # composition concept of OOP. not dependency injection
    
    def insert(self, word: str) -> None:
        cur = self.root # to the origin

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]  # which is also a Node
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end   #   

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True 
        
        