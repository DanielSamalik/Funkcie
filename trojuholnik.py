def trojuholnik(vyska):
    vyska=vyska+1
    for i in range(vyska):
        for o in range(vyska-i):
            print(end=" ")
        for p in range(i):
            print("*",end=" ")
        print(end="\n")
trojuholnik(6)