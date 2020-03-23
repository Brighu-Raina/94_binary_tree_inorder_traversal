from typing import List


# Definition for a binary tree node.
class Node:

  def __init__(self, x, left=None, right=None):
    self.val = x
    self.left = left
    self.right = right


class Solution:

  def inOrderRecursive(self, node: Node, ans=[]):
    if node == None or node.val == None:
      return ans

    left = []
    right = []
    if node.left != None:
      left = self.inOrderRecursive(node.left)
    if node.right != None:
      right = self.inOrderRecursive(node.right)

    return left + [node.val] + right

//
  def inOrderIteratively(self, root: Node):
    node = root
    stack = []
    path = []

    while True:

      print(node)
      print(node.val)
      print(node.left)
      while node != None and node.left != None:
        stack.append(node)
        node = node.left

      print('stack', stack)
      currentNode = stack.pop()
      path.append(currentNode.val)

      print('path', path)

      node = currentNode.right
      if node == None:
        return path

    return path

  def inorderTraversal(self, root: Node) -> List[int]:
    # return self.inOrderRecursive(root)
    return self.inOrderIteratively(root)


my = Solution()

# n = Node(1, None, Node(2, Node(3)))
n = Node(0, Node(1, Node(3, Node(7))), Node(4)), Node(2, Node(5), Node(6))

ans = my.inorderTraversal(n)

# nAns = [1, 3, 2]
nAns = [7, 3, 1, 3, 0, 5, 2, 6]
print("ans", ans, ans == nAns)
