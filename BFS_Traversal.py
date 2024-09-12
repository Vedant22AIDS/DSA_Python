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
    
class Node :

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

  def getData(self):
    return self.data

  def setData(self, data):
    self.data = data

  def setNext(self, next):
    self.next = next

  def getNext(self):
    return self.next
  
class QueueLL :
  def __init__(self):
    self.head = None
    self.tail = None
    self.size =0

  def isEmpty(self):
    return self.head == None # self.tail == None

  def enQue(self, data):
    node = Node(data)

    if self.isEmpty():
      self.head = node
      self.tail = node
    else :
      self.tail.setNext(node)
      self.tail = self.tail.getNext()
    self.size +=1

  def deQueue(self):
    if self.isEmpty():
      print("Queue underflow")
      return
    data = self.head.getData()

    #chek if it's the only element
    if(self.head == self.tail):
      self.head = None
      self.tail= None #Becase after deQue, Queue will be empty
    else:
      self.head = self.head.getNext()
    self.size -= 1
    return data

  def traverse(self):
    temp = self.head
    while(temp):
      print(temp.getData(), end="->")
      temp = temp.getNext()
    print()
def levelOrder(root):
  if not root :
    return
  q = QueueLL()
  q.enQue(root)
  while not q.isEmpty():
    #Deque the element from the queue
    temp = q.deQueue()
    print(temp.getData(), end="->")

    if temp.getLeft():
      q.enQue(temp.getLeft())
    if temp.getRight():
      q.enQue(temp.getRight())

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

levelOrder(root)