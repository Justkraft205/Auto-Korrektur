import string
import sys
# Initiale Variablen
line23 = buchstaben3 = buchstaben4 = anzahl = zei = var4 = graja = grana = ready = zur = falsch = korrekt = 0
wort_nummer = 0
wort60 = 1
var1 = var2 = var3 = wort23 = ""

def check():
    global line23, wort_nummer, lines, wort23
    print(f"Erstes Wort:{wort_nummer}, ist:{wort23}")
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
        print(f"Wort23:{wort23}, lines:{lines[line23].strip()}, lines:{len(lines)}, line23:{(line23 + 1)} ")
        line23 += 1

def vorcheck():
    check()


def gemeinsame_buchstaben_count():
    global line23, wort23, zei, wort_nummer, var1, var2, var3, var4, string1, graja, grana, ready
    line23 = 0
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
               # print(f"Gefunden! 80 % oder mehr der Buchstaben sind gleich. In Line:{line23}:1")
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
            print(f"line23:{line23}, buchstaben1:{buchstaben1}, buchstaben2:{buchstaben2}")
        ready = 0
        if line23 >= len(lines):
            wort_nummer += 1
            ta2 = False
            abfrage()
        if zei == 3:
            ta2 = False
            abfrage()

def abfrage():
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
eingabe = input("Dein Text zum Korrigirern:")

def grammatik():
    global wort23, var1, korrekt, falsch, graja, string1, grana
    print(f"Debug: grammatik() aufgerufen mit wort23={wort23}, var1={string1}")

    anzahl_buchstaben = len(wort23)
    anzahl_buchstaben6 = len(string1)
    print(f"buchstaben: {anzahl_buchstaben}, anzhal6: {anzahl_buchstaben6}")

    for zur in range(min(anzahl_buchstaben, anzahl_buchstaben6)):
        buchstaben = wort23[zur]
        buchstaben6 = string1[zur]
        print(f"buchstaben: {buchstaben}, buchstaben6: {buchstaben6}")
        if buchstaben == buchstaben6:
            korrekt += 1
        else:
            falsch += 1

    print(f"Ergebnisse: korrekt={korrekt}, falsch={falsch}")

    if korrekt > falsch:
        graja = 1
        print("Debug: graja auf 1 gesetzt, rufe gemeinsame_buchstaben_count() auf")
        falsch  = 0
        korrekt = 0
        gemeinsame_buchstaben_count()

    else:
        print("Debug: graja bleibt unverändert")
        grana = 1
        falsch = 0
        korrekt = 0
        gemeinsame_buchstaben_count()

def fertig():
    print("Fertig")
    sys.exit()
check()
