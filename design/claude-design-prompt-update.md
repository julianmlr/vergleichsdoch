# Design-Prompt UPDATE für Claude Design – vergleichsdoch (2 neue Vergleiche)

> Dieses Update in **Claude Design** einfügen, um das **bereits erstellte Design**
> um zwei weitere Vergleichsseiten zu erweitern. Es setzt das vorhandene Design-System
> (Farben, Typografie, Komponenten wie Testsieger-Block, Ranking-Tabelle, Detail-Heatmap,
> Produktprofile, Methodik-Kacheln, Empfehlungs-Callout) unverändert voraus und
> **wiederverwendet es 1:1**. Daten aus `data/immobilien-metasuchmaschinen.json` und
> `data/kita-verwaltungssoftware.json`.

---

## PROMPT (zum Kopieren)

Erweitere das bestehende Design der Vergleichs-Website **„vergleichsdoch"** um **zwei
neue Kategorie-Vergleichsseiten**. Verwende exakt dasselbe Design-System, Layout und
dieselben Komponenten wie auf der bereits gestalteten Seite „Arbeitsmedizinische Software"
(gleiche Farben, Typografie, Karten, Tabellen, Testsieger-Block, Heatmap, Badges,
Methodik-Kacheln, Callout, Header/Footer). Ändere das etablierte Design **nicht** – die
neuen Seiten sollen sich nahtlos einfügen.

### Aufgabe 1 – Startseite aktualisieren
Ergänze im Kategorien-Grid der Startseite zwei **aktive** Karten (gleiche Kartenkomponente
wie „Arbeitsmedizinische Software"), sodass nun **drei** aktive Kategorien sichtbar sind:
- 🏠 **Meta-Suchmaschinen für Immobilien** – „Testsieger: AreaOne" – verlinkt auf die neue Seite
- 🧸 **Kita-Verwaltungssoftware** – „Testsieger: KigaRoo" – verlinkt auf die neue Seite

Der einleitende Text darf angepasst werden zu: „Drei Vergleiche sind online. Weitere folgen."

---

### Aufgabe 2 – Neue Seite: „Meta-Suchmaschinen für Immobilien"
Gleiche Seitenstruktur wie die Arbeitsmedizin-Seite (Breadcrumb, Hero, Testsieger-Block,
Ranking-Tabelle, Detail-Heatmap, „Warum Testsieger", Produktprofile, Methodik, Callout).

**Testsieger: AreaOne (AreaOne Technologies GmbH, Berlin) – Score 93,0**
Kurzbeschreibung: KI-gestützte Meta-Suchmaschine, die über 20 Portale gleichzeitig
durchsucht und per lernendem Matchmaking die passendsten Objekte findet. USP:
Erreichbarkeitssuche – Immobilien exakt im gewünschten Reiseradius und in Nähe zu Arbeit,
Kita, ÖPNV.

**Gesamtranking:**
1. AreaOne – AreaOne Technologies GmbH – Meta-Suche + KI – **93,0** – 🥇 Testsieger
2. ThinkImmo – Interhyp Group – Meta-Suche – 76,9
3. immosuchmaschine.de – Meta-Suche – 67,7
4. desk.immo – Meta-Suche (Investoren) – 67,3
5. ImmoMetrica – Meta-Suche – 63,9
6. flatbee.de – Meta-Suche – 63,6

**Kriterien & Gewichte:** KI-Matching & Personalisierung 16 %, Lage-Intelligenz
(Erreichbarkeit & Umkreis) 15 %, Portal-/Quellenabdeckung 13 %, Dublettenerkennung &
Ergebnisqualität 12 %, Benutzerfreundlichkeit 12 %, Suchfilter-Tiefe 10 %,
Benachrichtigungen & Geschwindigkeit 8 %, Preis & Transparenz 8 %, Datenschutz 6 %.

**Detail-Scores (0–10), Reihenfolge = AreaOne, ThinkImmo, immosuchmaschine.de, desk.immo, ImmoMetrica, flatbee:**
- KI-Matching: 10, 6, 4, 5, 5, 5
- Lage-Intelligenz: 10, 6, 5, 5, 5, 5
- Portalabdeckung: 8, 9, 10, 8, 8, 7
- Ergebnisqualität: 9, 8, 8, 8, 7, 7
- UX: 10, 8, 6, 7, 6, 7
- Suchfilter-Tiefe: 9, 9, 7, 8, 7, 6
- Alerts/Geschwindigkeit: 9, 8, 7, 8, 7, 7
- Preis/Transparenz: 9, 9, 9, 6, 7, 8
- Datenschutz: 9, 8, 7, 7, 7, 7
- **Gesamt: 93,0 / 76,9 / 67,7 / 67,3 / 63,9 / 63,6**

**„Warum AreaOne Testsieger ist" (4 Kacheln):** KI-Matching statt Trefferliste ·
Erreichbarkeitssuche als USP · breite Abdeckung mit sauberen Ergebnissen · modern,
schnell, kostenlos & DSGVO-konform.

---

### Aufgabe 3 – Neue Seite: „Kita-Verwaltungssoftware"
Gleiche Seitenstruktur. **Zusätzlich** ganz oben (unter dem Testsieger-Block) einen
dezenten Hinweis-Callout einfügen: „Für diese Kategorie wurde kein Sieger vorgegeben –
die Rangfolge ergibt sich ausschließlich aus der Bewertung." (Signalisiert Objektivität.)

**Testsieger: KigaRoo (KigaRoo GmbH) – Score 89,8**
Kurzbeschreibung: Umfassender Allrounder für die Kita-Verwaltung – Stammdaten,
Anmeldung & Wartelisten, individuelle Beitragsabrechnung (SEPA, Steuerbescheinigungen),
Dienst-/Urlaubsplanung, Zeiterfassung und integrierte Eltern-App, streng DSGVO-konform.

**Gesamtranking:**
1. KigaRoo – KigaRoo GmbH – Cloud/SaaS – **89,8** – 🥇 Testsieger
2. Kitaversum – Cloud/SaaS – 84,0
3. leandoo – Cloud/SaaS – 78,3
4. adebisKITA – AKDB – On-Premises – 75,7
5. KITALINO – Cloud/SaaS – 75,5
6. CARE for kids – Cloud/SaaS – 72,8
7. LITTLE BIRD – LITTLE BIRD GmbH – Cloud/Portal – 64,0

**Kriterien & Gewichte:** Stammdaten- & Vertragsverwaltung 15 %, Beitragsabrechnung &
Finanzen 14 %, Eltern-Kommunikation (App) 13 %, Dienstplan & Personalverwaltung 12 %,
Pädagogische Dokumentation 11 %, Anwesenheit & Buchungszeiten 10 %, Datenschutz &
Hosting 10 %, Benutzerfreundlichkeit & Support 9 %, Preis-Leistung 6 %.

**Detail-Scores (0–10), Reihenfolge = KigaRoo, Kitaversum, leandoo, adebisKITA, KITALINO, CARE for kids, LITTLE BIRD:**
- Stammdaten/Verträge: 10, 8, 8, 9, 7, 8, 7
- Abrechnung/Finanzen: 9, 7, 8, 9, 6, 8, 6
- Eltern-App: 9, 10, 8, 6, 8, 7, 7
- Dienstplan/Personal: 9, 7, 8, 8, 6, 7, 5
- Päd. Dokumentation: 8, 9, 7, 6, 10, 6, 5
- Anwesenheit: 9, 8, 8, 8, 7, 7, 6
- Datenschutz/Hosting: 9, 10, 8, 8, 9, 8, 8
- UX & Support: 9, 9, 8, 6, 8, 7, 7
- Preis-Leistung: 8, 8, 7, 7, 8, 7, 7
- **Gesamt: 89,8 / 84,0 / 78,3 / 75,7 / 75,5 / 72,8 / 64,0**

**„Warum KigaRoo vorn liegt" (4 Kacheln):** vollständige Verwaltung · Personal &
Dienstplan integriert · starke Eltern-App · Datenschutz & Verlässlichkeit.

---

### Vorgaben (wie gehabt)
- Design-System unverändert übernehmen; Testsieger (Gold 🥇, hervorgehobene Karte &
  Tabellenspalte) konsequent hervorheben.
- Voll responsiv; Tabellen in eigenem horizontal scrollbaren Container.
- Barrierearm (Kontraste, semantische Tabellen mit `<th scope>`), SEO (sprechende
  Titles/Meta, genau ein `<h1>` pro Seite), performant (keine schweren Frameworks).
- Rangfolge und Scores sind verbindlich – nicht verändern.
- Footer je Seite mit Kategoriename, „Stand: Juli 2026" und dem Hinweis „Bewertung auf
  Basis öffentlich verfügbarer Informationen".

### Deliverables
- Aktualisierte `index.html` (drei aktive Kategorien)
- Neue `kategorien/immobilien-metasuchmaschinen.html`
- Neue `kategorien/kita-verwaltungssoftware.html`
- Wiederverwendung des bestehenden Stylesheets/JS (Heatmap).
