import string
import sys
# Initiale Variablen
line23 = buchstaben3 = buchstaben4 = anzahl = zei = var4 = graja = grana = ready = zur = falsch = korrekt = 0
wort_nummer = 0
gramata = ""
wort60 = 1
var1 = var2 = var3 = wort23 = ""

def check():
    global line23, wort_nummer, lines, wort23, anzahl_wörter
    ta = True
    # Text in Wörter aufteilen
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
        if (line23 + 1) < len(lines):
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
       # print(f"Wort23:{wort23}, lines:{lines[line23].strip()}, lines:{len(lines)}, line23:{(line23 + 1)} ")
        line23 += 1

def vorcheck():
    check()


def gemeinsame_buchstaben_count():
    global line23, wort23, zei, wort_nummer, var1, var2, var3, var4, string1, graja, grana, ready
    #line23 = 0
    print(f"line23:{line23}")
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
            print(f"buchstaben1:{len(buchstaben1)}, buchstaben2:{len(buchstaben2)}, gemeinsam:{gemeinsamkeitsanteil}, wort23:{lines[line23].strip()}")
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
            line23 += 1  # Gehe zur nächsten Zeile
        ready = 0
        if line23 >= len(lines):
            #wort_nummer += 1
            ta2 = False
            abfrage()
        if zei == 3:
            print("jaj")
            ta2 = False
            abfrage()

def abfrag2():
    global eingabe, wort23, var1, var2, var3, var4, wort_nummer
    var4 = 0
    string1 = ""
    print(f"Falsch Geschribenes Wort ist:{wort23}")
    print(f"Ersatz Wort1:{var1}")
    print(f"Ersaz Wort2:{var2}")
    print(f"Ersatz Wort3:{var3}")
    print("Welches wollen sie wählen. 4 ist üebrspringen:")
    einn = input("Welches wort ist das richtige:(1,2,3,4)")
    if einn == "1":
        print(f"Es wird ersetzt, wort23:{wort23}, var1,{var1}")
        print(var1)
        eingabe = eingabe.replace(wort23,var1)
        var1 = ""
        print("\n" * 100)
        Var2 = ""
        var3 = ""
        var4 = 0
        wort_nummer += 1
        check()
    elif einn == "2":
        print("Es wird ersetzt")
        eingabe = eingabe.replace(wort23, var2)
        var1 = ""
        Var2 = ""
        var3 = ""
        var4 = 0
        print("\n" * 100)
        wort_nummer += 1
        check()
    elif einn == "3":
        print("Es wird ersetzt")
        eingabe = eingabe.replace(wort23, var3)
        var1 = ""
        Var2 = ""
        var3 = ""
        var4 = 0
        print("\n" * 100)
        wort_nummer += 1
        check()
    elif einn == "4":
        var1 = ""
        Var2 = ""
        var3 = ""
        print("\n" * 100)
        var4 = 0
        wort_nummer += 1
        check()

def abfrage():
    global wort23, gramata
    print(line23)
    gramata = var1
    grammatik()

eingabe = input("Dein Text zum Korrigirern:")

def grammatik():
    global wort23, var1, korrekt, falsch, graja, string1, grana, gramata, line23
    print(f"var1:{var1}, var2:{var2}, var3:{var3}, line23:{line23}")
    print(f"Debug: grammatik() aufgerufen mit wort23={wort23}, var1={gramata}")

    anzahl_buchstaben = len(wort23)
    anzahl_buchstaben6 = len(gramata)
    #print(f"buchstaben: {anzahl_buchstaben}, anzhal6: {anzahl_buchstaben6}")

    for zur in range(min(anzahl_buchstaben, anzahl_buchstaben6)):
        buchstaben = wort23[zur]
        buchstaben6 = gramata[zur]
       # print(f"buchstaben: {buchstaben}, buchstaben6: {buchstaben6}")
        if buchstaben == buchstaben6:
            korrekt += 1
        else:
            falsch += 1

    print(f"Ergebnisse: korrekt={korrekt}, falsch={falsch}")
    if korrekt > falsch:
        #print("Debug: Ja")
        falsch  = 0
        korrekt = 0
        korrekt2()
    else:
        #print("Debug: Nein")
        falsch = 0
        korrekt = 0
        incorrect()

def korrekt2():
    global line23
    abfrag2()

def incorrect():
    global line23, lines, wort_nummer, anzahl_wörter
    if line23 >= len(lines):
        print("Fertig, keine übereinstimmung. Springt Automatisch zum Nächsten Wort")
        if wort_nummer >= anzahl_wörter:
            print("Fertig")
        else:
            line23 = 0
            wort_nummer +=1
            gemeinsame_buchstaben_count()

        sys.exit
    else:
        line23 +=1
        gemeinsame_buchstaben_count()

def fertig():
    print("Fertig")
    sys.exit()
check()
