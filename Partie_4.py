import time 
from datetime import datetime, timedelta

from Tree import Tree_BTS
from B_Tree import BTree
import Class_Individu as CI

t =  Tree_BTS()
Database = []
CI.lireFichierCSV('data.csv', Database)
d = [elem.ID for elem in Database ]

print("------------------Tree------------------")
t.addByList(d[0],[d[i] for i in range(1,100) ])
t.printTree()
print("------------------Calcul BF----------------------")
t.CalculBF()
t.print_TreeANDbf()

####Find
StartTime=datetime.now()
t.find(132)
EndTime = datetime.now()
ExecutionTime= (EndTime - StartTime).total_seconds()*100000


################ AVL ################
t.addByList_AVL(d[0],[d[i] for i in range(1,100) ])
print("------------------Inserting with AVL-------------------------")
t.printTree()
print("------------------Calcul BF----------------------")
t.print_TreeANDbf()

StartTime=datetime.now()
t.find(132)
EndTime = datetime.now()
ExecutionTime2 = (EndTime - StartTime).total_seconds()*100000

################ B tree ################
b =  BTree()
b.addByList(d, 5)
print("-------------------- B - Tree -------------------------")
b.printTree()

StartTime=datetime.now()
b.find(132)
EndTime = datetime.now()
ExecutionTime3 = (EndTime - StartTime).total_seconds()*100000

##Display 
## it is so fast because we have so little data
## so it is 0.0 most of the time 
## Activate this area with removing the '''

'''
print("The BST takes", end =" ")
print(ExecutionTime, end = " ")
print("microseconds.")

print("The BST with AVL takes", end =" ")
print(ExecutionTime2, end = " ")
print("microseconds.")

print("The B-Tree takes", end =" ")
print(ExecutionTime3, end = " ")
print("microseconds.")
'''