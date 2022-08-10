'''
递归
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        if root == None:
            return self.result
        self.zs_traversal(root)
        return self.result

    def zs_traversal(self, root):
        current = root
        if current == None:
            return
        self.zs_traversal(current.left)
        self.result.append(current.val)
        self.zs_traversal(current.right)
'''