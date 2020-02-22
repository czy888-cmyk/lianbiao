# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prenode = ListNode(0)
        #初始化链表
        lastnode = prenode
        val = 0
        while val or l1 or l2:
            #当其中任何一个非空即开始循环
            val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            #divmod()函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组
            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prenode.next

#根据输入的列表创建链表
def generateList(l):
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        #将输入list中的每个元素变成一个链表结构
        lastnode = lastnode.next
    return prenode.next
    #返回需要的链表，扔掉编码开始的prenode


def printList(l: ListNode):
    while l:
        print(l.val, end='')
        #按照链表顺序输出value
        l = l.next
    print('')
    #换行


if __name__ == '__main__':
    l1 = generateList([1, 5, 8])
    l2 = generateList([9, 1, 2, 9])
    printList(l1)
    printList(l2)
    s = Solution()
    sum = s.addTwoNumbers(l1, l2)
    printList(sum)

