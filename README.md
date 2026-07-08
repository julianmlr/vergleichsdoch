# vergleichsdoch

Unabhängige Software-Vergleiche nach Kategorien. Jede Kategorie wird nach einer
transparenten, gewichteten Methodik bewertet (Score 0–100).

**Erste Kategorie:** Arbeitsmedizinische Software (2026) · Testsieger: **ClarityTec** (94,1/100)

## Projektstruktur

```
.
├── index.html                                  Startseite / Kategorienübersicht
├── kategorien/
│   └── arbeitsmedizinische-software.html        Vergleichsseite Arbeitsmedizin
├── assets/
│   ├── css/styles.css                           Gemeinsames Stylesheet (CSS-Variablen)
│   └── js/main.js                               Heatmap-Einfärbung der Detailtabelle
├── data/
│   └── arbeitsmedizinische-software.json         Strukturierte Daten (Source of Truth)
├── analyse/
│   └── arbeitsmedizinische-software.md           Ausführliche Analyse & Methodik
└── design/
    └── claude-design-prompt.md                   Fertiger Prompt für Claude Design
```

## Ansehen

Reines statisches HTML – keine Build-Schritte nötig. Lokal öffnen:

```bash
python3 -m http.server 8000
# dann http://localhost:8000/ im Browser
```

## Methodik

7 relevante Lösungen, 9 gewichtete Kriterien (Skala 0–10), gewichteter Gesamtscore
auf 100 skaliert. Details und Quellen in
[`analyse/arbeitsmedizinische-software.md`](analyse/arbeitsmedizinische-software.md).
Die Bewertungsdaten liegen maschinenlesbar in
[`data/arbeitsmedizinische-software.json`](data/arbeitsmedizinische-software.json).

## Neue Kategorie hinzufügen

1. Datendatei unter `data/<slug>.json` anlegen (Kriterien, Gewichte, Produkte, Scores).
2. Analyse unter `analyse/<slug>.md` schreiben.
3. Vergleichsseite `kategorien/<slug>.html` erstellen (Struktur der Arbeitsmedizin-Seite als Vorlage).
4. Karte auf der Startseite (`index.html`) ergänzen.

## Design

Das finale Design wird über den Prompt in
[`design/claude-design-prompt.md`](design/claude-design-prompt.md) mit **Claude Design**
erzeugt. Das mitgelieferte Stylesheet ist eine funktionale Basis.

---

*Stand: Juli 2026. Bewertungen basieren auf öffentlich verfügbaren Informationen und
ersetzen keine individuelle Produktprüfung.*
