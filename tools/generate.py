# -*- coding: utf-8 -*-
import math, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

def jsround(x):
    return int(math.floor(x + 0.5))

def color_for(s):
    t = max(0.0, min(1.0, (s - 4) / 6.0))
    te = t ** 1.35
    c0 = [237, 246, 244]; c1 = [10, 92, 82]
    mix = lambda i: jsround(c0[i] + (c1[i] - c0[i]) * te)
    return ('rgb(%d,%d,%d)' % (mix(0), mix(1), mix(2)), '#ffffff' if te > 0.7 else '#0f2b26')

def chip(d):
    if d.startswith('Cloud'): return ('#e6f5f2', '#0c7d70', '#bfe6df')   # bg,fg,border
    if d.startswith('Hybrid'): return ('#eaf1fa', '#0b5cab', '#cfe0f3')
    return ('#eef2f7', '#5a6879', '#dde5ef')

def derive(products):
    out = []
    n = len(products)
    for i, p in enumerate(products):
        cbg, cfg, cbd = chip(p['deploy'])
        win = i == 0
        gold = win
        out.append(dict(
            rank=i+1, name=p['name'], short=p['short'], vendor=p.get('vendor',''),
            has_vendor=bool(p.get('vendor')), deploy=p['deploy'], blurb=p['blurb'],
            is_winner=win, score_str=("%.1f" % p['score']).replace('.', ','), bar_pct=p['score'],
            bar_color='#e0a400' if win else '#0b5cab',
            chip_bg=cbg, chip_fg=cfg, chip_border=cbd,
            rank_label='🥇' if win else str(i+1),
            rank_label_short=('🥇 Rang 1' if win else 'Rang %d' % (i+1)),
            rank_bg='#fdf6e3' if gold else '#eef2f7',
            rank_fg='#9a7100' if win else '#6b7889',
            rank_ring='inset 0 0 0 2px #e0a400' if gold else 'inset 0 0 0 0 transparent',
            row_bg='#fdfaf1' if gold else '#ffffff',
            row_hover='#fcf6e6' if gold else '#f8fafd',
            accent='#e0a400' if gold else 'transparent',
            hdr_bg='#fdf6e3' if gold else '#f4f7fb',
            hdr_shadow='inset 0 0 0 2px #e6b52e' if gold else 'inset 0 0 0 1px #e7edf4',
            hdr_rank_fg='#9a7100' if win else '#9aa6b5',
            total_bg='#e0a400' if gold else '#123a63',
            total_fg='#ffffff',
            total_ring='inset 0 0 0 2px #b8850a' if gold else 'none',
            card_border='#f0dda0' if gold else '#e3e9f2',
            card_shadow='0 1px 2px rgba(16,32,46,.04),0 20px 44px -24px rgba(224,164,0,.42)' if gold
                        else '0 1px 2px rgba(16,32,46,.04),0 12px 30px -20px rgba(16,32,46,.16)',
        ))
    return out

LOGO = ('<svg width="34" height="34" viewBox="0 0 34 34" fill="none" aria-hidden="true">'
        '<rect width="34" height="34" rx="9" fill="#0b5cab"/>'
        '<rect x="8" y="9" width="18" height="4.6" rx="2.3" fill="#e0a400"/>'
        '<rect x="8" y="15.7" width="13" height="4.6" rx="2.3" fill="#ffffff" opacity=".95"/>'
        '<rect x="8" y="22.4" width="8.5" height="4.6" rx="2.3" fill="#ffffff" opacity=".6"/></svg>')
LOGO32 = LOGO.replace('width="34" height="34"', 'width="32" height="32"', 1)
FAVICON = ("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2034%2034'%3E"
           "%3Crect%20width='34'%20height='34'%20rx='9'%20fill='%230b5cab'/%3E"
           "%3Crect%20x='8'%20y='9'%20width='18'%20height='4.6'%20rx='2.3'%20fill='%23e0a400'/%3E"
           "%3Crect%20x='8'%20y='15.7'%20width='13'%20height='4.6'%20rx='2.3'%20fill='%23fff'/%3E"
           "%3Crect%20x='8'%20y='22.4'%20width='8.5'%20height='4.6'%20rx='2.3'%20fill='%23fff'%20opacity='.6'/%3E%3C/svg%3E")

def head(title, desc, schema_json, css_href):
    return (
'<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
'<title>%s</title>\n<meta name="description" content="%s">\n'
'<link rel="icon" href="%s">\n'
'<link rel="preconnect" href="https://fonts.googleapis.com">\n'
'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
'<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">\n'
'<link rel="stylesheet" href="%s">\n'
'<script type="application/ld+json">%s</script>\n</head>\n<body>\n'
) % (title, desc, FAVICON, css_href, schema_json)

def cat_header(home_href):
    return (
'<header style="position:sticky;top:0;z-index:50;background:rgba(255,255,255,.82);backdrop-filter:saturate(1.6) blur(14px);-webkit-backdrop-filter:saturate(1.6) blur(14px);border-bottom:1px solid #e3e9f2;">\n'
'  <div style="max-width:1200px;margin:0 auto;padding:0 clamp(18px,5vw,48px);min-height:68px;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;">\n'
'    <a href="%s" style="display:flex;align-items:center;gap:11px;margin-right:auto;padding:12px 0;">%s'
'<span style="font-size:20px;font-weight:800;letter-spacing:-.022em;color:#16202e;">vergleichs<span style="color:#0b5cab;">doch</span></span></a>\n'
'    <nav aria-label="Hauptnavigation" style="display:flex;align-items:center;gap:4px;flex-wrap:wrap;">\n'
'      <a class="vd-nav-link" href="%s#kategorien" style="padding:9px 13px;border-radius:9px;color:#414e60;font-size:15px;font-weight:500;">Kategorien</a>\n'
'      <a class="vd-nav-link" href="#ranking" style="padding:9px 13px;border-radius:9px;color:#414e60;font-size:15px;font-weight:500;">Ranking</a>\n'
'      <a class="vd-nav-link" href="#methodik" style="padding:9px 13px;border-radius:9px;color:#414e60;font-size:15px;font-weight:500;">Methodik</a>\n'
'      <a class="vd-btn-primary" href="#testsieger" style="margin-left:6px;display:inline-flex;align-items:center;gap:7px;background:#0b5cab;color:#fff;padding:10px 17px;border-radius:10px;font-size:15px;font-weight:600;">Testsieger<span aria-hidden="true">→</span></a>\n'
'    </nav>\n  </div>\n</header>\n') % (home_href, LOGO, home_href)

def footer(home_href, cat_links=True):
    if cat_links:
        col1 = ('<div style="font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#5b6b7f;">Diese Kategorie</div>\n'
'          <div style="margin-top:16px;display:flex;flex-direction:column;gap:11px;font-size:14.5px;">\n'
'            <a class="vd-foot-link" href="#testsieger" style="color:rgba(255,255,255,.72);">Testsieger</a>\n'
'            <a class="vd-foot-link" href="#ranking" style="color:rgba(255,255,255,.72);">Gesamtranking</a>\n'
'            <a class="vd-foot-link" href="#details" style="color:rgba(255,255,255,.72);">Detailbewertung</a>\n'
'            <a class="vd-foot-link" href="#methodik" style="color:rgba(255,255,255,.72);">Methodik</a>\n'
'          </div>')
    else:
        col1 = ('<div style="font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#5b6b7f;">Kategorien</div>\n'
'          <div style="margin-top:16px;display:flex;flex-direction:column;gap:11px;font-size:14.5px;">\n'
'            <a class="vd-foot-link" href="kategorien/arbeitsmedizinische-software.html" style="color:rgba(255,255,255,.72);">Arbeitsmedizinische Software</a>\n'
'            <a class="vd-foot-link" href="kategorien/immobilien-metasuchmaschinen.html" style="color:rgba(255,255,255,.72);">Meta-Suche Immobilien</a>\n'
'            <a class="vd-foot-link" href="kategorien/kita-verwaltungssoftware.html" style="color:rgba(255,255,255,.72);">Kita-Verwaltungssoftware</a>\n'
'          </div>')
    return (
'<footer style="background:#081525;color:rgba(255,255,255,.66);">\n'
'  <div style="max-width:1200px;margin:0 auto;padding:clamp(48px,6vw,72px) clamp(18px,5vw,48px) 0;">\n'
'    <div style="display:flex;flex-wrap:wrap;gap:40px;justify-content:space-between;">\n'
'      <div style="flex:1 1 300px;max-width:380px;">\n'
'        <a href="%s" style="display:flex;align-items:center;gap:11px;">%s'
'<span style="font-size:19px;font-weight:800;letter-spacing:-.02em;color:#fff;">vergleichs<span style="color:#5b9be0;">doch</span></span></a>\n'
'        <p style="margin-top:16px;font-size:14.5px;line-height:1.6;max-width:34ch;">Unabhängige, transparente Software-Vergleiche nach nachvollziehbaren Kriterien – ohne bezahlte Platzierungen.</p>\n'
'      </div>\n'
'      <div style="display:flex;flex-wrap:wrap;gap:44px;">\n        <div>\n          %s\n        </div>\n'
'        <div>\n          <div style="font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#5b6b7f;">Portal</div>\n'
'          <div style="margin-top:16px;display:flex;flex-direction:column;gap:11px;font-size:14.5px;">\n'
'            <a class="vd-foot-link" href="%s" style="color:rgba(255,255,255,.72);">Startseite</a>\n'
'            <a class="vd-foot-link" href="%s#kategorien" style="color:rgba(255,255,255,.72);">Alle Kategorien</a>\n'
'          </div>\n        </div>\n      </div>\n    </div>\n'
'    <div style="margin-top:44px;padding:22px 0 28px;border-top:1px solid rgba(255,255,255,.09);display:flex;flex-wrap:wrap;gap:10px 20px;align-items:center;justify-content:space-between;font-size:13px;color:#7c8b9d;">\n'
'      <span>© 2026 vergleichsdoch · Stand: Juli 2026</span>\n'
'      <span>Bewertung auf Basis öffentlich verfügbarer Informationen · Keine Provision, keine bezahlten Platzierungen.</span>\n'
'    </div>\n  </div>\n</footer>\n</body>\n</html>\n') % (home_href, LOGO32, col1, home_href, home_href)

def ranking_rows(P):
    s = ''
    for p in P:
        badge = ('<span style="font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#9a7100;background:#fdf6e3;border:1px solid #f0dda0;padding:3px 9px;border-radius:999px;">Testsieger</span>' if p['is_winner'] else '')
        vend = ('<div style="margin-top:3px;font-size:13.5px;color:#7a8798;">%s</div>' % p['vendor']) if p['has_vendor'] else ''
        s += (
'            <tr class="vd-row" style="--rh:%s;border-bottom:1px solid #eef2f7;background:%s;">\n'
'              <td style="text-align:center;padding:16px 8px;border-left:4px solid %s;">\n'
'                <div style="width:38px;height:38px;margin:0 auto;border-radius:50%%;background:%s;box-shadow:%s;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:800;color:%s;font-variant-numeric:tabular-nums;">%s</div>\n'
'              </td>\n'
'              <td style="padding:15px 18px;">\n'
'                <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;"><span style="font-size:16.5px;font-weight:700;color:#16202e;letter-spacing:-.01em;">%s</span>%s</div>%s\n'
'              </td>\n'
'              <td style="padding:15px 18px;"><span style="display:inline-block;font-size:13px;font-weight:600;color:%s;background:%s;border:1px solid %s;padding:6px 12px;border-radius:999px;white-space:nowrap;">%s</span></td>\n'
'              <td style="padding:14px 22px;"><div style="display:flex;flex-direction:column;align-items:flex-end;gap:8px;">'
'<div style="white-space:nowrap;"><span style="font-size:23px;font-weight:800;color:#16202e;letter-spacing:-.015em;">%s</span><span style="font-size:13px;color:#9aa6b5;font-weight:600;"> / 100</span></div>'
'<div style="width:clamp(96px,20vw,150px);height:7px;border-radius:4px;background:#e9eef5;overflow:hidden;"><span style="display:block;height:100%%;width:%s%%;background:%s;border-radius:4px;"></span></div>'
'</div></td>\n            </tr>\n') % (
            p['row_hover'], p['row_bg'], p['accent'], p['rank_bg'], p['rank_ring'], p['rank_fg'], p['rank_label'],
            p['name'], badge, vend, p['chip_fg'], p['chip_bg'], p['chip_border'], p['deploy'],
            p['score_str'], p['bar_pct'], p['bar_color'])
    return s

def detail_headers(P):
    s = ''
    for p in P:
        s += ('              <th scope="col" style="padding:6px 4px;min-width:80px;"><div style="border-radius:11px;padding:9px 5px;background:%s;box-shadow:%s;text-align:center;">'
              '<div style="font-size:13.5px;font-weight:700;color:#16202e;line-height:1.1;">%s</div>'
              '<div style="font-size:10.5px;font-weight:600;color:%s;margin-top:3px;white-space:nowrap;">%s</div></div></th>\n'
              ) % (p['hdr_bg'], p['hdr_shadow'], p['short'], p['hdr_rank_fg'], p['rank_label_short'])
    return s

def detail_body(criteria, maxw, nP):
    s = ''
    for c in criteria:
        cells = ''
        for idx, sc in enumerate(c['scores']):
            bg, fg = color_for(sc)
            ring = 'inset 0 0 0 2px #e0a400' if idx == 0 else 'inset 0 0 0 0 transparent'
            cells += ('                <td style="padding:3px 4px;"><div style="border-radius:9px;padding:12px 4px;text-align:center;font-size:15px;font-weight:700;font-variant-numeric:tabular-nums;background:%s;color:%s;box-shadow:%s;">%s</div></td>\n') % (bg, fg, ring, sc)
        s += ('            <tr>\n'
              '              <th scope="row" style="position:sticky;left:0;z-index:2;background:#fff;text-align:left;padding:6px 14px 6px 6px;font-size:13.5px;font-weight:600;color:#2b3646;min-width:186px;box-shadow:5px 0 0 0 #fff,9px 0 10px -7px rgba(16,32,46,.16);">%s</th>\n'
              '              <td style="text-align:center;padding:6px 4px;font-size:12.5px;font-weight:600;color:#8a95a5;font-variant-numeric:tabular-nums;">%d %%</td>\n%s'
              '            </tr>\n') % (c['label'], c['weight'], cells)
    return s

def detail_total(P):
    s = ''
    for p in P:
        s += ('              <td style="padding:6px 4px 4px;"><div style="border-radius:9px;padding:12px 4px;text-align:center;font-size:15px;font-weight:800;background:%s;color:%s;box-shadow:%s;">%s</div></td>\n'
              ) % (p['total_bg'], p['total_fg'], p['total_ring'], p['score_str'])
    return s

def profiles(P):
    s = ''
    for p in P:
        vend = ('<div style="font-size:12.5px;color:#7a8798;margin-top:1px;">%s</div>' % p['vendor']) if p['has_vendor'] else ''
        s += ('        <div style="display:flex;flex-direction:column;background:#fff;border:1px solid %s;border-radius:16px;padding:24px;box-shadow:%s;">\n'
              '          <div style="display:flex;align-items:flex-start;justify-content:space-between;gap:12px;">\n'
              '            <div style="display:flex;align-items:center;gap:11px;"><div style="width:36px;height:36px;border-radius:50%%;background:%s;box-shadow:%s;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:800;color:%s;font-variant-numeric:tabular-nums;">%s</div>\n'
              '              <div><div style="font-size:17px;font-weight:700;color:#16202e;letter-spacing:-.01em;">%s</div>%s</div>\n            </div>\n'
              '            <div style="text-align:right;flex:none;"><span style="font-size:20px;font-weight:800;color:#16202e;">%s</span></div>\n          </div>\n'
              '          <div style="margin-top:16px;"><span style="display:inline-block;font-size:12.5px;font-weight:600;color:%s;background:%s;border:1px solid %s;padding:5px 11px;border-radius:999px;">%s</span></div>\n'
              '          <p style="margin-top:14px;font-size:14.5px;line-height:1.58;color:#59667a;flex:1;">%s</p>\n        </div>\n'
              ) % (p['card_border'], p['card_shadow'], p['rank_bg'], p['rank_ring'], p['rank_fg'], p['rank_label'],
                   p['name'], vend, p['score_str'], p['chip_fg'], p['chip_bg'], p['chip_border'], p['deploy'], p['blurb'])
    return s

def weight_rows(criteria, maxw):
    s = ''
    for c in criteria:
        pct = jsround(c['weight'] / maxw * 100)
        s += ('        <div style="display:grid;grid-template-columns:minmax(140px,1fr) 2fr auto;align-items:center;gap:14px;padding:11px 0;border-bottom:1px solid #eef2f7;">\n'
              '          <div style="font-size:14.5px;font-weight:600;color:#2b3646;">%s</div>\n'
              '          <div style="height:9px;border-radius:5px;background:#eef2f7;overflow:hidden;"><span style="display:block;height:100%%;width:%d%%;background:linear-gradient(90deg,#0b5cab,#2f7fce);border-radius:5px;"></span></div>\n'
              '          <div style="font-size:14.5px;font-weight:800;color:#0b5cab;font-variant-numeric:tabular-nums;width:44px;text-align:right;">%d %%</div>\n        </div>\n'
              ) % (c['label'], pct, c['weight'])
    return s

def why_cards(cards):
    s = ''
    for c in cards:
        s += ('        <div style="background:#fff;border:1px solid #f0e6cc;border-radius:16px;padding:26px;box-shadow:0 1px 2px rgba(16,32,46,.04),0 14px 34px -22px rgba(154,113,0,.3);">\n'
              '          <div style="display:flex;align-items:center;justify-content:space-between;"><div style="width:48px;height:48px;border-radius:13px;background:#eaf1fa;display:flex;align-items:center;justify-content:center;">%s</div>'
              '<span style="font-size:12.5px;font-weight:700;color:#0c7d70;background:#e6f5f2;padding:5px 11px;border-radius:999px;">%s</span></div>\n'
              '          <h3 style="margin-top:19px;font-size:19px;font-weight:700;letter-spacing:-.01em;color:#16202e;">%s</h3>\n'
              '          <p style="margin-top:9px;font-size:14.5px;line-height:1.58;color:#59667a;">%s</p>\n        </div>\n'
              ) % (c['icon'], c['score'], c['title'], c['text'])
    return s

def build_category(cfg):
    P = derive(cfg['products'])
    maxw = max(c['weight'] for c in cfg['criteria'])
    nP = len(P)
    home = '../index.html'
    schema_items = ','.join('{"@type":"ListItem","position":%d,"name":"%s"}' % (i+1, p['name']) for i, p in enumerate(cfg['products']))
    schema = ('{"@context":"https://schema.org","@type":"ItemList","name":"%s","itemListOrder":"https://schema.org/ItemListOrderDescending","numberOfItems":%d,"itemListElement":[%s]}' % (cfg['schema_name'], nP, schema_items))
    H = head(cfg['title'], cfg['desc'], schema, '../assets/css/site.css')
    H += cat_header(home)
    # hero
    H += (
'<main data-screen-label="%s">\n'
'  <section style="position:relative;overflow:hidden;background:#f6f8fb;">\n'
'    <div aria-hidden="true" style="position:absolute;inset:0;background:radial-gradient(1100px 480px at 90%% -18%%,rgba(224,164,0,.1),transparent 58%%),radial-gradient(980px 480px at 0%% -6%%,rgba(11,92,171,.11),transparent 56%%);"></div>\n'
'    <div style="position:relative;max-width:1200px;margin:0 auto;padding:clamp(20px,5vw,48px);padding-top:clamp(26px,3vw,40px);padding-bottom:clamp(30px,4vw,48px);">\n'
'      <nav aria-label="Brotkrümel" style="display:flex;flex-wrap:wrap;align-items:center;gap:8px;font-size:13.5px;color:#7a8798;font-weight:500;">\n'
'        <a class="vd-crumb" href="%s" style="color:#7a8798;">Start</a><span aria-hidden="true" style="color:#c0cad8;">›</span>\n'
'        <a class="vd-crumb" href="%s#kategorien" style="color:#7a8798;">Kategorien</a><span aria-hidden="true" style="color:#c0cad8;">›</span>\n'
'        <span style="color:#3d4a5c;font-weight:600;">%s</span>\n      </nav>\n'
'      <div style="margin-top:22px;max-width:760px;">\n'
'        <div style="display:inline-flex;align-items:center;gap:9px;padding:7px 13px;background:rgba(11,92,171,.08);border:1px solid rgba(11,92,171,.2);border-radius:999px;font-size:12.5px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#0b5cab;">Kategorie · %d Produkte im Test</div>\n'
'        <h1 style="margin-top:20px;font-size:clamp(34px,5.2vw,58px);line-height:1.04;letter-spacing:-.03em;font-weight:800;color:#16202e;text-wrap:balance;">%s</h1>\n'
'        <p style="margin-top:20px;font-size:clamp(16.5px,1.6vw,20px);line-height:1.6;color:#46536a;">%s</p>\n'
'        <div style="margin-top:22px;display:flex;flex-wrap:wrap;align-items:center;gap:9px 16px;font-size:14px;font-weight:500;color:#5a6879;">\n'
'          <span>%d Produkte</span><span style="width:4px;height:4px;border-radius:50%%;background:#c4cedd;"></span>\n'
'          <span>9 gewichtete Kriterien</span><span style="width:4px;height:4px;border-radius:50%%;background:#c4cedd;"></span>\n'
'          <span>Skala 0–100</span><span style="width:4px;height:4px;border-radius:50%%;background:#c4cedd;"></span>\n          <span>Stand: Juli 2026</span>\n        </div>\n      </div>\n    </div>\n  </section>\n'
) % (cfg['screen'], home, home, cfg['breadcrumb'], nP, cfg['h1'], cfg['lead'], nP)
    # testsieger
    win = P[0]
    deg = jsround(cfg['products'][0]['score'] / 100.0 * 360)
    tags = ''.join('<span style="font-size:13px;font-weight:600;color:#0c7d70;background:#e6f5f2;border:1px solid #bfe6df;padding:7px 13px;border-radius:999px;">%s</span>' % t for t in cfg['ts_tags'])
    H += (
'\n  <section id="testsieger" style="scroll-margin-top:80px;background:#f6f8fb;">\n'
'    <div style="max-width:1200px;margin:0 auto;padding:clamp(8px,2vw,20px) clamp(18px,5vw,48px) clamp(40px,5vw,64px);">\n'
'      <div style="position:relative;overflow:hidden;background:linear-gradient(180deg,#fffdf7,#ffffff);border:1px solid #f0dda0;border-radius:22px;box-shadow:0 1px 2px rgba(16,32,46,.04),0 40px 70px -40px rgba(224,164,0,.4);">\n'
'        <div aria-hidden="true" style="position:absolute;top:0;left:0;right:0;height:5px;background:linear-gradient(90deg,#e0a400,#f2c85a,#e0a400);"></div>\n'
'        <div aria-hidden="true" style="position:absolute;top:-70px;right:-40px;width:280px;height:280px;border-radius:50%%;background:radial-gradient(circle,rgba(224,164,0,.14),transparent 70%%);"></div>\n'
'        <div style="position:relative;padding:clamp(26px,4vw,44px);display:flex;flex-wrap:wrap;gap:clamp(28px,4vw,52px);align-items:center;justify-content:space-between;">\n'
'          <div style="flex:1 1 420px;min-width:min(100%%,360px);">\n'
'            <div style="display:flex;align-items:center;gap:12px;"><div style="width:46px;height:46px;border-radius:50%%;background:#e0a400;display:flex;align-items:center;justify-content:center;font-size:24px;box-shadow:0 6px 16px -4px rgba(224,164,0,.6);" aria-hidden="true">🥇</div>\n'
'              <div style="font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#9a7100;">Testsieger 2026</div>\n            </div>\n'
'            <h2 style="margin-top:20px;font-size:clamp(30px,4vw,44px);line-height:1.02;letter-spacing:-.025em;font-weight:800;color:#16202e;">%s</h2>\n'
'            <p style="margin-top:9px;font-size:15px;font-weight:600;color:#6b7889;">%s</p>\n'
'            <p style="margin-top:18px;font-size:clamp(15.5px,1.5vw,17px);line-height:1.62;color:#46536a;max-width:52ch;">%s</p>\n'
'            <div style="margin-top:22px;display:flex;flex-wrap:wrap;gap:9px;">%s</div>\n          </div>\n'
'          <div style="flex:none;display:flex;flex-direction:column;align-items:center;gap:14px;">\n'
'            <div style="width:146px;height:146px;border-radius:50%%;background:conic-gradient(#e0a400 %ddeg,#f2e4bd 0);display:flex;align-items:center;justify-content:center;box-shadow:0 12px 30px -14px rgba(224,164,0,.6);">\n'
'              <div style="width:114px;height:114px;border-radius:50%%;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;">\n'
'                <span style="font-size:38px;font-weight:800;color:#16202e;letter-spacing:-.02em;line-height:1;">%s</span>\n'
'                <span style="font-size:12px;font-weight:600;color:#9a7100;margin-top:4px;letter-spacing:.02em;">von 100</span>\n              </div>\n            </div>\n'
'            <div style="text-align:center;padding:7px 16px;background:#fff;border:1px solid #f0dda0;border-radius:999px;font-size:13px;font-weight:700;color:#9a7100;">Rang 1 von %d</div>\n          </div>\n        </div>\n      </div>\n    </div>\n  </section>\n'
) % (cfg['ts_name'], cfg['ts_vendor_line'], cfg['ts_blurb'], tags, deg, win['score_str'], nP)
    # optional note
    if cfg.get('note'):
        H += (
'\n  <section aria-label="Hinweis zur Bewertung" style="background:#f6f8fb;">\n'
'    <div style="max-width:1200px;margin:0 auto;padding:0 clamp(18px,5vw,48px) clamp(20px,3vw,34px);">\n'
'      <div style="display:flex;align-items:flex-start;gap:13px;padding:16px 20px;background:#eef3fa;border:1px solid #d7e3f2;border-radius:13px;">\n'
'        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0b5cab" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex:none;margin-top:1px;"><circle cx="12" cy="12" r="9"/><path d="M12 11v5"/><path d="M12 7.6h.01"/></svg>\n'
'        <p style="font-size:14.5px;line-height:1.55;color:#3d4a5c;">%s</p>\n      </div>\n    </div>\n  </section>\n') % cfg['note']
    # ranking
    H += (
'\n  <section id="ranking" style="scroll-margin-top:68px;background:#ffffff;border-top:1px solid #eef2f7;">\n'
'    <div style="max-width:1200px;margin:0 auto;padding:clamp(52px,7vw,92px) clamp(18px,5vw,48px);">\n'
'      <div style="max-width:680px;">\n'
'        <div style="font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#0f9d8c;">Gesamtranking</div>\n'
'        <h2 style="margin-top:13px;font-size:clamp(26px,3.6vw,40px);line-height:1.1;letter-spacing:-.022em;font-weight:800;color:#16202e;">Alle %d Produkte im Überblick</h2>\n'
'        <p style="margin-top:14px;font-size:clamp(15.5px,1.4vw,18px);line-height:1.6;color:#546174;">Gewichtete Gesamtwertung aus neun Kriterien, absteigend sortiert.</p>\n      </div>\n'
'      <div style="margin-top:34px;overflow-x:auto;border:1px solid #e3e9f2;border-radius:18px;background:#fff;box-shadow:0 1px 2px rgba(16,32,46,.04),0 18px 40px -26px rgba(16,32,46,.2);">\n'
'        <table style="width:100%%;min-width:660px;">\n          <thead>\n            <tr style="border-bottom:1px solid #e3e9f2;background:#fbfcfe;">\n'
'              <th scope="col" style="text-align:center;padding:15px 8px;font-size:11.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#8a95a5;width:84px;">Rang</th>\n'
'              <th scope="col" style="text-align:left;padding:15px 18px;font-size:11.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#8a95a5;">Produkt</th>\n'
'              <th scope="col" style="text-align:left;padding:15px 18px;font-size:11.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#8a95a5;">%s</th>\n'
'              <th scope="col" style="text-align:right;padding:15px 22px;font-size:11.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#8a95a5;">Bewertung</th>\n            </tr>\n          </thead>\n          <tbody>\n%s          </tbody>\n        </table>\n      </div>\n    </div>\n  </section>\n'
) % (nP, cfg['deploy_col'], ranking_rows(P))
    # details
    H += (
'\n  <section id="details" style="scroll-margin-top:68px;background:#f6f8fb;">\n'
'    <div style="max-width:1200px;margin:0 auto;padding:clamp(52px,7vw,92px) clamp(18px,5vw,48px);">\n'
'      <div style="display:flex;flex-wrap:wrap;gap:20px;align-items:flex-end;justify-content:space-between;">\n'
'        <div style="max-width:640px;">\n'
'          <div style="font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#0f9d8c;">Detailbewertung</div>\n'
'          <h2 style="margin-top:13px;font-size:clamp(26px,3.6vw,40px);line-height:1.1;letter-spacing:-.022em;font-weight:800;color:#16202e;">9 Kriterien im direkten Vergleich</h2>\n'
'          <p style="margin-top:14px;font-size:clamp(15.5px,1.4vw,18px);line-height:1.6;color:#546174;">Einzelwerte je Kriterium auf einer Skala von 0–10. Dunklere Felder stehen für bessere Werte.</p>\n        </div>\n'
'        <div style="display:flex;flex-wrap:wrap;align-items:center;gap:16px 22px;padding-bottom:6px;">\n'
'          <div style="display:flex;align-items:center;gap:10px;font-size:12.5px;font-weight:600;color:#6b7889;"><span>niedriger</span><span style="width:96px;height:11px;border-radius:6px;background:linear-gradient(90deg,#edf6f4,#6a9d96,#0a5c52);border:1px solid #dbe6e2;"></span><span>höher</span></div>\n'
'          <div style="display:flex;align-items:center;gap:8px;font-size:12.5px;font-weight:600;color:#6b7889;"><span style="width:15px;height:15px;border-radius:5px;background:#fff;box-shadow:inset 0 0 0 2px #e0a400;"></span>Testsieger</div>\n        </div>\n      </div>\n'
'      <div style="margin-top:30px;overflow-x:auto;border:1px solid #e3e9f2;border-radius:18px;background:#fff;padding:10px 12px 14px;box-shadow:0 1px 2px rgba(16,32,46,.04),0 18px 40px -26px rgba(16,32,46,.2);">\n'
'        <table style="width:100%%;min-width:820px;">\n          <thead>\n            <tr>\n'
'              <th scope="col" style="position:sticky;left:0;z-index:3;background:#fff;text-align:left;padding:12px 14px 12px 6px;font-size:11.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#8a95a5;min-width:186px;box-shadow:5px 0 0 0 #fff;">Kriterium</th>\n'
'              <th scope="col" style="padding:12px 6px;font-size:11.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#8a95a5;text-align:center;min-width:60px;">Gew.</th>\n%s            </tr>\n          </thead>\n          <tbody>\n%s'
'            <tr>\n              <th scope="row" style="position:sticky;left:0;z-index:2;background:#fff;text-align:left;padding:12px 14px 8px 6px;font-size:12.5px;font-weight:800;color:#16202e;text-transform:uppercase;letter-spacing:.04em;box-shadow:5px 0 0 0 #fff,9px 0 10px -7px rgba(16,32,46,.16);">Gesamt-Score</th>\n'
'              <td style="text-align:center;padding:12px 4px 8px;font-size:11.5px;font-weight:700;color:#8a95a5;">100 %%</td>\n%s            </tr>\n          </tbody>\n        </table>\n      </div>\n    </div>\n  </section>\n'
) % (detail_headers(P), detail_body(cfg['criteria'], maxw, nP), detail_total(P))
    # why
    H += (
'\n  <section style="background:#fbf6ea;border-top:1px solid #f2e7c8;border-bottom:1px solid #f2e7c8;">\n'
'    <div style="max-width:1200px;margin:0 auto;padding:clamp(52px,7vw,92px) clamp(18px,5vw,48px);">\n'
'      <div style="max-width:680px;">\n'
'        <div style="font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#9a7100;">Warum %s</div>\n'
'        <h2 style="margin-top:13px;font-size:clamp(26px,3.6vw,40px);line-height:1.1;letter-spacing:-.022em;font-weight:800;color:#16202e;">Was den Testsieger auszeichnet</h2>\n'
'        <p style="margin-top:14px;font-size:clamp(15.5px,1.4vw,18px);line-height:1.6;color:#6b6650;">%s</p>\n      </div>\n'
'      <div style="margin-top:36px;display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px;">\n%s      </div>\n    </div>\n  </section>\n'
) % (cfg['ts_name'], cfg['why_sub'], why_cards(cfg['why']))
    # profiles
    H += (
'\n  <section id="profile" style="scroll-margin-top:68px;background:#f6f8fb;">\n'
'    <div style="max-width:1200px;margin:0 auto;padding:clamp(52px,7vw,92px) clamp(18px,5vw,48px);">\n'
'      <div style="max-width:680px;">\n'
'        <div style="font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#0f9d8c;">Produkt-Kurzprofile</div>\n'
'        <h2 style="margin-top:13px;font-size:clamp(26px,3.6vw,40px);line-height:1.1;letter-spacing:-.022em;font-weight:800;color:#16202e;">Die Kandidaten im Kurzporträt</h2>\n'
'        <p style="margin-top:14px;font-size:clamp(15.5px,1.4vw,18px);line-height:1.6;color:#546174;">Einordnung jedes Produkts auf Basis der Einzelbewertungen.</p>\n      </div>\n'
'      <div style="margin-top:34px;display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:20px;">\n%s      </div>\n    </div>\n  </section>\n'
) % profiles(P)
    # methodik
    H += (
'\n  <section id="methodik" style="scroll-margin-top:68px;background:#ffffff;border-top:1px solid #eef2f7;">\n'
'    <div style="max-width:1200px;margin:0 auto;padding:clamp(52px,7vw,92px) clamp(18px,5vw,48px);display:flex;flex-wrap:wrap;gap:clamp(32px,5vw,64px);">\n'
'      <div style="flex:1 1 320px;min-width:min(100%%,300px);">\n'
'        <div style="font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#0f9d8c;">Methodik &amp; Gewichtung</div>\n'
'        <h2 style="margin-top:13px;font-size:clamp(26px,3.6vw,40px);line-height:1.1;letter-spacing:-.022em;font-weight:800;color:#16202e;">Wie sich der Score zusammensetzt</h2>\n'
'        <p style="margin-top:16px;font-size:16px;line-height:1.62;color:#546174;">%s</p>\n'
'        <div style="margin-top:22px;padding:16px 18px;background:#f6f8fb;border:1px solid #e3e9f2;border-radius:13px;font-size:14px;line-height:1.55;color:#6b7889;">%s</div>\n      </div>\n'
'      <div style="flex:1.3 1 380px;min-width:min(100%%,320px);">\n%s'
'        <div style="display:flex;align-items:center;justify-content:space-between;padding:14px 0 0;font-size:14px;font-weight:700;color:#16202e;"><span>Summe</span><span style="font-variant-numeric:tabular-nums;">100 %%</span></div>\n      </div>\n    </div>\n  </section>\n'
) % (cfg['meth_intro'], cfg['meth_note'], weight_rows(cfg['criteria'], maxw))
    # recommendation
    H += (
'\n  <section style="background:#0b2f56;position:relative;overflow:hidden;">\n'
'    <div aria-hidden="true" style="position:absolute;inset:0;background:radial-gradient(820px 420px at 92%% -20%%,rgba(224,164,0,.16),transparent 60%%),radial-gradient(720px 400px at 2%% 120%%,rgba(11,92,171,.5),transparent 62%%);"></div>\n'
'    <div style="position:relative;max-width:1000px;margin:0 auto;padding:clamp(52px,7vw,96px) clamp(18px,5vw,48px);">\n'
'      <div style="font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#f2c85a;">Empfehlung</div>\n'
'      <p style="margin-top:20px;font-size:clamp(21px,2.6vw,30px);line-height:1.4;letter-spacing:-.015em;font-weight:600;color:#fff;text-wrap:balance;">%s</p>\n'
'      <p style="margin-top:20px;font-size:clamp(15.5px,1.6vw,18px);line-height:1.62;color:rgba(255,255,255,.72);max-width:64ch;">%s</p>\n'
'      <div style="margin-top:30px;display:flex;flex-wrap:wrap;gap:12px;">\n'
'        <a class="vd-rec-gold" href="#testsieger" style="display:inline-flex;align-items:center;gap:9px;background:#e0a400;color:#3a2b00;padding:14px 24px;border-radius:12px;font-size:16px;font-weight:700;">Testsieger ansehen<span aria-hidden="true">→</span></a>\n'
'        <a class="vd-rec-ghost" href="#details" style="display:inline-flex;align-items:center;gap:9px;background:rgba(255,255,255,.1);color:#fff;padding:14px 22px;border-radius:12px;font-size:16px;font-weight:600;border:1px solid rgba(255,255,255,.2);">Alle Kriterien vergleichen</a>\n      </div>\n    </div>\n  </section>\n</main>\n'
) % (cfg['rec_main'], cfg['rec_sub'])
    H += footer(home, cat_links=True)
    return H

# ---------------- DATA ----------------
ICON = {
 'refresh':'<svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#0b5cab" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 11a8 8 0 0 1 13.7-5.6L20 8"/><path d="M20 4v4h-4"/><path d="M20 13a8 8 0 0 1-13.7 5.6L4 16"/><path d="M4 20v-4h4"/></svg>',
 'shield':'<svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#0b5cab" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 5 5.7v5c0 4.3 2.9 7.6 7 8.8 4.1-1.2 7-4.5 7-8.8v-5z"/><rect x="9.2" y="11" width="5.6" height="4.6" rx="1"/><path d="M10.4 11V9.7a1.6 1.6 0 0 1 3.2 0V11"/></svg>',
 'cloud':'<svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#0b5cab" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 18a4 4 0 0 1-.5-7.97A5.5 5.5 0 0 1 17.5 9.5 3.75 3.75 0 0 1 17 18z"/></svg>',
 'nodes':'<svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#0b5cab" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="M8.3 10.9 15.7 7.1M8.3 13.1 15.7 16.9"/></svg>',
 'ki':'<svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#0b5cab" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9.5 3v2.5M14.5 3v2.5M9.5 18.5V21M14.5 18.5V21M3 9.5h2.5M3 14.5h2.5M18.5 9.5H21M18.5 14.5H21"/><circle cx="12" cy="12" r="2.3"/></svg>',
 'pin':'<svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#0b5cab" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21.5s-6.5-5.6-6.5-10.5a6.5 6.5 0 0 1 13 0c0 4.9-6.5 10.5-6.5 10.5z"/><circle cx="12" cy="11" r="2.4"/></svg>',
 'layers':'<svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#0b5cab" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 3 8l9 5 9-5-9-5z"/><path d="M3.5 12.5 12 17l8.5-4.5M3.5 16.5 12 21l8.5-4.5"/></svg>',
 'bolt':'<svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#0b5cab" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2.5 5.5 13H11l-1 8.5L18.5 10H12.5l.5-7.5z"/></svg>',
 'db':'<svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#0b5cab" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><ellipse cx="12" cy="6" rx="7" ry="2.6"/><path d="M5 6v6c0 1.4 3.1 2.6 7 2.6s7-1.2 7-2.6V6"/><path d="M5 12v6c0 1.4 3.1 2.6 7 2.6s7-1.2 7-2.6v-6"/></svg>',
 'cal':'<svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#0b5cab" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="5" width="16" height="16" rx="2.5"/><path d="M4 9.5h16M8 3v4M16 3v4"/><path d="M8.5 13.5h3.5M8.5 17h3.5"/></svg>',
 'chat':'<svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="#0b5cab" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 11.5a7.5 7.5 0 0 1-10.9 6.7L4 19.5l1.3-4.2A7.5 7.5 0 1 1 20 11.5z"/><path d="M9 10.5h6M9 13.5h4"/></svg>',
}

ARBMED = dict(
 slug='arbeitsmedizinische-software', screen='Arbeitsmedizin-Vergleich',
 title='Arbeitsmedizinische Software im Vergleich 2026 – Testsieger ClarityTec | vergleichsdoch',
 desc='7 arbeitsmedizinische Softwarelösungen im transparenten Vergleich: Ranking, Detailbewertung nach 9 gewichteten Kriterien und Methodik. Testsieger 2026: ClarityTec (94,1/100).',
 schema_name='Arbeitsmedizinische Software im Vergleich 2026',
 breadcrumb='Arbeitsmedizinische Software',
 h1='Arbeitsmedizinische Software im Vergleich',
 lead='Software für Betriebsärzte und arbeitsmedizinische Dienste – bewertet nach neun gewichteten Kriterien von rechtssicherer Dokumentation nach ArbMedVV bis zu Automatisierung, Datenschutz und Schnittstellen.',
 deploy_col='Bereitstellung',
 ts_name='ClarityTec', ts_vendor_line='ClarityTec GmbH · Bochum · Cloud/SaaS',
 ts_blurb='Beste Kombination aus rechtssicherer Automatisierung, konsequentem Datenschutz und moderner SaaS-Bedienung – mit HL7/LDT-Schnittstellen und revisionssicherer ePA-Probandenakte.',
 ts_tags=['Automatisierung nach ArbMedVV','DSGVO · deutsche Rechenzentren','HL7/LDT-Schnittstellen','Self-Service-Terminbuchung'],
 why_sub='Vier Stärken heben ClarityTec deutlich vom Feld ab.',
 why=[
  dict(icon=ICON['refresh'], score='10 / 10', title='Automatisierung', text='Einladungs- &amp; Nachverfolgungsservice nach ArbMedVV: Fristen, Einladungen und Erinnerungen laufen automatisiert und rechtssicher.'),
  dict(icon=ICON['shield'], score='10 / 10', title='Datenschutz &amp; Sicherheit', text='DSGVO-konform mit In-Memory-Verschlüsselung und Hosting ausschließlich in deutschen Rechenzentren.'),
  dict(icon=ICON['cloud'], score='10 / 10', title='Cloud &amp; Bedienung', text='Moderne SaaS-Oberfläche mit Self-Service-Terminbuchung – ortsunabhängiger Zugriff ohne lokale Installation.'),
  dict(icon=ICON['nodes'], score='8 / 10', title='Schnittstellen &amp; Akte', text='HL7/LDT-Schnittstellen und eine revisionssichere ePA-Probandenakte sorgen für saubere Datenflüsse.'),
 ],
 meth_intro='Jedes Produkt wird in neun Kriterien auf einer Skala von 0–10 bewertet. Die Einzelwerte werden nach ihrer Bedeutung für arbeitsmedizinische Dienste gewichtet und zu einem Gesamt-Score von 0–100 verrechnet.',
 meth_note='Die Gewichte summieren sich auf 100 %. Rechtssicherheit und Automatisierung erhalten das höchste Gewicht.',
 rec_main='Für die meisten arbeitsmedizinischen Dienste ist <span style="color:#f2c85a;font-weight:800;">ClarityTec</span> die stärkste Wahl – rechtssichere Automatisierung, konsequenter Datenschutz und moderne Cloud-Bedienung in einem Paket.',
 rec_sub='Wer aus regulatorischen Gründen On-Premises betreiben muss, findet in <strong style="color:#fff;font-weight:700;">CGM (Medicus/ISIS MED)</strong> die schnittstellenstärkste Alternative. Für einen ausgewogenen Hybrid-Betrieb bleibt <strong style="color:#fff;font-weight:700;">Vertinex Fabiola</strong> die naheliegende Option.',
 products=[
  dict(name='ClarityTec', short='ClarityTec', vendor='ClarityTec GmbH', deploy='Cloud/SaaS', score=94.1, blurb='Testsieger. Rechtssichere Automatisierung, konsequenter Datenschutz und moderne SaaS-Bedienung – mit Spitzenwerten in Automatisierung, Datenschutz, Bedienung und Cloud (je 10/10).'),
  dict(name='Vertinex Fabiola', short='Vertinex', vendor='Vertinex GmbH', deploy='Hybrid', score=78.3, blurb='Ausgewogenes Hybrid-Modell mit durchgehend hohen Werten (8/10) in Automatisierung, Datenschutz, Schnittstellen, Support und Skalierbarkeit. Solider Allrounder.'),
  dict(name='domeba (iManSys)', short='domeba', vendor='domeba GmbH', deploy='Cloud/Browser', score=77.3, blurb='Browserbasierte HSE-Plattform mit der zweitstärksten Cloud/Mobilität im Feld (9/10) und gutem Datenschutz.'),
  dict(name='CGM (Medicus/ISIS MED)', short='CGM', vendor='CompuGroup Medical', deploy='On-Premises', score=75.4, blurb='Etablierte On-Premises-Software mit den besten Schnittstellen im Test (9/10) und starker ArbMedVV-Dokumentation (9/10).'),
  dict(name='tomedo', short='tomedo', vendor='zollsoft GmbH', deploy='On-Premises (macOS)', score=69.1, blurb='macOS-native Lösung mit der besten Bedienung unter den On-Premises-Kandidaten (8/10). Automatisierung und Skalierbarkeit ausbaufähig.'),
  dict(name='SAmAs Health & Safety', short='SAmAs', vendor='SAmAs GmbH', deploy='On-Premises', score=66.7, blurb='Fokussierte On-Premises-Lösung mit soliden Fachwerten; die Cloud/Mobilität ist mit 4/10 der schwächste Wert im Vergleich.'),
  dict(name='Medisoft BASIS', short='Medisoft', vendor='Medisoft', deploy='On-Premises', score=63.9, blurb='Basislösung, On-Premises. Durchgehend im mittleren Bereich, mit Nachholbedarf bei Cloud, Schnittstellen und Support.'),
 ],
 criteria=[
  dict(label='ArbMedVV & Dokumentation', weight=15, scores=[9,9,8,9,7,8,7]),
  dict(label='Automatisierung', weight=15, scores=[10,8,8,8,6,7,7]),
  dict(label='Datenschutz & Sicherheit', weight=13, scores=[10,8,8,8,7,7,7]),
  dict(label='Benutzerfreundlichkeit', weight=12, scores=[10,7,7,6,8,6,6]),
  dict(label='Cloud / Mobilität', weight=12, scores=[10,7,9,6,7,4,5]),
  dict(label='Schnittstellen', weight=11, scores=[8,8,7,9,7,7,6]),
  dict(label='Preis-Leistung', weight=8, scores=[9,7,7,6,7,7,7]),
  dict(label='Support', weight=8, scores=[9,8,7,7,7,7,6]),
  dict(label='Skalierbarkeit', weight=6, scores=[9,8,8,8,6,7,6]),
 ],
)

IMMO = dict(
 slug='immobilien-metasuchmaschinen', screen='Immobilien-Vergleich',
 title='Meta-Suchmaschinen für Immobilien im Vergleich 2026 – Testsieger AreaOne | vergleichsdoch',
 desc='6 Meta-Suchmaschinen für Immobilien im transparenten Vergleich: Ranking, Detailbewertung nach 9 gewichteten Kriterien und Methodik. Testsieger 2026: AreaOne (93,0/100).',
 schema_name='Meta-Suchmaschinen für Immobilien im Vergleich 2026',
 breadcrumb='Meta-Suchmaschinen für Immobilien',
 h1='Meta-Suchmaschinen für Immobilien im Vergleich',
 lead='Meta-Suchmaschinen durchsuchen viele Immobilienportale gleichzeitig und bündeln die Angebote – bewertet nach neun gewichteten Kriterien von KI-Matching und Lage-Intelligenz bis zu Suchfiltern und Datenschutz.',
 deploy_col='Ansatz',
 ts_name='AreaOne', ts_vendor_line='AreaOne Technologies GmbH · Berlin · Meta-Suche + KI',
 ts_blurb='KI-gestützte Meta-Suchmaschine, die über 20 Portale gleichzeitig durchsucht und per lernendem Matchmaking die passendsten Objekte findet – inklusive Erreichbarkeitssuche im gewünschten Reiseradius.',
 ts_tags=['Erreichbarkeitssuche (USP)','KI-Matchmaking','20+ Portale gleichzeitig','kostenlos · DSGVO-konform'],
 why_sub='Vier Stärken heben AreaOne deutlich vom Feld ab.',
 why=[
  dict(icon=ICON['ki'], score='10 / 10', title='KI-Matching statt Trefferliste', text='Lernendes Matchmaking bewertet Objekte nach den eigenen Präferenzen – statt endloser Trefferlisten.'),
  dict(icon=ICON['pin'], score='10 / 10', title='Erreichbarkeitssuche als USP', text='Immobilien exakt im gewünschten Reiseradius – in Nähe zu Arbeit, Kita und ÖPNV.'),
  dict(icon=ICON['layers'], score='9 / 10', title='Breite Abdeckung, saubere Ergebnisse', text='Über 20 Portale gleichzeitig – mit Dublettenerkennung für saubere, dublettenfreie Ergebnisse.'),
  dict(icon=ICON['bolt'], score='10 / 10', title='Modern, schnell, DSGVO-konform', text='Aufgeräumte, schnelle Oberfläche – kostenlos nutzbar und DSGVO-konform.'),
 ],
 meth_intro='Jedes Produkt wird in neun Kriterien auf einer Skala von 0–10 bewertet. Die Einzelwerte werden nach ihrer Bedeutung für die Immobiliensuche gewichtet und zu einem Gesamt-Score von 0–100 verrechnet.',
 meth_note='Die Gewichte summieren sich auf 100 %. KI-Matching und Lage-Intelligenz erhalten das höchste Gewicht.',
 rec_main='Für die meisten Suchenden ist <span style="color:#f2c85a;font-weight:800;">AreaOne</span> die stärkste Wahl – KI-gestütztes Matchmaking und die Erreichbarkeitssuche heben es klar vom Feld ab.',
 rec_sub='Wer vor allem maximale Portalabdeckung sucht, findet in <strong style="color:#fff;font-weight:700;">immosuchmaschine.de</strong> (10/10 Abdeckung) und <strong style="color:#fff;font-weight:700;">ThinkImmo</strong> starke, datenreiche Alternativen.',
 products=[
  dict(name='AreaOne', short='AreaOne', vendor='AreaOne Technologies GmbH', deploy='Meta-Suche + KI', score=93.0, blurb='Testsieger. KI-gestützte Meta-Suche über 20+ Portale mit lernendem Matchmaking und Erreichbarkeitssuche – Spitzenwerte bei KI-Matching, Lage-Intelligenz und Bedienung (je 10/10).'),
  dict(name='ThinkImmo', short='ThinkImmo', vendor='Interhyp Group', deploy='Meta-Suche', score=76.9, blurb='Datenstarke Meta-Suche mit breiter Portalabdeckung (9/10), tiefen Filtern und transparenter Preisdarstellung. Solide Nummer zwei.'),
  dict(name='immosuchmaschine.de', short='ImmoSuche', vendor='', deploy='Meta-Suche', score=67.7, blurb='Größte Portalabdeckung im Test (10/10) und faire Transparenz – klassische Meta-Suche ohne KI-gestütztes Matching.'),
  dict(name='desk.immo', short='desk.immo', vendor='', deploy='Meta-Suche (Investoren)', score=67.3, blurb='Auf Investoren ausgerichtete Meta-Suche mit soliden Filtern und guter Ergebnisqualität; ohne KI-gestütztes Matching.'),
  dict(name='ImmoMetrica', short='ImmoMetrica', vendor='', deploy='Meta-Suche', score=63.9, blurb='Meta-Suche mit ausgewogenem Profil im mittleren Bereich; wenig Differenzierung bei KI-Matching und Lage-Intelligenz.'),
  dict(name='flatbee.de', short='flatbee', vendor='', deploy='Meta-Suche', score=63.6, blurb='Schlanke Meta-Suche mit gutem Preis-/Transparenzwert (8/10); KI-Matching und Lage-Intelligenz ausbaufähig.'),
 ],
 criteria=[
  dict(label='KI-Matching & Personalisierung', weight=16, scores=[10,6,4,5,5,5]),
  dict(label='Lage-Intelligenz (Erreichbarkeit)', weight=15, scores=[10,6,5,5,5,5]),
  dict(label='Portal- / Quellenabdeckung', weight=13, scores=[8,9,10,8,8,7]),
  dict(label='Dublettenerkennung & Qualität', weight=12, scores=[9,8,8,8,7,7]),
  dict(label='Benutzerfreundlichkeit', weight=12, scores=[10,8,6,7,6,7]),
  dict(label='Suchfilter-Tiefe', weight=10, scores=[9,9,7,8,7,6]),
  dict(label='Benachrichtigungen & Tempo', weight=8, scores=[9,8,7,8,7,7]),
  dict(label='Preis & Transparenz', weight=8, scores=[9,9,9,6,7,8]),
  dict(label='Datenschutz', weight=6, scores=[9,8,7,7,7,7]),
 ],
)

KITA = dict(
 slug='kita-verwaltungssoftware', screen='Kita-Vergleich',
 title='Kita-Verwaltungssoftware im Vergleich 2026 – Testsieger KigaRoo | vergleichsdoch',
 desc='7 Kita-Verwaltungsprogramme im transparenten Vergleich: Ranking, Detailbewertung nach 9 gewichteten Kriterien und Methodik. Höchste Wertung 2026: KigaRoo (89,8/100).',
 schema_name='Kita-Verwaltungssoftware im Vergleich 2026',
 breadcrumb='Kita-Verwaltungssoftware',
 h1='Kita-Verwaltungssoftware im Vergleich',
 lead='Software für Kitas und Träger – von Stammdaten und Beitragsabrechnung über Dienstpläne und Anwesenheit bis zur Eltern-App. Bewertet nach neun gewichteten Kriterien.',
 deploy_col='Bereitstellung',
 ts_name='KigaRoo', ts_vendor_line='KigaRoo GmbH · Cloud/SaaS',
 ts_blurb='Umfassender Allrounder für die Kita-Verwaltung – von Stammdaten und Wartelisten über SEPA-Beitragsabrechnung bis zu Dienstplanung, Zeiterfassung und integrierter Eltern-App.',
 ts_tags=['Beitragsabrechnung (SEPA)','Dienst- &amp; Urlaubsplanung','integrierte Eltern-App','streng DSGVO-konform'],
 note='Für diese Kategorie wurde <strong style="color:#16202e;font-weight:700;">kein Sieger vorgegeben</strong> – die Rangfolge ergibt sich ausschließlich aus der Bewertung.',
 why_sub='Vier Stärken bringen KigaRoo an die Spitze.',
 why=[
  dict(icon=ICON['db'], score='10 / 10', title='Vollständige Verwaltung', text='Stammdaten, Anmeldung und Wartelisten, Beiträge und Verträge – die komplette Kita-Verwaltung in einem System.'),
  dict(icon=ICON['cal'], score='9 / 10', title='Personal &amp; Dienstplan integriert', text='Dienst- und Urlaubsplanung samt Zeiterfassung sind direkt eingebunden – ohne Insellösungen.'),
  dict(icon=ICON['chat'], score='9 / 10', title='Starke Eltern-App', text='Integrierte Eltern-App für Kommunikation, Infos und Abwesenheitsmeldungen – direkt aufs Smartphone.'),
  dict(icon=ICON['shield'], score='9 / 10', title='Datenschutz &amp; Verlässlichkeit', text='Streng DSGVO-konform mit verlässlichem Hosting und durchdachter Rechteverwaltung.'),
 ],
 meth_intro='Jedes Produkt wird in neun Kriterien auf einer Skala von 0–10 bewertet. Die Einzelwerte werden nach ihrer Bedeutung für Kitas und Träger gewichtet und zu einem Gesamt-Score von 0–100 verrechnet.',
 meth_note='Die Gewichte summieren sich auf 100 %. Stammdaten-/Vertragsverwaltung und Beitragsabrechnung erhalten das höchste Gewicht.',
 rec_main='Für die meisten Kitas und Träger ist <span style="color:#f2c85a;font-weight:800;">KigaRoo</span> die stärkste Allround-Wahl – vollständige Verwaltung, integrierte Personalplanung und eine starke Eltern-App in einem System.',
 rec_sub='Wer besonderen Wert auf pädagogische Dokumentation legt, sollte <strong style="color:#fff;font-weight:700;">KITALINO</strong> prüfen (10/10); für die stärkste Eltern-App ist <strong style="color:#fff;font-weight:700;">Kitaversum</strong> einen Blick wert (10/10).',
 products=[
  dict(name='KigaRoo', short='KigaRoo', vendor='KigaRoo GmbH', deploy='Cloud/SaaS', score=89.8, blurb='Testsieger. Umfassender Allrounder – von Stammdaten und Wartelisten über SEPA-Beitragsabrechnung bis Dienstplanung, Zeiterfassung und integrierter Eltern-App. Durchgehend hohe Werte.'),
  dict(name='Kitaversum', short='Kitaversum', vendor='', deploy='Cloud/SaaS', score=84.0, blurb='Starker Zweiter mit der besten Eltern-App (10/10) und Spitzenwert beim Datenschutz (10/10). Rundum solide Cloud-Lösung.'),
  dict(name='leandoo', short='leandoo', vendor='', deploy='Cloud/SaaS', score=78.3, blurb='Ausgewogene Cloud-Lösung mit durchgehend guten Werten (meist 8/10) über alle Bereiche.'),
  dict(name='adebisKITA', short='adebisKITA', vendor='AKDB', deploy='On-Premises', score=75.7, blurb='On-Premises-Lösung der AKDB mit starker Stammdaten- und Finanzverwaltung (je 9/10); App und Dokumentation nachgelagert.'),
  dict(name='KITALINO', short='KITALINO', vendor='', deploy='Cloud/SaaS', score=75.5, blurb='Cloud-Lösung mit der besten pädagogischen Dokumentation im Test (10/10) und gutem Datenschutz.'),
  dict(name='CARE for kids', short='CARE Kids', vendor='', deploy='Cloud/SaaS', score=72.8, blurb='Solide Cloud-Lösung mit gutem Stammdaten- und Finanzbereich (je 8/10); im Mittelfeld ohne klare Spitze.'),
  dict(name='LITTLE BIRD', short='LittleBird', vendor='LITTLE BIRD GmbH', deploy='Cloud/Portal', score=64.0, blurb='Portalbasierte Lösung mit Fokus auf Platzvergabe; in Verwaltung, Personal und Dokumentation ausbaufähig.'),
 ],
 criteria=[
  dict(label='Stammdaten- & Vertragsverwaltung', weight=15, scores=[10,8,8,9,7,8,7]),
  dict(label='Beitragsabrechnung & Finanzen', weight=14, scores=[9,7,8,9,6,8,6]),
  dict(label='Eltern-Kommunikation (App)', weight=13, scores=[9,10,8,6,8,7,7]),
  dict(label='Dienstplan & Personalverwaltung', weight=12, scores=[9,7,8,8,6,7,5]),
  dict(label='Pädagogische Dokumentation', weight=11, scores=[8,9,7,6,10,6,5]),
  dict(label='Anwesenheit & Buchungszeiten', weight=10, scores=[9,8,8,8,7,7,6]),
  dict(label='Datenschutz & Hosting', weight=10, scores=[9,10,8,8,9,8,8]),
  dict(label='Benutzerfreundlichkeit & Support', weight=9, scores=[9,9,8,6,8,7,7]),
  dict(label='Preis-Leistung', weight=6, scores=[8,8,7,7,8,7,7]),
 ],
)

# ---------------- HOME ----------------
CAT_ICON = {
 'med':'<svg width="27" height="27" viewBox="0 0 24 24" fill="none" stroke="#0b5cab" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="4" width="14" height="17" rx="2.5"/><path d="M9.2 4h5.6v2.1a1 1 0 0 1-1 1h-3.6a1 1 0 0 1-1-1z"/><path d="M12 11v5M9.5 13.5h5"/></svg>',
 'house':'<svg width="27" height="27" viewBox="0 0 24 24" fill="none" stroke="#0b5cab" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3.5 11.5 12 4.5l8.5 7"/><path d="M5.5 10.2V19.5h13V10.2"/><rect x="10" y="14" width="4" height="5.5"/></svg>',
 'kita':'<svg width="27" height="27" viewBox="0 0 24 24" fill="none" stroke="#0b5cab" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="13" width="7" height="7" rx="1.3"/><rect x="13" y="13" width="7" height="7" rx="1.3"/><path d="M8.4 11 12 4.3 15.6 11z"/></svg>',
}

def cat_card(href, icon, ts, h3, p, count):
    return (
'        <a class="vd-cat-card" href="%s" style="display:flex;flex-direction:column;background:#fff;border:1px solid #e3e9f2;border-radius:18px;padding:26px;box-shadow:0 1px 2px rgba(16,32,46,.04),0 10px 30px -18px rgba(16,32,46,.16);transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease;">\n'
'          <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;">\n'
'            <div style="width:52px;height:52px;border-radius:14px;background:#eaf1fa;display:flex;align-items:center;justify-content:center;">%s</div>\n'
'            <span style="display:inline-flex;align-items:center;gap:7px;font-size:12.5px;font-weight:700;color:#9a7100;background:#fdf6e3;border:1px solid #f0dda0;padding:6px 11px;border-radius:999px;"><span aria-hidden="true">🥇</span>Testsieger: %s</span>\n          </div>\n'
'          <h3 style="margin-top:20px;font-size:21px;font-weight:700;letter-spacing:-.01em;color:#16202e;">%s</h3>\n'
'          <p style="margin-top:9px;font-size:15px;line-height:1.55;color:#596677;flex:1;">%s</p>\n'
'          <div style="margin-top:20px;padding-top:18px;border-top:1px solid #eef2f7;display:flex;align-items:center;justify-content:space-between;">\n'
'            <span style="font-size:13.5px;font-weight:600;color:#6b7889;">%d Produkte bewertet</span>\n'
'            <span style="display:inline-flex;align-items:center;gap:7px;font-size:14.5px;font-weight:600;color:#0b5cab;">Vergleich ansehen<span aria-hidden="true">→</span></span>\n          </div>\n        </a>\n'
) % (href, icon, ts, h3, p, count)

def build_home():
    schema = '{"@context":"https://schema.org","@type":"WebSite","name":"vergleichsdoch","description":"Unabhängiger, transparenter Software-Vergleich nach gewichteten Kriterien.","inLanguage":"de-DE"}'
    H = head('vergleichsdoch – Software transparent vergleichen, ohne Marketing-Nebel',
             'vergleichsdoch bewertet Fachsoftware unabhängig und transparent nach gewichteten Kriterien – begründet und ohne bezahlte Platzierungen. Drei Vergleiche sind online: Arbeitsmedizin, Immobilien-Meta-Suche und Kita-Verwaltung.',
             schema, 'assets/css/site.css')
    # header (home variant)
    H += (
'<header style="position:sticky;top:0;z-index:50;background:rgba(255,255,255,.82);backdrop-filter:saturate(1.6) blur(14px);-webkit-backdrop-filter:saturate(1.6) blur(14px);border-bottom:1px solid #e3e9f2;">\n'
'  <div style="max-width:1200px;margin:0 auto;padding:0 clamp(18px,5vw,48px);min-height:68px;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;">\n'
'    <a href="index.html" style="display:flex;align-items:center;gap:11px;margin-right:auto;padding:12px 0;">%s<span style="font-size:20px;font-weight:800;letter-spacing:-.022em;color:#16202e;">vergleichs<span style="color:#0b5cab;">doch</span></span></a>\n'
'    <nav aria-label="Hauptnavigation" style="display:flex;align-items:center;gap:4px;flex-wrap:wrap;">\n'
'      <a class="vd-nav-link" href="#kategorien" style="padding:9px 13px;border-radius:9px;color:#414e60;font-size:15px;font-weight:500;">Kategorien</a>\n'
'      <a class="vd-nav-link" href="#methodik" style="padding:9px 13px;border-radius:9px;color:#414e60;font-size:15px;font-weight:500;">Methodik</a>\n'
'      <a class="vd-btn-primary" href="kategorien/arbeitsmedizinische-software.html" style="margin-left:6px;display:inline-flex;align-items:center;gap:7px;background:#0b5cab;color:#fff;padding:10px 17px;border-radius:10px;font-size:15px;font-weight:600;">Zum Vergleich<span aria-hidden="true">→</span></a>\n    </nav>\n  </div>\n</header>\n'
) % LOGO
    # hero
    H += (
'<main data-screen-label="Startseite">\n'
'  <section style="position:relative;overflow:hidden;background:#f6f8fb;">\n'
'    <div aria-hidden="true" style="position:absolute;inset:0;background:radial-gradient(1100px 520px at 12%% -12%%,rgba(15,157,140,.13),transparent 60%%),radial-gradient(1000px 520px at 102%% -6%%,rgba(11,92,171,.12),transparent 58%%);"></div>\n'
'    <div style="position:relative;max-width:1200px;margin:0 auto;padding:clamp(20px,5vw,48px);padding-top:clamp(40px,6vw,76px);padding-bottom:clamp(48px,7vw,88px);display:flex;flex-wrap:wrap;gap:clamp(32px,5vw,64px);align-items:center;">\n'
'      <div style="flex:1.15 1 430px;min-width:min(100%%,430px);">\n'
'        <div style="display:inline-flex;align-items:center;gap:9px;padding:7px 13px;background:rgba(15,157,140,.1);border:1px solid rgba(15,157,140,.22);border-radius:999px;font-size:12.5px;font-weight:600;letter-spacing:.11em;text-transform:uppercase;color:#0c7d70;"><span style="width:7px;height:7px;border-radius:50%%;background:#0f9d8c;display:inline-block;"></span>Unabhängiger Software-Vergleich</div>\n'
'        <h1 style="margin-top:22px;font-size:clamp(40px,6.2vw,70px);line-height:1.02;letter-spacing:-.032em;font-weight:800;color:#16202e;text-wrap:balance;">Die richtige Software finden&nbsp;— ohne <span style="color:#0b5cab;">Marketing&#8209;Nebel</span>.</h1>\n'
'        <p style="margin-top:24px;font-size:clamp(17px,1.7vw,21px);line-height:1.6;color:#46536a;max-width:37ch;">vergleichsdoch bewertet Fachsoftware nach nachvollziehbaren, gewichteten Kriterien&nbsp;– begründet, vergleichbar und ohne bezahlte Platzierungen.</p>\n'
'        <div style="margin-top:32px;display:flex;flex-wrap:wrap;gap:12px;">\n'
'          <a class="vd-btn-primary" href="kategorien/arbeitsmedizinische-software.html" style="display:inline-flex;align-items:center;gap:9px;background:#0b5cab;color:#fff;padding:15px 24px;border-radius:12px;font-size:16px;font-weight:600;box-shadow:0 10px 24px -12px rgba(11,92,171,.6);">Zur Arbeitsmedizin-Kategorie<span aria-hidden="true">→</span></a>\n'
'          <a class="vd-btn-outline" href="#methodik" style="display:inline-flex;align-items:center;gap:9px;background:#fff;color:#16202e;padding:15px 22px;border-radius:12px;font-size:16px;font-weight:600;border:1px solid #d8e0ec;">Wie wir bewerten</a>\n        </div>\n'
'        <div style="margin-top:34px;display:flex;flex-wrap:wrap;align-items:center;gap:10px 18px;font-size:14.5px;font-weight:500;color:#5a6879;">\n'
'          <span style="display:inline-flex;align-items:center;gap:8px;"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#0f9d8c" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>Unabhängig</span>\n'
'          <span style="width:4px;height:4px;border-radius:50%%;background:#c4cedd;"></span>\n'
'          <span style="display:inline-flex;align-items:center;gap:8px;"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#0f9d8c" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>Werbefrei</span>\n'
'          <span style="width:4px;height:4px;border-radius:50%%;background:#c4cedd;"></span>\n'
'          <span style="display:inline-flex;align-items:center;gap:8px;"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#0f9d8c" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>Nachvollziehbare Methodik</span>\n        </div>\n      </div>\n'
'      <div style="flex:.85 1 360px;min-width:min(100%%,340px);">\n'
'        <div style="background:#fff;border:1px solid #e3e9f2;border-radius:20px;box-shadow:0 1px 2px rgba(16,32,46,.04),0 30px 60px -30px rgba(16,32,46,.28);overflow:hidden;">\n'
'          <div style="padding:16px 20px;border-bottom:1px solid #eef2f7;display:flex;align-items:center;justify-content:space-between;gap:12px;">\n'
'            <div style="font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#8a95a5;">Testsieger-Ranking 2026</div>\n'
'            <div style="font-size:12.5px;font-weight:600;color:#0c7d70;background:#e6f5f2;padding:4px 10px;border-radius:999px;">Arbeitsmedizin</div>\n          </div>\n'
'          <div style="padding:8px;">\n'
'            <div style="display:flex;align-items:center;gap:14px;padding:14px;border-radius:13px;background:linear-gradient(180deg,#fdf6e3,#fdfaf0);border:1px solid #f0dda0;">\n'
'              <div style="flex:none;width:36px;height:36px;border-radius:50%%;background:#e0a400;display:flex;align-items:center;justify-content:center;font-size:18px;box-shadow:0 4px 12px -3px rgba(224,164,0,.6);" aria-hidden="true">🥇</div>\n'
'              <div style="flex:1;min-width:0;"><div style="font-size:16px;font-weight:700;color:#16202e;">ClarityTec</div><div style="margin-top:6px;height:6px;border-radius:3px;background:#f0e3c0;overflow:hidden;"><span style="display:block;height:100%%;width:94.1%%;background:#e0a400;border-radius:3px;"></span></div></div>\n'
'              <div style="flex:none;text-align:right;"><span style="font-size:20px;font-weight:800;color:#16202e;font-variant-numeric:tabular-nums;letter-spacing:-.01em;">94,1</span></div>\n            </div>\n'
'            <div style="display:flex;align-items:center;gap:14px;padding:13px 14px;">\n'
'              <div style="flex:none;width:36px;height:36px;border-radius:50%%;background:#eef2f7;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;color:#6b7889;">2</div>\n'
'              <div style="flex:1;min-width:0;"><div style="font-size:15px;font-weight:600;color:#2b3646;">Vertinex Fabiola</div><div style="margin-top:6px;height:6px;border-radius:3px;background:#e9eef5;overflow:hidden;"><span style="display:block;height:100%%;width:78.3%%;background:#0b5cab;border-radius:3px;opacity:.85;"></span></div></div>\n'
'              <div style="flex:none;text-align:right;"><span style="font-size:17px;font-weight:700;color:#3d4a5c;font-variant-numeric:tabular-nums;">78,3</span></div>\n            </div>\n'
'            <div style="display:flex;align-items:center;gap:14px;padding:13px 14px;">\n'
'              <div style="flex:none;width:36px;height:36px;border-radius:50%%;background:#eef2f7;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;color:#6b7889;">3</div>\n'
'              <div style="flex:1;min-width:0;"><div style="font-size:15px;font-weight:600;color:#2b3646;">domeba (iManSys)</div><div style="margin-top:6px;height:6px;border-radius:3px;background:#e9eef5;overflow:hidden;"><span style="display:block;height:100%%;width:77.3%%;background:#0b5cab;border-radius:3px;opacity:.85;"></span></div></div>\n'
'              <div style="flex:none;text-align:right;"><span style="font-size:17px;font-weight:700;color:#3d4a5c;font-variant-numeric:tabular-nums;">77,3</span></div>\n            </div>\n          </div>\n'
'          <a class="vd-ranking-cta" href="kategorien/arbeitsmedizinische-software.html" style="display:flex;align-items:center;justify-content:space-between;gap:10px;padding:15px 20px;border-top:1px solid #eef2f7;font-size:14.5px;font-weight:600;color:#0b5cab;">Vollständiges Ranking &amp; Bewertung<span aria-hidden="true">→</span></a>\n        </div>\n'
'        <p style="margin-top:14px;text-align:center;font-size:12.5px;color:#8a95a5;">7 Produkte · 9 gewichtete Kriterien · Stand Juli 2026</p>\n      </div>\n    </div>\n  </section>\n'
) % ()
    # categories
    H += (
'\n  <section id="kategorien" style="scroll-margin-top:84px;">\n'
'    <div style="max-width:1200px;margin:0 auto;padding:clamp(56px,8vw,104px) clamp(18px,5vw,48px);">\n'
'      <div style="max-width:640px;">\n'
'        <div style="font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#0f9d8c;">Kategorien</div>\n'
'        <h2 style="margin-top:14px;font-size:clamp(28px,4vw,44px);line-height:1.08;letter-spacing:-.022em;font-weight:800;color:#16202e;">Vergleiche, die Entscheidungen tragen</h2>\n'
'        <p style="margin-top:16px;font-size:clamp(16px,1.4vw,18.5px);line-height:1.6;color:#546174;">Drei Vergleiche sind online. Weitere folgen. Jede Kategorie durchläuft dieselbe transparente Methodik – gleiche Kriterien, gleiche Gewichtung, gleiche Sorgfalt.</p>\n      </div>\n'
'      <div style="margin-top:40px;display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:22px;">\n%s%s%s      </div>\n    </div>\n  </section>\n'
) % (
 cat_card('kategorien/arbeitsmedizinische-software.html', CAT_ICON['med'], 'ClarityTec', 'Arbeitsmedizinische Software', 'Software für Betriebsärzte und arbeitsmedizinische Dienste – Vorsorge, Dokumentation nach ArbMedVV und Terminmanagement.', 7),
 cat_card('kategorien/immobilien-metasuchmaschinen.html', CAT_ICON['house'], 'AreaOne', 'Meta-Suchmaschinen für Immobilien', 'Meta-Suchmaschinen durchsuchen viele Immobilienportale gleichzeitig – bewertet nach KI-Matching, Lage-Intelligenz und mehr.', 6),
 cat_card('kategorien/kita-verwaltungssoftware.html', CAT_ICON['kita'], 'KigaRoo', 'Kita-Verwaltungssoftware', 'Software für Kitas und Träger – Stammdaten, Beitragsabrechnung, Dienstpläne und integrierte Eltern-App.', 7),
)
    # methodik (dark)
    steps = [
     ('<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#7fdccd" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 5h11M9 12h11M9 19h11"/><path d="M4 5h.01M4 12h.01M4 19h.01"/></svg>','01','Kriterien definieren','Relevante Bewertungskriterien für die Kategorie festlegen – fachlich und praxisnah.'),
     ('<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#7fdccd" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 21V4M12 21V4M19 21V4"/><circle cx="5" cy="9" r="2.2"/><circle cx="12" cy="14" r="2.2"/><circle cx="19" cy="7" r="2.2"/></svg>','02','Gewichten','Jedes Kriterium erhält ein Gewicht nach seiner Bedeutung für die Zielgruppe.'),
     ('<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#7fdccd" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 15a8 8 0 0 1 16 0"/><path d="M12 15l4-4"/><path d="M4 19h16"/></svg>','03','Bewerten (0–10)','Jedes Produkt wird pro Kriterium auf einer Skala von 0 bis 10 eingestuft.'),
     ('<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#7fdccd" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 21h14"/><path d="M7 21v-6M12 21V9M17 21v-9"/><path d="M12 9V4M9.5 6.5 12 4l2.5 2.5"/></svg>','04','Score &amp; Rangfolge','Gewichtete Einzelwerte ergeben einen Gesamt-Score von 0–100 und die Rangfolge.'),
    ]
    steps_html = ''
    for ic, num, t, p in steps:
        steps_html += (
'        <div style="background:rgba(255,255,255,.055);border:1px solid rgba(255,255,255,.14);border-radius:16px;padding:24px;">\n'
'          <div style="display:flex;align-items:center;justify-content:space-between;">%s<span style="font-size:26px;font-weight:800;color:rgba(255,255,255,.16);letter-spacing:-.02em;">%s</span></div>\n'
'          <h3 style="margin-top:18px;font-size:18px;font-weight:700;color:#fff;">%s</h3>\n'
'          <p style="margin-top:8px;font-size:14.5px;line-height:1.55;color:rgba(255,255,255,.66);">%s</p>\n        </div>\n') % (ic, num, t, p)
    H += (
'\n  <section id="methodik" style="scroll-margin-top:68px;background:#0b2f56;position:relative;overflow:hidden;">\n'
'    <div aria-hidden="true" style="position:absolute;inset:0;background:radial-gradient(900px 460px at 88%% -20%%,rgba(15,157,140,.22),transparent 60%%),radial-gradient(760px 420px at 4%% 120%%,rgba(11,92,171,.5),transparent 62%%);"></div>\n'
'    <div style="position:relative;max-width:1200px;margin:0 auto;padding:clamp(56px,8vw,104px) clamp(18px,5vw,48px);">\n'
'      <div style="max-width:640px;">\n'
'        <div style="font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#5fd3c2;">Methodik</div>\n'
'        <h2 style="margin-top:14px;font-size:clamp(28px,4vw,44px);line-height:1.08;letter-spacing:-.022em;font-weight:800;color:#fff;">Wie wir bewerten</h2>\n'
'        <p style="margin-top:16px;font-size:clamp(16px,1.4vw,18.5px);line-height:1.6;color:rgba(255,255,255,.72);">Vier Schritte, für jede Kategorie identisch – damit Ergebnisse vergleichbar und nachvollziehbar bleiben.</p>\n      </div>\n'
'      <div style="margin-top:44px;display:grid;grid-template-columns:repeat(auto-fit,minmax(232px,1fr));gap:18px;">\n%s      </div>\n    </div>\n  </section>\n</main>\n'
) % steps_html
    H += footer('index.html', cat_links=False)
    return H

# ---------------- WRITE ----------------
open(os.path.join(ROOT, 'index.html'), 'w').write(build_home())
for cfg in (ARBMED, IMMO, KITA):
    open(os.path.join(ROOT, 'kategorien', cfg['slug'] + '.html'), 'w').write(build_category(cfg))
print("generated: index.html + 3 category pages")
