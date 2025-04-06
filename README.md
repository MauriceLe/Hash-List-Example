# Hash-List Beispiel

Dieses Projekt demonstriert ein einfaches Beispiel zur Implementierung einer Hash-Liste mit einer stackartigen Struktur zur Verwaltung von Studenten-Daten in Python. Der Code implementiert grundlegende Operationen wie Hinzufügen, Entfernen, Modifizieren und Anzeigen von Studenten unter Verwendung einer Hash-basierten Liste.

## Anforderungen

- Python 3.x

## Projektstruktur

- **main.py**: Das Hauptskript, das die Benutzeroberfläche verwaltet und Operationen auf der `HashList` durchführt.
- **src/Student.py**: Definiert die `Student`-Klasse, die Informationen über Studenten (Vorname, Nachname, ID) speichert.
- **src/HashList.py**: Definiert die `HashList`-Klasse, die die Hash-Tabelle implementiert und Operationen wie Hinzufügen, Löschen und Modifizieren unterstützt.
- **src/StackList.py**: Implementiert eine Stack-Struktur zur Handhabung von Studenten mit demselben Nachnamen (Kollisionen in der Hash-Tabelle).
- **src/StackElement.py**: Repräsentiert ein einzelnes Element in der `StackList`, das einen Studenten und einen Verweis auf das nächste Element im Stack enthält.
- **Data.txt**: Eine Datei, die Studenten-Daten (Vorname, Nachname, ID) enthält, um die Hash-Liste zur Laufzeit zu befüllen.

## Verwendung

1. **Programm ausführen**:
   Um das Programm zu starten, führen Sie folgenden Befehl aus:
   ```bash
   python main.py
   ```

2. **Menüoptionen**:
   Nach dem Start des Programms wird ein Menü angezeigt, in dem Sie eine der folgenden Optionen auswählen können:
   - `1` – Neuen Studenten hinzufügen.
   - `2` – Einen Studenten nach Nachnamen entfernen.
   - `3` – Den Nachnamen eines Studenten ändern.
   - `4` – Alle Studenten anzeigen.
   - `5` – Programm beenden.

3. **Hinzufügen von Studenten**:
   Beim Hinzufügen eines Studenten werden Sie nach dem Vornamen, Nachnamen und der ID gefragt. Der Student wird dann der `HashList` hinzugefügt.

4. **Entfernen von Studenten**:
   Um einen Studenten zu entfernen, müssen Sie nur den Nachnamen eingeben.

5. **Modifizieren von Studenten**:
   Um den Nachnamen eines Studenten zu ändern, müssen Sie den alten Nachnamen und den neuen Nachnamen angeben.

6. **Datei einlesen**:
   Beim Start des Programms wird die Datei `Data.txt` eingelesen und die Hash-Liste mit den Studenten-Daten befüllt.

## Code-Überblick

### `Student.py`

Die `Student`-Klasse speichert den Vornamen, Nachnamen und die ID eines Studenten. Sie stellt Methoden zur Verfügung, um den Nachnamen des Studenten zu holen und zu setzen sowie die Student-Objekte in eine string-basierte Darstellung zu konvertieren.

### `HashList.py`

Die `HashList`-Klasse implementiert die Hash-Tabelle, die die Studenten-Daten speichert. Die Größe der Tabelle wird bei der Initialisierung festgelegt. Die Methode `hash` erzeugt einen Hash-Wert für den Nachnamen eines Studenten. Die Klasse unterstützt das Hinzufügen, Löschen und Modifizieren von Studenten-Daten und verarbeitet Kollisionen mithilfe einer `StackList`.

### `StackList.py` und `StackElement.py`

Diese Klassen definieren die Stack-Struktur, die zur Behandlung von Hash-Kollisionen verwendet wird. Wenn mehrere Studenten denselben Nachnamen haben, werden sie im Stack an demselben Index der Hash-Tabelle gespeichert. Die `StackList`-Klasse verwaltet den Stack, und `StackElement` repräsentiert einzelne Elemente (Studenten) im Stack.

## Beispiel

Hier ein Beispiel, wie das Programm funktioniert:

```text
Reading file took 50ms.


[1 = Add student]
[2 = Remove student]
[3 = Modify student]
[4 = Show students]
[5 = End]

Select an option: 1
First Name: John
Last Name: Doe
ID: 123

[1 = Add student]
[2 = Remove student]
[3 = Modify student]
[4 = Show students]
[5 = End]

Select an option: 4
HASHTABLE
1: (John,Doe,123) ->
TAIL
```

## Funktionsweise

#### `readFile()`
Liest die Datei `Data.txt` ein und befüllt die Hash-Liste mit Studenten-Objekten. Es misst auch die Zeit, die benötigt wird, um die Datei zu lesen und den zuletzt hinzugefügten Studenten zu löschen.

#### `printMenu()`
Zeigt das Hauptmenü mit den verfügbaren Optionen an.

#### `userInput()`
Verarbeitet die Benutzereingabe und ordnet sie der entsprechenden Funktion zu.

#### `options(i)`
Ordnet die Benutzereingabe einer bestimmten Option (Hinzufügen, Löschen, Modifizieren, Anzeigen oder Beenden) zu.

#### `add()`
Fügt einen neuen Studenten zur Hash-Liste hinzu, indem der Benutzer nach dem Vornamen, Nachnamen und der ID des Studenten gefragt wird.

#### `delete()`
Entfernt einen Studenten aus der Liste anhand des Nachnamens.

#### `modify()`
Ändert den Nachnamen eines bestehenden Studenten.

#### `show()`
Zeigt alle Studenten an, die derzeit in der Hash-Liste gespeichert sind.

Dieses Projekt ist unter der MIT-Lizenz lizenziert – siehe die [LICENSE](LICENSE)-Datei für Details.

---

Viel Spaß beim Arbeiten mit dieser Hash-basierten Listen-Implementierung in Python!
