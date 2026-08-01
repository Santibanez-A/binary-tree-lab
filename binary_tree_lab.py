from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


# Determine the maximum depth of a binary tree.
def max_depth(root: Optional[TreeNode]) -> int:
    # Base case: an empty tree has depth 0.
    if root is None:
        return 0

    # Recursively calculate the depth of each subtree.
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # Return the larger depth plus this node.
    return 1 + max(left_depth, right_depth)


# Find the Lowest Common Ancestor in a Binary Search Tree.
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Base case.
    if root is None:
        return None

    # Both nodes are smaller than the current node.
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)

    # Both nodes are larger than the current node.
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)

    # Otherwise, this node is the split point (the LCA).
    return root