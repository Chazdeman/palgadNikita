def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    """
    file=open(file,"r")
    list_=[]
    for stroka in file:
        list_.append(stroka.strip())
    file.close()
    return list_

def lisa(palk:list,inimesed:list):
    """ Lisab inimese ja tema palga,Aga .txt faili ei lisa

    """
    a=input("Sissesta nimi=>")
    inimesed.append(a)
    b=int(input("Sisesta palk=>"))
    palk.append(b)
    return palk,inimesed

def otsing_nimi_jargi(inimesed:list,palk:list):
    nimi=input("Keda otsime?")
    for inimene in inimesed:
        if inimene.upper()==nimi.upper():
            n=inimesed.count(nimi)
            print("Inimene on olemas, selline nimi kohtume",n, "korda")
            b=0
            t=[]
            for i in range(n):
                k=inimesed.index(nimi,b)
                palk=palk[k]
                b+=k+1
                t.append(nimi+str(palk))
                print(nimi, palk)
            break
        else:
            t="Ei ole nimi kirjas"
    return t

def suurim(i:list,p:list):
    """ otsime suurim palk
    :rtype: str,str:
    """
    suurim=max(p)
    b=p.index(suurim)
    kellel=i[b]
    return suurim , kellel

def keskmine(i:list,p:list):
    """Keskmise palka leidmine. Kui ta on loetelus, siis näiame kes saab seda kätte
    :rtype var:
    """
    summa=0
    for palk in p:
        summa+=p
        kesk=summa/len(p)
        print(kesk)
        vahe=0
        if 0<=p.index(kesk)<len(p)-1:
            kesk=i[p.index(kesk)]
            return kesk
        else:
            kesk="Puudub"
            return kesk

"""
def sur():
    palgad=[]
    with open("palk.txt" , "r") as f1:
        for stro in f1:
            palgad.append(stro.strip())
    f=open("inimesed.txt" , "r")
    inimesed=[]
    for stroka in f:
        inimesed.append(stroka.strip())
    f.close()
    palgad_c=palgad.copy()
    palgad_c.sort()
    a=palgad_c[0]
    b=palgad.index(a)
    print(palgad_c)
    return a , inimesed[b]"""