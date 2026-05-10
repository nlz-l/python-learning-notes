"""
案例: 自定义代码, 模拟二叉树.

树结构解释:
    概述:
        它属于数据结构的一种, 属于 非线性结构(N个前驱, N个后继)
    特点:
        1.机器学习概述. 有且只能有1个根节点.
        2. 每个节点都可以有1个父节点 及 任意个子节点, 根节点除外(没有父节点).
        3. 没有子节点的节点, 称之为: 叶子节点.
    常用分类:
        无序树:
        有序树:
        二叉树:
            完全二叉树: 最后一层不满, 其它都是满的.
            满二叉树: 都是满的.
            非完全二叉树: 中间有断的.
            平衡二叉树: 任意节点的两个子树的高度差不超过1

        我们用的最多的就是: 二叉树
    存储:
        顺序存储: 既要存储数据, 又要存储节点的关系.
        链式存储: 采用节点(item, lchild, rchild)的方式, 形成链表来存储

抽取方法的快捷键: ctrl + alt + M
"""


class Node:
    def __init__(self,item):
        self.item = item
        self.lchild = None
        self.rchild = None

class BinaryTree:
    def __init__(self,node =  None):
        self.root = node

    def add(self,item):
        new_code = Node(item)
        if self.root is None:
            self.root = new_code
            return
        queue = []
        queue.append(self.root)
        while True:
            node = queue.pop(0)
            if node.lchild is None:
                node.lchild = new_code
                return
            else:
                queue.append(node.lchild)
            if node.rchild is None:
                node.rchild = new_code
                return
            else:
                queue.append(node.rchild)


    # 广度优先遍历
    def breadth_travel(self):
        if self.root is None:
            return
        queue = [self.root]
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.item,end=" ")
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)
    # 深度优先遍历
    # 前序遍历
    def preorder_travel(self,root):
        if root is not None:
            print(root.item,end=" ")
            self.preorder_travel(root.lchild)
            self.preorder_travel(root.rchild)

    # 中序遍历
    def inorder_travel(self,root):
         if root is not None:
            self.inorder_travel(root.lchild)
            print(root.item,end=" ")
            self.inorder_travel(root.rchild)
    # 后序遍历
    def postorder_travel(self,root):
        if root is not None:
            self.postorder_travel(root.lchild)
            self.postorder_travel(root.rchild)
            print(root.item,end=" ")


def dm01():
    node1 = Node("A")
    print(f'元素域:{node1.item}')
    print(f'左子树:{node1.lchild}')
    print(f'右子树:{node1.rchild}')
    print('-' * 23)
    bt = BinaryTree(node1)
    print(f'根节点:{bt.root.item}')

def dm02():
    queue = []
    queue.append("A")
    queue.append("B")
    queue.append("C")
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue)
    print('-' * 23)

def dm03():
    bt = BinaryTree()
    bt.add("A")
    bt.add("B")
    bt.add("C")
    bt.add("D")
    bt.add("E")
    bt.add("F")
    bt.add("G")
    bt.add("H")
    bt.add("I")
    bt.add("J")
    bt.breadth_travel()

def dm04():
    bt = BinaryTree()
    bt.add(0)
    bt.add(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.add(5)
    bt.add(6)
    bt.add(7)
    bt.add(8)
    bt.add(9)
    print("先序:", end=" ")
    bt.preorder_travel(bt.root)
    print("")
    print("中序:", end=" ")
    bt.inorder_travel(bt.root)
    print("")
    print("后序:", end=" ")
    bt.postorder_travel(bt.root)
    print("")
if __name__ == '__main__':
    # dm01()
    # dm02()
    # dm03()
    dm04()


