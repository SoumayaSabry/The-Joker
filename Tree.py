
class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.BF= -1
        self.v = val
######################################################################		
######################################################################        
class Tree_BTS:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root
    ######################################################################
    def _printInorder(self,node):
        if (node != None):
            self._printInorder(node.l)
            print(node.v,end=" ")
            self._printInorder(node.r)

    def _printPreorder(self,node):
        if (node != None):
            print(node.v,end=" ")
            self._printPreorder(node.l)
            self._printPreorder(node.r)
            
    def _printPostorder(self,node):
        if (node != None):
            self._printPostorder(node.l)
            self._printPostorder(node.r)
            print(node.v, end=" ")

    def printTreeInOrder(self):
        if (self.root != None):
            self._printInorder(self.root)
        print()
    def printTreePostOrder(self):
        if (self.root != None):
            self._printPostorder(self.root)
        print()
    def printTreePreOrder(self):
        if (self.root != None):
            self._printPreorder(self.root)
        print()
                     
    ####################################################################   
    def _print_Tree (self , node, h):
        if(node != None):
            for i in range (h):
                print("|---",end = "")
            print(node.v)
            if(self.is_Leaf(node)== False):
                self._print_Tree (node.l, h+1)
                self._print_Tree (node.r, h+1)
        else :
            for i in range (h):
                print("|---",end ="")
            print("X", end = "\n")
    def printTree(self):
       if (self.root != None):
            self._print_Tree(self.root,0) 
    ####################################################################
    
    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)
                
    def add(self,val):
        if(self.root == None):
            self.root = Node(val)
        if(self.find(val) == False):
            self._add(val,self.root)
            
    def addByList(self,Root, ListVal):
        self.add(Root)
        for val in ListVal :
            self.add(val)
    ####################################################################

    def _find(self, val, node):
        if(val == node.v):
            return True  ##node
        elif(val < node.v and node.l != None):
            return self._find(val, node.l)
        elif(val > node.v and node.r != None):
            return self._find(val, node.r)
        else : 
            return False #None
    def find(self, val):
        if(self.root == None):
            return None
        else:
            return self._find(val,self.root)
    ####################################################################       
    def is_Leaf(self,node):
        if (node == None):
            return None
        elif (node.l == None and node.r == None) :
            return True
        else :
            return False
    def Nb_Leaf(self,node):
        if (node == None):
            return None
        elif (node.l == None and node.r == None) :
            return 0
        elif (node.l == None or node.r == None) :
            return 1
        else :
            return 2
    ######################################################################
    def size(self,node, counter):
        if node:
            left = self.size(node.l, counter+1)
            right = self.size(node.r, counter+1)
            return left if left > right else right
        else:
            return counter-1
    def height (self):
        if self.root :
            return size(self,self.root,0)
        else : 
            return 0
    ######################################################################
    def find_max(self,node):
        if self.is_Leaf(node):
            return node.v
        else :
            
            nodeL = nodeR= node.v 
            if node.r != None:
                nodeR = self.find_max(node.r)
            if node.l != None :
                nodeL = self.find_max(node.l)
            
            if(nodeL > nodeR ):
                return nodeL
            else :
                return nodeR
            
    def find_min(self,node):
        if self.is_Leaf(node):
            return node
        else :
            
            nodeL = node 
            nodeR = node 
            if node.r != None:
                nodeR = self.find_min(node.r)
            if node.l != None :
                nodeL = self.find_min(node.l)
            
            if(nodeL.v < nodeR.v):
                return nodeL
            else :
                return nodeR
    ######################################################################
    def _delete(self, node_Acc):
        nb = self.Nb_Leaf(node_Acc)
        if(nb==0):
            return None
        if(nb==1):
            if(node_Acc.l != None):
                return node_Acc.l
            else :
                return node_Acc.r
        if(nb==2):
            max_Tree = self.find_max(node_Acc.l)
            self.delete(max_Tree)
            node_Acc.v = max_Tree
            return node_Acc
            
    def delete(self, val):
        if(self.root.v == val):
            self._delete(self.root)
        elif(self.find(val)):
            node_temp=self.root 
            is_not_finish =True
            while(is_not_finish):
                if(val < node_temp.v and node_temp.l != None):
                    if(node_temp.l.v == val):
                        node_temp.l = self._delete(node_temp.l)
                        is_not_finish = False
                    else:
                        node_temp = node_temp.l
                        is_not_finish =True
                elif(val > node_temp.v and node_temp.r != None):
                #just pour etre sur mais il ya jamais node_temp.r == None
                    if(node_temp.r.v == val):
                        node_temp.r = self._delete(node_temp.r)
                        is_not_finish =False
                    else:
                        node_temp = node_temp.r
                        is_not_finish =True  
            #print ("Done")
        else :
            print("Element n'existe pas ")
    ######################################################################
    #####################################AVL##############################
    ######################################################################
    def BF(self,node):
        return abs(self.size(node.l, 0) - self.size(node.r, 0))
    def _CalculBF(self,node):
        if node:
            node.BF =self.BF(node)
            self._CalculBF(node.l)
            self._CalculBF(node.r)
    def CalculBF(self):
        if self.root :
            self._CalculBF(self.root)
    def Rotation(self,node):
    #Choose the Type of rotation and
    #Choose A B C  ==> A<B<C
        if node.r and self.is_Leaf(node.r) == False and self.size(node.r, 0)>self.size(node.l, 0):
            #the right branche should be bigger than the left one 
            if node.r.r:
                # Left rotation
                A= node
                B= node.r
                C= node.r.r
                B.r = None 
                A.r = None 
            else:
                #Right-Left rotation
                A= node
                B= node.r.l
                C= node.r
                C.l = None
                A.r=None
            
        else :
            
            if node.l.r:
                #Left-Right rotation
                A= node.l
                B= node.l.r
                C= node
                A.r=None
                C.l=None
            else:
                #Right rotation
                A= node.l.l
                B= node.l
                C= node
                B.l=None
                C.l=None
            
        #check children to B 
        List_Chlid_B=[]
        if self.is_Leaf(B)== False:
            if B.r :
                self.TreeToList(B.r,List_Chlid_B) 
            if B.l :
                self.TreeToList(B.l,List_Chlid_B)
        
        #rotation 
        B.l = A
        B.r = C
        #re add 
        if len(List_Chlid_B) != 0:
            self.addByList(List_Chlid_B[0],List_Chlid_B)
        #recount of BF out side of this function 
        return B
    def TreeToList(self,node,L):
        if node == None:
            return None
        else :
            L.append(node.v)
            if node.r:
                r = self.TreeToList(node.r,L)
                if r != None:
                    L.append(r)
            if node.l:
                l = self.TreeToList(node.l,L)
                if l!= None :
                    L.append(l)
    ######################################################################
    def LoopCheckAVL(self, node, Check):
        #check BF of each node if bf > 1 then True
        if node :
                if Check == True :
                    Check = self.CheckIfAVL(node) 
                if Check == True :
                    Check = self.LoopCheckAVL(node.l,Check)
                if Check == True :
                    Check = self.LoopCheckAVL(node.r,Check)

        return Check
    def CheckIfAVL(self,node):
        return False if node.BF > 1 else True
    def _Repair(self,node):
        if self.is_Leaf(node)== False:
            if node.r:
                self._Repair(node.r)
                if self.CheckIfAVL(node.r) == False :
                    node.r = self.Rotation(node.r)
                    #recount of BF 
                    self.CalculBF()
            if node.l:
                self._Repair(node.l)
                if self.CheckIfAVL(node.l) == False :
                    node.l = self.Rotation(node.l)
                    #recount of BF 
                    self.CalculBF()
    def Repair(self):
        if self.root:
            self._Repair(self.root)
            if self.CheckIfAVL(self.root)==False :
                self.root = self.Rotation(self.root)
                #recount of BF 
                self.CalculBF()
     ######################################################################       
    def addByList_AVL(self,root,List):
        self.add(root)
        self.CalculBF()
        for val in List:
            self.add(val)
            self.CalculBF()
            while self.LoopCheckAVL(self.root,True)==False :
                self.Repair()   
     ######################################################################
    def _print_TreeANDbf (self , node, h):
        if(node != None):
            for i in range (h):
                print("|---",end = "")
            print(node.v , '(',node.BF,')')
            if(self.is_Leaf(node)== False):
                self._print_TreeANDbf (node.l, h+1)
                self._print_TreeANDbf (node.r, h+1)
        else :
            for i in range (h):
                print("|---",end ="")
            print("X", end = "\n")
    def print_TreeANDbf(self):
        if (self.root != None):
            self._print_TreeANDbf(self.root,0)