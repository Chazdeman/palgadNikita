from module1 import *
from keyboard import *
palk=loe_failist_listisse("palk.txt")
inimesed=loe_failist_listisse("inimesed.txt")

while 1:
    print("*"*100, "\nKeskmine - A\nMinimum - B\nMaksimum -C\nOtsing -G\nLisa - V")
    print("Vajuta nuppu==>")

    if read_key()=="A":
        kesk_palk=round(keskmine(palk),2)
        print("Keskmine palk on ",kesk_palk)

    elif read_key()=="B":
        min_palk,kellel=minimum(palk,inimesed)
        print("Minimaalne palk=> ", min_palk, " Kellel=> ",kellel)
    
    elif read_key()=="C":
        max_palk,kellel=maksimum(palk,inimesed)
        print("Maksimaalne palk=> ", max_palk, " Kellel=> ",kellel)
    
    elif read_key()=="G":
        vastus=otsing_nimi_jargi(inimesed, palk)
        print(vastus)

    elif read_key()=="V":
        i=adding(palk,inimesed)
        print(palk,inimesed)



        




