#########"liste des dictionnaires:
########"exercice1
# MEEE
"""
def find(chaine):
    liste=[]
    for i in chaine:
        liste.append(i)
    dic={}
    for i in liste:
        d=liste.count(i)
        dic.update({i:d})
    return dic
chaine="bounjour"
"""

#EXERCICE1

def find(chaine):
    dic={}
    for i in chaine :
        dic[i]=chaine.count(i)
    return dic 


#exercice2

def dic(chaine):
    d={}
    l=chaine.splitlines()
    for i in l:
        infos=i.split(";")
        d[int(infos[0])]=infos[1]+" "+infos[2]
    return d     

#exercice3
##########b
def SVentes(dic):
    d=0
    for i in dic :
        d+=dic[i]
    return d
############c
def nom_vendeur(dictionnaire):
    m=max(dictionnaire.values())
    for i in dictionnaire:
        if dictionnaire[i]==m:
            return i
############"d
def Supprime_bas_vendeur(dictionnaire):
    mini=min(dictionnaire.values())
    l=[]
    for i in dictionnaire:
        if d[i]==min :
            l.append(i)
    for i in l:
        d.pop(i)
#e
def Supprimer(dictionnaire,nomv):
    d.pop(nomv)

#g
def Modifier(d,nomv):
    #dic[cle]=nv_valeur
    d[nomv]=int(input("Entrez lz nouveau nombre des ventes :"))

#f
def Dict_Trie(dictionnaire):
    d_trie={}
    for i in sorted(dictionnaire.values()):
        for j in dicrionnaire:
            if d[j]==i :
                d_trie[j]=i
    return d_trie
#methode2
"""
TEST={"Aupont":14, "Cervy":19, "Beoffroy":177, "Nayec":21}
print(sorted(TEST,reverse=True))
print(sorted(TEST,key=TEST.get,reverse=True))
"""
#methode3
"""for i in d.values():
    print(i) # i prend les valeurs
    for j in d :
        if i == d[j] :
            print(j)"""

#h
def enregistrer_ventres(dic):
    f=open('ventes.txt',"w+")
    for i,j in dic.items():
        f.write(f"{i} => {j} \n")
    f.close()

######################""programme principale

while True:
    choix=int(input("""\n 1 : Ajouter les ventes 
    2 : Afficher les ventes.
    3 : Afficher les ventes triées.
    4 : Modifier les ventes d’un vendeur .
    5 : Rechercher les ventes d’un vendeur .
    6 : Supprimer un vendeur .
    7 :Afficher le nombre total des ventes
    8 :Afficher le vendeur qui a réalisé plus de vente
    9 : Enregistrer dans un fichier 
    10: Quittez le programme 
    Tapez votre choix :"""))
    ventes={"Dupont":14, "Hervy":19, "Geoffroy":15, "Layec":21}
    if choix==1:
        nb=int(input("entrez le nombres des vendeurs:"))
        for i in range(nb):
            nom=input("entre le nom de vendeur")
            ventes[nom]=int(input(f"Entrez le nombre de ventes {nom} :"))
        
    elif choix==2:
        for i ,j in ventes.items() :
            print(f"vendeur :{i}=> le nombres des ventes {j}")
    
    elif choix==3:
        for i ,j in Dict_Trie(ventes).items() :
            print(f"vendeur :{i}=> le nombres des ventes {j}")
 
    elif choix==4:
        nomv=input("entrez le nom de vendeur:")
        Modifier(ventes,nomv)
    
    elif choix==5:
        nomv=input("entrez le nom de vendeur:")
        if nomv in ventes:
                print("le vendeure de",i,"est",ventes[i])
        else:
            print("ce valeur n'exicte pas")
                
    elif choix==6:
        nomv=input("entrez le nom de vendeur:")
        Supprimer(ventes,nomv)
        
    elif choix==7:
        print("le nombres totale des ventes et ",SVentes(ventes))
        
    elif choix==8:
        print("le meilleuer vendeur est ",nom_vendeur(ventes))
        
    elif choix==9:
        enregistrer_ventres(ventes)         
    else:
        print("fin")
        break

#exercice4
def remlire(d):#d il existe dans p.principale
    nb=int(input("entrez le nombre des stagiare :"))
    nbm=int(input("entrez le nombres des module:"))
    liste=[]
    for i in range(nbm):
         liste.append(input("entrez le nome de modues:"))
    for i in range(nb):
        nom=input("entrez le nom de stagiare :")
        mod={}
        for j in liste:
            note=float(input("entrz le notes :"))
            mod[j]=note
        d[nom]=mod
        
def moyeene(dic):
    for i,j in d:
       m= sum(j.values())/len(j)
       print(f"la moyenne du stagiare {i} est {m}")

def supprimer(d,nom):
    if nom in d:
        d.pop(nom)
    else:
        print("ce stagiaire n'est existe pas")

def moyen_classe():
    mc=0
    for i,j in d.items():
       m= sum(j.values())/len(j)              # la moyenne de chaque stqgiaire 
       mc+=m
    return mc/len(d)


def trier(dic ):
    d={}
    for i in sorted(dic.keys()):
        d[i]=dic[i]
    return d

def modifier(d,nom):
    if nom in d:
       mod={}
       for i in d[noms]:
           d[noms][i]=float(input(f"entrez la notes du module{i}"))
       return d 
    else:
        print("se stagoares n'execita pas ")


#7
def premieR (d):
    ds={}
    for i , j in d.items():
        m=sum(j.values())/len(j)
        ds[i]=m
    return max(ds,key=ds.get)

#8
def notMaxe(d):
    for i , j in d.items():
        nots=max(j.values())
        nom=max(j,key=j.get)
        print(f"le stagiares {i} a eu la note maximale {nots}dans le module :{nom}")

#09
def moyenneparmodule(d, nom):
    for i , j in d.items():
        di=j
        break
    if nom in di :
        mc=0
        for i in d:
            mc+=d[i][nom]
        return mc/len(d)
    else:
        return "nom in vlide"

#######################################exercice5
#1
def remplir(d):#d el exicicte dans programe principale 
    nb=int(input("entrez le nmbre des elements du dictionnaire:" ))
    for i in range(nb):
        code=input("entrez la reference du produit:")
        nom=input("entrez le nom du produit:")
        pa=float(input("entrez le prix d'achats:"))
        pv=float(input("entrez le prix de vente:"))
        qte=int(input("entrez la quantite en stock:")) 
        d.update({code:[nom,pa,pv,qte]})
"""d[cod]=[nom,pa,pv,qte]"""

##2
def rechercher(d,cp):
    return cp in d

##3
def modifier(d,cp):
    if cp in d:
        nom=input("entrez le nv nom du produit:")
        pa=float(input("entrez le nv prix d'achats:"))
        pv=float(input("entrez le nv prix de vente:"))
        qte=int(input("entrez la nv quantite en stock:")) 
        d[cp]=[nom,pa,pv,qte]
    else:
        print("ce produit n'existe pas")
        
##4
def supprimer_produits(d):
    dc=d.copy()
    for i,j in dc.items():
        if j[-1]==0:
            d.pop(i)
            
##5
def nbreprdstock(d):
    s=0
    for i in d.values():
        s+=i[-1]
    return s
####
##6-a
def remplirdclt(d , dp):
    nbclt=int(input("entrez le nombre des clients:"))
    for i in range(nbclt):
        cc=input("entrez le code du client:")
        nba=int(input("entrez le nombre des produits achetez:"))
        prd={}
        for j in range(nba):
            ref=input("entrez la reference du produit achetez:")
            if ref in dp:
                qte=int(input("entrez la quantite achetez:"))
                prd[ref]=qte
            else:
                print("ce produit n'execite pas")
        d[cc]=prd

##6-b
def prix_a_payer(dp,dc):
    for i,j in dc.items(): #i: cle / j :valeur(dictionnaire)
        p=0
        for k,l in j.items(): # k: cle (reference de produits) / l:valeur ( qte achete du prd)
            p+=dp[k][2]*l
        print(f"le client {i} a paye :{p} dh ")

###6-c
def prix_totale(dp,dc):
    p=0
    for i,j in dc.items(): #i: cle / j :valeur(dictionnaire)
        for k,l in j.items(): # k: cle (reference de produits) / l:valeur ( qte achete du prd)
            p+=dp[k][2]*l
    return p

#77777
def info_produits(dic):
    inf=open("infoProduit.txt","w+")
    k=0
    for i,j in dic.items():
            inf.write(f"___________________\n code de produit = > {i} \n  nom => {j[k]} \n prix d'achat => {j[k+1]} \n prix de ventes => {j[k+2]} \n quantite dans stock =>{j[k+3]} \n")
    print(inf.read())
    inf.close()


