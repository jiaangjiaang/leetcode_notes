class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        if not(self.sub_left(root) or self.sub_right(root)):
            return True
        if not (self.sub_left(root) and self.sub_right(root)):
            return False
        if self.sub_left(root) != self.sub_right(root):
            return False
        return True

    def sub_left(self, root):
        if root:
            return self.sub_left(root.left)

    def sub_right(self, root):
        if root:
            return self.sub_right(root.right)