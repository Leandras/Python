import re
import string
import os

i=0
max = 0
with open("adatok.txt") as adatbe:
  adatok = adatbe.readlines()
kimeno=open("eredmeny.txt",'w')
def szamok(input):
   return any(char.isdigit() for char in input)
for line in adatok:
 	if szamok(adatok[i]):
		ar = re.findall("\d+",adatok[i])
		nev = re.findall("\w+",adatok[i])
		print nev, ar
		if ar>max:	
		   max=''.join(ar)		 
	else : 
		if i>0:
		 ki=targy ,"------", max
		 print ki
		 kimeno.writelines(ki)
		targy=adatok[i]
		max=0
	i+=1
kimeno.close()
print "ökom bákom áá"