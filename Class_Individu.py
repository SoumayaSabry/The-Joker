import csv

class Individu:    
    def __init__(self, ID1, nickname1, location1, trust_level1):
        self.ID = ID1
        self.nickname = nickname1
        self.location = location1
        self.trust_level = trust_level1
    
    def __str__(self):
        if self.ID==0:
            return "/!\ /!\ He isn't a Joker /!\ /!\ "
        else:
            return str(self.ID)+" "+self.nickname+" "+self.location+" "+ str(self.trust_level)

def lireFichierCSV(fichier,list_name):
    with open(fichier, newline='') as csvfile:
        i=0
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        next(spamreader) #skip the first line which is the header
        for row in spamreader:
            list_name.append(Individu(int(row[0]),row[1],row[2],int(row[3])))

def affichageDatabase(list_name):
    for line in list_name:
        print(line.ID, end = " ")
        print(line.nickname, end = " ")
        print(line.location, end = " ")
        print(line.trust_level)

