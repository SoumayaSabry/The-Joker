

class BNode:
    def __init__(self, val, n, p = None):
        self.nbVal = n
        self.listVal = []
        self.pere= p
        self.listVal.append(val)
        self.listKey = [None]*(n+1)

######################################################################		
######################################################################  

class BTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root
    ####################################################################   
    def _print_Tree (self , node, h):
        if(node != None):
                for val in node.listVal:
                    for i in range (h):
                        print("|---",end = "")
                    print(val)
                if(self.is_Leaf(node) == False):
                    for key in  node.listKey :
                        if key != None :
                            self._print_Tree (key, h+1)
                            print("-----------------")
        else :
            for i in range (h):
                print("|---",end ="")
            print("X", end = "\n")
    def printTree(self):
       if (self.root != None):
            self._print_Tree(self.root,0)
            
    ####################################################################
    def is_Leaf(self,node):
        if (node == None):
            return None
        else :
            isL = True
            for i in node.listKey :
                if i != None : isL = False
            return isL
    def is_Full(self,node):
        if (node == None):
            return None
        if len(node.listVal)==node.nbVal:
            return True
        else :
            return False
    def _find (self,id , node):
        if id in node.listVal:
            return True
        elif id < node.listVal[0] and node.listKey[0] != None:
            return self._find(id, node.listKey[0])
        elif id > node.listVal[len(node.listVal)-1] and node.listKey[len(node.listVal)] != None:
            return self._find(id,node.listKey[len(node.listVal)])    
        elif id > node.listVal[0] and id < node.listVal[len(node.listVal)-1]:
            for i in  range(len(node.listVal)-1) : 
                if node.listVal[i] < id and id < node.listVal[i+1]:
                    if node.listKey[i+1] != None :
                        return self._find(id, node.listKey[i+1])
                    else: return False
        else : 
            return False #None
    def find (self, ID):
        if(self.root == None): return None
        else:
            return self._find(ID,self.root)
    ####################################################################
    def split(self, node, n, val, index):
        listTemp = node.listVal.copy()
        listTemp.insert(index,val)
        valMilieu= listTemp[len(listTemp)//2-1]

        FirstHalf= listTemp[:len(listTemp)//2-1]
        SectHalf = listTemp[len(listTemp)//2:]
        
        NodeFirstHalf=BNode(FirstHalf[0],n,node)
        for i in range (1,len(FirstHalf)): NodeFirstHalf.listVal.append(FirstHalf[i])

        #bigger right 
        NodeSecHalf =BNode(SectHalf[0],n,node)
        for i in range (1,len(SectHalf)): NodeSecHalf.listVal.append(SectHalf[i])

        return [valMilieu,NodeFirstHalf,NodeSecHalf]
         
    def Promote(self,pere,node , v , FirstHalf,SecondHalf,not_Finish):
        if pere == None and  not_Finish :##ROOT
            n = BNode(v,node.nbVal)
            FirstHalf.pere = n
            SecondHalf.pere = n 
            n.listKey[0]=FirstHalf
            n.listKey[1]=SecondHalf
            self.root = n
            not_Finish= False
        elif pere == None and  not_Finish == False :
            self.root = node
        elif pere != None and not_Finish == False : 
            self.Promote(pere,None,None,None,not_Finish)
        elif pere != None and not_Finish :
            if self.is_Full(pere) :
                #insert the val + split 
                if v < pere.listVal[0]:
                    index = 0
                    [newV,NF,NS] =self.split(pere,pere.nbVal,v,index)
                    
                elif v > pere.listVal[len(pere.listVal)-1]:
                    index = len(pere.listVal)
                    [newV,NF,NS] =self.split(pere,pere.nbVal,v,index)
                else :
                    for i in  range(len(pere.listVal)-1) : 
                        if pere.listVal[i] < v and v < pere.listVal[i+1]:
                            index = i+1
                            [newV,NF,NS] =self.split(pere,pere.nbVal,v,index)
                ##recorrigere les pere 
                FirstHalf.pere = pere
                SecondHalf.pere = pere 

                ###copy key + insert

                listTempK=pere.listKey.copy()
                listTempK.remove(node)
                listTempK.insert(index,FirstHalf)
                listTempK.insert(index+1,SecondHalf)

                ##split the Keys + correction pere ## a corriger 
                FirstHalfK= listTempK[:len(listTempK)//2]
                SectHalfK = listTempK[len(listTempK)//2:]
                for i in range (0,len(FirstHalfK)):
                    NF.listKey[i]=FirstHalfK[i]
                    if FirstHalfK[i] != None :
                        FirstHalfK[i].pere=NF
                for i in range (0,len(SectHalfK)):
                    NS.listKey[i]=SectHalfK[i] 
                    if SectHalfK[i] != None :
                        SectHalfK[i].pere=NS

                ###Promote 
                self.Promote(pere.pere,pere,newV,NF,NS,not_Finish)
                
            else :
                ##ajout la valeur en position 
                not_Finish = False

                if v < pere.listVal[0]:
                    index = 0
            
                    pere.listVal.insert(index,v)
                    
                elif v > pere.listVal[len(pere.listVal)-1]:
                    index = len(pere.listVal)
                    pere.listVal.append(v)
                else :
                    for i in  range(len(pere.listVal)-1) : 
                        if pere.listVal[i] < v and v < pere.listVal[i+1]:
                            index = i+1
                            pere.listVal.insert(index,v)
                #mise a jour Pere
                FirstHalf.pere=pere
                SecondHalf.pere=pere
                # ajout des key en position 
                listTemp = pere.listKey.copy()
                pere.listKey[index]=FirstHalf
                pere.listKey[index+1]=SecondHalf
                comp = index+2
                for i in range(index+1,len(pere.listKey)):
                    if comp < len(pere.listKey):
                        pere.listKey[comp]=listTemp[i]
                        comp = comp+1

 
    def _add(self, val, node, n):

        if val < node.listVal[0]:
                if node.listKey[0] == None:
                    if self.is_Full(node) :
                        ## Split
                        [v,NF,NS] = self.split(node,n,val,0)
                        ## Promote
                        self.Promote(node.pere,node,v , NF, NS,True)
                    else : node.listVal.insert(0,val)
                        
                else :
                    self._add(val,node.listKey[0],n)
        elif  val > node.listVal[len( node.listVal)-1]:
                if node.listKey[len(node.listVal)] == None:
                    if self.is_Full(node) :
                        ## Split
                        [v,NF,NS] = self.split(node,n,val,len(node.listVal))
                        ## Promote
                        self.Promote(node.pere,node,v , NF, NS,True)
                    else : 
                       node.listVal.append(val)
                else :
                    self._add(val,node.listKey[len(node.listVal)],n)
        else :
            for i in range(len(node.listVal)-1):
                ## le -1 pour eviter l'eurreur et ne pas depasser mla limite du list
                if node.listVal[i] < val and val < node.listVal[i+1]:
                    if node.listKey[i+1] == None:
                        if self.is_Full(node) :
                            ## Split 
                            [v,NF,NS] = self.split(node,n,val,i+1)
                            ## Promote
                            self.Promote(node.pere,node,v , NF, NS,True)
                        else :  node.listVal.insert(i+1,val)  
                    else :
                        self._add(val,node.listKey[i+1],n)
    ####################################################################
    def add(self,val, n):
        if(self.root == None):
            self.root = BNode(val,n)
        else : 
            self._add(val,self.root, n)
            
    def addByList(self, ListVal,n):
        for val in ListVal :
            self.add(val, n)
    

