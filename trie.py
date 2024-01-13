import collections

class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.terminal = False

class Trie:
    dict = {}
    for i in range(1, 27):
        dict[i] = chr(ord('a') + i - 1)
    def __init__(self):
        self.root = TrieNode([])

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode(letter)
            curr_node = curr_node.children[letter]
        curr_node.terminal = True

    def does_word_exist(self, word):
        if word == "":
            return True
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return curr_node.terminal
    
    def get_key_from_value(self, dictionary, value):
        for key, val in dictionary.items():
            if val == value:
                return key
        return None

    
# trie = Trie()
# words = ["wait", "waiter", "shop", "asdf"]
# nums = []

for word in words:
    curr = []
    for let in range(len(word)):
        if (trie.get_key_from_value(trie.dict, word[let])):
            curr.append(trie.get_key_from_value(trie.dict, word[let]))
    
    nums.append(curr)

# for i in nums:
#     print(i)

