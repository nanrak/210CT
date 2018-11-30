'''
   Task 1 - 1
   ------------------
   Implement in the language of your choice a function that deletes a node in a Binary Search Tree.
   Integrate this function in the code provided to you on Moodle.
   The deletion operation should be performed based on the key (value) of the node.
   It is up to you how you print the binary search tree - you can just use a traversal method such as in-order or you can create a fancier, more visual representation. 
'''

class BinTreeNode(object):

    def __init__(self, value):
           self.value=value
           self.left=None
           self.right=None

def tree_insert(tree, item):
    if tree==None:
         tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def tree_delete(tree, item): 
    if item < tree.value: 
        tree.left = tree_delete(tree.left, item) 
    elif(item > tree.value): 
        tree.right = tree_delete(tree.right, item) 
    else:  
        if tree.left is None : 
            temp = tree.right  
            tree = None 
            return temp
        elif tree.right is None : 
            temp = tree.left  
            tree = None
            return temp 
  
        temp = tree.right
        while(temp.left is not None): 
            temp = temp.left
        
        tree.value = temp.value 
        tree.right = tree_delete(tree.right , temp.value)
  
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
       postorder(tree.right)
    print (tree.value)


def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)

###################################################################################

if __name__ == '__main__':
  t = tree_insert(None,6)
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  print 'Inorder Traversal\n================='
  in_order(t)
  t = tree_delete(t,3)
  t = tree_delete(t,6)
  print '\nAfter deleting 3 and 6\n======================'
  in_order(t)
