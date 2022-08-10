'''
递归
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        if root == None:
            return self.result
        self.qx_traversal(root)
        return self.result

    def qx_traversal(self, root):
        current = root
        if current == None:
            return
        self.result.append(current.val)
        self.qx_traversal(current.left)
        self.qx_traversal(current.right)
'''