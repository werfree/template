class Trie:
    def __init__(self):
        self.root = {"*": "*"}

    def addWord(self, word):
        currNode = self.root

        for letter in word:
            if letter not in currNode:
                currNode[letter] = {}
            currNode = currNode[letter]
        currNode["*"] = "*"

    def findWord(self, word):
        currNode = self.root

        for letter in word:
            if letter in currNode:
                currNode = currNode[letter]
            else:
                return "Not Found"
        if currNode.get("*") == None:
            return "Not Found"
        else:
            return "Found"


trie = Trie()
words = ["wait", "waiter", "shop", "shopper"]
for word in words:
    trie.addWord(word)

print(trie.root)

print(trie.findWord("wait"))
print(trie.findWord(""))
print(trie.findWord("waiter"))
print(trie.findWord("shop"))
print(trie.findWord("shopkeeper"))
print(trie.findWord("shopper"))
