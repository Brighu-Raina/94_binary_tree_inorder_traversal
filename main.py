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

  def inOrderIteratively(self, root: Node):
    node = root
    stack = []
    path = []
    print('node')
    print('node', node)
    print('node.val', node.val)

    while True:

      node != None and print(node.val)
      while node != None and node.left != None:
        stack.append(node)
        node = node.left

      print('stack', [item.val for item in stack])
      if len(stack) == 0:
        return path

      currentNode = stack.pop()
      path.append(currentNode.val)

      print('path', path)

      print('current', currentNode.val)
      node = currentNode.right

      # if node != None:
      #   path.append(node.val)

      # if node == None:
      #   if len(stack) > 0:
      #     node = stack.pop()
      #   else:
      #     return path
      # print('new node', node.val)

    return path

  def inorderTraversal(self, root: Node) -> List[int]:
    # return self.inOrderRecursive(root)
    return self.inOrderIteratively(root)


#          0
#        1   2
#      3  4  5  6
#     7

my = Solution()

# n = Node(1, None, Node(2, Node(3)))
n = Node(0, Node(1, Node(3, Node(7)), Node(4)), Node(2, Node(5), Node(6)))

ans = my.inorderTraversal(n)

# nAns = [1, 3, 2]
nAns = [7, 3, 1, 3, 0, 5, 2, 6]
print("ans", ans, ans == nAns)
