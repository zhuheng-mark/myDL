from typing import List
from common import gen_root,TreeNode
from collections import defaultdict, deque
class Solution:
    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        # dfs:深度优先搜索
        result = defaultdict(list)
        # 递归解法，将每层的值放入result中
        def dfs(node, n):
            if node is None:
                return
            # val值可能为0，所以不能用if node.val来判断
            if node.val is not None :
                result[n].append(node.val)
            if node.left is not None:
                dfs(node.left, n + 1)
            if node.right is not None:
                dfs(node.right, n + 1)
        dfs(root, 0)
        return list(result.values())

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # nfs: 广度优先搜索
        result = []
        def nfs(queue):
            while(queue):
                level = []
                # 计算该层节点数目，将下层节点入栈
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node is not None:
                        level.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                if level:
                    result.append(level)
        # 使用双端队列左边遍历上一层节点，右边入栈下一层节点
        nfs(deque([root]))
        return result


s = Solution()
root = gen_root()
print(s.levelOrder(root))
                        
