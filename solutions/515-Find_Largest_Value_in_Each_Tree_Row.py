class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:
        if root is None:
            return []

        maxVals = []
        rows = { 0: [root], 1: []}

        i = 0
        while i < len(rows):
            rows[i + 1] = []

            maxVal = -float('inf')
            for treeNode in rows[i]:
                if treeNode.left is not None:
                    rows[i + 1].append(treeNode.left)
                
                if treeNode.right is not None:
                    rows[i + 1].append(treeNode.right)

                maxVal = max(maxVal, treeNode.val)

            maxVals.append(maxVal)

            if len(rows[i + 1]) == 0:
                break

            i += 1

        return maxVals