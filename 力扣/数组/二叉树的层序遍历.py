class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 返回层序遍历的逆即可
        res = []
        if root is None:
            return []
        queue = [root] # root 入队
        while queue:
            level = [] # 存储每一层遍历的结果
            for i in range(len(queue)): # 遍历每一层的节点
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res[::-1]