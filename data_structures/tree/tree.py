from collections import deque
import sys
d= sys.maxsize
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearchTree(data)

    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inOrderTraversal()

        return elements


    def search(self, val):

        if self.data == val:
            return True
        if self.data > val:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if self.data < val:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def findMin(self):
        if self.left is None:
            return self.data
        return self.left.findMin()

    def findMax(self):
        if self.right is None:
            return self.data
        return self.right.findMax()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_value = self.right.findMin()
            self.data = min_value
            self.right = self.right.delete(min_value)
        return self

    def levelOrderTraversal(self):
        elements = []
        if self.data is None:
            return
        else:
            queue = deque()
            queue.appendleft(self)
            while len(queue) > 0:
                count = len(queue)
                a=[]
                while count > 0:
                    node = queue.pop()
                    elements.append(node.data)
                    a.append(node.data)
                    if node.left:
                        queue.appendleft(node.left)
                    if node.right:
                        queue.appendleft(node.right)
                    count -= 1
                print(a)
        return elements



    def verticalOrderTraversal(self):
        elements = []
        if self.data is None:
            return
        else:
            dict = {}
            node_Dictionary = {}
            queue = deque()
            queue.appendleft(self)
            node_Dictionary[self.data] = 0

            while len(queue) > 0:
                temp = []
                node = queue.pop()
                if node is not None:
                    level = node_Dictionary[node.data]
                    if level in dict:
                        temp = dict.get(level)
                        temp.append(node.data)
                    else:
                        temp.append(node.data)
                        dict[level] = temp
                    if node.left is not None:
                        left_node = node.left
                        queue.appendleft(left_node)
                        node_Dictionary[left_node.data] = node_Dictionary[node.data] - 1
                    if node.right is not None:
                        right_node = node.right
                        queue.appendleft(right_node)
                        node_Dictionary[right_node.data] = node_Dictionary[node.data] + 1

            for val in sorted(dict.items()):
                elements.extend(val[1])
            print(f"vetical order traversal is {elements}")


    def topViewTraversal(self):
        elements = []
        if self.data is None:
            return
        else:
            dict = {}
            node_Dictionary = {}
            queue = deque()
            queue.appendleft(self)
            node_Dictionary[self.data] = 0

            while len(queue) > 0:
                temp = []
                node = queue.pop()
                if node is not None:
                    level = node_Dictionary[node.data]
                    if level in dict:
                        temp = dict.get(level)
                        temp.append(node.data)
                    else:
                        temp.append(node.data)
                        dict[level] = temp
                    if node.left is not None:
                        left_node = node.left
                        queue.appendleft(left_node)
                        node_Dictionary[left_node.data] = node_Dictionary[node.data] - 1
                    if node.right is not None:
                        right_node = node.right
                        queue.appendleft(right_node)
                        node_Dictionary[right_node.data] = node_Dictionary[node.data] + 1
            for val in sorted(dict.items()):
                elements.append(val[1][0])
            print(f"top view traversal is {elements}")



    def bottomview(self):
        elements = []
        if self.data is None:
            return
        else:
            dict = {}
            node_Dictionary = {}
            queue = deque()
            queue.appendleft(self)
            node_Dictionary[self.data] = 0

            while len(queue) > 0:
                temp = []
                node = queue.pop()
                if node is not None:
                    level = node_Dictionary[node.data]
                    if level in dict:
                        temp = dict.get(level)
                        temp.append(node.data)
                    else:
                        temp.append(node.data)
                        dict[level] = temp
                    if node.left is not None:
                        left_node = node.left
                        queue.appendleft(left_node)
                        node_Dictionary[left_node.data] = node_Dictionary[node.data] - 1
                    if node.right is not None:
                        right_node = node.right
                        queue.appendleft(right_node)
                        node_Dictionary[right_node.data] = node_Dictionary[node.data] + 1
            print(sorted(dict.items()))
            for val in sorted(dict.items()):
                elements.append(val[1][-1])
            for val in elements:
                print(val,end=" ")



    def RightView(self):
        val=[]
        if self.data is None:
            return
        else:
            queue = deque()
            queue.appendleft(self)
            while len(queue) > 0:
                count = len(queue)
                elements = []
                while count > 0:
                    node = queue.pop()
                    elements.append(node.data)
                    if node.left:
                        queue.appendleft(node.left)
                    if node.right:
                        queue.appendleft(node.right)
                    count -= 1
                val.append(elements[-1])
        return val

    def height_of_binary_tree(self):
        global left_height, right_height
        if self is None:
            return 0
        else:
            if self.left:
                left_height= self.left.height_of_binary_tree() + 1
            if self.right:
                right_height= self.right.height_of_binary_tree() + 1
            return max(left_height,right_height)



    def levelorder_inline(self):

        if self is None:
            return
        else:
            queue = deque()

            queue.appendleft(self)
            while len(queue) > 0:
                count = len(queue)
                element = []
                while count > 0:
                    node = queue.pop()
                    element.append(node.data)
                    if node.left:
                        queue.appendleft(node.left)
                    if node.right:
                        queue.appendleft(node.right)
                    count -= 1
                # print(element)
                for val in element:
                    print(val, end=" ")
                print("$", end=" ")
            print()


    def printSpiral(self):
        if self is None:
            return
        else:
            ele = []
            queue = deque()
            queue.appendleft(self)
            rev = 0
            while len(queue) > 0:
                count = 0
                l1 = []
                while count > 0:
                    node = queue.pop()
                    l1.append(node.data)
                    if node.left:
                        queue.appendleft(node.left)
                    if node.right:
                        queue.appendleft(node.right)
                    count -= 1
                if rev % 2 == 0:
                    ele.append(l1[::-1])
                else:
                    ele.append(l1)
                count += 1
            for i in range(len(ele)):
                for j in range(len(ele[i])):
                    print(ele[i][j], end=" ")

    def nodes_to_added(self,height,length):
        avl_nodes=2**height-1
        return  avl_nodes-length

    def getMaxSum(self):
        if self is None:
            return
        else:
            level = 0
            s1 = 0
            s2 = 0
            queue = deque()
            queue.append(self)
            while len(queue) > 0:
                co = len(queue)
                while co > 0:
                    node = queue.pop()
                    if level % 2 == 0:
                        s1 += node.data
                    else:
                        s2 += node.data
                    if node.left:
                        queue.appendleft(node.left)
                    if node.right:
                        queue.appendleft(node.right)
                    co -= 1
                level += 1
            return max(s1, s2)

def buildTree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.addChild(elements[i])
    return root

def convert_expression(expression, i):
    l=len(expression)
    if i>=l:
        return None
    root=BinarySearchTree(expression[i])
    i+=1
    if i<l and expression[i]=="?":
        root.left=convert_expression(expression,i+1)
    elif i<l and expression[i]==":":
        root.right=convert_expression(expression,i+1)
    return root

def maxDepth(node):
    if node is None:
        return 0

    else:

        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        # Use the larger one
        if (lDepth > rDepth):
            return lDepth + 1
        else:
            return rDepth + 1

if __name__ == "__main__":
    numbers = [5,4,7,1,0,2,10,9]

    numbreTree = buildTree(numbers)
    print(numbreTree.inOrderTraversal())
    print(numbreTree.getMaxSum())
    # # numbreTree.delete(20)
    # print(numbreTree.inOrderTraversal())
    # print(numbreTree.RightView())
    print(numbreTree.levelOrderTraversal())
    print(numbreTree.verticalOrderTraversal())
    # print(numbreTree.topViewTraversal())
    # print(numbreTree.bottomview())
    # print(numbreTree.search(20))
    # print(numbreTree.levelorder_inline())
    # print(numbreTree.height_of_binary_tree())
    # print(numbreTree.nodes_to_added(numbreTree.))
    # print(numbreTree.printSpiral())
    # print(numbreTree.topViewTraversal())

    # print(maxDepth(numbreTree))
    # print(numbreTree.nodes_to_added(maxDepth(numbreTree),len(numbers)))

# def inOrderTraversal(root):
#     elements=[]
#     if root.left:
#         elements+=inOrderTraversal(root.left)
#     elements.append(root.data)
#     if root.right:
#         elements+=inOrderTraversal(root.right)
#     return elements
#
# def isIdentical(root1, root2):
#     tree1=inOrderTraversal(root1)
#     tree2=inOrderTraversal(root2)
#     if len(tree1)==len(tree2):
#         for i in range(len(tree1)):
#             if tree1[i]==tree2[i]:
#                 pass
#             else:
#                 return False
#     else:
#         return False
#     return True