
from Graph import Graph
def main():
  
  graph = [[  0.0,  8.1,  9.2,  7.7,  9.3,  2.3,  5.1, 10.2,  6.1,  7.0],
           [  8.1,  0.0, 12.0,  0.9, 12.0,  9.5, 10.1, 12.8,  2.0,  1.0],
           [  9.2, 12.0,  0.0, 11.2,  0.7, 11.1,  8.1,  1.1, 10.5, 11.5],
           [  7.7,  0.9, 11.2,  0.0, 11.2,  9.2,  9.5, 12.0,  1.6,  1.1],
           [  9.3, 12.0,  0.7, 11.2,  0.0, 11.2,  8.5,  1.0, 10.6, 11.6],
           [  2.3,  9.5, 11.1,  9.2, 11.2,  0.0,  5.6, 12.1,  7.7,  8.5],
           [  5.1, 10.1,  8.1,  9.5,  8.5,  5.6,  0.0,  9.1,  8.3,  9.3],
           [ 10.2, 12.8,  1.1, 12.0,  1.0, 12.1,  9.1,  0.0, 11.4, 12.4],
           [  6.1,  2.0, 10.5,  1.6, 10.6,  7.7,  8.3, 11.4,  0.0,  1.1],
           [  7.0,  1.0, 11.5,  1.1, 11.6,  8.5,  9.3, 12.4,  1.1,  0.0]]

  g = Graph()
  g.InsertGraph_FromMatrix(graph)
  print("_________________________Displaying Cities Details___________________________")
  print("There is the other cities that we want to visit", end=":")
  print(g.nodes)
  print("There is the distance between each city and another", end=": \n")
  for nodes,dist in g.distances.items():
      print("Distance between ", end = "")
      for n in nodes : print (n, end = " ")
      print (" is "+str(round(dist,1))+"")
      
  print("_________________________ Applying Dijsktra _________________________")
  d=g.dijsktra('g1')
  print(d)
  t = g.Path_ToTree('g1',d[1],d[0])
  print("There is the Tree of the path :::")
  t.printTree()
  print("Based on our Calculating, We will send "+ str(t.Nb_Volunteers())+" Volunteers")


main()