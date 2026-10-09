import sys

class TreeNode:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if self.root is None:
            self.root = TreeNode(word)
        else:
            self._insert(self.root, word)

    def _insert(self, node, word):
        if word < node.word:
            if node.left is None:
                node.left = TreeNode(word)
            else:
                self._insert(node.left, word)
        elif word > node.word:
            if node.right is None:
                node.right = TreeNode(word)
            else:
                self._insert(node.right, word)
        # Ignore duplicates

    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node:
            yield from self.inorder(node.left)
            yield node.word
            yield from self.inorder(node.right)

def read_words(filename):
    with open(filename, 'r') as f:
        for line in f:
            for word in line.strip().split():
                yield word

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <textfile>")
        sys.exit(1)

    filename = sys.argv[1]
    tree = BinaryTree()
    for word in read_words(filename):
        tree.insert(word)

    # Avoid recursion limit by using an explicit stack for inorder traversal
    def inorder_iter(tree):
        stack = []
        node = tree.root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.word
            node = node.right

    count = sum(1 for _ in inorder_iter(tree))
    print(f"Number of nodes in the tree: {count}")

if __name__ == "__main__":
    main()