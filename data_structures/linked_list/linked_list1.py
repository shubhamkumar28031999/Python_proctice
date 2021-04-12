def get_value(head, k):
    count = 0
    while count <= k - 1:
        head = head.next
        count += 1
    return head.data


class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def length(self):
        curr = self.head
        total = 0
        while curr.next != None:
            total += 1
            curr = curr.next
        return total

    def display(self):
        curr_node = self.head
        array = []
        while curr_node.next != None:
            curr_node = curr_node.next
            array.append(curr_node.data)
        print(array)

    def get(self, index):
        if index >= self.length():
            return "out of range"
        else:
            flag = 0
            curr_node = self.head
            while index != flag:
                curr_node = curr_node.next
                flag += 1
            return curr_node.data

    def erase(self, index):
        if index >= self.length():
            print("out of range")
            return None
        else:
            curr_node = self.head
            flag = 0
            while True:
                last_node = curr_node
                curr_node = curr_node.next
                if flag == index:
                    last_node.next = curr_node.next
                    return
                flag += 1

    def insert_at_begning(self, data):
        new_node = node(data)
        curr_node = self.head
        new_node.next = curr_node.next
        curr_node.next = new_node

    def insert_at_end(self, data):
        new_node = node(data)
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def insert_at_position(self, data, index):
        if index >= self.length() + 1:
            return "out of range"
        else:
            new_node = node(data)
            flag = 0
            curr_node = self.head
            while True:
                flag += 1
                last_node = curr_node
                curr_node = curr_node.next
                if index == flag:
                    last_node.next = new_node
                    new_node.next = curr_node
                    break

    def get_value(self, index):
        curr = self.head
        count = 0
        while count <= index:
            curr = curr.next
            count += 1
        print(curr.data)

    def reverse(self):
        curr = self.head
        prev = None
        while curr.next != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        self.head = prev

    def rotateList(self, k):
        temp = self.head
        curr_node = self.head
        count = 1
        while count <= k-1:
            curr_node = curr_node.next
            count += 1
        self.head = curr_node.next
        break_node= curr_node
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = temp
        break_node.next=None

    # def groupRotate(self, k):
    #     curr = self.head
    #     while curr.next!=None:
    #         count=0
    #         while

list = linked_list()
list.append(10)
list.append(20)
list.append(40)
list.append(50)
list.insert_at_begning(200)
list.insert_at_begning(300)
list.insert_at_begning(100)
list.insert_at_end(400)
# print(f"value at index 10 :{list.get(10)}")
# print(list.length())
list.display()

# list.insert_at_position(1000,3)
# list.display()
# print(get_value(list.head,2))
# list.reverse()
# list.display()
# list.rotateList(4)
list.display()