import random
random.seed(702140)

n=1000

List_Nicknames=["Assi","Aggy","Ben","Bob","Bully" ,"Cobra","Cats Eyes" ,"Cloudy",
"Dolfo" ,"Dutch","Eagle", "Fish","Fighter","Gabby" ,"Hoppy" ,"Hamish" ,"Igo" ,
"Jake","Johnny","Kinch" ,"Lock","Mick","Mouse" ,"Pancho" ,"Pete","Red",
"Sandy" ,"Soaad","Tex" ,"Tim" ,"Vanyish","Wop","Uncle","Wolverine","Yola"]

List_Loc=["Uptown","MidTown","DownTown","Sheal","PettsBurg","South Hinkley"]

ListID=[]
for i in range(0,n):
    ListID.append(i+1)
random.shuffle(ListID)
with open('data1000.csv', 'w', newline='') as csvfile:
    csvfile.write("ID" + ';')
    csvfile.write("Nickname" + ';')
    csvfile.write("Location" + ';')
    csvfile.write("Level of Trust" + ';')
    csvfile.write('\n')
    for i in range(0,n):
        csvfile.write(str(ListID[i]) + ';')
        csvfile.write(random.choice(List_Nicknames) + ';')
        csvfile.write(random.choice(List_Loc) + ';')
        csvfile.write(str(random.randint(1, 10)) + ';')
        csvfile.write('\n')