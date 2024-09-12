class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def setData(self,data):
        self.data=data

    def getData(self):
        return self.data
    
    def setLeft(self,node):
        self.left=node
    
    def getLeft(self):
        return self.left
    
    def setRight(self,node):
        self.right=node

    def getRight(self):
        return self.right
    
# Pre Order Traversal
def preorder(root):
    #Base condition
    if not root:
        return
    print(root.getData(),end="->")
    #traversal of left-Subtree
    preorder(root.getLeft())
    #traversal of right-Subtree
    preorder(root.getRight())

#Inorder
def Inorder(root):
    if not root:
        return
    Inorder(root.getLeft())
    print(root.getData(),end="->")
    Inorder(root.getRight())

#Postorder
def Postorder(root):
    if not root:
        return
    Postorder(root.getLeft())
    Postorder(root.getRight())
    print(root.getData(),end="->")

#finding maximum element in Tree
def maximum(a,b,c):
  if a>=b :
    if a>=c :
      return a
    else :
      return c
  else :
    if b >=c :
      return b
    else :
      return c
    
def max(root):
    if not root:
        return float('-inf') # represents the num smaller than all other numbers
    max_left=max(root.getLeft())
    max_right=max(root.getRight())
    return maximum(max_left,max_right,root.getData())

#finding minimum element in Tree
def minimum(a,b,c):
  if a<=b:
    if a<=c:
      return a
    else:
      return c
  else:
    if b<=c:
      return b
    else:
      return c

    
def min(root):
  if not root:
    return float('inf')

  min_left = min(root.getLeft())
  min_right = min(root.getRight())
  return minimum(min_left, min_right, root.getData())

# Creating structure of Tree
root=TreeNode(1)

#Left Subtree
leftR=TreeNode(2)
leftR.setLeft(TreeNode(3))
leftR.setRight(TreeNode(4))
root.setLeft(leftR)

#RightSubTree
rightR=TreeNode(5)
rightR.setRight(TreeNode(6))
rightR.setRight(TreeNode(7))
root.setRight(rightR)

print("Pre-order Traversal :")
preorder(root)

print("\nIn-order Traversal :")
Inorder(root)

print("\nPost-order Traversal :")
Postorder(root)

print("\nMaximum Element of Tree is : ",max(root))
print("\nMinimum Element of Tree is : ",min(root))
