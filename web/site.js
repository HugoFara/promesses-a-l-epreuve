/* Chiffrages à l'épreuve : script du site public (web/index.html).

   Lit les CSV publiés de data/ (aucune valeur en dur : tous les chiffres affichés en viennent), découpe le
   contenu en vues accessibles par l'adresse (#/hier, #/programmes…) et trace les graphiques avec d3.
   Affichage : depuis la racine du projet, `python3 -m http.server 8000` puis http://localhost:8000/web/. */
"use strict";

const SOURCES = {
  mesures: "mesures_cout_calc", stats: "couche1_stats", causes: "couche1_par_cause", effets: "mesures_effets",
  ps: "ps_calc", pairs: "pairs_frankel_schreger", regles: "regles_calibration", hypotheses: "hypotheses_defaut",
  elasticites: "elasticites", application: "application_lignes", programmes: "application_programmes",
  parametres: "application_parametres", paniers: "paniers", moteur: "moteur_lignes", totaux: "moteur_totaux",
  variantes: "moteur_variantes", sensibilite: "sensibilite_chiffreurs", confiance: "confiance_programmes",
  projection: "projection", projection_controle: "projection_controle", validation_resume: "validation_resume",
  validation_regles: "validation_regles", distributif: "distributif_menages", grille: "distributif_grille", reformes: "distributif_reformes",
  meta: "meta", regles_def: "regles", moteur_regles: "moteur_regles", moteur_parametres: "moteur_parametres",
};

// Fichiers proposés au téléchargement (vue Méthode), avec une description lisible.
const FICHIERS = [
  ["mesures_cout", "Coût annoncé et coût réel des mesures passées"],
  ["mesures_effets", "Effets promis et effets mesurés"],
  ["programmes_stabilite_fr", "Objectifs et réalisations de déficit des programmes de stabilité"],
  ["pairs_frankel_schreger", "Comparaison européenne des prévisions"],
  ["regles_calibration", "Règles de correction"],
  ["elasticites", "Études de comportement, avec leurs sources"],
  ["application_lignes", "Programmes 2024, mesure par mesure"],
  ["paniers", "Scénarios de financement des mesures phares"],
  ["moteur_totaux", "Résultats corrigés et fourchettes"],
  ["sensibilite_chiffreurs", "Résultats selon l'organisme de chiffrage"],
  ["projection", "Trajectoires de dette et de déficit 2026-2032"],
  ["validation_resume", "Test de la méthode sur le passé"],
  ["distributif_menages", "Effet sur les foyers types"],
  ["distributif_grille", "Effet sur toutes les situations du simulateur « Mon foyer »"],
];

const CRISES_T3 = [2009, 2010, 2020, 2021];

/* ------------------------------------------------------------------ formats */
const FR = d3.formatLocale({decimal: ",", thousands: " ", grouping: [3], currency: ["", " €"], minus: "−"});
const n0 = FR.format(",.0f"), n1 = FR.format(",.1f");
const sg = (v, f = n1) => isNaN(v) || v === null ? "—" : (v > 0 ? "+" : "") + f(v);
const pc = (v, f = n0) => f(v) + " %";
// Moins de 10 milliards : une décimale (5,5 et non 6) ; au-delà, l'arrondi à l'unité suffit
const md = v => (Math.abs(v) < 10 ? n1 : n0)(Math.abs(v)) + "\u00a0milliard" + (Math.abs(v) >= 2 ? "s" : "") + " d'euros";
const pts = v => n1(v) + " point" + (Math.abs(v) >= 2 ? "s" : "");
const eur = v => n0(v) + " €";
const num = x => (x === "" || x == null) ? NaN : Number(x);
const sum = (a, f) => a.reduce((s, r) => s + f(r), 0);
const mean = a => a.reduce((s, v) => s + v, 0) / a.length;

/* ------------------------------------------------------------------ DOM */
const $ = (s, el = document) => el.querySelector(s);
const $$ = (s, el = document) => [...el.querySelectorAll(s)];
function h(tag, attrs, ...kids) {
  const el = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (v === null || v === undefined || v === false) continue;
    if (k === "class") el.className = v; else if (k === "text") el.textContent = v; else el.setAttribute(k, v);
  }
  for (const c of kids.flat()) if (c !== null && c !== undefined && c !== false) el.append(c.nodeType ? c : String(c));
  return el;
}
function lien(url, txt) {
  return /^https?:\/\//.test(url || "") ? h("a", {href: url, target: "_blank", rel: "noopener"}, txt || "source") : (txt && url ? txt : "");
}
function signCls(v, eps = 0.05) { return v > eps ? "pos" : v < -eps ? "neg" : ""; }

/** Tableau générique. cols : [{t: titre, f: r => texte|nœud, num: bool, cls: r => classe}] ;
    group : r => libellé de groupe (insère une ligne d'intertitre à chaque changement). */
function table(el, cols, rows, opt = {}) {
  el.textContent = "";
  const t = h("table", {}, opt.caption ? h("caption", {}, opt.caption) : null,
    h("thead", {}, h("tr", {}, cols.map(c => h("th", {scope: "col", class: c.num ? "num" : null}, c.t)))));
  const tb = h("tbody");
  let cur = null;
  rows.forEach(r => {
    if (opt.group && opt.group(r) !== cur) {
      cur = opt.group(r);
      tb.append(h("tr", {class: "group"}, h("th", {scope: "colgroup", colspan: cols.length}, cur)));
    }
    tb.append(h("tr", {class: opt.rowCls ? opt.rowCls(r) : null},
      cols.map(c => h("td", {class: [c.num ? "num" : "", c.cls ? c.cls(r) : ""].join(" ").trim() || null}, c.f(r)))));
  });
  t.append(tb);
  el.append(t);
}
function badge(txt, kind) { return h("span", {class: "badge " + (kind || "")}, txt); }
function legend(el, items) {
  el.textContent = "";
  items.forEach(([n, c, forme]) => el.append(h("li", {}, (() => {
    const i = h("i", {class: forme || "", "aria-hidden": "true"});
    if (forme === "dash") i.style.borderTopColor = c; else i.style.background = c;
    return i;
  })(), n)));
}
const css = v => getComputedStyle(document.documentElement).getPropertyValue(v).trim();
/** Couleur de texte lisible sur un fond donné (#rrggbb) : noir ou blanc selon la luminance. */
function textOn(hex) {
  const [r, g, b] = [1, 3, 5].map(i => parseInt(hex.slice(i, i + 2), 16) / 255).map(c => c <= .03928 ? c / 12.92 : ((c + .055) / 1.055) ** 2.4);
  return .2126 * r + .7152 * g + .0722 * b > .18 ? "#111" : "#fff";
}

/* ------------------------------------------------------------------ données */
const D = {}, K = {};

function calculer() {
  const par = id => num(D.parametres.find(x => x.id === id).valeur);
  const pib = par("pib_2027");

  // Mesures passées : statistique principale (inclus_stats = 1)
  const st = D.stats.find(r => r.echantillon.startsWith("principal"));
  K.mes_n = st.n; K.mes_mediane = pc(num(st.erreur_abs_mediane_pct)); K.mes_15 = st.a_15pct;

  // Effets promis
  const rates = D.effets.filter(r => ["Surestimé", "Non réalisé"].includes(r.verdict));
  K.eff_n = D.effets.length; K.eff_rates = rates.length;

  // Programmes de stabilité, hors crises
  D.ps.forEach(r => {
    r.e1 = num(r.e1); r.e3 = r.e3 === "" ? null : num(r.e3);
    r.crise = CRISES_T3.includes(num(r.annee_t3));
  });
  const t3 = D.ps.filter(r => r.e3 !== null && !r.crise).map(r => r.e3);
  const biais = Math.abs(mean(t3));
  K.ps_n3 = t3.length; K.ps_opt = t3.filter(v => v < 0).length;
  K.ps_biais = pts(biais) + " de PIB"; K.ps_md = md(biais * pib / 100);
  K.pib = md(pib); K.pt_pib = md(pib / 100);

  // Pays
  D.pairs.forEach(r => { r.v = num(r.erreur_3ans); });

  // Lignes corrigées par le moteur
  const mot = new Map(D.moteur.map(r => [r.fichier + "|" + r.id, r]));
  D.app = D.application.map(r => ({...r, corrige: num(mot.get("application_lignes|" + r.id)?.corrige_central)}));

  // Programmes : autant que les données en contiennent, regroupés par élection. Chacun est jugé par rapport à
  // sa propre référence (deficit_reference, biais_reference) : 2024 → programme de stabilité + biais à 3 ans.
  K.prev_actuelle = par("prevision_2027_actuelle");
  const desc = id => D.parametres.find(x => x.id === id).description;
  D.progs = D.programmes.map(p => {
    const t = D.totaux.find(r => r.fichier === "application_lignes" && r.groupe === p.programme && r.composante === "solde");
    const lignes = D.app.filter(r => r.programme === p.programme), c = num(t.central);
    const ref = par(p.deficit_reference), biais = par(p.biais_reference);
    return {id: p.id, nom: p.programme, court: p.programme.replace(/\s+20\d\d.*$/, ""), position: p.position_parti,
      scrutin: p.scrutin, annee: num((p.scrutin.match(/\d{4}/) || [0])[0]),
      annonce: p.solde_annonce === "" ? null : num(p.solde_annonce), depart: sum(lignes, r => num(r.independant)),
      sources: sourcesDepart(lignes), corrige: c, p10: num(t.p10), p90: num(t.p90), pts_pib: -c / pib * 100,
      ref, refId: p.deficit_reference, refLib: desc(p.deficit_reference).replace(/\s*\(.*$/, "").replace(/,.*$/, ""),
      biais, biaisLib: (desc(p.biais_reference).match(/à \d ans?/) || [""])[0],
      deficit: ref + biais - c / pib * 100};
  });
  D.scrutins = [...new Set(D.progs.map(p => p.scrutin))].sort((a, b) => num(b.match(/\d{4}/)) - num(a.match(/\d{4}/)));

  // Limites : l'écart entre chiffreurs publiés, sur le programme où il est le plus grand
  const ecarts = [...new Set(D.sensibilite.map(r => r.programme))].map(p => {
    const v = D.sensibilite.filter(r => r.programme === p && r.solde_publie !== "").map(r => num(r.solde_publie));
    return {p, lo: d3.min(v), hi: d3.max(v)};
  }).filter(e => e.lo !== undefined).sort((a, b) => (b.hi - b.lo) - (a.hi - a.lo));
  if (ecarts.length) K.lim_chiffreurs = `Pour ${ecarts[0].p}, les chiffrages publiés vont de ${sg(ecarts[0].lo, n0)} à ${sg(ecarts[0].hi, n0)} milliards d'euros.`;
  D.pan = D.paniers.map(r => ({...r, corrige: num(mot.get("paniers|" + r.id)?.corrige_central)}));

  // Scénarios d'équilibre
  const groupes = [...new Set(D.paniers.map(r => r.variante))];
  D.scen = groupes.map(g => {
    const t = comp => D.totaux.find(r => r.fichier === "paniers" && r.groupe === g && r.composante === comp);
    const v = D.variantes.find(x => x.groupe === g && x.variante === "degel");
    const s = t("solde");
    return {nom: g, mesures: num(t("Mesure phare")?.central), financement: num(t("Financement")?.central),
      investissement: t("investissement") ? num(t("investissement").central) : 0,
      solde: num(s.central), p10: num(s.p10), p90: num(s.p90), loi: num(s.loi_votee_seule), degel: v ? num(v.solde_central) : null,
      lignes: D.pan.filter(r => r.variante === g)};
  });

  K.el_n = D.elasticites.length;
  const dd = D.meta.find(r => r.cle === "date_donnees")?.valeur;
  if (dd) K.maj = new Date(dd + "T12:00:00").toLocaleDateString("fr-FR", {day: "numeric", month: "long", year: "numeric"});
}

/** Résumé lisible de la provenance du chiffrage de départ d'un programme : « Institut Montaigne (9 mesures), … ». */
function sourcesDepart(lignes) {
  const cat = s => /^médiane/i.test(s) ? "médiane des autres chiffreurs" : /^calcul/i.test(s) ? "calcul propre" : /^montant du parti/i.test(s) ? "montant du parti" : s;
  const n = d3.rollup(lignes, v => v.length, r => cat(r.source_independant));
  return [...n].sort((a, b) => b[1] - a[1]).map(([k, v]) => `${k} (${v} mesure${v > 1 ? "s" : ""})`).join(", ");
}

/* ------------------------------------------------------------------ choix des programmes affichés */
const SEL = {scrutin: null, caches: new Set()};
const progsVus = () => D.progs.filter(p => p.scrutin === SEL.scrutin && !SEL.caches.has(p.nom));

/* ------------------------------------------------------------------ graphiques */
function svgIn(box, H, label) {
  box.textContent = "";
  const W = Math.max(280, box.clientWidth);
  const svg = d3.select(box).append("svg").attr("width", W).attr("height", H).attr("viewBox", `0 0 ${W} ${H}`)
    .attr("role", "img").attr("aria-label", label);
  return {svg, W};
}
const FS = () => parseFloat(getComputedStyle(document.documentElement).fontSize) || 16;
function txtW(svg, s, size) {
  const t = svg.append("text").style("font-size", size + "px").text(s);
  const w = t.node().getComputedTextLength(); t.remove(); return w;
}
function wrapText(svg, s, size, maxW) {
  const words = s.split(/\s+/), lines = [];
  let cur = "";
  words.forEach(w => {
    const t = cur ? cur + " " + w : w;
    if (txtW(svg, t, size) > maxW && cur) { lines.push(cur); cur = w; } else cur = t;
  });
  if (cur) lines.push(cur);
  return lines;
}

/** Barres horizontales autour de zéro, libellé au-dessus de chaque barre (lisible sur mobile). */
function hbars(box, rows, o) {
  const fs = FS() * .875, lh = fs * 1.3;
  const tmp = svgIn(box, 10, o.label);
  const lines = rows.map(r => wrapText(tmp.svg, r.label, fs, tmp.W - 4));
  const barH = Math.max(14, fs * 1.1), gap = fs * .9;
  const rowH = lines.map(l => l.length * lh + barH + gap + 4);
  const H = d3.sum(rowH) + fs * 2;
  const {svg, W} = svgIn(box, H, o.label);
  const vals = rows.map(r => r.v);
  const lo = Math.min(0, d3.min(vals)), hi = Math.max(0, d3.max(vals));
  const vw = txtW(svg, "−000 %", fs) + 8;
  const x = d3.scaleLinear([lo, hi], [vw, W - vw]).nice();
  const yEnd = H - fs * 1.6;
  x.ticks(W < 480 ? 4 : 6).forEach(t => {
    svg.append("line").attr("x1", x(t)).attr("x2", x(t)).attr("y1", 0).attr("y2", yEnd).attr("stroke", t === 0 ? css("--axis") : css("--grid"));
    svg.append("text").attr("x", x(t)).attr("y", H - 4).attr("text-anchor", "middle").attr("class", "lbl-muted").style("font-size", fs + "px").text(o.tick ? o.tick(t) : n0(t));
  });
  let y = 0;
  rows.forEach((r, i) => {
    const g = svg.append("g").attr("transform", `translate(0,${y})`);
    lines[i].forEach((l, j) => g.append("text").attr("x", 0).attr("y", (j + 1) * lh - 3).style("font-size", fs + "px").style("font-weight", r.strong ? 700 : 400).text(l));
    const by = lines[i].length * lh + 2;
    g.append("rect").attr("x", x(Math.min(0, r.v))).attr("y", by).attr("width", Math.max(2, Math.abs(x(r.v) - x(0)))).attr("height", barH).attr("rx", 2).attr("fill", r.color || o.color(r));
    g.append("text").attr("x", r.v >= 0 ? x(r.v) + 5 : x(r.v) - 5).attr("y", by + barH * .78).attr("text-anchor", r.v >= 0 ? "start" : "end")
      .style("font-size", fs + "px").style("font-weight", 700).style("font-variant-numeric", "tabular-nums").text(o.fmt(r.v));
    y += rowH[i];
  });
}

function drawWaffle() {
  const box = $("#ch-waffle");
  const rows = D.mesures.filter(r => r.inclus_stats === "1").map(r => ({...r, e: Math.abs(num(r.ecart_pct))}))
    .sort((a, b) => a.e - b.e);
  const cats = [
    ["À 15 % près", css("--ok"), e => e <= 15],
    ["Écart de 15 à 50 %", css("--warn"), e => e > 15 && e <= 50],
    ["Écart de plus de 50 %", css("--bad"), e => e > 50],
  ];
  legend($("#lg-waffle"), cats.map(([n, c, f]) => [`${n} (${rows.filter(r => f(r.e)).length})`, c]));
  const fs = FS(), side = Math.max(26, fs * 1.9), pad = 6;
  const W0 = Math.max(280, box.clientWidth), per = Math.max(5, Math.floor((W0 + pad) / (side + pad)));
  const H = Math.ceil(rows.length / per) * (side + pad);
  const {svg} = svgIn(box, H, `${rows.length} mesures : ` + cats.map(([n, , f]) => `${rows.filter(r => f(r.e)).length} ${n.toLowerCase()}`).join(", "));
  rows.forEach((r, i) => {
    const c = cats.find(([, , f]) => f(r.e));
    svg.append("rect").attr("x", (i % per) * (side + pad)).attr("y", Math.floor(i / per) * (side + pad)).attr("width", side).attr("height", side).attr("rx", 3).attr("fill", c[1])
      .append("title").text(`${r.mesure} : écart de ${pc(r.e)}`);
  });
}

function drawEcarts() {
  const rows = D.mesures.filter(r => r.inclus_stats === "1").map(r => ({label: r.mesure, v: num(r.ecart_pct)})).sort((a, b) => b.v - a.v);
  hbars($("#ch-ecarts"), rows, {label: "Écart entre coût réel et coût annoncé, par mesure", fmt: v => sg(v, n0) + " %", tick: t => sg(t, n0) + " %",
    color: r => r.v >= 0 ? css("--ok") : css("--bad")});
}

function drawPS() {
  const box = $("#ch-ps"), fs = FS() * .875;
  legend($("#lg-ps"), [["Année normale", css("--s1")], ["Année cible en crise (exclue de la moyenne)", css("--border-strong")]]);
  const rows = D.ps.filter(r => r.e3 !== null).map(r => ({...r, d: -r.e3}));
  const H = 300, m = {t: 24, r: 8, b: fs * 3, l: fs * 2.6};
  const {svg, W} = svgIn(box, H, `Dépassement moyen de l'objectif de déficit à trois ans : ${K.ps_biais}, hors crises`);
  const x = d3.scaleBand(rows.map(r => r.annee_t3), [m.l, W - m.r]).padding(.2);
  const y = d3.scaleLinear([Math.min(0, d3.min(rows, r => r.d)), d3.max(rows, r => r.d)], [H - m.b, m.t]).nice();
  y.ticks(5).forEach(t => {
    svg.append("line").attr("x1", m.l).attr("x2", W - m.r).attr("y1", y(t)).attr("y2", y(t)).attr("stroke", t === 0 ? css("--axis") : css("--grid"));
    svg.append("text").attr("x", m.l - 6).attr("y", y(t) + 4).attr("text-anchor", "end").attr("class", "lbl-muted").style("font-size", fs + "px").text(n0(t));
  });
  const step = W < 520 ? 3 : W < 800 ? 2 : 1;
  rows.forEach((r, i) => {
    svg.append("rect").attr("x", x(r.annee_t3)).attr("width", x.bandwidth()).attr("y", Math.min(y(0), y(r.d))).attr("height", Math.max(1, Math.abs(y(r.d) - y(0))))
      .attr("fill", r.crise ? css("--border-strong") : css("--s1")).append("title").text(`Objectif fixé en ${r.millesime.slice(3, 7)} pour ${r.annee_t3} : ${sg(r.d)} point de PIB` + (r.crise ? " (crise)" : ""));
    if (i % step === 0) svg.append("text").attr("x", x(r.annee_t3) + x.bandwidth() / 2).attr("y", H - m.b + fs * 1.3).attr("text-anchor", "middle").attr("class", "lbl-muted").style("font-size", fs + "px").text(r.annee_t3);
  });
  const moy = mean(rows.filter(r => !r.crise).map(r => r.d));
  svg.append("line").attr("x1", m.l).attr("x2", W - m.r).attr("y1", y(moy)).attr("y2", y(moy)).attr("stroke", css("--text")).attr("stroke-dasharray", "5 4");
  svg.append("text").attr("x", W - m.r).attr("y", y(moy) - 6).attr("text-anchor", "end").style("font-size", fs + "px").style("font-weight", 700).style("paint-order", "stroke").style("stroke", css("--bg-raised")).style("stroke-width", 4).text(`Moyenne hors crises : ${pts(moy)}`);
  svg.append("text").attr("x", m.l).attr("y", H - 4).attr("class", "lbl-muted").style("font-size", fs + "px").text("Année visée par l'objectif");
  svg.append("text").attr("x", 0).attr("y", 12).attr("class", "lbl-muted").style("font-size", fs + "px").text("Points de PIB");
}

function drawPairs() {
  const rows = D.pairs.map(r => ({label: r.pays, v: r.v, strong: r.pays === "France"})).sort((a, b) => b.v - a.v);
  hbars($("#ch-pairs"), rows, {label: "Optimisme des prévisions de déficit à trois ans, par pays", fmt: v => sg(v) + " pt", tick: t => n0(t),
    color: r => r.strong ? css("--s1") : css("--s5")});
}

/** Barres groupées horizontales : un groupe par entité, une barre par série. */
function groupedBars(box, groups, series, o) {
  const fs = FS() * .875, barH = Math.max(16, fs * 1.25), lab = fs * 1.35, gap = 8, head = fs * 1.9;
  const grpH = head + series.length * (lab + barH + gap) + fs;
  const H = groups.length * grpH + fs * 1.8;
  const {svg, W} = svgIn(box, H, o.label);
  const vals = groups.flatMap(g => series.map(s => g[s.k]).filter(v => v !== null && !isNaN(v)));
  const lo = Math.min(0, d3.min(vals)), hi = Math.max(0, d3.max(vals));
  const vw = txtW(svg, "−000", fs) + 10;
  const x = d3.scaleLinear([lo, hi], [vw, W - vw]).nice();
  const yEnd = H - fs * 1.6;
  x.ticks(W < 480 ? 4 : 6).forEach(t => {
    svg.append("line").attr("x1", x(t)).attr("x2", x(t)).attr("y1", 0).attr("y2", yEnd).attr("stroke", t === 0 ? css("--axis") : css("--grid"));
    svg.append("text").attr("x", x(t)).attr("y", H - 4).attr("text-anchor", "middle").attr("class", "lbl-muted").style("font-size", fs + "px").text(n0(t));
  });
  groups.forEach((g, i) => {
    const G = svg.append("g").attr("transform", `translate(0,${i * grpH})`);
    G.append("text").attr("x", 0).attr("y", fs * 1.2).style("font-size", fs * 1.1 + "px").style("font-weight", 700).text(g.nom);
    series.forEach((s, j) => {
      const v = g[s.k], y0 = head + j * (lab + barH + gap), y = y0 + lab;
      const vide = v === null || isNaN(v);
      G.append("text").attr("x", x(0) + (x(0) > W / 2 ? -6 : 6)).attr("y", y0 + fs).attr("text-anchor", x(0) > W / 2 ? "end" : "start").attr("class", "lbl-muted").style("font-size", fs + "px")
        .text(s.n + (vide ? " : pas de chiffrage" : ""));
      if (vide) return;
      G.append("rect").attr("x", x(Math.min(0, v))).attr("y", y).attr("width", Math.max(2, Math.abs(x(v) - x(0)))).attr("height", barH).attr("rx", 2).attr("fill", s.c)
        .append("title").text(`${g.nom}, ${s.n} : ${sg(v)} Md€`);
      G.append("text").attr("x", v >= 0 ? x(v) + 5 : x(v) - 5).attr("y", y + barH * .75).attr("text-anchor", v >= 0 ? "start" : "end")
        .style("font-size", fs + "px").style("font-weight", 700).style("font-variant-numeric", "tabular-nums").text(sg(v, n0));
    });
  });
}

const SERIES_APP = () => [
  {k: "annonce", n: "Annoncé par le parti", c: css("--s5")},
  {k: "depart", n: "Chiffrage indépendant de départ", c: css("--s6")},
  {k: "corrige", n: "Après correction", c: css("--s1")},
];
function drawApp() {
  const S = SERIES_APP();
  legend($("#lg-app"), S.map(s => [s.n, s.c]));
  groupedBars($("#ch-app"), progsVus(), S, {label: "Effet des programmes sur le solde public : " + progsVus().map(p => `${p.court} ${sg(p.corrige, n0)} Md€ après correction`).join(", ")});
}

function drawDef() {
  const box = $("#ch-def"), fs = FS() * .875, P = progsVus();
  const parts = [["ref", "Prévision officielle de référence", css("--s5")], ["biais", "Dépassement habituel", css("--s2")], ["pts_pib", "Coût du programme, après correction", css("--s1")]];
  // Trait de comparaison : la prévision actuelle, seulement si elle n'est pas déjà la référence de tous les programmes
  const trait = P.some(p => p.refId !== "prevision_2027_actuelle");
  legend($("#lg-def"), [...parts.map(([, n, c]) => [n, c]), trait ? ["Prévision actuelle du gouvernement", css("--text"), "dash"] : null].filter(Boolean));
  const refs = d3.groups(P, p => `${p.refLib.toLowerCase()} (${n1(p.ref)} %), plus le dépassement habituel ${p.biaisLib} (${pts(p.biais)})`);
  $("#def-how").textContent = refs.map(([t, ps]) => (refs.length > 1 ? liste(ps.map(p => p.court)) + " : " : "Référence : ") + t + ".").join(" ") + (trait ? " Le trait pointillé montre la prévision actuelle du gouvernement pour 2027." : "");
  const barH = Math.max(26, fs * 2), rowH = fs * 1.8 + barH + fs * 1.2, H = P.length * rowH + fs * 2;
  const {svg, W} = svgIn(box, H, "Déficit 2027 : " + P.map(p => `${p.court} ${n1(p.deficit)} % du PIB`).join(", "));
  const x = d3.scaleLinear([0, d3.max(P, p => Math.max(p.deficit, p.ref + p.biais, K.prev_actuelle)) * 1.05], [0, W - 4]).nice();
  const yEnd = H - fs * 1.6;
  x.ticks(W < 480 ? 4 : 8).forEach(t => {
    svg.append("line").attr("x1", x(t)).attr("x2", x(t)).attr("y1", 0).attr("y2", yEnd).attr("stroke", css("--grid"));
    svg.append("text").attr("x", x(t)).attr("y", H - 4).attr("text-anchor", "middle").attr("class", "lbl-muted").style("font-size", fs + "px").text(n0(t) + " %");
  });
  P.forEach((p, i) => {
    const G = svg.append("g").attr("transform", `translate(0,${i * rowH})`);
    G.append("text").attr("x", 0).attr("y", fs * 1.2).style("font-size", fs * 1.1 + "px").style("font-weight", 700).text(`${p.court} : ${n1(p.deficit)} % du PIB`);
    let x0 = 0;
    parts.forEach(([k, n, c]) => {
      const w = x(p[k]) - x(0), neg = w < 0;
      // Un programme qui réduit le déficit : segment en retrait, en clair, depuis la fin de la barre
      G.append("rect").attr("x", neg ? x0 + w : x0).attr("y", fs * 1.8).attr("width", Math.max(1, Math.abs(w) - 2)).attr("height", barH).attr("fill", c)
        .attr("fill-opacity", neg ? .35 : 1).append("title").text(`${n} : ${sg(p[k])} pt`);
      if (Math.abs(w) > txtW(svg, "−0,0", fs) + 10) G.append("text").attr("x", x0 + w / 2).attr("y", fs * 1.8 + barH * .68).attr("text-anchor", "middle").style("font-size", fs + "px").style("font-weight", 700)
        .style("fill", neg ? css("--text") : textOn(c)).text(neg ? sg(p[k]) : n1(p[k]));
      x0 += neg ? 0 : w;
    });
  });
  if (trait) {
    const r = K.prev_actuelle;
    svg.append("line").attr("x1", x(r)).attr("x2", x(r)).attr("y1", fs * 1.5).attr("y2", yEnd).attr("stroke", css("--text")).attr("stroke-width", 2).attr("stroke-dasharray", "5 4");
  }
}

function drawSens() {
  const box = $("#ch-sens");
  box.textContent = "";
  const progs = progsVus().map(p => p.nom).filter(p => D.sensibilite.some(r => r.programme === p));
  if (!progs.length) box.append(h("p", {class: "muted"}, "Pas encore d'autre chiffrage indépendant pour ces programmes."));
  progs.forEach(p => {
    box.append(h("h4", {style: "margin:1rem 0 .25rem"}, p));
    const sub = h("div", {class: "chart"}); box.append(sub);
    const rows = D.sensibilite.filter(r => r.programme === p).map(r => ({label: r.chiffreur + (r.statut !== "indépendant" ? ` (${r.statut})` : ""), v: num(r.complete_corrige)})).sort((a, b) => a.v - b.v);
    hbars(sub, rows, {label: `${p} : effet corrigé selon l'organisme`, fmt: v => sg(v, n0) + " Md€", tick: t => n0(t), color: () => css("--s1")});
  });
}

function drawInc() {
  const box = $("#ch-inc"), fs = FS() * .875;
  legend($("#lg-inc"), [["Estimation centrale", css("--s1")], ["Fourchette (8 chances sur 10)", css("--s5"), "line"]]);
  const rows = D.scen, rowH = fs * 4.2, H = rows.length * rowH + fs * 2;
  const {svg, W} = svgIn(box, H, "Solde des scénarios : " + rows.map(r => `${r.nom} ${sg(r.solde, n0)} Md€ (de ${sg(r.p10, n0)} à ${sg(r.p90, n0)})`).join(", "));
  const x = d3.scaleLinear([Math.min(0, d3.min(rows, r => r.p10)), Math.max(0, d3.max(rows, r => r.p90))], [12, W - 12]).nice();
  const yEnd = H - fs * 1.6;
  x.ticks(W < 480 ? 4 : 8).forEach(t => {
    svg.append("line").attr("x1", x(t)).attr("x2", x(t)).attr("y1", 0).attr("y2", yEnd).attr("stroke", t === 0 ? css("--axis") : css("--grid")).attr("stroke-width", t === 0 ? 2 : 1);
    svg.append("text").attr("x", x(t)).attr("y", H - 4).attr("text-anchor", "middle").attr("class", "lbl-muted").style("font-size", fs + "px").text(n0(t));
  });
  rows.forEach((r, i) => {
    const y0 = i * rowH, yc = y0 + fs * 2.6;
    svg.append("text").attr("x", 0).attr("y", y0 + fs * 1.2).style("font-size", fs * 1.05 + "px").style("font-weight", 700)
      .text(`${r.nom} : ${sg(r.solde, n0)} Md€ (de ${sg(r.p10, n0)} à ${sg(r.p90, n0)})`);
    svg.append("line").attr("x1", x(r.p10)).attr("x2", x(r.p90)).attr("y1", yc).attr("y2", yc).attr("stroke", css("--s5")).attr("stroke-width", 6).attr("stroke-linecap", "round");
    svg.append("circle").attr("cx", x(r.solde)).attr("cy", yc).attr("r", 8).attr("fill", css("--s1")).attr("stroke", css("--bg-raised")).attr("stroke-width", 2);
  });
}

/** Scénarios de projection, lus dans projection.csv (hors variantes « stress », qui en sont dérivées). */
function PROJ() {
  const pal = ["--s2", "--s4", "--s3", "--s6", "--s1"];
  let i = 0;
  return [...new Set(D.projection.map(r => r.scenario))].filter(n => !/, stress /.test(n)).map(n =>
    n === "Référence du gouvernement" ? {n, c: css("--s5"), court: "Gouvernement", leg: "Prévision du gouvernement"}
    : n === "Référence corrigée du biais" ? {n, c: css("--text"), court: "Gouvernement corrigé", leg: "Prévision corrigée de l'optimisme habituel"}
    : {n, c: css(pal[i++ % pal.length]), court: n.replace(/^Panier /, ""), leg: "Scénario " + n.replace(/^Panier /, "")});
}
const projNom = (n, stress) => {
  if (!stress) return n;
  const st = n.replace(" du biais", "") + ", stress +25 pb";
  return D.projection.some(r => r.scenario === st) ? st : n;  // sans variante « stress » (gouvernement) : série d'origine
};
function projSeries(ind, stress) {
  return PROJ().map(s => ({...s, pts: D.projection.filter(r => r.scenario === projNom(s.n, stress))
    .map(r => ({a: num(r.annee), v: num(r[ind]), ext: r.extrapole === "1"}))}));
}

function drawProj() {
  const ind = $("input[name=ind]:checked").value, stress = $("#f-stress").checked;
  const lib = ind === "dette_pct" ? "Dette publique" : "Déficit public";
  $("#titre-proj").textContent = lib + ", en % du PIB";
  const series = projSeries(ind, stress);
  legend($("#lg-proj"), series.map(s => [s.leg, s.c, "line"]));
  const box = $("#ch-proj"), fs = FS() * .875;
  const W0 = Math.max(280, box.clientWidth), endLab = W0 >= 600;
  const H = 340, m = {t: 14, r: endLab ? 170 : 12, b: fs * 2.2, l: fs * 2.6};
  const last = series.map(s => s.pts[s.pts.length - 1]);
  const {svg, W} = svgIn(box, H, `${lib} en ${last[0]?.a} : ` + series.map((s, i) => `${s.court} ${n1(last[i].v)} %`).join(", "));
  const annees = [...new Set(series.flatMap(s => s.pts.map(p => p.a)))].sort();
  const x = d3.scalePoint(annees, [m.l, W - m.r]);
  const all = series.flatMap(s => s.pts.map(p => p.v));
  const y = d3.scaleLinear([d3.min(all), d3.max(all)], [H - m.b, m.t]).nice();
  y.ticks(6).forEach(t => {
    svg.append("line").attr("x1", m.l).attr("x2", W - m.r).attr("y1", y(t)).attr("y2", y(t)).attr("stroke", css("--grid"));
    svg.append("text").attr("x", m.l - 6).attr("y", y(t) + 4).attr("text-anchor", "end").attr("class", "lbl-muted").style("font-size", fs + "px").text(n0(t));
  });
  annees.forEach((a, i) => { if (W < 420 && i % 2) return; svg.append("text").attr("x", x(a)).attr("y", H - fs * .6).attr("text-anchor", "middle").attr("class", "lbl-muted").style("font-size", fs + "px").text(a); });
  const ln = d3.line().x(p => x(p.a)).y(p => y(p.v));
  series.forEach(s => {
    const k = s.pts.findLastIndex(p => !p.ext);
    svg.append("path").attr("d", ln(s.pts.slice(0, k + 1))).attr("fill", "none").attr("stroke", s.c).attr("stroke-width", 3);
    svg.append("path").attr("d", ln(s.pts.slice(Math.max(0, k)))).attr("fill", "none").attr("stroke", s.c).attr("stroke-width", 3).attr("stroke-dasharray", "6 4");
  });
  if (endLab) {
    // Étiquettes de fin de courbe, écartées pour ne pas se chevaucher
    const labs = series.map((s, i) => ({s, y: y(last[i].v), v: last[i].v})).sort((a, b) => a.y - b.y);
    const minGap = fs * 1.35;
    for (let i = 1; i < labs.length; i++) if (labs[i].y - labs[i - 1].y < minGap) labs[i].y = labs[i - 1].y + minGap;
    labs.forEach(l => svg.append("text").attr("x", W - m.r + 8).attr("y", l.y + 4).style("font-size", fs + "px").style("font-weight", 700).style("fill", l.s.c).text(`${l.s.court} ${n1(l.v)}`));
  }
  // Tableau
  table($("#tb-proj"), [{t: "Année", f: r => r.a}, ...series.map(s => ({t: s.court, num: true, f: r => {
    const p = s.pts.find(q => q.a === r.a); return p ? n1(p.v) + (p.ext ? "*" : "") : "—"; }}))],
    annees.map(a => ({a})), {caption: lib + " (% du PIB) ; * = prolongation des tendances"});
}

/* ------------------------------------------------------------------ remplissage des vues */
function remplirK() {
  $$("[data-k]").forEach(el => { if (K[el.dataset.k] !== undefined) el.textContent = K[el.dataset.k]; });
}

function vueHier() {
  table($("#tb-ecarts"), [{t: "Mesure", f: r => r.mesure}, {t: "Écart", num: true, f: r => sg(num(r.ecart_pct), n0) + " %", cls: r => signCls(num(r.ecart_pct), .5)}],
    D.mesures.filter(r => r.inclus_stats === "1").sort((a, b) => num(b.ecart_pct) - num(a.ecart_pct)));

  const V = {"Surestimé": "bad", "Non réalisé": "bad", "Non mesuré": "", "Conforme": "ok", "Au moins conforme": "ok", "Sous-estimé": "warn"};
  const box = $("#cards-effets"); box.textContent = "";
  D.effets.forEach(r => {
    const k = Object.keys(V).find(v => r.verdict.startsWith(v));
    box.append(h("article", {class: "card"},
      h("h3", {}, r.mesure), h("p", {class: "muted", style: "margin-bottom:.75rem"}, r.effet),
      h("dl", {}, h("dt", {}, "Annoncé"), h("dd", {style: "font-weight:400;text-align:left"}, r.annonce),
        h("dt", {}, "Mesuré"), h("dd", {style: "font-weight:400;text-align:left"}, r.mesure_ex_post)),
      h("p", {class: "verdict"}, badge(r.verdict, V[k] || ""), " ", r.source_ex_post ? lien(r.source_ex_post, "source") : "")));
  });

  table($("#tb-ps"), [{t: "Programme", f: r => r.millesime}, {t: "Année visée", num: true, f: r => r.annee_t3},
    {t: "Objectif", num: true, f: r => n1(num(r.prev_t3))}, {t: "Réalisé", num: true, f: r => n1(num(r.real_t3))},
    {t: "Dépassement", num: true, f: r => sg(-r.e3) + (r.crise ? " (crise)" : "")}], D.ps.filter(r => r.e3 !== null),
    {caption: "Solde public en % du PIB (négatif = déficit)"});

  const CF = {high: ["élevée", "ok"], medium: ["moyenne", "warn"], low: ["faible", "bad"]};
  table($("#tb-mesures"), [
    {t: "Mesure", f: r => [r.mesure, r.inclus_stats === "1" ? "" : h("div", {class: "small muted"}, "exclue de la statistique principale")]},
    {t: "Année", num: true, f: r => r.annee},
    {t: "Annoncé", num: true, f: r => n1(num(r.ex_ante))},
    {t: "Réel", num: true, f: r => n1(num(r.ex_post_central))},
    {t: "Écart", num: true, f: r => sg(num(r.ecart_pct), n0) + " %", cls: r => signCls(num(r.ecart_pct), .5)},
    {t: "Cause principale", f: r => r.cause_principale},
    {t: "Fiabilité", f: r => badge(...(CF[r.confiance] || [r.confiance]))},
    {t: "Sources", f: r => [lien(r.source_ex_ante, "avant"), " ", lien(r.source_ex_post, "après")]},
  ], D.mesures);

  table($("#tb-causes"), [{t: "Cause", f: r => r.cause_principale}, {t: "Mesures", num: true, f: r => r.n},
    {t: "Erreur habituelle", num: true, f: r => pc(num(r.erreur_abs_mediane_pct))}], D.causes);
}

function vueProgrammes() {
  const recents = D.scrutins.filter(sc => num(sc.match(/\d{4}/)) >= 2027);
  $("#note-scrutin").textContent = recents.length
    ? `Les programmes ${liste(recents.map(scrutinDe))} sont ajoutés au fur et à mesure de leur publication et de leur chiffrage.`
    : `Les programmes de la présidentielle de 2027 ne sont pas encore publiés : les exemples portent sur ${liste(D.scrutins.map(scrutinLes))}.`;
  // Choix de l'élection (si plusieurs) et des programmes affichés (s'il y en a plus de deux)
  SEL.scrutin = D.scrutins[0];
  const fsS = $("#choix-scrutin"), fsP = $("#choix-progs");
  fsS.hidden = D.scrutins.length < 2;
  $$(".choice", fsS).forEach(e => e.remove());
  D.scrutins.forEach((sc, i) => fsS.append(h("label", {class: "choice"}, h("input", {type: "radio", name: "scrutin", value: sc, checked: i === 0 ? "" : null}), h("span", {}, sc))));
  fsS.onchange = () => { SEL.scrutin = $("input[name=scrutin]:checked").value; SEL.caches.clear(); majProgrammes(); };
  fsP.onchange = e => { e.target.checked ? SEL.caches.delete(e.target.value) : SEL.caches.add(e.target.value); majProgrammes(); };
  $("#f-prog").onchange = tableProgrammes;
  majProgrammes();
}

function majProgrammes() {
  const tous = D.progs.filter(p => p.scrutin === SEL.scrutin), P = progsVus();
  const fsP = $("#choix-progs");
  fsP.hidden = tous.length < 3;
  $$(".check", fsP).forEach(e => e.remove());
  tous.forEach(p => fsP.append(h("label", {class: "check"}, h("input", {type: "checkbox", name: "prog", value: p.nom, checked: SEL.caches.has(p.nom) ? null : ""}), p.nom)));

  $("#lede-programmes").textContent = `${SEL.scrutin} : ${tous.length === 1 ? "le programme" : "les programmes"} ${liste(tous.map(p => p.nom))}. ` +
    "On part d'un chiffrage indépendant, mesure par mesure, puis on le corrige avec les leçons du passé.";

  const bref = $("#bref-programmes"); bref.textContent = "";
  P.forEach(p => {
    const ann = p.annonce === null ? "n'a pas publié de chiffrage global" : p.annonce === 0 ? "se présente comme équilibré" : `annonce ${sg(p.annonce, n0)} Md€`;
    const eff = p.corrige < 0 ? `augmenterait le déficit d'environ ${md(p.corrige)} par an, soit ${pts(p.pts_pib)} de PIB` : `réduirait le déficit d'environ ${md(p.corrige)} par an`;
    bref.append(h("li", {}, h("strong", {}, p.court), ` ${ann}. Après correction, il ${eff}.`));
  });
  const au = P.filter(p => p.deficit > p.ref);
  if (au.length) bref.append(h("li", {}, `${au.length === P.length && P.length > 1 ? "Pour tous les programmes affichés, le" : "Le"} déficit de 2027 dépasserait la prévision officielle de référence : ` +
    au.map(p => `${n1(p.deficit)} % du PIB pour ${p.court} (référence ${n1(p.ref)} %)`).join(", ") + "."));
  if (!P.length) bref.append(h("li", {}, "Aucun programme sélectionné."));

  const box = $("#cards-programmes"); box.textContent = "";
  P.forEach(p => box.append(h("article", {class: "card"}, h("h3", {}, p.nom), h("p", {class: "muted small"}, p.position),
    h("dl", {},
      h("dt", {}, "Annoncé par le parti"), h("dd", {}, p.annonce === null ? "non chiffré" : sg(p.annonce, n0) + " Md€"),
      h("dt", {}, "Chiffrage indépendant de départ"), h("dd", {}, sg(p.depart, n0) + " Md€"),
      h("dt", {class: "total"}, "Après correction"), h("dd", {class: "total " + signCls(p.corrige)}, sg(p.corrige, n0) + " Md€"),
      h("dt", {}, "Fourchette (8 chances sur 10)"), h("dd", {}, `${sg(p.p10, n0)} à ${sg(p.p90, n0)}`),
      h("dt", {}, "Déficit 2027 qui en résulte"), h("dd", {}, n1(p.deficit) + " % du PIB")),
    h("p", {style: "margin:.9rem 0 0"}, btnTotal("application_lignes", p.nom, "Pourquoi ce chiffre ?")),
    h("p", {class: "small muted", style: "margin:.9rem 0 0"}, "Point de départ : " + p.sources + "."))));

  const sel = $("#f-prog");
  sel.textContent = ""; sel.append(h("option", {value: ""}, P.length > 1 ? "Tous les programmes affichés" : P[0]?.nom || "—"));
  if (P.length > 1) P.forEach(p => sel.append(h("option", {value: p.nom}, p.nom)));
  tableProgrammes();

  const noms = new Set(P.map(p => p.nom));
  table($("#tb-sens"), [
    {t: "Chiffreur", f: r => r.chiffreur}, {t: "Statut", f: r => r.statut},
    {t: "Lignes chiffrées", num: true, f: r => `${r.lignes_chiffrees} / ${r.lignes_programme}`},
    {t: "Publié", num: true, f: r => sg(num(r.solde_publie))},
    {t: "Propre, statique", num: true, f: r => sg(num(r.propre_statique))}, {t: "Propre, corrigé", num: true, f: r => sg(num(r.propre_corrige))},
    {t: "Complété, statique", num: true, f: r => sg(num(r.complete_statique))}, {t: "Complété, corrigé", num: true, f: r => sg(num(r.complete_corrige))},
  ], D.sensibilite.filter(r => noms.has(r.programme)), {group: r => r.programme});

  const cols = Object.keys(D.confiance[0]).filter(c => c.startsWith("correction_"));
  table($("#tb-confiance"), [{t: "Programme ou scénario", f: r => r.groupe},
    ...cols.map(c => ({t: c.replace("correction_", "").replace(/_/g, " ").replace(/^./, s => s.toUpperCase()), num: true, f: r => sg(num(r[c]))})),
    {t: "Part confirmée", num: true, f: r => r.part_confirmee_pct + " %"}], D.confiance.filter(r => r.fichier !== "application_lignes" || noms.has(r.groupe)));

  if (vueCourante === "programmes") dessiner();
}

function tableProgrammes() {
  const v = $("#f-prog").value, noms = new Set(progsVus().map(p => p.nom));
  table($("#tb-app"), [
    {t: "Mesure", f: r => r.ligne},
    {t: "Annoncé par le parti", num: true, f: r => r.annonce_parti === "" ? "—" : sg(num(r.annonce_parti))},
    {t: "Indépendant", num: true, f: r => sg(num(r.independant))},
    {t: "Source", f: r => r.source_independant},
    {t: "Après correction", num: true, f: r => [sg(r.corrige), " ", btnPourquoi("application_lignes", r.id, r.ligne)], cls: r => signCls(r.corrige - num(r.independant))},
    {t: "Règle", f: r => r.regle},
    {t: "Justification", f: r => r.justification},
    {t: "Autres chiffrages", f: r => r.autres_estimations},
  ], D.app.filter(r => v ? r.programme === v : noms.has(r.programme)), {group: r => r.programme});
}

/** « Législatives 2024 » → « les législatives de 2024 » ; « Présidentielle 2027 » → « la présidentielle de 2027 ». */
function scrutinLes(sc) {
  const m = sc.match(/^(.*\S)\s+(\d{4})$/);
  if (!m) return sc;
  const nom = m[1].toLowerCase();
  return (/s$/.test(nom) ? "les " : "la ") + nom + " de " + m[2];
}
/** … avec « de » contracté : « des législatives de 2024 », « de la présidentielle de 2027 ». */
const scrutinDe = sc => { const t = scrutinLes(sc); return t.startsWith("les ") ? "des " + t.slice(4) : "de " + t; };

/** « A », « A et B », « A, B et C » */
function liste(a) { return a.length < 2 ? a.join("") : a.slice(0, -1).join(", ") + " et " + a[a.length - 1]; }

function vueEquilibre() {
  const bref = $("#bref-equilibre"); bref.textContent = "";
  D.scen.forEach(s => bref.append(h("li", {}, h("strong", {}, s.nom), s.solde >= 0
    ? ` : les recettes couvrent les mesures phares, avec un excédent d'environ ${md(s.solde)} par an` + (s.investissement ? `, hors investissement emprunté (${md(s.investissement)}).` : ".")
    : ` : il manque environ ${md(s.solde)} par an pour financer les mesures phares.`)));
  bref.append(h("li", {}, "Ces montants sont des estimations : la fourchette ci-dessous montre leur marge d'incertitude."));

  const box = $("#cards-paniers"); box.textContent = "";
  D.scen.forEach(s => {
    const fin = s.lignes.filter(r => r.role === "Financement").sort((a, b) => b.corrige - a.corrige);
    box.append(h("article", {class: "card"}, h("h3", {}, s.nom),
      h("dl", {},
        h("dt", {}, "Coût des mesures phares"), h("dd", {class: "neg"}, sg(s.mesures, n0) + " Md€"),
        h("dt", {}, "Recettes et économies"), h("dd", {class: "pos"}, sg(s.financement, n0) + " Md€"),
        s.investissement ? [h("dt", {}, "Investissement emprunté (hors équilibre)"), h("dd", {}, sg(s.investissement, n0) + " Md€")] : null,
        h("dt", {class: "total"}, "Solde"), h("dd", {class: "total " + signCls(s.solde)}, sg(s.solde, n0) + " Md€")),
      h("p", {class: "verdict"}, s.solde >= 0 ? badge("Financé", "ok") : badge("Non financé", "bad"), " ", btnTotal("paniers", s.nom, "Pourquoi ce chiffre ?")),
      h("details", {class: "data-toggle"}, h("summary", {}, "Qui paierait ?"),
        h("ul", {class: "small", style: "padding-left:1.1rem"}, fin.map(r => h("li", {}, `${r.qui_paie} : ${sg(r.corrige)} Md€ (${r.ligne})`))))));
  });

  const sel = $("#f-var");
  if (sel.options.length === 1) D.scen.forEach(s => sel.append(h("option", {value: s.nom}, s.nom)));
  const drawTb = () => table($("#tb-pan"), [
    {t: "Ligne", f: r => r.ligne}, {t: "Rôle", f: r => r.role},
    {t: "Statique", num: true, f: r => sg(num(r.statique))},
    {t: "Après correction", num: true, f: r => [sg(r.corrige), " ", btnPourquoi("paniers", r.id, r.ligne)], cls: r => signCls(r.corrige)},
    {t: "Règle", f: r => r.regle}, {t: "Incertitude", f: r => r.incertitude}, {t: "Qui paie", f: r => r.qui_paie},
    {t: "Source", f: r => lien(r.url, r.source) || r.source},
  ], D.pan.filter(r => !sel.value || r.variante === sel.value), {group: r => r.variante});
  sel.onchange = drawTb; drawTb();

  const deg = new Map(D.scen.map(s => [s.nom, s.degel]));
  table($("#tb-inc"), [
    {t: "Composante", f: r => r.composante}, {t: "Central", num: true, f: r => sg(num(r.central))},
    {t: "Loi votée seule", num: true, f: r => sg(num(r.loi_votee_seule))},
    {t: "P10", num: true, f: r => sg(num(r.p10))}, {t: "P50", num: true, f: r => sg(num(r.p50))}, {t: "P90", num: true, f: r => sg(num(r.p90))},
    {t: "Variante « dégel »", num: true, f: r => r.composante === "solde" && deg.get(r.groupe) != null ? sg(deg.get(r.groupe)) : ""},
  ], D.totaux, {group: r => r.groupe, rowCls: r => r.composante === "solde" ? "strong" : null});
}

function vueFoyer() {
  const ref = new Map(D.reformes.map(r => [r.id, r]));
  const origine = id => {
    const [f, lid] = (ref.get(id)?.ligne_liee || "").split(" ");
    // ligne_liee nomme une ligne (« nfp_flat ») ou un préfixe commun aux variantes d'une ligne (« l_smic » → l_smic_i, l_smic_a)
    const ok = r => r.id === lid || r.id.startsWith(lid + "_");
    const src = !lid ? "" : f === "paniers" ? D.paniers.find(ok)?.variante : D.application.find(ok)?.programme;
    return src ? src.replace(/ (intégral|ajusté)$/, "") : "";
  };
  const lignes = rs => {
    const out = $("#foyer-result"); out.textContent = "";
    rs.forEach(r => {
      const g = num(r.gain_annuel), cls = g > 0 ? "gain" : g < 0 ? "perte" : "neutre", o = origine(r.reforme);
      out.append(h("div", {class: "foyer-row " + cls},
        h("div", {}, h("strong", {}, ref.get(r.reforme)?.libelle || r.reforme), o ? h("div", {class: "small muted"}, "Mesure étudiée dans : " + o) : null),
        h("div", {class: "amt " + (g > 0 ? "pos" : g < 0 ? "neg" : "muted")}, g === 0 ? "Aucun effet" : sg(g, n0) + " €"),
        g !== 0 ? h("div", {class: "per"}, `par an, soit ${sg(g / 12, n0)} € par mois (${sg(num(r.gain_pct))} % du revenu)`) : null));
    });
  };

  // Simulateur : la grille précalculée (distributif_grille.csv) contient toutes les combinaisons du formulaire
  const G = D.grille, f = $("#sim-foyer");
  const val = n => $(`input[name=${n}]:checked`, f)?.value;
  const uniq = (rs, c) => [...new Set(rs.map(r => r[c]))].sort((x, y) => num(x) - num(y));
  const smic = v => v === 1 ? "SMIC à temps plein" : v < 1 ? `SMIC à temps partiel, ${n0(v * 100)} %` : `${FR.format(",.2~f")(v)} SMIC`;
  $("#sim-capital").textContent = "";
  uniq(G, "capital").forEach(c => $("#sim-capital").append(h("option", {value: c}, num(c) === 0 ? "Aucun" : eur(num(c)))));
  const show = () => {
    const st = val("statut");
    $("#sim-enfants").hidden = st === "retraite";
    if (st === "retraite") $("input[name=enfants][value='0']", f).checked = true;
    const cle = {statut: st, composition: val("composition"), enfants: val("enfants"), capital: $("#sim-capital").value};
    const rs = G.filter(r => Object.entries(cle).every(([k, v]) => r[k] === v));
    // Libellés des revenus en euros nets, recalculés pour la situation (la CSG des pensions dépend du foyer)
    const sel = $("#sim-niveau"), rang = Math.max(0, sel.selectedIndex), avant = sel.dataset.statut === st ? rang : (st === "actif" ? 1 : 2);
    sel.dataset.statut = st; sel.textContent = "";
    $("#sim-niveau-l").textContent = st === "actif" ? "Salaire net par mois, par personne qui travaille" : "Pension nette par mois, par personne retraitée";
    uniq(rs, "niveau").forEach(v => {
      const r = rs.find(x => x.niveau === v), nv = num(v);
      sel.append(h("option", {value: v}, `environ ${eur(num(r.net_mensuel_reference))} (${st === "actif" ? smic(nv) : eur(nv) + " bruts"})`));
    });
    sel.selectedIndex = Math.min(avant, sel.options.length - 1);
    const choix = rs.filter(r => r.niveau === sel.value);
    if (!choix.length) return;
    const rev = num(choix[0].revenu_disponible_avant);
    $("#foyer-intro").textContent = `Revenu disponible actuel du foyer (après impôts et prestations) : ${eur(rev)} par an, soit environ ${eur(rev / 12)} par mois.`;
    lignes(choix);
  };
  f.onchange = show; f.onsubmit = e => e.preventDefault(); show();

  // En bref : qui est touché, dans toute la grille
  const ids = [...new Set(G.map(r => r.id))].length, bref = $("#bref-foyer"); bref.textContent = "";
  [...new Set(G.map(r => r.reforme))].forEach(id => {
    const gs = G.filter(r => r.reforme === id).map(r => num(r.gain_annuel)), pos = gs.filter(g => g > 0), neg = gs.filter(g => g < 0);
    const part = (a, verbe) => {
      if (!a.length) return "";
      const lo = d3.min(a, Math.abs), hi = d3.max(a, Math.abs);
      return `${a.length} situation${a.length > 1 ? "s" : ""} sur ${ids} y ${verbe[a.length > 1 ? 1 : 0]} (${lo === hi ? eur(lo) : `de ${eur(lo)} à ${eur(hi)}`} par an)`;
    };
    const txt = [part(pos, ["gagne", "gagnent"]), part(neg, ["perd", "perdent"])].filter(Boolean).join(", ");
    bref.append(h("li", {}, h("strong", {}, ref.get(id)?.libelle || id), " : ", txt || "aucun effet sur les situations calculées", "."));
  });
  bref.append(h("li", {}, "Les autres situations ne sont pas touchées : chaque mesure vise un public précis."));

  const rg = $("#foyer-regles"); rg.textContent = "";
  D.reformes.forEach(r => rg.append(h("li", {}, h("strong", {}, r.libelle), " : ", r.note || "", ". ",
    origine(r.id) ? `Mesure étudiée dans : ${origine(r.id)}. ` : "", lien(r.url, "Source"))));

  const menages = [...new Set(D.distributif.map(r => r.menage))];
  const reformes = [...new Map(D.distributif.map(r => [r.reforme, r.libelle]))];
  table($("#tb-dist"), [{t: "Foyer", f: m => m}, {t: "Revenu disponible", num: true, f: m => eur(num(D.distributif.find(r => r.menage === m).revenu_disponible_avant))},
    ...reformes.map(([id, l]) => ({t: l, num: true, f: m => {
      const r = D.distributif.find(x => x.menage === m && x.reforme === id), g = r ? num(r.gain_annuel) : NaN;
      return isNaN(g) ? "—" : g === 0 ? "0 €" : `${sg(g, n0)} € (${sg(num(r.gain_pct))} %)`;
    }, cls: m => ""}))], menages);
}

function vueDemain() {
  const sd = projSeries("dette_pct", false).map(s => ({...s, fin: s.pts[s.pts.length - 1]}));
  const gouv = sd.find(s => s.n === "Référence du gouvernement"), corr = sd.find(s => s.n === "Référence corrigée du biais");
  const autres = sd.filter(s => s !== gouv && s !== corr);
  const bref = $("#bref-demain"); bref.textContent = "";
  if (gouv) bref.append(h("li", {}, `Selon la trajectoire du gouvernement prolongée, la dette serait de ${n0(gouv.fin.v)} % du PIB en ${gouv.fin.a}.`));
  if (corr) bref.append(h("li", {}, `Si les objectifs sont manqués comme d'habitude, elle atteindrait plutôt ${n0(corr.fin.v)} %.`));
  if (autres.length) bref.append(h("li", {}, "Avec les scénarios : " + autres.map(s => `${s.court} ${n0(s.fin.v)} %`).join(", ") + "."));
  bref.append(h("li", {}, "Au-delà de 2029, ces chiffres prolongent simplement les tendances : ils sont indicatifs."));
  $$("input[name=ind], #f-stress").forEach(i => i.onchange = drawProj);
  const nt = $("#nt-proj");
  nt.textContent = "Contrôle : le calcul retrouve la trajectoire publiée dans le budget 2027 (" + D.projection_controle.map(r =>
    `${r.indicateur === "dette_pct" ? "dette" : "déficit"} ${r.annee} : ${n1(num(r.calcule))} % calculé, ${n1(num(r.plf))} % publié`).join(" ; ") + ").";
}

function vueMethode() {
  table($("#tb-regles"), [{t: "Type de chiffrage", f: r => r.categorie}, {t: "Correction appliquée", f: r => h("strong", {}, r.correction_2027)},
    {t: "Ce qu'on a observé", f: r => r.base_empirique}], D.regles);

  const g = n => D.validation_resume.find(r => r.groupe.trim().startsWith(n));
  const lignes = [["Effets annoncés", "les effets promis (emplois, investissements)"], ["Chiffrages officiels, statistique principale", "le coût des mesures chiffrées par l'État"], ["Chiffrages d'instituts (tous)", "les chiffrages des instituts"]];
  const box = $("#bref-validation"); box.textContent = "";
  box.append(h("h3", {}, "En bref"));
  box.append(h("ul", {}, lignes.map(([k, lib]) => {
    const r = g(k), a = num(r.erreur_mediane_depart_pct), b = num(r.erreur_mediane_nous_pct);
    const verdict = b < a * .75 ? "nette amélioration" : b < a ? "légère amélioration" : b > a ? "pas d'amélioration" : "aucun changement";
    return h("li", {}, h("strong", {}, `Pour ${lib} : ${verdict}.`), ` L'erreur habituelle passe de ${pc(a)} à ${pc(b)} (${r.n} cas).`);
  })));
  box.append(h("p", {style: "margin-top:.75rem"}, "La méthode est donc surtout utile pour repérer les promesses d'effets trop optimistes ; sur le coût direct des mesures, les chiffrages officiels sont déjà assez bons."));

  table($("#tb-valr"), [{t: "Groupe", f: r => r.groupe.trim(), cls: r => /^\s/.test(r.groupe) ? "sub" : ""},
    {t: "Cas", num: true, f: r => r.n}, {t: "Erreur avant", num: true, f: r => pc(num(r.erreur_mediane_depart_pct))},
    {t: "Erreur après", num: true, f: r => pc(num(r.erreur_mediane_nous_pct)), cls: r => signCls(num(r.erreur_mediane_depart_pct) - num(r.erreur_mediane_nous_pct))},
    {t: "Améliorées / dégradées", num: true, f: r => `${r.ameliores} / ${r.degrades}`}], D.validation_resume, {rowCls: r => /^\s/.test(r.groupe) ? null : "strong"});

  const ST = {"confirmée": "ok", "contredite": "bad", "mitigée": "warn"};
  table($("#tb-valg"), [{t: "Règle", f: r => r.regle}, {t: "Statut", f: r => badge(r.statut, ST[r.statut] || "")},
    {t: "Cas", num: true, f: r => r.n}, {t: "Détail", f: r => r.note}], [...D.validation_regles].sort((a, b) => num(b.n) - num(a.n)));

  table($("#tb-hyp"), [{t: "Levier", f: r => r.levier}, {t: "Hypothèse", f: r => r.hypothese}, {t: "Effet sur le chiffrage", f: r => r.effet_chiffrage}], D.hypotheses);

  const sd = $("#f-domaine"), st = $("#f-texte");
  if (sd.options.length === 1) [...new Set(D.elasticites.map(r => r.domaine))].forEach(d => sd.append(h("option", {value: d}, d)));
  const drawEl = () => {
    const q = st.value.trim().toLowerCase();
    const rows = D.elasticites.filter(r => (!sd.value || r.domaine === sd.value) && (!q || Object.values(r).join(" ").toLowerCase().includes(q)));
    $("#nb-elast").textContent = `${rows.length} étude${rows.length > 1 ? "s" : ""} affichée${rows.length > 1 ? "s" : ""}.`;
    table($("#tb-elast"), [{t: "Paramètre", f: r => r.parametre}, {t: "Valeur", f: r => r.valeur_centrale}, {t: "Fourchette", f: r => r.fourchette},
      {t: "Contexte", f: r => r.pays_periode}, {t: "Méthode", f: r => r.methode}, {t: "Usage", f: r => r.usage_2027},
      {t: "Source", f: r => lien(r.url, r.source) || r.source}], rows);
  };
  sd.onchange = drawEl; st.oninput = drawEl; drawEl();

  table($("#tb-fichiers"), [{t: "Contenu", f: r => r[1]}, {t: "Fichier", f: r => h("a", {href: `../data/${r[0]}.csv`, download: ""}, r[0] + ".csv")}], FICHIERS);
}

/* ------------------------------------------------------------------ « Pourquoi ce chiffre ? »
   Pour chaque montant corrigé : chiffrage de départ et sa source, règle appliquée et ce qui la fonde, part déjà
   dans la référence, recoupements, résultat et fourchette, et ce que le test sur le passé dit de la règle.
   corrige_central = montant × facteur_moteur × facteur_reference × facteur_interaction (moteur.py). */
const n2 = FR.format(",.2f");
const impact = v => v < 0 ? `un coût de ${md(v)} par an` : v > 0 ? `un gain de ${md(v)} par an` : "aucun effet";
let pqOrigine = null;

function btnPourquoi(fichier, id, libelle) {
  const b = h("button", {type: "button", class: "btn-pq", "aria-label": `Pourquoi ce chiffre : ${libelle}`}, "Pourquoi ?");
  b.onclick = () => pourquoi(fichier, id);
  return b;
}
function btnTotal(fichier, groupe, txt) {
  const b = h("button", {type: "button", class: "btn-pq big"}, txt);
  b.onclick = () => pourquoiTotal(fichier, groupe);
  return b;
}
function ouvrir(titre, ...corps) {
  const dlg = $("#pq");
  pqOrigine = document.activeElement;
  $("#pq-titre").textContent = titre;
  const c = $("#pq-corps"); c.textContent = ""; c.append(...corps.flat().filter(Boolean));
  if (!dlg.open) dlg.showModal();
  c.scrollTop = 0; dlg.scrollTop = 0;
  $("#pq-fermer").focus();
}

/** Sources d'une règle : ids de regles.csv (élasticités ou mesures du backtest) rendus en liens lisibles. */
function sourcesRegle(refs) {
  return (refs || "").split(/\s+/).filter(Boolean).map(id => {
    const e = D.elasticites.find(r => r.id === id);
    if (e) return h("li", {}, `${e.parametre} : ${e.valeur_centrale} (${e.pays_periode}). `, lien(e.url, e.source) || e.source);
    const m = D.mesures.find(r => r.id === id);
    if (m) return h("li", {}, `${m.mesure} (${m.annee}) : annoncé ${n1(num(m.ex_ante))}, réel ${n1(num(m.ex_post_central))} Md€. `, lien(m.source_ex_post, "évaluation"));
    const f = D.effets.find(r => r.id === id);
    if (f) return h("li", {}, `${f.mesure}, ${f.effet.toLowerCase()} : annoncé ${f.annonce}, mesuré ${f.mesure_ex_post}. `, lien(f.source_ex_post, "évaluation"));
    return h("li", {}, id);
  });
}
function statutRegle(regle) {
  if (regle === "Aucune") return null;
  const v = D.validation_regles.find(r => r.regle === regle);
  if (!v) return null;
  const k = {"confirmée": "ok", "contredite": "bad", "mitigée": "warn"}[v.statut] || "";
  const phrase = v.statut === "confirmée" ? `Testée sur ${v.n} mesure${v.n > 1 ? "s" : ""} passée${v.n > 1 ? "s" : ""}, elle a amélioré les chiffrages.`
    : v.statut === "contredite" ? "Testée sur le passé, elle n'a pas amélioré les chiffrages : ce montant est à prendre avec prudence."
    : v.statut === "mitigée" ? "Testée sur le passé, elle a donné des résultats partagés."
    : "Elle n'a pas encore pu être vérifiée sur des mesures passées (pas de précédent comparable).";
  return [h("h3", {}, "Cette règle est-elle fiable ?"), h("p", {}, badge("Règle " + v.statut, k), " ", phrase), h("p", {class: "small muted"}, v.note)];
}

function pourquoi(fichier, id) {
  const m = D.moteur.find(r => r.fichier === fichier && r.id === id);
  const l = (fichier === "paniers" ? D.paniers : D.application).find(r => r.id === id);
  if (!m || !l) return;
  const dep = num(m.montant), f = num(m.facteur_moteur), fr = num(m.facteur_reference || 1), fi = num(m.facteur_interaction || 1), c = num(m.corrige_central);
  const R = D.regles_def.find(r => r.regle === m.regle) || {};
  const src = fichier === "paniers" ? l.source : l.source_independant;
  const etapes = [
    ["Chiffrage de départ", sg(dep)],
    f !== 1 ? ["Règle « " + m.regle + " »", "× " + n2(f)] : null,
    fr !== 1 ? ["Part pas encore votée", "× " + n2(fr)] : null,
    fi !== 1 ? ["Recoupements", "× " + n2(fi)] : null,
    ["Après correction", sg(c)],
  ].filter(Boolean);
  const CF = {high: ["source lue directement", "ok"], medium: ["source secondaire", "warn"], low: ["estimation fragile", "bad"]};
  ouvrir(l.ligne,
    h("p", {class: "small muted"}, `${m.groupe} · montants en milliards d'euros par an, effet sur le solde public (négatif = coût)`),
    h("ol", {class: "pq-etapes", "aria-label": "Calcul"}, etapes.map(([t, v], i) => h("li", {class: i === etapes.length - 1 ? "fin" : null}, h("span", {}, t), h("strong", {class: "num"}, v)))),
    h("h3", {}, "1. Le point de départ"),
    h("p", {}, `Chiffrage retenu au départ : ${impact(dep)}.`),
    h("p", {class: "small"}, "Source : " + src + ". ", lien(l.url, "Consulter la source"), " ", l.confiance ? badge(...(CF[l.confiance] || [l.confiance])) : null),
    h("h3", {}, "2. La correction"),
    m.regle === "Aucune" ? h("p", {}, "Aucune correction : " + (R.base || "").replace(/^./, x => x.toLowerCase()) + ".")
      : h("p", {}, `On applique la règle « ${m.regle} », qui multiplie le montant par ${n2(f)}. `, h("span", {class: "muted"}, "Ce sur quoi elle repose : " + (R.base || "") + ".")),
    l.justification && l.justification !== R.base ? h("p", {}, "Pour cette mesure : " + l.justification + ".") : null,
    m.mode === "forfait" ? h("p", {class: "small muted"}, `Facteur forfaitaire : la formule détaillée attend encore des paramètres (${m.parametres_manquants.split(/\s+/).join(", ")}).`) : null,
    fr !== 1 ? h("p", {}, `Une partie de la mesure est déjà prévue par la loi ou les budgets 2027 : seuls ${pc(fr * 100)} sont comptés, pour ne pas les compter deux fois.`, l.note_reference ? h("span", {class: "small muted"}, " " + l.note_reference) : null) : null,
    fi !== 1 ? h("p", {}, `Cette mesure recoupe d'autres mesures du même programme (même impôt ou même assiette) : son montant est multiplié par ${n2(fi)}.`) : null,
    h("h3", {}, "3. Le résultat"),
    h("p", {}, `Après correction : ${impact(c)}. Compte tenu des incertitudes, le résultat se situe entre ${sg(num(m.p10))} et ${sg(num(m.p90))} milliards dans 8 cas sur 10.`),
    statutRegle(m.regle),
    R.references ? h("details", {class: "data-toggle"}, h("summary", {}, "Les études et mesures passées sur lesquelles repose la règle"), h("ul", {class: "small"}, sourcesRegle(R.references))) : null,
    h("details", {class: "data-toggle"}, h("summary", {}, "Le détail du calcul (spécialistes)"),
      h("p", {class: "small num"}, `${n1(dep)} × ${n2(f)} × ${n2(fr)} × ${n2(fi)} = ${n1(c)}`),
      h("dl", {class: "pq-dl small"},
        [["Mode", m.mode === "moteur" ? "formule du moteur" : "facteur forfaitaire"], ["Facteur forfaitaire de la ligne", n2(num(m.facteur_forfait))],
         ["Facteur du moteur", n2(f) + (num(m.ecart_facteur_pct) ? ` (écart ${sg(num(m.ecart_facteur_pct))} %)` : "")],
         ["Loi votée seule", sg(num(m.corrige_loi_votee))], ["En 2028", sg(num(m.corrige_2028))],
         ["Statut de référence", l.statut_reference || "—"], ["Fiabilité de la référence", l.confiance_reference || "—"],
         ["Autres chiffrages", l.autres_estimations || "—"], ["Qui paie", l.qui_paie || "—"], ["Incertitude", l.incertitude || "—"]]
          .filter(([, v]) => v && v !== "—").map(([k, v]) => [h("dt", {}, k), h("dd", {}, v)])),
      paramsRegle(m.regle)));
}

/** Paramètres de la formule d'une règle (moteur_regles → moteur_parametres), avec leur provenance. */
function paramsRegle(regle) {
  const mr = D.moteur_regles.find(r => r.regle === regle);
  if (!mr || !mr.parametres) return null;
  const ids = mr.parametres.split(";").map(x => x.split("=").pop().trim()).filter(x => x && x !== "un" && x !== "zero");
  const P = ids.map(id => D.moteur_parametres.find(r => r.id === id)).filter(Boolean);
  if (!P.length) return null;
  return [h("p", {class: "small", style: "margin:.75rem 0 .25rem"}, h("strong", {}, `Formule « ${mr.formule} », paramètres :`)),
    h("ul", {class: "small"}, P.map(q => h("li", {}, `${q.id} = ${q.val_central}` + (q.val_bas ? ` (de ${q.val_bas} à ${q.val_haut})` : "") + (q.unite ? ` ${q.unite}` : "") + (q.note ? ` — ${q.note}` : ""))))];
}

/** Total d'un programme ou d'un scénario : somme des lignes, en commençant par les corrections qui pèsent le plus. */
function pourquoiTotal(fichier, groupe) {
  const L = D.moteur.filter(r => r.fichier === fichier && r.groupe === groupe);
  const lignes = (fichier === "paniers" ? D.paniers : D.application);
  const nom = id => lignes.find(r => r.id === id)?.ligne || id;
  const dep = sum(L, r => num(r.montant)), c = sum(L, r => num(r.corrige_central));
  const parCorr = [...L].sort((a, b) => Math.abs(num(b.corrige_central) - num(b.montant)) - Math.abs(num(a.corrige_central) - num(a.montant)));
  const corrigees = parCorr.filter(r => Math.abs(num(r.corrige_central) - num(r.montant)) >= 0.05);
  const item = r => h("li", {}, h("button", {type: "button", class: "btn-lien"}, nom(r.id)), ` : ${sg(num(r.montant))} → ${sg(num(r.corrige_central))} `,
    h("span", {class: "muted"}, `(${sg(num(r.corrige_central) - num(r.montant))})`));
  const listeMesures = rs => { const ul = h("ul", {class: "pq-liste"}, rs.map(item)); $$("button", ul).forEach((b, i) => b.onclick = () => pourquoi(fichier, rs[i].id)); return ul; };
  ouvrir(groupe,
    h("p", {class: "small muted"}, "Montants en milliards d'euros par an, effet sur le solde public (négatif = coût)"),
    h("ol", {class: "pq-etapes"}, h("li", {}, h("span", {}, "Somme des chiffrages de départ"), h("strong", {class: "num"}, sg(dep))),
      h("li", {}, h("span", {}, `Corrections (${corrigees.length} mesure${corrigees.length > 1 ? "s" : ""})`), h("strong", {class: "num"}, sg(c - dep))),
      h("li", {class: "fin"}, h("span", {}, "Après correction"), h("strong", {class: "num"}, sg(c)))),
    h("p", {}, `Ce total additionne ${L.length} mesures. Chacune part d'un chiffrage indépendant, puis reçoit, si besoin, une correction tirée des erreurs passées. Les corrections qui changent le plus le résultat :`),
    corrigees.length ? listeMesures(corrigees.slice(0, 8)) : h("p", {class: "muted"}, "Aucune mesure n'est corrigée."),
    h("details", {class: "data-toggle"}, h("summary", {}, `Toutes les mesures (${L.length})`), listeMesures(parCorr)),
    h("p", {class: "small muted"}, "Cliquez sur une mesure pour voir le détail de son calcul."));
}

/* ------------------------------------------------------------------ vues et navigation */
const DESSINS = {
  hier: [drawWaffle, drawEcarts, drawPS, drawPairs],
  programmes: [drawApp, drawDef, drawSens],
  equilibre: [drawInc],
  demain: [drawProj],
};
let vueCourante = null, pret = false, premier = true;

/* ------------------------------------------------------------------ état dans l'adresse (liens partageables)
   Les choix faits dans une vue (boutons, cases, listes, recherche) s'écrivent dans l'adresse après « ? » :
   #/foyer?statut=retraite&composition=couple_2. Seuls les choix différents de ceux par défaut y figurent.
   Ouvrir un tel lien rétablit les choix, en déclenchant les mêmes événements qu'un clic. */
const DEFAUTS = {};
const partie = () => {
  const [chemin, qs = ""] = location.hash.replace(/^#\/?/, "").split("?");
  const [v, sub] = chemin.split("/");
  return {v: v || "accueil", sub, params: new URLSearchParams(qs)};
};
const controles = sec => $$("input, select", sec).filter(el => !el.closest("dialog") && (el.name || el.id));
const cle = el => el.type === "radio" || (el.type === "checkbox" && el.name) ? el.name : el.id.replace(/^(f|sim)-/, "");
function lireEtat(sec) {
  const etat = new Map();
  controles(sec).forEach(el => {
    const k = cle(el);
    if (el.type === "radio") { if (el.checked) etat.set(k, el.value); else if (!etat.has(k)) etat.set(k, ""); }
    else if (el.type === "checkbox" && el.name) etat.set(k, [etat.get(k), el.checked ? el.value : null].filter(Boolean).join("|"));
    else if (el.type === "checkbox") etat.set(k, el.checked ? "1" : "0");
    else etat.set(k, el.value);
  });
  return etat;
}
function lienEtat(v) {
  const sec = $("#v-" + v), def = DEFAUTS[v] || new Map(), qs = new URLSearchParams();
  if (sec) lireEtat(sec).forEach((val, k) => { if (def.has(k) && def.get(k) !== val) qs.set(k, val); });
  return "#/" + v + (qs.size ? "?" + qs : "");
}
function appliquerEtat(sec, params) {
  // Dans l'ordre de l'adresse : un choix peut reconstruire les suivants (élection → programmes, statut → revenus)
  params.forEach((val, k) => {
    const els = controles(sec).filter(el => cle(el) === k);
    if (!els.length) return;
    const el = els[0], evt = el.type === "search" ? "input" : "change";
    if (el.type === "radio") {
      const r = els.find(x => x.value === val);
      if (r && !r.checked) { r.checked = true; r.dispatchEvent(new Event("change", {bubbles: true})); }
    } else if (el.type === "checkbox" && el.name) {
      const vus = new Set(val.split("|"));
      if (!els.some(x => vus.has(x.value))) return;  // valeur inconnue (programme retiré) : on garde le choix par défaut
      els.forEach(x => { if (x.checked !== vus.has(x.value)) { x.checked = vus.has(x.value); x.dispatchEvent(new Event("change", {bubbles: true})); } });
    } else if (el.type === "checkbox") {
      if (el.checked !== (val === "1")) { el.checked = val === "1"; el.dispatchEvent(new Event("change", {bubbles: true})); }
    } else if (el.value !== val && (el.tagName !== "SELECT" || [...el.options].some(o => o.value === val))) {
      el.value = val; el.dispatchEvent(new Event(evt, {bubbles: true}));
    }
  });
}
function ecrireEtat() {
  const {v, sub} = partie();
  if (!pret || sub) return;  // une adresse vers une sous-partie (#/hier/ecarts) reste telle quelle
  const cible = lienEtat(v);
  if (location.hash !== cible) history.replaceState(null, "", cible);
}

function route() {
  const {v: v0, sub, params} = partie();
  const v = v0;
  const sec = $("#v-" + v) || $("#v-introuvable");
  $$(".view").forEach(s => { s.hidden = s !== sec || !pret; });
  $$("#menu a").forEach(a => a.getAttribute("href") === "#/" + v ? a.setAttribute("aria-current", "page") : a.removeAttribute("aria-current"));
  document.title = (v === "accueil" ? "" : sec.dataset.titre + " – ") + "Chiffrages à l'épreuve";
  $("#nav").classList.remove("open"); $("#btn-menu").setAttribute("aria-expanded", "false");
  vueCourante = v;
  if (!pret) return;
  const vue = $("#v-" + v);
  if (vue && params.size) appliquerEtat(vue, params);
  ecrireEtat();
  dessiner();
  if (sub) {
    const t = $("#g-" + sub);
    if (t) { t.scrollIntoView(); t.setAttribute("tabindex", "-1"); t.focus({preventScroll: true}); }
  } else if (!premier) {
    window.scrollTo(0, 0);
    const h1 = $("h1", sec); h1.setAttribute("tabindex", "-1"); h1.focus({preventScroll: true});
  }
  premier = false;
}
function dessiner() {
  (DESSINS[vueCourante] || []).forEach(f => { try { f(); } catch (e) { console.error(f.name, e); } });
}

/* ------------------------------------------------------------------ affichage */
function initAffichage() {
  const root = document.documentElement, panel = $("#settings"), btn = $("#btn-settings");
  const store = (k, v) => { try { v ? localStorage.setItem(k, v) : localStorage.removeItem(k); } catch (e) {} };
  const theme = root.dataset.theme || "system", taille = root.dataset.taille || "normal";
  $(`input[name=theme][value="${theme}"]`).checked = true;
  $(`input[name=taille][value="${taille}"]`).checked = true;
  $$("input[name=theme]").forEach(i => i.onchange = () => {
    if (i.value === "system") delete root.dataset.theme; else root.dataset.theme = i.value;
    store("ce-theme", i.value === "system" ? null : i.value); if (pret) dessiner();
  });
  $$("input[name=taille]").forEach(i => i.onchange = () => {
    if (i.value === "normal") delete root.dataset.taille; else root.dataset.taille = i.value;
    store("ce-taille", i.value === "normal" ? null : i.value); if (pret) dessiner();
  });
  const toggle = open => { panel.hidden = !open; btn.setAttribute("aria-expanded", String(open)); if (open) $("input:checked", panel).focus(); else btn.focus(); };
  btn.onclick = () => toggle(panel.hidden);
  $("#btn-settings-close").onclick = () => toggle(false);
  matchMedia("(prefers-color-scheme: dark)").addEventListener("change", () => { if (pret) dessiner(); });
  const menu = $("#btn-menu");
  menu.onclick = () => { const o = !$("#nav").classList.contains("open"); $("#nav").classList.toggle("open", o); menu.setAttribute("aria-expanded", String(o)); };
}

/* ------------------------------------------------------------------ partager et imprimer */
function initPartage() {
  $$(".view").forEach(sec => {
    if (sec.id === "v-introuvable") return;
    const etat = h("p", {class: "small muted outils-etat", role: "status"});
    const copier = h("button", {type: "button", class: "btn-tool"}, "Copier le lien de cette page");
    const imprimer = h("button", {type: "button", class: "btn-tool"}, "Imprimer");
    copier.onclick = async () => {
      const url = location.origin + location.pathname + lienEtat(sec.id.slice(2));
      etat.textContent = "";
      try {
        await navigator.clipboard.writeText(url);
        etat.textContent = "Lien copié. Il rouvre cette page avec vos choix.";
      } catch (e) {
        // Presse-papiers refusé : on affiche le lien, sélectionné, pour une copie à la main
        const champ = h("input", {type: "text", readonly: "", value: url, "aria-label": "Lien de cette page", class: "outils-lien"});
        etat.append("Copiez ce lien : ", champ); champ.select();
      }
    };
    imprimer.onclick = () => print();
    const barre = h("div", {class: "outils-page"}, copier, imprimer, etat);
    const crumb = $(".crumb", sec);
    crumb ? crumb.after(barre) : sec.prepend(barre);
  });

  // Impression : accordéons ouverts, couleurs claires, mention de l'adresse et de la date
  const root = document.documentElement;
  let fermes = [], themeAvant, enImpression = false;
  addEventListener("beforeprint", () => {
    if (enImpression) return;  // certains navigateurs l'envoient deux fois
    enImpression = true;
    fermes = $$("details.acc:not([open])"); fermes.forEach(d => d.open = true);
    const sombre = root.dataset.theme === "dark" || (!root.dataset.theme && matchMedia("(prefers-color-scheme: dark)").matches);
    themeAvant = root.dataset.theme;
    if (sombre) { root.dataset.theme = "light"; if (pret) dessiner(); }
    const {v} = partie();
    $("#print-info").textContent = `Imprimé le ${new Date().toLocaleDateString("fr-FR", {day: "numeric", month: "long", year: "numeric"})} depuis ` +
      `${location.origin + location.pathname + lienEtat(v)}. Données mises à jour le ${$("[data-k=maj]")?.textContent || "—"}.`;
  });
  addEventListener("afterprint", () => {
    if (!enImpression) return;
    enImpression = false;
    fermes.forEach(d => d.open = false); fermes = [];
    if (root.dataset.theme !== themeAvant) {
      if (themeAvant) root.dataset.theme = themeAvant; else delete root.dataset.theme;
      if (pret) dessiner();
    }
  });
}

async function init() {
  initAffichage();
  initPartage();
  const dlg = $("#pq");
  $("#pq-fermer").onclick = () => dlg.close();
  dlg.addEventListener("click", e => { if (e.target === dlg) dlg.close(); });  // clic sur le fond
  dlg.addEventListener("close", () => { if (pqOrigine && document.contains(pqOrigine)) pqOrigine.focus(); });
  addEventListener("hashchange", route);
  route();
  try {
    await Promise.all(Object.entries(SOURCES).map(async ([k, f]) => { D[k] = await d3.csv(`../data/${f}.csv`); }));
  } catch (e) {
    $("#chargement").className = "error";
    $("#chargement").innerHTML = "<strong>Les données n'ont pas pu être chargées.</strong> Cette page doit être ouverte par un serveur web : depuis le dossier du projet, lancez <code>python3 -m http.server 8000</code>, puis ouvrez <a href='http://localhost:8000/web/'>http://localhost:8000/web/</a>.";
    console.error(e);
    return;
  }
  calculer();
  remplirK();
  [vueHier, vueProgrammes, vueEquilibre, vueFoyer, vueDemain, vueMethode].forEach(f => { try { f(); } catch (e) { console.error(f.name, e); } });
  $("#chargement").remove();
  // Choix par défaut de chaque vue, avant d'appliquer ceux de l'adresse
  $$(".view").forEach(sec => { DEFAUTS[sec.id.slice(2)] = lireEtat(sec); });
  // Chaque choix met l'adresse à jour (sans ajouter d'entrée à l'historique)
  $$(".view").forEach(sec => { sec.addEventListener("change", ecrireEtat); sec.addEventListener("input", ecrireEtat); });
  pret = true;
  route();
  let t;
  addEventListener("resize", () => { clearTimeout(t); t = setTimeout(dessiner, 150); });
}
document.addEventListener("DOMContentLoaded", init);
