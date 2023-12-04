class Trie(object):
    root = [{}, False]

    def __init__(self):
        pass

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for char in word:
            newNode = [{}, False]
            cur[0][char] = newNode
            cur = newNode
        cur[1] = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for char in word:
            if char not in cur[0].keys(): return False
            cur = cur[0][char]
        return cur[1]
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for char in prefix:
            if char not in cur[0].keys(): return False
            cur = cur[0][char]
        return True

obj = Trie()
print(obj.startsWith('a'))
