from collections import deque
class Tree:
    def __init__(self,data):
            self.data=data
            self.left=None
            self.right=None




def add_child(root, data):
    if root.data == None:
        return
    else:
        if root.data > data:
            if root.left:
                add_child(root.left,data)
            else:
                root.left = Tree(data)
        if root.data < data:
            if root.right:
                add_child(root.right,data)
            else:
                root.right = Tree(data)
# ==========================================Inorder  Traversal==========================================================
def InorderTraversal(root):
    elements=[]
    if root:
        if root.left:
            elements+=InorderTraversal(root.left)
        elements.append(root.data)
        if root.right:
            elements+=InorderTraversal(root.right)
        return elements
def InorderTraversal_type_2(root):
    if root:
        InorderTraversal_type_2(root.left)
        print(root.data,end=" ")
        InorderTraversal_type_2(root.right)
def InorderTraversal_Iterative(root):
    elements=[]
    stack=deque()
    curr=root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr=curr.left
        else:
            curr=stack.pop()
            elements.append(curr.data)
            curr=curr.right
    return elements

# =======================================PreOrder Traversal=====================================================

def preOrder_traversal(root):
    if root:
        print(root.data,end=" ")
        preOrder_traversal(root.left)
        preOrder_traversal(root.right)

def preOrderTraversal_2(root):
    elements=[]
    if root:
        elements.append(root.data)
        if root.left:
            elements+=preOrderTraversal_2(root.left)
        if root.right:
            elements+=preOrderTraversal_2(root.right)
    return elements

def preOrderTraversalIterative(root):
    if root:
        elements=[]
        stack=deque()
        stack.append(root)
        while stack:
            curr=stack.pop()
            elements.append(curr.data)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
    return elements

# =======================================PostOrder Traversal=====================================================

def postOrderTraversal(root):
    if root:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.data,end=" ")

def postOrderTraversal_2(root):
    if root:
        elements=[]
        if root.left:
            elements+=preOrderTraversal_2(root.left)
        if root.right:
            elements+=postOrderTraversal_2(root.right)
        elements.append(root.data)
        return elements
def postOrderTraversalIter(root):
    if root:
        stack=deque()
        stack.append(root)
        element=[]
        while stack:
            curr=stack.pop()
            element.append(curr.data)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return element[::-1]


def LevelOrderTraversal(root):
    if root:
        stack=deque()
        elements=[]
        stack.append(root)
        while stack:
            temp_len=len(stack)
            a=[]
            while temp_len>0:
                node=stack.pop()
                a.append(node.data)
                if node.left:
                    stack.appendleft(node.left)
                if node.right:
                    stack.appendleft(node.right)
                temp_len-=1
            print(a)
            elements+=a
        return elements



def verticalOrderTraversal(root):
    if root:
        elements=[]
        queue=deque()
        dict={}
        node_dict={}
        queue.append(root)
        node_dict[root.data]=0
        while queue:
            temp=[]
            node=queue.pop()
            if node:
                level=node_dict[node.data]
                if level in dict:
                    temp=dict.get(level)
                    temp.append(node.data)
                else:
                    temp.append(node.data)




def buildTree(arr):
    Node=Tree(arr[0])
    for val in arr[1:]:
        add_child(Node,val)
    return Node





if __name__ == "__main__":
    arr = [5, 3, 4, 1, 2, 8, 7, 10]
    node = buildTree(arr)
    # print(InorderTraversal(node))
    # InorderTraversal_type_2(node)
    # print()
    # print(InorderTraversal_Iterative(node))
    # preOrder_traversal(node)
    # print()
    # print(preOrderTraversal_2(node))
    # print(preOrderTraversalIterative(node))
    print(postOrderTraversal_2(node))
    postOrderTraversal(node)
    print()
    print(postOrderTraversalIter(node))
    print(LevelOrderTraversal(node))