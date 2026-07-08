# Design-Prompt für Claude Design – vergleichsdoch

> Diesen Prompt in **Claude Design** einfügen, um das finale, hochwertige Design der
> Vergleichsseite zu erzeugen. Die Inhalte, Scores und Rangfolge stammen aus
> `data/arbeitsmedizinische-software.json` bzw. `analyse/arbeitsmedizinische-software.md`.
> Der Prompt ist so formuliert, dass er direkt kopiert werden kann.

---

## PROMPT (zum Kopieren)

Du bist ein Senior Product- und Webdesigner. Entwirf und baue eine **hochwertige,
vertrauenswürdige Vergleichs-Website** namens **„vergleichsdoch"**. Das Portal
vergleicht Software transparent nach Kategorien. Die erste Kategorie ist
**Arbeitsmedizinische Software**. Liefere sauberes, responsives HTML/CSS (optional
minimales JS), in sich geschlossen und ohne externe Abhängigkeiten außer Google Fonts.

### Marke & Tonalität
- **Name:** vergleichsdoch (Wortspiel: „vergleichs doch" / „vergleich's doch")
- **Charakter:** unabhängig, sachlich, kompetent, aufgeräumt – wie ein seriöses
  Fachmagazin, nicht wie eine Affiliate-Schleuderseite. Vertrauen ist die wichtigste
  Design-Währung.
- **Sprache:** Deutsch (Sie-Ansprache im Fließtext vermeiden, neutral formulieren).
- **Zielgruppe der ersten Kategorie:** Betriebsärzte, Leitungen arbeitsmedizinischer
  Dienste, HSE-/HR-Verantwortliche in Unternehmen. Fachlich, entscheidungsorientiert.

### Design-System
- **Farben:** kühles, vertrauensbildendes Blau als Primärfarbe (#0b5cab), Teal als
  Akzent (#0f9d8c), warmes Gold nur für den Testsieger/Rang 1 (#e0a400). Neutrale
  Graustufen für Flächen und Text, viel Weißraum. Heller Hintergrund (#f6f8fb),
  weiße Karten. Optional zusätzlich ein eleganter Dark Mode.
- **Typografie:** moderne, gut lesbare Sans-Serif (z. B. „Inter"). Große, klare
  Überschriften mit leicht negativem Letter-Spacing; großzügige Zeilenhöhe im Fließtext.
- **Formen:** abgerundete Ecken (12–16 px), weiche, dezente Schatten, dünne Linien
  (#e3e9f2). Nichts Verspieltes.
- **Datenvisualisierung:** Scores als Zahlen + optionale Balken/Heatmap. Der Testsieger
  wird durchgängig hervorgehoben (Gold-Medaille 🥇, farbige Karte, hervorgehobene Spalte).

### Seitenstruktur

**1. Startseite (`index.html`)**
- Sticky-Header mit Logo „vergleichs**doch**" und Navigation (Kategorien, Arbeitsmedizin, Methodik).
- Hero: starke Headline zum Nutzenversprechen („Die richtige Software finden – ohne
  Marketing-Nebel"), kurzer Lead-Text, primärer CTA zur Arbeitsmedizin-Kategorie.
- Abschnitt „Kategorien": Karten-Grid. Aktiv: **Arbeitsmedizinische Software**
  (Badge „Testsieger: ClarityTec"). Zwei weitere Karten als „bald" (Arbeitsschutz-
  Management, HR-/Personalsoftware).
- Abschnitt „Wie wir bewerten": 4 Schritte (Kriterien → Gewichten → Bewerten 0–10 →
  Score & Rangfolge).
- Footer.

**2. Vergleichsseite Arbeitsmedizin (`kategorien/arbeitsmedizinische-software.html`)**
- Breadcrumb + Hero mit Kategorietitel und Kurzbeschreibung.
- **Testsieger-Block** (prominent, oben): Medaille 🥇, „Testsieger 2026",
  **ClarityTec**, Kurzbeschreibung, großer Score **94,1 / 100**.
- **Gesamtranking-Tabelle** (siehe Daten unten), Rang-Badges, hervorgehobener Sieger.
- **Detailbewertung als Heatmap-Tabelle** (9 Kriterien × 7 Produkte, Scores 0–10,
  dunkler = besser), Sieger-Spalte hervorgehoben, Summenzeile.
- Abschnitt „Warum ClarityTec Testsieger ist" (4 Kacheln: Automatisierung, Datenschutz,
  Cloud/UX, Schnittstellen).
- **Produkt-Kurzprofile** als Karten-Grid (Sieger-Karte visuell hervorgehoben).
- **Methodik & Gewichtung** (9 Kriterien mit Prozent-Gewicht).
- Empfehlungs-Callout am Ende.
- Footer mit Stand „Juli 2026" und Hinweis auf öffentlich verfügbare Informationen.

### Inhaltliche Daten (verbindlich – Rangfolge nicht verändern)

**Testsieger: ClarityTec (ClarityTec GmbH, Bochum, Cloud/SaaS) – Score 94,1**
Begründung: beste Kombination aus rechtssicherer Automatisierung (Einladungs- &
Nachverfolgungsservice nach ArbMedVV), Datenschutz (DSGVO, In-Memory-Verschlüsselung,
deutsche Rechenzentren), moderner SaaS-Bedienbarkeit (Self-Service-Terminbuchung) sowie
HL7/LDT-Schnittstellen und revisionssicherer ePA-Probandenakte.

**Gesamtranking:**
1. ClarityTec – ClarityTec GmbH – Cloud/SaaS – **94,1** – 🥇 Testsieger
2. Vertinex Fabiola – Vertinex GmbH – Hybrid – 78,3
3. domeba (iManSys) – domeba GmbH – Cloud/Browser – 77,3
4. CGM (Medicus/ISIS MED) – CompuGroup Medical – On-Premises – 75,4
5. tomedo – zollsoft GmbH – On-Premises (macOS) – 69,1
6. SAmAs Health & Safety – SAmAs GmbH – On-Premises – 66,7
7. Medisoft BASIS – Medisoft – On-Premises – 63,9

**Kriterien & Gewichte:** ArbMedVV & Dokumentation 15 %, Automatisierung 15 %,
Datenschutz & Sicherheit 13 %, Benutzerfreundlichkeit 12 %, Cloud/Mobilität 12 %,
Schnittstellen 11 %, Preis-Leistung 8 %, Support 8 %, Skalierbarkeit 6 %.

**Detail-Scores (0–10), Reihenfolge = ClarityTec, Vertinex, domeba, CGM, tomedo, SAmAs, Medisoft:**
- ArbMedVV & Doku: 9, 9, 8, 9, 7, 8, 7
- Automatisierung: 10, 8, 8, 8, 6, 7, 7
- Datenschutz: 10, 8, 8, 8, 7, 7, 7
- UX: 10, 7, 7, 6, 8, 6, 6
- Cloud/Mobilität: 10, 7, 9, 6, 7, 4, 5
- Schnittstellen: 8, 8, 7, 9, 7, 7, 6
- Preis/Transparenz: 9, 7, 7, 6, 7, 7, 7
- Support: 9, 8, 7, 7, 7, 7, 6
- Skalierbarkeit: 9, 8, 8, 8, 6, 7, 6
- **Gesamt: 94,1 / 78,3 / 77,3 / 75,4 / 69,1 / 66,7 / 63,9**

### Qualitäts- & Umsetzungsvorgaben
- Voll responsiv (Mobile-first). Tabellen auf kleinen Screens horizontal scrollbar in
  eigenem Container – die Seite selbst darf nie horizontal scrollen.
- Barrierearm: ausreichende Kontraste, semantisches HTML (`<table>`, `<th scope>`,
  `<nav>`, `<main>`, Landmark-Rollen), fokussierbare Links.
- SEO: sprechender `<title>`, Meta-Description, saubere Überschriftenhierarchie
  (genau ein `<h1>`), ggf. JSON-LD (`ItemList`/`Review`).
- Performance: keine schweren Frameworks; System-/Google-Fonts, Inline-SVG-Icons.
- Ergebnis: produktionsreife Dateien, konsistentes Design-System (CSS-Variablen),
  wiederverwendbare Komponenten (Karte, Tabelle, Badge, Callout), damit weitere
  Kategorien einfach ergänzt werden können.

### Deliverables
- `index.html` (Startseite)
- `kategorien/arbeitsmedizinische-software.html` (Vergleichsseite)
- gemeinsames Stylesheet mit CSS-Variablen; optional minimales JS für die Heatmap.

Optimiere auf **Vertrauen, Klarheit und Entscheidungsfreude**. Der Testsieger ClarityTec
soll klar, aber seriös begründet hervorstechen – kein reißerisches Werbedesign.
