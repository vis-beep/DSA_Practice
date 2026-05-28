class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = 0


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):

        n = len(wordsContainer)

        global_best = 0

        for i in range(1, n):
            if len(wordsContainer[i]) < len(wordsContainer[global_best]):
                global_best = i

        root = TrieNode()
        root.best_index = global_best

        for i, word in enumerate(wordsContainer):
            self.insert(root, word, i, wordsContainer)

        ans = []

        for word in wordsQuery:
            ans.append(self.search(root, word))

        return ans

    def insert(self, root, word, index, wordsContainer):

        node = root

        for ch in reversed(word):

            if ch not in node.children:
                node.children[ch] = TrieNode()
                node.children[ch].best_index = index

            node = node.children[ch]

            current_best = node.best_index

            if len(wordsContainer[index]) < len(wordsContainer[current_best]):
                node.best_index = index

    def search(self, root, word):

        node = root

        for ch in reversed(word):

            if ch not in node.children:
                break

            node = node.children[ch]

        return node.best_index
