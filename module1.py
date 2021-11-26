def adding(palk,inimesed):
    """ Добавляет человека и его зарплату
    """
    add=input("Sissesta nimi=>")
    inimesed.append(add)
    add_palk=int(input("Sisesta palk=>"))
    palk.append(add_palk)
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
                #print(nimi, palk)
        else:
            t="Ei ole nimi kirjas"
    return t

def maksimum(palk,inimesed):
    max_palk=palk[0]
    kellel=inimesed[0]
    for p in palk:
        if p>max_palk:
            max_palk=p
            i=palk.index(max_palk)
            kellel=inimesed[i]
    return max_palk, kellel   

def minimum(palk,inimesed):
    min_palk=palk[0]
    kellel=inimesed[0]
    for p in palk:
        if p<min_palk:
            min_palk=p
            i=palk.index(min_palk)
            kellel=inimesed[i]
    return min_palk, kellel    
    
def keskmine(palk):
    summa=0
    n=len(palk)
    for p in palk:
        summa+=p
    summa=summa/n
    return summa

def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    """
    file=open(file,"r")
    list_=[]
    for stroka in file:
        list_.append(stroka.strip())
    file.close()
    return list_