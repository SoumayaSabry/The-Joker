# Part3

import csv
from time import gmtime, strftime
from datetime import datetime, timedelta
import Class_Individu as CI

Database = []
CI.lireFichierCSV('data.csv', Database)

def Iteratif(ResearchedID):
	is_Found=False
	for line in Database:
		if line.ID == ResearchedID:
			print(line)
			is_Found=True
			break
	if is_Found == False:
		print("/!\ /!\ He isn't a Joker /!\ /!\ ")

def DivideAndConquer(ResearchedID,left,right):
	ind0 = CI.Individu(0,"None","None",0)
	if left==right:
		return Database[left]
	else:
		if (left+right)%2==0:
			moitie = (left+right)/2
		else:
			moitie = (left+right-1)/2
		temp1 = DivideAndConquer(ResearchedID, left,int(moitie))
		temp2 = DivideAndConquer(ResearchedID, int(moitie)+1,right)
		if temp1.ID == ResearchedID:
			return temp1
		else: 
			if temp2.ID == ResearchedID:
				return temp2
			else:
				return ind0

def MergeSort(ArrayL):
    if len(ArrayL) == 1:
        return [ArrayL[0]]
    else :
        L = MergeSort([ArrayL[i]for i in range (0,int(len(ArrayL)/2))])
        G = MergeSort([ArrayL[i]for i in range (int(len(ArrayL)/2), len(ArrayL))])
        res = []
        indexL =0
        indexG =0
        AcomparerUN = L[indexL]
        AcomparerDEUX = G[indexG]
        estFini = 0
        while estFini == 0 :
            estFini = 1
            if AcomparerUN.ID < AcomparerDEUX.ID :
                res.append(AcomparerUN)
                indexL = indexL +1
                if indexL < len(L):
                    estFini = 0
                    AcomparerUN = L[indexL]
            else :
                res.append(AcomparerDEUX)
                indexG = indexG +1
                if indexG < len(G):
                    estFini = 0
                    AcomparerDEUX =  G[indexG]
                
                    
        if len(res) < len(L)+len(G) :
            if indexL <len(L):
                for i in range(indexL , len(L)):
                    res.append(L[i])
            else :
                for i in range(indexG , len(G)):
                    res.append(G[i])
            
        return res

def BinarySearch(ResearchedID,JokersList):
	ind0 = CI.Individu(0,"None","None",0)
	l=len(JokersList)
	m = int(len(JokersList)/2)
	if l == 1 :
		if JokersList[m].ID == ResearchedID:
			return JokersList[m]
		else:
			return ind0
	elif JokersList[m].ID == ResearchedID:
		return JokersList[m]
	elif JokersList[m].ID > ResearchedID:
		return BinarySearch(ResearchedID, JokersList[1:m])
	else:
		return BinarySearch(ResearchedID,JokersList[m:l])

def Main():
	#Iterative method
	StartTime = datetime.now()
	Iteratif(1000)
	EndTime = datetime.now()
	ExecutionTime = (EndTime - StartTime).total_seconds()
	print("The iterative method takes", end =" ")
	print(ExecutionTime, end = " ")
	print("seconds.")
	
	#DivideAndConquer Method
	StartTime=datetime.now()
	print(DivideAndConquer(1000,0,len(Database)-1))
	EndTime = datetime.now()
	ExecutionTime = (EndTime - StartTime).total_seconds()
	print("The divide and conquer method takes", end = " ")
	print(ExecutionTime, end = " ")
	print("seconds.")

	#Merge Sort & Binary search
	Sorted_database = MergeSort(Database)
	StartTime=datetime.now()
	print(BinarySearch(1000,Sorted_database))
	EndTime = datetime.now()
	ExecutionTime = (EndTime - StartTime).total_seconds()
	print("The Binary Search method takes", end = " ")
	print(ExecutionTime, end = " ")
	print("seconds.")


Main()