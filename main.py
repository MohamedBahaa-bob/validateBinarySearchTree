# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def validate(node, left, right):
    if not node:
        return True
    if node.val <= left or node.val >= right:
        return False
    return validate(node.left, left, node.val) and validate(node.right, node.val, right)


class Solution:
    def isValidBST(self, root) -> bool:
        return validate(root, float("-inf"), float("inf"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # obj = Solution()
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
