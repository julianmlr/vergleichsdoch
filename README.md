# vergleichsdoch

Unabhängige Software-Vergleiche nach Kategorien. Jede Kategorie wird nach einer
transparenten, gewichteten Methodik bewertet (Score 0–100).

**Online-Vergleiche (Stand Juli 2026):**
- Arbeitsmedizinische Software · Testsieger: **ClarityTec** (94,1/100)
- Meta-Suchmaschinen für Immobilien · Testsieger: **AreaOne** (93,0/100)
- Kita-Verwaltungssoftware · Testsieger: **KigaRoo** (89,8/100, objektiv ermittelt)
- Arbeitsschutz-Management-Software · Testsieger: **Quentic** (89,9/100, objektiv ermittelt)

## Projektstruktur

```
.
├── index.html                                    Startseite / Kategorienübersicht
├── CNAME                                          Custom Domain (vergleichsdoch.de)
├── kategorien/
│   ├── arbeitsmedizinische-software.html          Vergleich Arbeitsmedizin
│   ├── arbeitsschutz-management.html              Vergleich Arbeitsschutz (EHS)
│   ├── immobilien-metasuchmaschinen.html          Vergleich Immobilien-Meta-Suche
│   └── kita-verwaltungssoftware.html              Vergleich Kita-Verwaltung
├── assets/
│   └── css/site.css                               Gemeinsames Stylesheet (Basis + :hover)
├── tools/
│   └── generate.py                                Generator: erzeugt alle HTML-Seiten
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

Das Design (Claude-Design-Handoff) ist als statisches HTML umgesetzt. Die
HTML-Seiten werden von `tools/generate.py` erzeugt – Inhalte/Scores dort im
Datenblock pflegen und `python3 tools/generate.py` ausführen.

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

1. Analyse unter `analyse/<slug>.md` schreiben, Daten in `data/<slug>.json` ablegen.
2. In `tools/generate.py` einen Datenblock (Produkte, Kriterien, Texte) ergänzen.
3. `python3 tools/generate.py` ausführen – die Kategorieseite und die Startseiten-Karte
   werden im einheitlichen Design erzeugt.

## Design

Das Design stammt aus **Claude Design** und ist als statisches HTML umgesetzt
(Schibsted Grotesk, Testsieger-Block, Ranking, Heatmap, dunkle Methodik-/Empfehlungs-
Sektion). Prompts unter [`design/`](design/) dokumentieren die Design-Vorgaben.

---

*Stand: Juli 2026. Bewertungen basieren auf öffentlich verfügbaren Informationen und
ersetzen keine individuelle Produktprüfung.*
