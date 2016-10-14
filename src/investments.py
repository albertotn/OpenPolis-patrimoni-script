# Test script to gather all data from http://patrimoni.openpolis.it
#
# Aim for this script is to get an easy and understable list of investments from italian politician 
# as csv file (using ; as separator), use Excel or other tool to get data visualization 

# imports
import requests

# global variables
separator = ";"
investments = []

# functions
def dichiarazione( cognome , nome,  url ):
    r = requests.get(url)
    data = r.json()
    s = ""
    for e in data:
        #print(e["partecipazioni_soc"])
        part = e["partecipazioni_soc"]
        for p in part:
            #print(p["denominazione"]+","+p["numero_azioni_quote"])
            s = s+cognome+separator+nome+separator+p["denominazione"]+separator
            investments.append(p["denominazione"])
    return s


# main
anno = 2014
url= "http://patrimoni.openpolis.it/api/politici"
print("Benvenuto in OpenPolis patrimoni script")
print("Questo script scarica i dati delle dichiarazioni dei politici per l'anno "+str(anno)+" e li aggrega per formare una panoramica degli investimenti dei politici nelle aziende cosi come presenti nelle dichiarazioni dei redditi dei politici")
print("\n Scaricamento dati da "+url +" in corso")
r = requests.get(url)
print("Elaborazione in corso...")
data = r.json()
print("Numero politici presenti "+str(len(data)))
for e in data:
    s = ""
    ds = e["dichiarazioni"]
    for d in ds:
        if d["dichiarazione"]is not None and d["anno"] == anno :
            s = ""
            s = s+dichiarazione(e["cognome"],e["nome"],d["dichiarazione"])
            #if s is not None:
            #    print(s)
icount = {}
for i in investments:
    # print(i)
    icount[i] = icount.get(i, 0) + 1
print("Numero aziende "+str(len(icount)))
# get investments as a set
s = set(investments)
print("Aggregazione dati in corso.. \n")
for inv in s:
    if inv is not None: 
        print(inv+";"+str(icount.get(inv)))   

print("Lavoro completato")
