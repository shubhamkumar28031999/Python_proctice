from collections import deque
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return
        else:
            if self.data > data:
                if self.left:
                    self.left.add_child(data)
                else:
                    self.left = Tree(data)
            if self.data < data:
                if self.right:
                    self.right.add_child(data)
                else:
                    self.right = Tree(data)

    def InOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.InOrderTraversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.InOrderTraversal()
        return elements

    def PostOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.InOrderTraversal()
        if self.right:
            elements += self.right.InOrderTraversal()
        elements.append(self.data)
        return elements

    def PreOrderTraversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.InOrderTraversal()
        if self.right:
            elements += self.right.InOrderTraversal()
        return elements


    def PreOrderTraversalItervative(self):
        if self is None:
            return
        elements = []
        stack = deque()
        stack.append(self)
        while len(stack) > 0:
            node = stack.pop()
            elements.append(node.data)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return elements

    def search(self, data):
        if self.data == data:
            return True
        else:
            if self.data > data:
                if self.left:
                    return self.left.search(data)
                else:
                    return False
            if self.data < data:
                if self.right:
                    return self.right.search(data)
                else:
                    return False

    def min(self):
        if self.left == None:
            return self.data
        else:
            self.left.min()

    def delete_node(self, data):
        if self.data > data:
            if self.left:
                self.left = self.left.delete_node(data)
        elif self.data < data:
            if self.right:
                self.right = self.right.delete_node(data)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            min_val = self.right.min()
            self.data = min_val
            self.right = self.right.delete_node(min_val)
        return self

    def LevelOrderTraversal(self):
        elements = []
        if self is None:
            return
        else:
            queue = deque()
            queue.append(self)
            while len(queue) > 0:
                count = len(queue)
                a = []
                while count > 0:
                    node = queue.pop()
                    elements.append(node.data)
                    a.append(node.data)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append((node.right))
                    count -= 1
                print(a)
        return elements


def buildTree(elements):
    root = Tree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


def inoreder(root):
    if root:
        inoreder(root.left)
        print(root.data, end=" ")
        inoreder(root.right)


def preoreder(root):
    if root:
        print(root.data, end=" "),
        preoreder(root.left)
        preoreder(root.right)


def postoreder(root):
    if root:
        postoreder(root.left)
        postoreder(root.right)
        print(root.data, end=" "),


def inorderIter(root):
    stack = deque()
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.data, end=" ")
            curr = curr.right


def preorderIter(root):
    if root is None:
        return
    stack = deque()
    stack.append(root)
    while stack:
        curr = stack.pop()
        print(curr.data, end=" ")
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

def zigzagLevelOrder(root):
    flag = 1
    queue = deque()
    queue.append(root)
    element = []
    if root is None:
        return
    while queue:
        count = len(queue)
        arr = []
        while count > 0:
            node = queue.pop()
            if flag % 2 == 1:
                arr.append(node.data)
            else:
                arr.insert(0, node.data)
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
            count -= 1
        flag += 1
        element.append(arr)
    return element

def levelOrder( root):
    levels = []
    def helper(node, level):
        if len(levels) == level:
            levels.append([])
        levels[level].append(node.data)
        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)
    if not root:
        return None
    helper(root, 0)
    return levels

def postorederIter(root):
    stack = deque()
    stack.append(root)
    out = deque()
    while stack:
        curr = stack.pop()
        out.append(curr.data)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    while out:
        print(out.pop(), end=" ")


def vertical_Order_Traversal(root):
    elements = []
    if root is None:
        return
    dict = {}
    node_dict = {}
    queue = deque()
    queue.append(root)
    node_dict[root.data] = 0
    while len(queue) > 0:
        temp = []
        node = queue.pop()
        if node is not None:
            level = node_dict[node.data]
            if level in dict:
                temp = dict.get(level)
                temp.append(node.data)
            else:
                temp.append(node.data)
                dict[level] = temp
            if node.left is not None:
                left_node = node.left
                queue.appendleft(left_node)
                node_dict[left_node.data] = node_dict[node.data] - 1
            # print(node_dict)
            if node.right is not None:
                right_node = node.right
                queue.appendleft(right_node)
                node_dict[right_node.data] = node_dict[node.data] + 1
    print(node_dict)
    print(max(dict.keys()) - min(dict.keys()))
    print(dict)

def virticalTra(root):
    if root:
        dict={}
        node_dict={}
        queue= deque()
        queue.append(root)
        node_dict[root.data]=0
        while queue:
            node=queue.pop()
            if node:
                level=node_dict.get(node.data)
                if level in dict:
                    dict.get(level).append(node.data)
                else:
                    dict[level]=[node.data]
                if node.left:
                    left_node=node.left
                    queue.appendleft(left_node)
                    node_dict[left_node.data]=node_dict[node.data]-1
                if node.right:
                    right_node=node.right
                    queue.appendleft(right_node)
                    node_dict[right_node.data]=node_dict[node.data]+1
        print(dict)


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameter(root):
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    ldia = diameter(root.left)
    rdia = diameter(root.right)
    return max(1 + lheight + rheight, max(ldia, rdia))


def fillMap(root, d, l, m):
    if (root == None):
        return

    if d not in m:
        m[d] = [root.data, l]
    elif (m[d][1] > l):
        m[d] = [root.data, l]
    fillMap(root.left, d - 1, l + 1, m)
    fillMap(root.right, d + 1, l + 1, m)


def topView(root):
    m = {}

    fillMap(root, 0, 0, m)
    print(m)
    for it in sorted(m.keys()):
        print(m[it][0], end=" ")


def diagonalview(root):
    if root is None:
        return
    dic = dict()
    node_dict = dict()
    queue = deque()
    queue.append(root)
    node_dict[root.data] = 0
    while len(queue) > 0:
        temp = []
        node = queue.pop()
        if node is not None:
            level = node_dict[node.data]
            if level in dic:
                temp = dic.get(level)
                temp.append(node.data)
            else:
                temp.append(node.data)
                dic[level] = temp
            if node.left is not None:
                left_node = node.left
                queue.appendleft(left_node)
                node_dict[left_node.data] = node_dict[node.data] - 1
            if node.right is not None:
                right_node = node.right
                queue.appendleft(right_node)
                node_dict[right_node.data] = node_dict[node.data]
    for val in sorted(dic.keys()):
        print(f"{val}={dic[val]}")


def printLeftNodeExceptLast(root):
    if root is None:
        return
    elif root.left is None and root.right is None:
        return
    else:
        print(root.data, end=" ")
        printLeftNodeExceptLast(root.left)


def leefNone(node):
    elements=[]
    def helper(root):
        if root is None:
            return
        elif root.left is None and root.right is None:
            elements.append(root.data)
        else:
            helper(root.left)
            helper(root.right)
    helper(node)
    print(elements)


def printrightNodeExceptLast(root):
    if root is None:
        return
    elif root.left is None and root.right is None:
        return
    else:
        printLeftNodeExceptLast(root.right)
        print(root.data, end=" ")


def boundryTraversal(root):
    printLeftNodeExceptLast(root)
    leefNone(root)
    printrightNodeExceptLast(root)


def mirror(root):
    if root is None:
        return
    mirror(root.left)
    mirror(root.right)
    root.left, root.right = root.right, root.left


def leefnode(root):
    queue = deque()
    queue.append(root)
    elements = []
    while len(queue) > 0:
        count = len(queue)
        while count > 0:
            node = queue.pop()
            if node.left is None and node.right is None:
                elements.append(node.data)
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
            count -= 1
    print(elements)

def getleefCount(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        return getleefCount(root.left)+getleefCount(root.right)

def InOrderTraversal(root):
    elements=[]
    if root.left:
        elements+=InOrderTraversal(root.left)
    elements.append(root.data)
    if root.right:
        elements+=InOrderTraversal(root.right)
    return elements


def minswap(root):
    elements=InOrderTraversal(root)
    count=0
    for i in range(len(elements)):
        for j in range(-1,-len(elements)+i):
            if elements[i]>elements[j]:
                elements[i],elements[j]=elements[j],elements[i]
                count+=1
    return count


# def dublicateSubString(root):


if __name__ == "__main__":
    arr = [5, 3, 4, 1, 2, 8, 7, 10,0,-1]
    node = buildTree(arr)
    # print(node.InOrderTraversal())
    # print(node.PreOrderTraversal())
    # print(node.PreOrderTraversalItervative())
    # preoreder(node)
    # print()
    # inorderIter(node)
    # print()
    # preorderIter(node)
    # print()
    # vertical_Order_Traversal(node)
    # print(topView(node))
    # diagonalview(node)
    # mirror(node)
    # print()
    # leefnode(node)
    # print(getleefCount(node))
    # print(levelOrder(node))
    # vertical_Order_Traversal(node)
    # virticalTra(node)
    leefNone(node)
    leefnode(node)
    # print(minswap(node))
    # print(zigzagLevelOrder(node))

