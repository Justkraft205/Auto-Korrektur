import string

# Initiale Variablen
line23 = 0
wort_nummer = 0

def check():
    global line23, wort_nummer
    ta = True
    # Text in Wörter aufteilen
    wörter = text.split()
    anzahl_wörter = len(wörter)
    while ta:
        # Wenn alle Wörter abgearbeitet sind, beende die Schleife
        if wort_nummer >= anzahl_wörter:
            ta = False
            break
        wort23 = wörter[wort_nummer]
        # Entferne alle Satzzeichen
        wort23 = wort23.translate(str.maketrans("", "", string.punctuation))
        # Datei öffnen und Zeilen einlesen (im Encoding `utf-8`)
        with open("datei.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        # Überprüfen, ob `line23` innerhalb des Indexbereichs von `lines` liegt
        if line23 < len(lines):
            # Wortvergleich in der Datei
            if wort23 == lines[line23].strip():
                print("gefunden")
                line23 = 0
                wort_nummer += 1
            else:
                pass
        else:
            # Wenn `line23` außerhalb des Bereichs ist, füge leere Zeilen hinzu
            while len(lines) <= line23:
                lines.append("\n")  # Leere Zeilen hinzufügen, wenn mehr Zeilen benötigt werden
            wort23 = wort23.translate(str.maketrans("", "", string.punctuation))
            # Wort in die entsprechende Zeile schreiben
            lines[line23] = wort23 + "\n"
            with open("datei.txt", "w", encoding="utf-8") as file:
                file.writelines(lines)
            print(f"Wort '{wort23}' wurde in Zeile {line23 + 1} gespeichert.")
            wort_nummer += 1
            line23 = 0
        line23 += 1

# Benutzer zur Eingabe von Wörtern auffordern
text = input("Bitte gib die Wörter ein (getrennt durch Leerzeichen): ")
check()
