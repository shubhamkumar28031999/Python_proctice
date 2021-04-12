from itertools import combinations
from collections import  deque
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None


    def insert_at_begning(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node

    def print_linked_list(self):
        if self.head is None:
            print("Linked list is Empty")
        curr_node=self.head
        while curr_node is not None:
            print(curr_node.data,end='==>')
            curr_node=curr_node.next
        print()

    def insert_at_end(self,val):
        curr_node=self.head
        while curr_node.next is not None:
            curr_node=curr_node.next
        node=Node(val)
        node.next=curr_node.next
        curr_node.next=node


    def insert_array(self,arr):
        for val in arr:
            self.insert_at_end(val)

    def length(self):
        count=0
        curr_node=self.head
        while curr_node is not None:
            count+=1
            curr_node=curr_node.next
        return count
    def value_at_index(self,index):
        index-=1
        if index>self.length()-1:
            print("invalid index")
        else:
            curr=self.head
            while index!=0:
                curr=curr.next
                index-=1
            print(curr.data)
    def erase(self,index):
        index-=1
        if index>self.length()-1:
            print("invalid")
        else:
            curr=self.head
            while index-1!=0:
                curr=curr.next
                index-=1
            curr.next=curr.next.next

    def insert_at_position(self,data,index):
        index -= 1
        if index > self.length():
            print("invalid")
        else:
            curr=self.head
            while index-1!=0:
                curr=curr.next
                index-=1
            node=Node(data)
            node.next=curr.next
            curr.next=node
    def get_val(self,index):
        index-=1
        if index>self.length()-1:
            print("invalid index")
        else:
            curr_node=self.head
            while index !=0:
                curr_node=curr_node.next
                index-=1
            print(curr_node.data)

    def reverseIterative(self):
        curr = self.head
        prev = None
        while curr.next != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        curr.next = prev
        self.head = curr

    def reverse_Recursive(self):
        curr_node=self.head
        if curr_node is None or curr_node.next is None:
            return self.head
        node1=curr_node.next.reverse_Recursive()
        curr_node.next.next=curr_node
        curr_node.next=None
        return node1

    def count_repeted_val(self):
        count=0
        curr_node=self.head
        next_node=curr_node.next
        while next_node.next is not None:
            if curr_node.data == next_node.data:
                count+=1
            curr_node=next_node
            next_node=next_node.next
        print(count)

    def remove_repeted_val_sorted(self):
        prev_node=self.head
        curr_node=prev_node.next
        while curr_node.next is not None:
            if prev_node.data == curr_node.data:
                prev_node.next=curr_node.next
            prev_node=curr_node
            curr_node=curr_node.next
    def remove_repeted_val_unsorted(self):
        arr=[]
        prev_node=self.head
        curr_node=prev_node
        arr.append(prev_node.data)
        while curr_node.next is not None:
            if curr_node.data in arr:
                prev_node.next=curr_node.next
            prev_node=curr_node
            arr.append(prev_node.data)
            curr_node=curr_node.next





    def detect_loop(self):
        arr=[]
        flag=1
        curr=self.head
        while curr.next is not None:
            if curr.next in arr:
                flag=0
                break
            curr=curr.next
        if flag==0:
            print("loop detected")
        else:
            print("No loop detected")

    def move_last_element_in_front(self):
        prev=self.head

        curr_node=prev.next
        while curr_node.next is not None:
            prev=curr_node
            curr_node=curr_node.next
        prev.next=None
        curr_node.next=self.head
        self.head=curr_node


    def reverse_group_util(self,head,k):
        curr = head
        prev = None
        next=None
        count=0
        while curr != None and count<k:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            count+=1
        if next is not None:
            head.next=self.reverse_group_util(next,k)
        return prev

    def reverse_group(self,k):
        self.reverse_group_util(self.head,k)

    def solve(self,k):
        curr=self.head
        while curr is not None:
            curr.data=(curr.data//k)*k
            curr=curr.next


if __name__=="__main__":
    ll=LinkedList()
    ll.insert_at_begning(1)
    # ll.insert_at_begning(10)
    ll.insert_array([2,3,4,5])
    ll.solve(2)
    ll.print_linked_list()
    # ll.insert_at_position(5,3)
    # ll.erase(6)
    # ll.reverse_group(3)
    # ll.remove_repeted_val()
    # ll.move_last_element_in_front()
    # ll.print_linked_list()
    # ll.count_repeted_val()
    # print(ll.length())
    # ll.value_at_index(2)
    # ll.get_val(3)



