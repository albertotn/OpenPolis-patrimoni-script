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
            # +separator+p["numero_azioni_quote"]
            investments.append(p["denominazione"])
    return s


# main
r = requests.get("http://patrimoni.openpolis.it/api/politici")
data = r.json()
first = data[0]
for e in data:
    s = ""
    ds = e["dichiarazioni"]
    for d in ds:
        if d["dichiarazione"]is not None and d["anno"] == 2014 :
            s = ""
            s = s+dichiarazione(e["cognome"],e["nome"],d["dichiarazione"])
            #if s is not None:
            #    print(s)
icount = {}
for i in investments:
    # print(i)
    icount[i] = icount.get(i, 0) + 1
# get investments as a set
s = set(investments)
for inv in s:
    print(inv+";"+str(icount.get(inv)))   


