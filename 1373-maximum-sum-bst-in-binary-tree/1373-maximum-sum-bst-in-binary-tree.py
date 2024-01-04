# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxsum = 0
        def dfs(node):
            if not node.left and not node.right:
                self.maxsum = max(self.maxsum, node.val)
                return node.val, True, node.val, node.val
            left_sum, right_sum = 0,0
            left_valid, right_valid = True, True
            current_min = node.val
            current_max = node.val
            if node.left:
                left_sum, left_valid, left_min, left_max = dfs(node.left)
                if left_max >= node.val:
                    left_valid = False
                current_max = max(current_max, left_max)
                current_min = min(current_min, left_min)
            if node.right:
                right_sum, right_valid, right_min, right_max = dfs(node.right)
                if right_min <= node.val:
                    right_valid = False
                current_max = max(current_max, right_max)
                current_min = min(current_min, right_min)
            curr_node_valid = left_valid and right_valid
            current_sum = left_sum + right_sum + node.val
            if curr_node_valid:
                self.maxsum = max(self.maxsum, current_sum)
            return current_sum, curr_node_valid, current_min, current_max
    
        dfs(root)
        return self.maxsum