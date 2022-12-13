# ls helps us create nodes. i.e., it creates
# children for that directory.
class TreeNode:
    def __init__(self, val, parent, children, size=0):
        self.val = val
        self.size = size
        self.parent = parent
        self.children = children

class Solution:
    def __init__(self):
        self.home = TreeNode("/", None, {})
        f = open("./day7input.txt")
        self.commands = [line.strip() for line in f.readlines()][2:]
    
    def create_tree(self):
        node = self.home
        for c in self.commands:
            c = c.split()
            if c[0] != "$":
                child = TreeNode(c[1], node, {})
                if c[0] != "dir":
                    child.size = int(c[0])
                node.children[c[1]] = child
            if c[1] == "cd":
                if c[2] == "..":
                    node = node.parent
                else:
                    node = node.children[c[2]]
        self.update_size(self.home)

    def update_size(self, node):
        if not node:
            return 0
        size = 0
        for child in node.children.values():
            size += self.update_size(child)
        
        node.size += size

        return node.size

    def solve(self):
        self.create_tree()
        
        ans = 0
        def dfs(node):
            nonlocal ans
            if node.size <= 100000 and node.children:
                ans += node.size
            for child in node.children.values():
                dfs(child)

        dfs(self.home)
        return ans


sol = Solution()
print(sol.solve())



