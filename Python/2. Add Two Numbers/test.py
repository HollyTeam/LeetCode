# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = ListNode(None) # 定义结果链表

    temp_node = ListNode(None)

    head = temp_node

    # 进位
    carry_bit = 1
    carry_flag = 0

    # 如果有一方为0，则返回另一个
    if (l1.val == 0) and (not l1.next):
        return l2
    if (l2.val == 0) and (not l2.next):
        return l1

    # while循环，遇到有进位：carry_bit=1  比如5+7=12，则12%10=2放在新链表，然后将carry_bit加在下一次中
    while l1:
        # 判断计算当前val是否需要加上进位 carry_bit
        if carry_flag == 1:
            temp_node.val = l1.val + l2.val + carry_bit
        elif carry_flag == 0:
            temp_node.val = l1.val + l2.val
        # 判断是否需要进位，大于等于10则需要进位
        if temp_node.val >= 10:
            temp_node.val = temp_node.val % 10
            carry_flag = 1
        else:
            carry_flag = 0
        # print("temp_node.val:  ",temp_node.val)

        # 将l1和l2移动到下一个
        l1 = l1.next
        l2 = l2.next

        # 只要二者有一个不为空，就需要下一个结点
        if l1 or l2:
            temp_node.next = ListNode(None)
            temp_node = temp_node.next

        # 如果l2已经结束了
        if not l2 :
            break

    # l1比l2长，当l1还有的时候
    while l1:
        if carry_flag == 1:
            temp_node.val = l1.val + carry_bit
        elif carry_flag == 0:
            temp_node.val = l1.val

        if temp_node.val >= 10:
            temp_node.val %=  10
            carry_flag = 1
        else:
            carry_flag = 0

        l1 = l1.next
        if l1:
            temp_node.next = ListNode(None)
            temp_node = temp_node.next

    # l2比l1长，当l2还有的时候
    while l2:
        if carry_flag == 1:
            temp_node.val = l2.val + carry_bit
        elif carry_flag == 0:
            temp_node.val = l2.val

        if temp_node.val >= 10:
            temp_node.val %=  10
            carry_flag = 1
        else:
            carry_flag = 0

        l2 = l2.next
        if l2:
            temp_node.next = ListNode(None)
            temp_node = temp_node.next

    # 最后还要判断一下是否需要多一个进位  比如4->5->6, 2->5->7   结果为 6->0->4->1
    if carry_flag == 1:
        temp_node.next = ListNode(1)
        temp_node = temp_node.next

    return head


# [0,8,6,5,6,8,3,5,7]
# [6,7,8,0,8,5,8,9,7]

def create_link_list(list_arr):
    head = ListNode(None)
    l = ListNode(None)
    head = l
    for i in range(len(list_arr)):
        l.val = list_arr[i]
        if i == len(list_arr)-1:
            l.next = None
        else:
            l.next = ListNode(None)
            l = l.next

    return head


l1 = create_link_list([0,8,6,5,6,8,3,5,7])

l2 = create_link_list([6,7,8,0,8,5,8,9,7])


head = addTwoNumbers(l1, l2)

while head:
    print(head.val,end="")
    head = head.next
    if head:
        print("->",end="")

