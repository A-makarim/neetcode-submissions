class Node:
    def __init__(self):
        self.children = {} # max 26
        self.end = False # word end


class WordDictionary:

    def __init__(self):
        self.root = Node() # OOP composition

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(i, root): 
            cur = root
            for i in range(i, len(word)):
                if word[i] == ".":
                    # run every child
                    for child in cur.children.values(): # cuz we need to enter node in dfs. not a char    
                        if dfs(i + 1, child):
                            return True
                    return False
                if word[i] not in cur.children:
                    return False
                cur = cur.children[word[i]]
            return cur.end

        return dfs(0, self.root)

                


            
        
        
