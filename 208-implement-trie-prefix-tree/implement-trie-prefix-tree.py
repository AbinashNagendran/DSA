class Trie(object):

    def __init__(self):
        self.trie = {}

        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        pointer = self.trie
        for letter in word:
            if not letter in pointer:
                pointer[letter] = {}
            
            pointer = pointer[letter]
        pointer['.'] = '.'
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        pointer = self.trie
        for letter in word:
            if not letter in pointer:
                return False
            pointer = pointer[letter]
        return '.' in pointer
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        pointer = self.trie
        for letter in prefix:
            if not letter in pointer:
                return False
            pointer = pointer[letter]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)