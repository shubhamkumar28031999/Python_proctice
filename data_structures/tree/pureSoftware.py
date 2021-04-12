from collections import deque
class Tree:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.data=val

    def add_child(self,val):
        if self.data==val:
            return
        else:
            if self.data>val:
                if self.left:
                    self.left.add_child(val)
                else:
                    self.left=Tree(val)
            if self.data<val:
                if self.right:
                    self.right.add_child(val)
                else:
                    self.right=Tree(val)

def InOrderTraversal(node):
    elements=[]
    if node.left:
        elements+=InOrderTraversal(node.left)
    elements.append(node.data)
    if node.right:
        elements+=InOrderTraversal(node.right)
    return elements

def InOrder2(node):
    if node:
        InOrder2(node.left)
        print(node.data,end=" ")
        InOrder2(node.right)
    else:
        return

def InOrderIter(root):
    stack=deque()
    curr=root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr=curr.left
        else:
            node=stack.pop()
            print(node.data,end=" ")
            curr=node.right


def preOrderRec1(node):
    elements=[]
    elements.append(node.data)
    if node.left:
        elements+=preOrderRec1(node.left)
    if node.right:
        elements+=preOrderRec1(node.right)
    return elements

def preOrderRec2(node):
    if node:
        print(node.data,end=" ")
        preOrderRec2(node.left)
        preOrderRec2(node.right)

def preOrderIter(root):
    stack=deque()
    stack.append(root)
    while stack:
        node=stack.pop()
        print(node.data,end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data,end=" ")

def posrOrder(root):
    elements=[]
    if root.left:
        elements+=posrOrder(root.left)
    if root.right:
        elements+=posrOrder(root.right)
    elements.append(root.data)
    return elements

def printBoundaryLeft(root):
    if (root):
        if (root.left):
            print(root.data,end=" ")
            printBoundaryLeft(root.left)

        elif (root.right):
            print(root.data,end=" ")
            printBoundaryLeft(root.right)

def leftView(node):
    if node:
        if node.left:
            print(node.data,end=" ")
            leftView(node.left)
        elif node.right:
            print(node.data,end=" ")
            leftView(node.right)
def rightView(node):
    if node:
        if node.right:
            print(node.data,end=" ")
            leftView(node.right)
        elif node.left:
            print(node.data,end=" ")
            leftView(node.left)
def leefNode(root):
    if root:
        leefNode(root.left)
        if root.left is None and root.right is None:
            print(root.data,end=" ")
        leefNode(root.right)

def BoundryTraversal(root):
    if root:
        print(root.data,end=" ")
        leftView(root.left)
        leefNode(root)
        rightView(root.right)


def levelOrder(root):
    queue=deque()
    queue.append(root)
    elements=[]
    while queue:
        l=len(queue)
        arr=[]
        while l>0:
            node=queue.pop()
            arr.append(node.data)
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
            l-=1
        elements.append(arr)
    return elements

def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left),height(root.right))

def max_diameter(root):
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    ldia = max_diameter(root.left)
    rdia = max_diameter(root.right)
    return max(1 + lheight + rheight, max(ldia, rdia))

def verticalOrederTraversal(root):
    elements=[]
    if root is None:
        return []
    dict={}
    node_dict={}
    queue=deque()
    queue.append(root)
    node_dict[root.data]=0
    while queue:
        temp=[]
        node=queue.pop()
        if node is not None:
            level = node_dict[node.data]
            if level in dict:
                dict[level].append(node.data)

def MakeTree(arr):
    tree=Tree(arr[0])
    for val in arr[1:]:
        tree.add_child(val)
    return tree


if __name__=='__main__':
    arr = [5, 3, 4, 1, 2, 8, 7, 10,0]
    node=MakeTree(arr)
    print(InOrderTraversal(node))
    InOrder2(node)
    print()
    InOrderIter(node)
    print()

    print()
    print(preOrderRec1(node))
    # preOrderRec2(node)
    print()
    # preOrderIter(node)
    printBoundaryLeft(node)
    print()
    leftView(node)
    print()
    leefNode(node)
    print()
    rightView(node)
    print()
    BoundryTraversal(node)
    print()
    print(levelOrder(node))
