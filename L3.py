class TreeNode:
   def __init__(self, data, left = None, right = None , parent= None):
      self.parent=parent
      self.data = data
      self.left = left
      self.right = right
class BTree:
   def __init__(self):
      self.root=None
   def setroot(self,root):
      self.root=root
   def inorder(self,x):
      if x!=None:
         self.inorder(x.left)
         print(x.data,end=' ')
         self.inorder(x.right)
#saramazaheri
   def postorder(self,x):
      if x!=None:
         self.postorder(x.left)
         self.postorder(x.right)
         print(x.data,end=' ')
   def preorder(self,x):
      if x!=None:
         print(x.data,end=' ')
         self.preorder(x.left)
         self.preorder(x.right)
         #saramazaheri
ex= input("Enter Expression:")
stack=[]
Tree=BTree()
for e in ex:
   if e.isalpha() or (e!='(' and e!=')'):
      New_Node=TreeNode(e)
      stack.append(New_Node)
   if e==')':
      e3=stack.pop()
      e2=stack.pop()
      e1=stack.pop()
      e2.left=e1
      e2.right=e3
      e1.parent=e2
      e3.parent=e2
      Tree.root=e2
      stack.append(e2)
print('InOrder: ',end=' ')
Tree.inorder(Tree.root)
print('\nPreOrder: ',end=' ')
Tree.preorder(Tree.root)
print('\nPostOrder: ',end=' ')
Tree.postorder(Tree.root)





