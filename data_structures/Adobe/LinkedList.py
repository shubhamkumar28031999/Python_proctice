class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    def returnhead(self):
        return self.head
    def insert_at_end(self, val):
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        node = Node(val)
        curr_node.next = node

    def insert_at_begning(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node

    def printlinkedList(self):
        curr_ele = self.head
        while curr_ele.next is not None:
            print(curr_ele.data, end="-->")
            curr_ele = curr_ele.next
        print(curr_ele.data)

    def middleElement(self):
        if self.head is None:
            return None
        curr_ele=self.head
        midElement=self.head
        while curr_ele is not None:
            curr_ele=curr_ele.next
            if curr_ele is not None:
                curr_ele=curr_ele.next
                midElement=midElement.next
            else:
                break
        return midElement.data

    # def addTwoNumbers(self, l1, l2):
    #     if l1 is None or l2 is None:
    #         return l1 if l1 is not None else l2
    #     head = l1
    #     carry = 0
    #     while l1.next is not None and l2.next is not None:
    #         s = l1.val + l2.val + carry
    #         l1.val = int(s % 10)
    #         carry = s // 10
    #         l1 = l1.next
    #         l2 = l2.next
    #     if l1.next is not None:
    #         while l1 is not None:
    #             s = l1.val + carry
    #             l1.val = int(s % 10)
    #             carry = s // 10
    #             l1 = l1.next
    #     if l2 is not None:
    #         l1.next = l2.next
    #         while l2 is not None:
    #             s = l2.val + carry
    #             l2.val = int(s % 10)
    #             carry = s // 10
    #             l2 = l2.next
    #     if carry > 0:
    #         new_node = Node(carry)
    #         l1.next = new_node
    #     return head

def printlinked(node):
    curr_ele = node
    while curr_ele.next is not None:
        print(curr_ele.data, end="-->")
        curr_ele = curr_ele.next
    print(curr_ele.data)

def addTwoNumbers(l1, l2):
    if l1 is None and l2 is None:
        return None
    elif l1 is None:
        return l2
    elif l2 is None:
        return l1
    head = l1
    carry = 0
    prev_l1=0
    prev_l2=0
    while l1 is not None and l2 is not None:
        s = l1.data + l2.data + carry
        l1.val = int(s % 10)
        carry = s // 10
        prev_l1=l1
        prev_l2=l2
        l1 = l1.next
        l2 = l2.next
    temp_pointer = 0
    if l1 is not None:
        while l1 is not None:
            s = l1.data + carry
            l1.data = int(s % 10)
            carry = s // 10
            temp_pointer = l1
            l1 = l1.next
    if l2 is not None:
        prev_l1.next = l2
        while l2 is not None:
            s = l2.data + carry
            l2.data = int(s % 10)
            carry = s // 10
            temp_pointer = l2
            l2 = l2.next

    if carry>0:
        new_node=Node(carry)
        temp_pointer.next=new_node
    return head



if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert_at_begning(9)
    l1.insert_at_begning(9)
    l1.insert_at_end(9)
    l1.insert_at_end(9)
    # l1.printlinkedList()
    l1_head = l1.returnhead()
    l2 = LinkedList()
    l2.insert_at_begning(9)
    l2.insert_at_end(9)
    l2.insert_at_end(9)
    l2.insert_at_end(9)
    l2.insert_at_end(9)
    l2.insert_at_end(9)
    l2.insert_at_end(9)
    l2_head = l2.returnhead()
    # l2.printlinkedList()

    # l1.printlinkedList()
    # l2.printlinkedList()
    printlinked(l1_head)
    printlinked(l2_head)
    printlinked(addTwoNumbers(l1_head,l2_head))
