from typing import Optional, List

class Solution:
    def balanceBST(self, root: Optional['TreeNode']) -> Optional['TreeNode']:
        def inorder(node: Optional['TreeNode'], vals: List[int]):
            if not node:
                return
            inorder(node.left, vals)
            vals.append(node.val)
            inorder(node.right, vals)        
        def buildBalancedBST(vals: List[int], left: int, right: int) -> Optional['TreeNode']:
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(vals[mid])
            node.left = buildBalancedBST(vals, left, mid - 1)
            node.right = buildBalancedBST(vals, mid + 1, right)
            return node        
        sorted_vals = []
        inorder(root, sorted_vals)
        
        return buildBalancedBST(sorted_vals, 0, len(sorted_vals) - 1)
