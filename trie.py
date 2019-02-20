
class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {} # <key, value> = <element, TrieNode>

    def containsChild(self, letter):
        return letter in self.children

    def insertChild(self, letter):
        self.children[letter] = TrieNode()

    def getChildNode(self, letter):
        return self.children[letter]

    def setEnd(self):
        self.isEnd = True

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """insert word into Trie starting at root"""
        node = self.root
        for c in word:
            if not node.containsChild(c):
                node.insertChild(c)
            node = node.getChildNode(c)
        node.setEnd()


    def exists(self, word):
        """does word exist in Trie"""
        node = self.root
        for c in word:
            if not node.containsChild(c):
                return False
            node = node.getChildNode(c)
        return node.isEnd

    def prefixExists(self, prefix):
        """does prefix exist in Trie"""
        node = self.root
        for c in prefix:
            if not node.containsChild(c):
                return False
            node = node.getChildNode(c)
        return True

if __name__ == "__main__":
    dictionary = ['words', 'spicy', 'great', 'america']
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    # validation
    val_words = ['word', 'spi', 'america', 'great', 'fake']
    for word in val_words:
        print '\'{}\' whole word exists in Trie? \n\t{}'.format(word, trie.exists(word))
        print '\'{}\' prefix exists in Trie? \n\t{}'.format(word, trie.prefixExists(word))