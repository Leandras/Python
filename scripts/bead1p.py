# -*- coding: iso-8859-2 -*-
# Név: Breznay Dávid
# EHA-kód: BRDSAAI.ELTE
# E-mail cím: breznaydavid@freemail.hu
import sys,os

def findFile(arver) :
    if os.path.isfile(arver) :
        pass
    else :
        print "Nincs ilyen file!"
        sys.exit(0)

if len(sys.argv) > 1 :
    arver = sys.argv[1]
else :
    arver = raw_input("Kerem az arverezo fajl nevet: ")
    findFile(arver)

def compare(ered,kkar) :
    if ered > kkar :
        kkar=ered
    return kkar;

adatolv=open(arver,'r')
eredir=open("eredmeny.txt",'w')
targy=adatolv.readline()
kkar=0

for ered in adatolv :
    if ered[0:-1].isdigit() :
        if ered > 0 :
            eredmeny=compare(ered,kkar)
            kkar=eredmeny
    else :
        kiir=[targy[0:-1], kkar[0:-1], "\n"]
        eredir.write(" ".join(kiir))
        targy=ered
        kkar=0
kiir=[targy[0:-1], kkar[0:-1], "\n"]
eredir.write(" ".join(kiir))
eredir.close()
adatolv.close()
