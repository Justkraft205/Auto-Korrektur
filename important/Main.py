import string, sys
line23 = buchstaben3 = buchstaben4 = anzahl = zei = var4 = graja = grana = ready = zur = falsch = korrekt = 0
wort_nummer = var7 = yane = var6 = breaken = 0
wort60 = 1
mein_dict = {}
var1 = var2 = var3 = wort23 = gramata = ""

def check():
    global line23, wort_nummer, lines, wort23, anzahl_wörter, wörter
    ta = True
    line23 = 0
    wörter = eingabe.split()
    anzahl_wörter = len(wörter)
    while ta:
        if wort_nummer >= anzahl_wörter:
            ta = False
            print(eingabe)
            fertig()
        wort23 = wörter[wort_nummer]
        wort23 = wort23.replace(",", "")
        wort23 = wort23.replace(".", "")
        wort23 = wort23.replace("!", "")
        wort23 = wort23.replace("?", "")
        wort23 = wort23.replace("(", "")
        wort23 = wort23.replace(")", "")
        with open("datei.txt", "r") as file:
            lines = file.readlines()
        if (line23+1) < len(lines):
            if wort23 == lines[line23].strip():
                line23 = 0
                wort_nummer += 1
                ta = False
                vorcheck()
            else:
                pass
        else:
            line23 = 0
            gemeinsame_buchstaben_count()
            ta = False
        line23 += 1

def vorcheck():
    print(f"wort gefunden")
    check()

def gemeinsame_buchstaben_count():
    global line23, wort23, zei, wort_nummer, var1, var2, var3, var4, string1, graja, grana, ready, breaken
    ta2 = True
    while ta2:
        string1 = lines[line23].strip()
        string2 = wort23
        buchstaben1 = set(string1.lower())
        buchstaben2 = set(string2.lower())
        gemeinsame_buchstaben = buchstaben1 & buchstaben2
        gemeinsamkeitsanteil = len(gemeinsame_buchstaben) / min(len(buchstaben1), len(buchstaben2))
        anzahl_woerter2 = len(string2.replace(" ", ""))
        anzahl_woerter1 = len(string1.replace(" ", ""))
        buchstaben3 = anzahl_woerter1
        buchstaben4 = anzahl_woerter1
        buchstaben4 -=1
        buchstaben3 +=1
        if gemeinsamkeitsanteil >= 0.8:
            if anzahl_woerter2 == buchstaben3:
                if var4 == 0:
                    var1 = string1
                    var4 += 1
                elif var4 == 1:
                    var2 = string1
                    var4 += 1
                elif var4 == 2:
                    var3 = string1
                    var4 += 1
                zei += 1
                line23 += 1
                ready = 1
            elif  anzahl_woerter2 == buchstaben4:
                if var4 == 0:
                    var1 = string1
                    var4 += 1
                elif var4 == 1:
                    var2 = string1
                    var4 += 1
                elif var4 == 2:
                    var3 = string1
                    var4 += 1
                zei += 1
                line23 += 1
                ready = 1
            elif anzahl_woerter2 == anzahl_woerter1:
                if var4 == 0:
                    var1 = string1
                    var4 += 1
                elif var4 == 1:
                    var2 = string1
                    var4 += 1
                elif var4 == 2:
                    var3 = string1
                    var4 += 1
                zei += 1
                line23 += 1
                ready = 1
            else:
                line23 += 1
                ready = 1
        else:
            line23 += 1
        ready = 0
        if line23 >= len(lines):
            ta2 = False
            breaken  =1
            abfrage()
        if zei == 3:
            var4 = 0
            ta2 = False
            abfrage()

def abfrag2():
    global eingabe, wort23, var1, var2, var3, var4, wort_nummer, mein_dict, var7
    var4 = 0
    string1 = ""
    print(f"wortnummrt:{wort_nummer}")
    print(f"Falsch Geschribenes Wort ist:{wort23}")
    print(f"Ersatz Wörter:{mein_dict}")
    print("Welches wollen sie wählen. 4 ist üebrspringen:")
    einn = input("Welches wort ist das richtige:(1,2,3,4)")
    if einn == "1":
        var1 = mein_dict["1"]
        eingabe = eingabe.replace(wort23,var1)
        var1 = ""
        print("\n" * 100)
        var2 = var3= ""
        var7 = var4 = line23 = 0
        mein_dict = {}
        check()
    elif einn == "2":
        print("Es wird ersetzt")
        var2 = mein_dict["2"]
        eingabe = eingabe.replace(wort23, var2)
        var1 = ""
        Var2 = ""
        var3 = ""
        var7 = 0
        var4 = 0
        line23 = 0
        print("\n" * 100)
        mein_dict = {}
        check()
    elif einn == "3":
        print("Es wird ersetzt")
        var3 = mein_dict["3"]
        eingabe = eingabe.replace(wort23, var3)
        var1 = ""
        Var2 = ""
        var3 = ""
        var4 = 0
        var7 = 0
        line23 = 0
        print("\n" * 100)
        mein_dict = {}
        check()
    elif einn == "4":
        var1 = ""
        Var2 = ""
        var3 = ""
        print("\n" * 100)
        mein_dict = {}
        var4 = 0
        check()

def abfrage():
    global wort23, gramata, line23
    gramata = var1
    incorrect()

def grammatik():
    global wort23, korrekt, falsch, graja, string1, grana, gramata, line23, yane
    yane = 0
    anzahl_buchstaben = len(wort23)
    anzahl_buchstaben6 = len(gramata)
    for zur in range(min(anzahl_buchstaben, anzahl_buchstaben6)):
        buchstaben = wort23[zur]
        buchstaben6 = gramata[zur]
        if buchstaben == buchstaben6:
            korrekt += 1
        else:
            falsch += 1
    if korrekt > falsch:
        yane = 1
        korrekt = 0
        falsch = 0
        korrekt2()
    else:
        yane = 0
        korrekt = 0
        falsch = 0
        korrekt2()

def korrekt2():
    global line23, yane, gramata, var6, zei, var7
    zei = 0
    if yane == 1:
        var7 +=1
        if var7 == 1:
            mein_dict["1"] = gramata
        elif var7 == 2:
            mein_dict["2"] = gramata
        elif var7 == 3:
            mein_dict["3"] = gramata
    else:
        incorrect()
    incorrect()

def incorrect():
    global line23, lines, wort_nummer, anzahl_wörter, var6, variable_value, var1, var2, var3, gramata, korrekt, falsch, zei, wörter
    if var6 > 3:
        if line23 >= len(lines) - 1:
            if var6 > 3:
                wort_nummer += 1
                if wort_nummer > anzahl_wörter:
                    if line23 >= len(lines):
                        wort_nummer -= 2
                        abfrag2()
                    else:
                        var1 = ""
                        var2 = ""
                        var3 = ""
                        gemeinsame_buchstaben_count()
                else:
                    line23 = 0
                    check
        else:
            line23 += 1
            var6 = 0
            var1 = ""
            var2 = ""
            var3 = ""
            gemeinsame_buchstaben_count()
    else:
        gramata = ""
        if var6 == 1:
            gramata = var1
        if var6 == 2:
            gramata = var2
        if var6 == 3:
            gramata = var3
        var6 += 1
        grammatik()

def fertig():
    print("Fertig")
    sys.exit()

eingabe = input("Dein Text zum Korrigirern:")
check()
