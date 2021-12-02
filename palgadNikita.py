from module1 import *
from keyboard import *
palgad=loe_failist_listisse("palk.txt")
inimesed=loe_failist_listisse("inimesed.txt")

while 1:
    print("*"*100, "\nKeskmine - 1\nMinimum - 2\nMaksimum -3\nOtsing -4\nLisa - 5")
    print("Vajuta nuppu==>")

    if read_key()=="1":
        kesk=keskmine(inimesed,palgad)
        print("Keskmine palk on ",summa)

    elif read_key()=="2":
        min_palk,kellel=minimum(palk,inimesed)
        print("Minimaalne palk=> ", min_palk, " Kellel=> ",kellel)
    
    elif read_key()=="3":
        suurim,kellel=suurim(inimesed,palgad)
        print("Maksimaalne palk=> ", suurim, " Kellel=> ",kellel)
    
    elif read_key()=="4":
        vastus=otsing_nimi_jargi(inimesed, palgad)
        print(vastus)

    elif read_key()=="5":
        palgad,inimesed=lisa(palgad,inimesed)
        print(palgad,inimesed)


        




