#(1991) 트리 순회

import sys

class Node:
    def __init__(self, item, right, left):
        self.item = item
        self.right = right
        self.left = left

number = int(sys.stdin.readline())
tree = {}
for _ in range(number):
    node, left, right = sys.stdin.readline().split()
    tree[node] = Node(node,right,left)

def preorder(node):
    sys.stdout.write(node.item)
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    sys.stdout.write(node.item)
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    sys.stdout.write(node.item)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
