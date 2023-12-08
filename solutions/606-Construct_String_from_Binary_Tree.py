class Solution:
    def tree2str(self, root: TreeNode) -> str:
        left = ''
        if root.left != None:
            left = f'({self.tree2str(root.left)})'

        right = ''
        if root.right != None:
            right = f'({self.tree2str(root.right)})'

            if left == '':
                left = '()'

        return f'{root.val}{left}{right}'