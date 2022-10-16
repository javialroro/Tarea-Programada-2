from bs4 import BeautifulSoup as BS
import requests
import pandas as pd

url = "https://atlasdeastronomia.com/astronomos/"
page= requests.get(url)
soup = BS(page.content, "html.parser")

nom= soup.find_all("h2",class_="articletitle")
divs = soup.find_all('div', class_ = 'articledescrip',)
lugares= list()
nombres = list()
lugarlist = list()
texto=list()
annos= list()
desc= list()
descripciones= list()
epoca= list()
llaves= list()

for div in divs:
    if div.strong !=None:
        texto+= [str(div.strong.text)]

for div in divs:
    desc += [div.text]

for des in desc:
    for text in texto:
        if des.find(text) != -1:
            des1=des.replace(text,"")
            descripciones+=[des1.replace("\n","")]


for i in nom:
    nombres.append(i.text)

for i in texto:
    var=list(i.split(","))
    lugares.append(var[0])
    annos.append(var[1])
for i in annos:
    epoca+=[[i.replace(" ",'')]]

for i in range(len(epoca)):
    if "-" in epoca[i][0]:
        epoca[i][0]=epoca[i][0].split("-")
    if len(epoca[i][0])==2:
        epoca[i]=tuple(epoca[i][0])
    else:# len(epoca[i][0])==1:
        epoca[i]+=" "
        epoca[i]=tuple(epoca[i])

#print(epoca)

for i in range(len(epoca)):
    llave=""
    llave+=nombres[i][0]
    for j in epoca[i][0]:
        if j.isdigit()==True:
            llave+=j
    if llave not in llaves:
        llaves.append(llave)

listagrande= list()
for i in range(len(llaves)):
    listagrande.append([nombres[i],lugares[i],epoca[i],descripciones[i]])

def importarAstronomo(cantidad):
    listatupla=[]
    for i in range(0,cantidad):
        tupla = [llaves[i], listagrande[i]]
        listatupla.append(tuple(tupla))
    dicc=dict(listatupla)
    return dicc

print(importarAstronomo(10))


#hola


