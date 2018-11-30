'''
   Task 1 - 2
   ------------------
   Build a Binary Search Tree (BST) to hold English language words in its nodes.
   Use a paragraph (1 paragraph would suffice) of any text in order to extract words and to determine their frequencies.
   Input: You should read the paragraph from a suitable file format, such as .txt.
      The following tree operations should be implemented:
       a) Printing the tree in pre-order.
       b) Finding a word. Regardless whether found or not found, your program should output the path traversed in determining the answer, followed by yes if found or no, respectively.
    Note: In order to deal with identical words, add another attribute to the Binary Search Tree node that would keep track of the frequency of that word.
'''

class Node:

      def __init__(self,word): 
          self.word = word  
          self.freq = 1     
          self.left = None  
          self.right = None 

      def __str__(self):
          return self.word + ' ' + str(self.freq)

class searchtree:

      def __init__(self):
          self.root = None

      def create(self,val):
          if self.root == None:
             self.root = Node(val)
          else:
             current = self.root
             while 1:
                  if val < current.word:
                        if current.left:
                              current = current.left
                        else:
                              current.left = Node(val)
                              break;      
                  elif val > current.word:
                        if current.right:
                              current = current.right
                        else:
                              current.right = Node(val)
                              break;      
                  else:
                        current.freq += 1
                        break 

      def preorder(self,node):
           if node is not None:
              print (node)
              self.preorder(node.left)
              self.preorder(node.right)

      def find(self,search) :
            if self.root == None:
                  print 'Tree is empty'
            else:
                  current = self.root
                  while 1:
                        print current
                        if search == current.word:
                              print 'Yes'
                              break;
                        elif search < current.word:
                              if current.left:
                                    current = current.left
                              else:
                                    print 'No'
                                    break;
                        elif search > current.word:
                              if current.right:
                                    current = current.right
                              else:
                                    print 'No'
                                    break;

###################################################################################

tree = searchtree()
file = open('paragraph.txt', 'r')
for word in file.read().split():
    tree.create(word)
file.close()
print 'Preorder Traversal\n=================='
tree.preorder(tree.root)
print '\n'
print 'Search for word \'world\'\n======================='
tree.find('world')
print '\n'
print 'Search for word \'over\'\n======================'
tree.find('over')
