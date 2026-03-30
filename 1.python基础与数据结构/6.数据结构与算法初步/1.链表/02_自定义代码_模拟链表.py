"""
案例: 自定义代码模拟链表

链表介绍:
    概述:
        它属于数据结构之 线性结构的一种, 每个节点都只能有 1个前驱 和 1个后继节点.
    作用:
        用于优化顺序表的弊端(如果没有足够的连续的内存空间, 会导致扩容失败)
        链表扩容时, 有地儿就行, 连不连续无所谓.
    组成:
        由 节点 组成, 其中节点由 元素域(数值域) 和 链接域(地址域)组成.
    分类:
        根据 节点类型不同, 链表主要分为:
        单向链表: 节点由1个数值域 和 1个地址域组成, 前边节点的地址域存储的是后续节点的地址, 最后1个节点的地址域为 None
        单向循环链表:
        双向链表:
        双向循环链表:
        详见今日随堂图片.

自定义代码模拟链表, 思路分析:
    1. 自定义SingleNode类, 表示 节点类.
        属性:
            item   数值域(元素域)
            next   地址域(链接域)

    2. 自定义SingleLinkedList类, 表示: 链表
        属性:
            head  表示头结点, 指向第1个节点.
        行为:
            is_empty(self) 链表是否为空
            length(self) 链表长度
            travel(self. ) 遍历整个链表
            add(self, item) 链表头部添加元素
            append(self, item) 链表尾部添加元素
            insert(self, pos, item) 指定位置添加元素
            remove(self, item) 删除节点
            search(self, item) 查找节点是否存在

    3. 测试.
"""
from idlelib.debugobj import myrepr
from itertools import count


class SingleNode:
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleLinkedList:
    def __init__(self,node=None):
        self.head = node

    # is_empty(self)链表是否为空
    def is_empty(self):
        #1. 写法一
        # if self.head is None:
        #     return True
        # else:
        #     return False

        # 2. 写法二
        # return True if self.head is None else False
        # 3. 写法三
        return self.head is None


    # length(self)链表长度
    def length(self):
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur =cur.next
        return count
    # travel(self.)遍历整个链表
    def travel(self):
        cur = self.head
        while cur is not None:
            print(f'元素域:{cur.item}')
            cur = cur.next

    # add(self, item)链表头部添加元素
    def add(self, item):
        new_node = SingleNode(item)
        new_node.next = self.head
        self.head = new_node

    # append(self, item)链表尾部添加元素
    def append(self, item):
        new_node = SingleNode(item)
        if self.is_empty():
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur =cur.next
            cur.next = new_node

    # insert(self, pos, item)指定位置添加元素
    def insert(self, pos, item):

        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            cur = self.head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            new_node = SingleNode(item)
            new_node.next = cur.next
            cur.next = new_node

    # remove(self, item)删除节点
    def remove(self, item):
        cur = self.head
        pre = None
        while cur is not None:
            if cur.item == item:
                if cur == self.head:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                    cur.next = None
                return
            else:
                pre = cur
                cur = cur.next

    # search(self, item)查找节点是否存在
    def search(self, item):
        cur = self.head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                cur =cur.next
        return False




if __name__ == '__main__':
    # node1 = SingleNode(10)
    # print(f'元素域:{node1.item}')
    # print(f'地址域:{node1.next}')
    # print(f'node的类型:{type(node1)}')
    # print(f'node1对象:{node1}')  #地址值
    # print('-' * 23)
    #
    # my_linkedlist = SingleLinkedList(node1)
    # print(f'头节点为:{my_linkedlist.head}')
    # print(f'头节点的元素域:{my_linkedlist.head.item}')
    # print(f'头节点的地址域:{my_linkedlist.head.next}')

    node1 = SingleNode("大哥")
    my_linkedlist = SingleLinkedList(node1)         # 设置 创建头节点 并创建链表
    #my_linkedlist = SingleLinkedList()

    my_linkedlist.add("二弟")
    my_linkedlist.add("三弟")
    my_linkedlist.append("四弟")
    my_linkedlist.append("五弟")
    my_linkedlist.insert(2, "六弟")
    my_linkedlist.insert(0, "七弟")
    my_linkedlist.remove("大哥")


    #print(f'头节点:{my_linkedlist.head}')
    #print(f'头节点元素域:{my_linkedlist.head.item}')
    print('-' * 23)
    print(f'链表是否为空:{my_linkedlist.is_empty()}')

    print(f'链表长度:{my_linkedlist.length()}')
    my_linkedlist.travel()
    print(my_linkedlist.search("六弟"))
    print(my_linkedlist.search("大哥"))

