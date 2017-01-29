import random
from time import sleep
		
# creation de la liste de personnes
liste = ["diarra kane",
	"guihini",
	"aboubakrine",
	"jonas hounsou",
	"valerie",
	"oury diallo",
	"aboubacar thiam",
	"bassirou ngom",
	"marelha sane",
	"ousmane sine",
	"famara",
	"kama",
	"emmanuel",
	"papa moussa",
	"khadim lo",
	"ibrahima ndoye",
	"assane seck",
	"fallou ngom",
	"philippe",
	"oumy fall",
	"kany mane",
	"awa diagne",
	"modou ndiaye"]

nbpers =-1
while nbpers < 0 or nbpers > len(liste):
	nbpers= int(raw_input("donnez le nombre de personnes par groupe :"))

nbgroupe = len(liste)/nbpers
reste = len(liste)%nbpers

print "\tdonc il y'aura " + str(nbgroupe+1) + " groupes\n"

masters = "ouietnon"
while masters != "oui" and masters !="non":
	masters = raw_input("y'a -t-il des masters ? :")

if masters == "non" :
	random.shuffle(liste)
	i=1
	while i<=nbgroupe :
		print "groupe "+str(i)
		result = random.sample(liste,nbpers)
		print result
		for item in result :
			liste.remove(item)
		sleep(1)
		i=i+1
	nbpers_res = len(liste)
	print "groupe "+str(nbgroupe+1)
	print liste

elif masters == "oui" :
	nbmasters = int(raw_input("combien de masters ?:"))
	if nbmasters > nbgroupe+1 or nbmasters < 1:
		print "nombre de masters incorrect"
		while nbmasters > nbgroupe+1:
			nbmasters = int(raw_input("combien de masters ?:"))
	masters = list()
	i=1
	while i <= nbmasters :	
		master = "neant" #au hasard
		while master not in liste :
			master = raw_input("donnez le master numero " + str(i)+":")
		masters.append(master)
		i=i+1
	for item in masters :
		liste.remove(item)
	rockys = liste

	random.shuffle(masters)
	random.shuffle(rockys)
	if nbmasters == nbgroupe +1 :
		i=1
		j = nbgroupe
		while i <= j :
			print "groupe "+str(i)
			groupe = list()
			groupe.append(masters[0])
			masters.remove(masters[0])
			result = random.sample(rockys,nbpers-1)
			groupe.append(result)
			for it in result :
				rockys.remove(it)
			print groupe
			sleep(1)
			i=i+1	
		random.shuffle(rockys)
		groupe = list()
		groupe.append(masters[0])
		masters.remove(masters[0])
		result = random.sample(rockys,len(rockys))
		groupe.append(result)
		for it in result :
			rockys.remove(it)
		print "groupe "+str(i)
		print groupe
	else :	
		i=1
		j = nbmasters
		while i <= j :
			print "groupe "+str(i)
			groupe = list()
			groupe.append(masters[0])
			masters.remove(masters[0])
			result = random.sample(rockys,nbpers-1)
			groupe.append(result)
			for it in result :
				rockys.remove(it)
			print groupe
			sleep(1)
			i=i+1	
		random.shuffle(rockys)
		groupe = list()
		nbgroupe_res = len(rockys)/nbpers
		j= 1
		while j <= nbgroupe_res:
			print "groupe "+str(i)
			result = random.sample(liste,nbpers)
			print result
			for item in result :
				liste.remove(item)
			sleep(1)
			j=j+1
			i=i+1
		nbpers_res = len(liste)
		print "groupe "+str(nbgroupe+1)
		print liste
	





