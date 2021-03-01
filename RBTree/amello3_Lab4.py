"""
Author: Austin Mello
Date: 03/05/2020
Description: Red/Black Tree
Note: Skeleton code provided by Jared Hall, The Magnificent
    Pseudocode provided by Cormem, Leiserson, Rivest, Stein. 
        "Introduction to Algorithms".
"""

from mealticket import *

class Sentinal():
    """This class builds the sentinal nodes and includes some nifty methods"""
    def __init__(self):
        """The constructor for the sentinal class"""
        self.key = None
        self.value = None
        self.leftChild = self
        self.rightChild = self
        self.parent = self
        self.color = "black"
        
    def isSentinal(self):
        """ This method makes it easy to check if a given node is a sentinal"""
        return True
    
class RBNode(object):
    """ Description: This is the node class for the Red-Black Tree."""
    def __init__(self, ticket, color = "red"):
        """Constructor for the RBNode class"""
        #Build sentinal nodes and set the initial parent
        self.key = ticket.ticketID
        self.value = ticket
        self.color = color
        self.parent = None
        self.leftChild = Sentinal()
        self.rightChild = Sentinal()


    def __str__(self):
        """ Returns a string rep of the node (for debugging ^,^) """
        returnValue = "Node: {} - Color: {}\n".format(self.key, self.color)
        returnValue += "Parent: {}\n".format(self.parent.key)
        returnValue += "Left Child: {}\n".format(self.leftChild.key)
        returnValue += "Right Child: {}\n".format(self.rightChild.key)
        return returnValue

    def isSentinal(self):
        """makes it easy to check if a node is a sentinal"""
        return False

    def hasLeftChild(self):
        """ This method returns true if the current node has a left child """
        returnValue = False
        if(self.leftChild.parent == self and self.leftChild != self):
            if(not self.leftChild.isSentinal()):
                returnValue = True
        return returnValue

    def hasRightChild(self):
        """ This method returns true|false depending on if the current
            node has a right child or not."""
        returnValue = False
        if(self.rightChild.parent == self and self.rightChild != self):
            if(not self.rightChild.isSentinal()):
                returnValue = True
        return returnValue

    def hasOnlyOneChild(self):
        """ Returns True if the current node has only one child."""
        LC = self.hasLeftChild()
        RC = self.hasRightChild()
        return (LC and not RC) or (not LC and RC)
    
    def hasBothChildren(self):
        """ Returns True if the current node has both children"""
        return self.hasLeftChild() and self.hasRightChild()

    def isLeaf(self):
        """ Returns true if the current node is a leaf node."""
        returnValue = False
        if(self.rightChild.isSentinal() and self.leftChild.isSentinal()):
            returnValue = True
        return returnValue

    def isLeftChild(self):
        """Returns true if the current node is a left child"""
        return self.parent.leftChild == self

    def isRightChild(self):
        """Returns true if the current node is a right child"""
        return self.parent.rightChild == self

class RedBlackTree:
    """ Skeleton code for the red-black tree"""
    def __init__(self):
        """ The constructor for the red-black tree"""
        self.size = 0
        self.output = ""
        # All leaf nodes point to self.sentinel, rather than 'None'
        # Parent of root should also be self.sentinel
        self.sentinel = Sentinal()
        self._root = self.sentinel
        self.sentinel.parent = self.sentinel
        self.sentinel.leftChild = self.sentinel
        self.sentinel.rightChild = self.sentinel

    def traverse(self, mode):
        """The traverse method returns a string rep of the tree according to
           the specified mode
        """
        self.output = ""
        if(type(mode) == str):
            if(mode == "in-order"):
                self.inorder(self._root)
            elif(mode == "pre-order"):
                self.preorder(self._root)
            elif(mode == "post-order"):
                self.postorder(self._root)
        else:
            self.output = "  "
        return self.output[:-2]

    def inorder(self, node):
        """ computes the preorder traversal """
        if(node.key is not None):
            self.inorder(node.leftChild)
            self.output += str(node.key) + ", "
            self.inorder(node.rightChild)

    def preorder(self, node):
        """computes the pre-order traversal"""
        if(node.key is not None):
            self.output += str(node.key) + ", "
            self.preorder(node.leftChild)
            self.preorder(node.rightChild)

    def postorder(self, node):
        """ compute postorder traversal"""
        if(node.key is not None):
            self.postorder(node.leftChild)
            self.postorder(node.rightChild)
            self.output += str(node.key) + ", "

    def findSuccessor(self, node):
        """
        This method returns the sucessor of a given node.
        """
        successor = None
        # if node has a right child
        if(node.hasRightChild()):
            # then successor is the min of the right subtree
            currentNode = node.rightChild
            while currentNode.hasLeftChild():
                currentNode = currentNode.leftChild
            successor = currentNode
        elif(node.parent): # node has no right child, but has a parent
            if(node.isLeftChild()): # node is a left child
                successor = self.parent # then succ is the parent
            else: # node is right child, and has not right child
                # remove parent's rightChild reference
                node.parent.rightChild = None
                # recursively find call findSuccessor on parent
                successor = findSuccessor(node.parent)
                # replace parent's rightChild reference
                node.parent.rightChild = node
        return successor

    
    #=========================== Manditory Methods =============================
    #You write these.

    def insert(self, ticket):
        """
        Description: Inserts a node into the tree "BST-style" and colors red. 
        Calls insertFixup afterwards to rebalance the colors.
        Input: Mealticket
        Output: True/False
        Notes: Pseudocode provided by Cormem, Leiserson, Rivest, Stein. 
        "Introduction to Algorithms".
        """

        if (ticket == None):
            return False

        parentalUnit = self.sentinel
        current = self._root
        newGuy = RBNode(ticket)

        while(current != None and not current.isSentinal()):
            parentalUnit = current
            if (newGuy.key < current.key):
                current = current.leftChild
            else:
                current = current.rightChild

        newGuy.parent = parentalUnit

        if (parentalUnit.isSentinal()):
            self._root = newGuy
        elif (newGuy.key < parentalUnit.key):
            parentalUnit.leftChild = newGuy
        else:
            parentalUnit.rightChild = newGuy
        newGuy.leftChild = self.sentinel
        newGuy.rightChild = self.sentinel
        newGuy.color = "red"

        if (self.insertFixup(newGuy)):
            return True
        else: 
            return False

    def insertFixup(self, newGuy):
        """
        Description: Called after insert to rebalance the tree.
        Input: RBNode
        Output: True/False
        Notes: Pseudocode provided by Cormem, Leiserson, Rivest, Stein. 
        "Introduction to Algorithms"."""

        current = newGuy
        
        if (current.parent.color != "red" and current.parent.color != "black"):
            return False

        while (current.parent.color == "red" and not current.isSentinal()):

            if (current.parent.isLeftChild()):
                uncle = current.parent.parent.rightChild

                if (uncle != None and uncle.color == "red"):
                    current.parent.color = "black"
                    uncle.color = "black"
                    current.parent.parent.color = "red"
                    current = current.parent.parent
                else:
                    if (current.isRightChild()):
                        current = current.parent
                        self.leftRotate(current)

                    current.parent.color = "black"
                    current.parent.parent.color = "red"
                    self.rightRotate(current.parent.parent)

            else: # (current.parent.isRightChild()):
                uncle = current.parent.parent.leftChild

                if (uncle != None and uncle.color == "red"):
                    current.parent.color = "black"
                    uncle.color = "black"
                    current.parent.parent.color = "red"
                    current = current.parent.parent
                else:
                    if (current.isLeftChild()):
                        current = current.parent
                        self.rightRotate(current)
                    
                    current.parent.color = "black"
                    current.parent.parent.color = "red"
                    self.leftRotate(current.parent.parent)

        self._root.color = "black"
        return True

    def leftRotate(self, currentNode):
        """ 
        Description: Perform a left rotation from a given node.
        Input: RBNode
        Output: None
        Pseudocode provided by Cormem, Leiserson, Rivest, Stein. "Introduction
        to Algorithms".
        """

        x = currentNode
        y = x.rightChild
        x.rightChild = y.leftChild
        
        if (not y.leftChild.isSentinal()):
            y.leftChild.parent = x

        y.parent = x.parent

        if (x.parent.isSentinal()):
            self._root = y
        elif (x.isLeftChild()):
            x.parent.leftChild = y
        else: 
            x.parent.rightChild = y
        y.leftChild = x
        x.parent = y
            
    def rightRotate(self, currentNode):
        """ 
        Description: Perform a right rotation from a given node.
        Input: RBNode
        Output: None
        Pseudocode provided by Cormem, Leiserson, Rivest, Stein. "Introduction
        to Algorithms".
        """

        current = currentNode
        y = current.leftChild
        current.leftChild = y.rightChild
        
        if (not y.rightChild.isSentinal()):
            y.rightChild.parent = current

        y.parent = current.parent

        if (current.parent.isSentinal()):
            self._root = y
        elif (current.isRightChild()):
            current.parent.rightChild = y
        else: 
            current.parent.leftChild = y
        y.rightChild = current
        current.parent = y

    def find(self, ticketID):
        """ 
        Description: Finds a node and returns its value
        Input: Integer
        Output: RBNode.value
        """

        if (self._root == None):
            print("tree is empty")
            return False

        current = self._root

        while (not current.isSentinal() and current.key != ticketID):

            if (current.key > ticketID):
                current = current.leftChild
            elif (current.key < ticketID):
                current = current.rightChild

        if (current == None or current.key != ticketID):
            print("didnt find it...")
            return False

        return current.value
        
    def findNode(self, ticketID):
        """
        Description: Similar to find but returns a node (used internally for 
        find sucessor and delete). Same steps as above, just return currentNode
        """
        
        if (self._root == None):
            print("nothing in the root")
            return False

        current = self._root

        while (not current.isSentinal() and current.key != ticketID):

            if (current.key > ticketID):
                current = current.leftChild
            else:
                current = current.rightChild

        if (current == None or current.key != ticketID):
            print("didnt find it...")
            return False

        return current

    def delete(self, ticketID):
        """ Finds and deletes a node "BST-style," then calls a fixup function
        to rebalance the colors.
        Input: ticketID (int)
        Output: None
        Notes: Pseudocode provided by Cormem, Leiserson, Rivest, Stein. 
        "Introduction to Algorithms"."""

                
        z = self.findNode(ticketID)
        y = z
        yColor = y.color

        if (z.leftChild.isSentinal()):
            x = z.rightChild
            self.transplant(z, z.rightChild)

        elif (z.rightChild.isSentinal()):
            x = z.leftChild
            self.transplant(z, z.leftChild)

        else: 
            y = self.treeTop(z.rightChild)
            yColor = y.color
            x = y.rightChild

            if (y.parent == z):
                x.parent = y
            else:
                self.transplant(y, y.rightChild)
                y.rightChild = z.rightChild
                y.rightChild.parent = y

            self.transplant(z, y)
            y.leftChild = z.leftChild
            y.leftChild.parent = y
            y.color = z.color

        if (yColor == "black"):
            return self.deleteFixup(x)
        
        return True

    def deleteFixup(self, currentNode):
        """
        Description: Balances the tree after the delete method is complete.
        Input: RBNode
        Output: None
        """

        x = currentNode

        while (x.color == "black" and x != self._root):
            if (x == x.parent.leftChild):
                sibling = x.parent.rightChild

                if (sibling.color == "red"):
                    sibling.color = "black"
                    x.parent.color = "red"
                    self.leftRotate(x.parent)
                    sibling = x.parent.rightChild

                if (sibling.leftChild.color == "black" and 
                    sibling.rightChild.color == "black"):
                    sibling.color = "red"
                    x = x.parent

                else:
                    if (sibling.rightChild.color == "black"):
                        sibling.leftChild.color = "black"
                        sibling.color = "red"
                        self.rightRotate(sibling)
                        sibling = sibling.parent.rightChild

                    sibling.color = x.parent.color
                    x.parent.color = "black"
                    sibling.rightChild.color = "black"
                    self.leftRotate(x.parent)
                    x = self._root

            else: #(x == x.parent.rightchild)
                sibling = x.parent.leftChild

                if (sibling.color == "red"):
                    sibling.color = "black"
                    x.parent.color = "red"
                    self.rightRotate(x.parent)
                    sibling = x.parent.leftChild

                if (sibling.leftChild.color == "black" 
                   and sibling.rightChild.color == "black"):
                    sibling.color = "red"
                    x = x.parent

                else:
                    if (sibling.leftChild.color == "black"):
                        sibling.rightChild.color = "black"
                        sibling.color = "red"
                        self.leftRotate(sibling)
                        sibling = x.parent.leftChild

                    sibling.color = x.parent.color
                    x.parent.color = "black"
                    sibling.leftChild.color = "black"
                    self.rightRotate(x.parent)
                    x = self._root

        x.color = "black"

    def transplant(self, currentNode, successor):
        """Description: Splices in the sucessor of the current node
        Input: RBNode x2
        Output: None
        Notes: Pseudocode provided by Cormem, Leiserson, Rivest, Stein. 
        "Introduction to Algorithms".
        """

        if (currentNode.parent.isSentinal()):
            self._root = successor
        elif (currentNode.isLeftChild()):
            currentNode.parent.leftChild = successor
        else:
            currentNode.parent.rightChild == successor
            
        successor.parent = currentNode.parent

    def treeTop(self, current):
        """Description: Finds the node with the smallest ticketID
        Input: RBNode
        Output: RBnode
        """

        while (not current.leftChild.isSentinal()):
            current = current.leftChild
        return current


if(__name__ == "__main__"):
    #Write a main to test your code. Share on Piazza if you wanna ^,^
    pass