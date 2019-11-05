class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWord = False
        self.characters = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self
        for ch in word:
            if ch not in trie.characters:
                trie.characters[ch] = Trie()
            trie = trie.characters[ch]
        trie.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self
        for ch in word:
            if ch not in trie.characters: return False
            trie = trie.characters[ch]
        return trie.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self
        for ch in prefix:
            if ch not in trie.characters: return False
            trie = trie.characters[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
