class TrieNode:
    def __init__(self, value: str) -> None:
        self.value = value
        self.children = {}
        self.is_end = False

class Trie:
	def __init__(self):
		root = TrieNode


class Node:
	def __init__(self, c):
		self.c = c
		self.is_word = False
		self.children = {}


class Trie:
	def __init__(self):
		self.root = Node('\0')

	def insert(self, word):
		curr = self.root
		for char in word:
			if char not in curr.children:
				curr.children[char] = Node(char)
			curr = curr.children[char]

		curr.is_word = True

	def search(self, word):
		node = self.getNode(word)
		return node is not None and node.is_word

	def startsWith(self, prefix):
		node = self.getNode(prefix)
		return node is not None;

	def getNode(self, word):
		curr = self.root
		for char in word:
			if char not in curr.children:
				return None
			curr = curr.children[char]

		return curr


def main():
	obj = Trie()
	obj.insert('rops')
	print(obj.search('ropis'))
	print(obj.startsWith('rop'))


main()