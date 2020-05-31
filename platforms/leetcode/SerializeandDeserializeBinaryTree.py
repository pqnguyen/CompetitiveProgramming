# https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/995/
import json


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def serializeUtil(root, ls):
            if not root:
                ls.append(None)
                return
            ls.append(root.val)
            serializeUtil(root.left, ls)
            serializeUtil(root.right, ls)

        ls = []
        serializeUtil(root, ls)
        return json.dumps(ls)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.index = 0

        def deserializeUtil(ls):
            if self.index >= len(ls) or ls[self.index] is None:
                return None
            node = TreeNode(ls[self.index])
            self.index += 1
            node.left = deserializeUtil(ls)
            self.index += 1
            node.right = deserializeUtil(ls)
            return node

        ls = json.loads(data)
        root = deserializeUtil(ls)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
