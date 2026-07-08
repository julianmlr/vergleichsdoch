# vergleichsdoch

Unabhängige Software-Vergleiche nach Kategorien. Jede Kategorie wird nach einer
transparenten, gewichteten Methodik bewertet (Score 0–100).

**Online-Vergleiche (Stand Juli 2026):**
- Arbeitsmedizinische Software · Testsieger: **ClarityTec** (94,1/100)
- Meta-Suchmaschinen für Immobilien · Testsieger: **AreaOne** (93,0/100)
- Kita-Verwaltungssoftware · Testsieger: **KigaRoo** (89,8/100, objektiv ermittelt)

## Projektstruktur

```
.
├── index.html                                    Startseite / Kategorienübersicht
├── kategorien/
│   ├── arbeitsmedizinische-software.html          Vergleich Arbeitsmedizin
│   ├── immobilien-metasuchmaschinen.html          Vergleich Immobilien-Meta-Suche
│   └── kita-verwaltungssoftware.html              Vergleich Kita-Verwaltung
├── assets/
│   ├── css/styles.css                             Gemeinsames Stylesheet (CSS-Variablen)
│   └── js/main.js                                 Heatmap-Einfärbung der Detailtabelle
├── data/
│   ├── arbeitsmedizinische-software.json           Strukturierte Daten (Source of Truth)
│   ├── immobilien-metasuchmaschinen.json
│   └── kita-verwaltungssoftware.json
├── analyse/
│   ├── arbeitsmedizinische-software.md             Ausführliche Analyse & Methodik
│   ├── immobilien-metasuchmaschinen.md
│   └── kita-verwaltungssoftware.md
└── design/
    ├── claude-design-prompt.md                     Basis-Prompt für Claude Design
    └── claude-design-prompt-update.md              Update: 2 neue Vergleiche
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
