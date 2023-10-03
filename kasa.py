
nakup =[]
utrata = 0
loop = True

while loop:
    print("")
    print("pečivo")
    print("ovoce")
    print("maso")
    print("konec")
    print("Napiš, co chceš kupovat?")
    vyber = input()

    if vyber == "pečivo":
        print("Napiš co chceš: ")
        print("chleba - 50kč")
        print("rohlík - 3kč")
        print("houska - 6kč")

        polozka = input()
        nakup.append(polozka)

        if polozka == "chleba":
           utrata = utrata + 50
        elif polozka == "rohlík":
            utrata = utrata + 3
        elif polozka == "houska":
            utrata = utrata + 6
        else:
            print("Taková položka není zkus to znova")  
        continue


    elif vyber == "ovoce":
        print("Napiš co chceš: ")
        print("jablko - 10kč")
        print("banán - 8kč")
        print("hruška - 7kč")

        polozka = input()
        nakup.append(polozka)

        if polozka == "jablko":
           utrata = utrata + 10
        elif polozka == "banán":
            utrata = utrata + 8
        elif polozka == "hruška":
            utrata = utrata + 7
        else:
            print("Taková položka není zkus to znova") 
        continue


    elif vyber == "maso":
        print("Napiš co chceš: ")
        print("kuřecí - 150kč")
        print("jehněčí - 200kč")
        print("vepřové - 300kč")

        polozka = input()
        nakup.append(polozka)

        if polozka == "kuřecí":
           utrata = utrata + 150
        elif polozka == "jehněčí":
            utrata = utrata + 200
        elif polozka == "vepřové":
            utrata = utrata + 300
        else:
            print("Taková položka není zkus to znova") 
        continue

    elif vyber == "konec":
        loop = False
        print(f"celkem to bude:  {utrata}  Kč.")
        print("Tvé zboží:")
        print(*nakup)

    else:
        print("Toto ve výběru není, zkus to znova:")
