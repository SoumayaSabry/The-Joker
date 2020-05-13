from collections import defaultdict
import csv
import pandas

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[frozenset ({from_node, to_node})] = distance
####################################################################
  def InsertGraph_FromMatrix(self, matrix): 
      for i in range(len(matrix)):
          self.add_node("g"+str(i+1))
      for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != 0 and i > j :
                self.add_edge("g"+str(i+1), "g"+str(j+1), matrix[i][j])
  
  def InsertGraph_FromCSV(self,fichier):
      with open(fichier, newline='') as csvfile:
          spamreader=csv.reader(csvfile, delimiter=';', quotechar='|')
          next(spamreader) #skip the first line which is the header
          for row in spamreader:
              self.add_edge(int(row[0]),int(row[1]),int(row[2]))

  def initialisationNodes(self):
      nodeExists = False
      for keys,value in self.distances.items():
          for key_n in keys:
              for node_n in self.nodes:
                  if key_n == node_n:
                      nodeExists = True
              if nodeExists == False:
                  self.add_node(key_n)
              nodeExists = False

			
  def Graph_ToMatrix(self):
      matrix = [[0]*len(self.nodes) for i in range(len(self.nodes))]
      for i in range(0,len(self.distances)):
          w = self.distances[list(self.distances)[i]]
          lst = []
          for n in list(self.distances)[i]:
              lst.append(n)
          i = lst[0]
          j = lst[1]
          matrix[i-1][j-1] = w
          matrix[j-1][i-1] = w
      frame = pandas.DataFrame(matrix)
      frame.index += 1
      frame.columns +=1
      print(frame)

##########################Partie_1##################################
####################################################################
  def find(self,root, i):
      if root[i-1] == i:
          return i
      return self.find(root, root[i-1])
  
  def connect(self,root,height,x,y):
      xroot = self.find(root,x)
      yroot = self.find(root,y)

      if height[xroot-1] < height[yroot-1]:
          root[xroot-1] = yroot
      elif height[xroot-1] > height[yroot-1]:
          root[yroot-1] = xroot
      else:
          root[yroot-1] = xroot
          height[xroot-1] += 1

  def Kruskal(self):
      result = {}

      i=0
      e=0
      d = sorted(self.distances.items(),key=lambda t:t[1])
      root = []
      height = []
      
      number = len(self.nodes)

      for node in range(1,number+1):
          root.append(node)
          height.append(0)

      while e < len(self.nodes) - 1:
          l = list(list(d[i])[0])
          source = l[0]
          destination = l[1]
          weight = list(d[i])[1]

          i=i+1
          rs = self.find(root,source)
          rd = self.find(root,destination)

          if rs!=rd:
              e=e+1
              result[(source,destination)]=weight
              self.connect(root,height,rs,rd)

      for edge_n in result:
          print(str(edge_n[0]) + " ------- " + str(edge_n[1]) + " = " + str(result[edge_n]))
      return result


##########################Partie_2##################################
####################################################################
  def dijsktra(self, initial):
        current_n = {initial: 0}
        path = {}

        nodes = set(self.nodes)

        while nodes: 
            #we find the minimal node
            node_min = None
            for node in nodes:
                if node in current_n:
                    if node_min is None:
                        node_min = node
                    elif current_n[node] < current_n[node_min]:
                        node_min = node

            if node_min is None:
                break
            
            #we remove the node with the min distance from the list of nodes aka to block it 
            nodes.remove(node_min)

            current_weight = current_n[node_min]

            for edge in self.edges[node_min]:
                weight = current_weight + self.distances[frozenset({node_min, edge})]
                if edge not in current_n or weight < current_n[edge]:
                    current_n[edge] = weight
                    path[edge] = node_min

        return current_n, path
  def Path_ToTree(self,initial,visited, path):
      t = Tree_ForGraph()
      t .InsertPath(initial,visited,path)
      return t
####################################################################
####################################################################
####################################################################
class Node_ForGraph:
    def __init__(self, val, d):
        self.ListChlid= []
        self.v = val
        self.distance= d

class Tree_ForGraph :
  def __init__(self):
      self.root = None 
  #################################################
  def _print_Tree (self , node, h):
        if(node != None):
            for i in range (h):
                print("|---",end = "")
            print(node.v, end = " ")
            print("("+ str(round(node.distance, 2))+")")
            if(self.is_Leaf(node)== False):
                for n in node.ListChlid :
                  self._print_Tree (n, h+1)
        else :
            for i in range (h):
                print("|---",end ="")
            print("X", end = "\n")
  def printTree(self):
       if (self.root != None):
            self._print_Tree(self.root,0)
            
  ############################################       
  def InsertPath(self,Root, path,distance):
        self.root = Node_ForGraph(Root,0)
        self.add(self.root,path,distance)
        
  def add (self, node,path,distance):
    if len(path)!= 0  :
      l=[]
      for key, val in path.items():
        if val == node.v :
          node.ListChlid.append(Node_ForGraph(key,distance[key]))
          l.append(key)
      for key in l :
          del path[key]
      for n in node.ListChlid :
        self.add(n,path,distance)

  ############################################ 
  def is_Leaf(self,node):
        if (node == None):
            return None
        elif len(node.ListChlid) == 0 :
            return True
        else :
            return False
  def Total_leaf(self, node,sum):
      if self.is_Leaf(node):
          return sum + 1
      else: 
          if(node != None):
              if(self.is_Leaf(node) == False):
                for n in node.ListChlid :
                  sum = self.Total_leaf(n, sum)
          return sum
  def Nb_Volunteers(self):
        if (self.root != None):
            res = self.Total_leaf(self.root,0)
            return res
        else :
            return -1

