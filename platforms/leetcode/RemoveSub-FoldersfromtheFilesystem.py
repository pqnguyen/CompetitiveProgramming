from typing import List


class Node:
    def __init__(self):
        self.trie = {}
        self.isLeaf = False


class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        root = Node()
        for folder in folders:
            path = folder.split("/")
            self.addPath(root, path)

        res = []
        self.dfs(root, [], res)
        return res

    def dfs(self, root, path, res):
        if root.isLeaf:
            res.append(self.path2form(path))
            return

        for key, trie in root.trie.items():
            path.append(key)
            self.dfs(trie, path, res)
            path.pop()

    def path2form(self, path):
        return "/" + "/".join(path)

    def addPath(self, root, path):
        for folder in path:
            if not folder: continue
            if folder not in root.trie:
                root.trie[folder] = Node()
            root = root.trie[folder]
        root.isLeaf = True


folders = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
res = Solution().removeSubfolders(folders)
print(res)
