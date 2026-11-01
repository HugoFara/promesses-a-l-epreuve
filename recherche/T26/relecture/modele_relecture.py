#!/usr/bin/env python3
"""Relecture indépendante du facteur de référence de la ligne l_bandeaux (T26).

Calcul statique : part du rendement de la ligne Bozio-Wasmer « suppression des
bandeaux, extinction à 1,88 SMIC » qui reste à gagner en 2027 quand la référence
contient la RGDU (votée), le gel du SMIC de référence (2026 voté, 2027 proposé)
et l'intégration de l'intéressement/participation à l'assiette (proposée).

Toutes les entrées sont citées dans notes.md (§ 1) ; aucune n'est complétée de mémoire.
Usage : python3 modele_relecture.py  (aucune dépendance hors numpy)
"""
import itertools
import numpy as np

# ---------------------------------------------------------------- distribution
# Insee Première n° 2079 (oct. 2025), fig. 3 : salaires mensuels nets EQTP 2024,
# secteur privé, ensemble (euros). C99 = 10 261 € = « 7,3 fois le Smic ».
Q_P = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
Q_NET = [1492, 1669, 1823, 1992, 2190, 2442, 2785, 3305, 4334, 5593, 10261]
SMIC_NET = 10261 / 7.3          # Smic net mensuel implicite 2024 (même source)
# Rapport brut/net par catégorie (même source, fig. 1) : employés 2500/1941,
# cadres 6224/4629 ; salaires nets moyens 1941 et 4629.
R_EMP, W_EMP = 2500 / 1941, 1941 / SMIC_NET
R_CAD, W_CAD = 6224 / 4629, 4629 / SMIC_NET


def quantile_grid(n=50_000, interp="loglin", brut="progressif", lam=1.0):
    """Salaire brut EQTP en multiples du Smic brut, pour p uniforme sur ]0,1[."""
    p = (np.arange(n) + 0.5) / n
    qp = np.array([0.0] + Q_P + [1.0])
    qw = np.array(Q_NET) / SMIC_NET
    # bornes : bas de distribution 0,5 Smic (apprentis), queue Pareto au-delà de C99
    lw = np.log(np.concatenate([[0.5], qw, [qw[-1]]]))
    if interp == "loglin":
        lwp = np.interp(p, qp[:-1], lw[:-1])
    else:  # interpolation monotone (PCHIP maison) sur log w
        from_ = qp[:-1]; y = lw[:-1]
        h = np.diff(from_); d = np.diff(y) / h
        m = np.zeros_like(y)
        for i in range(1, len(y) - 1):
            if d[i - 1] * d[i] > 0:
                w1, w2 = 2 * h[i] + h[i - 1], h[i] + 2 * h[i - 1]
                m[i] = (w1 + w2) / (w1 / d[i - 1] + w2 / d[i])
        m[0], m[-1] = d[0], d[-1]
        idx = np.clip(np.searchsorted(from_, p) - 1, 0, len(h) - 1)
        t = (p - from_[idx]) / h[idx]
        h00 = 2 * t**3 - 3 * t**2 + 1; h10 = t**3 - 2 * t**2 + t
        h01 = -2 * t**3 + 3 * t**2; h11 = t**3 - t**2
        lwp = h00 * y[idx] + h10 * h[idx] * m[idx] + h01 * y[idx + 1] + h11 * h[idx] * m[idx + 1]
    w_net = np.exp(lwp)
    top = p > 0.99                      # Pareto alpha 2 au-delà de C99
    w_net[top] = qw[-1] * ((1 - 0.99) / (1 - p[top])) ** 0.5
    if brut != "constant":
        slope = (R_CAD - R_EMP) / (W_CAD - W_EMP)
        r = lambda x: R_EMP + slope * (np.clip(x, 1.0, W_CAD) - W_EMP)
        w_net = w_net * r(w_net) / r(1.0)
    # lam < 1 resserre la distribution autour du Smic (log w × lam) : calage sur
    # la DSN 2025 (annexe 9 : 49 % de la masse salariale entre 1 et 2 Smic) et sur
    # les coûts 2024 des bandeaux (B-W tableau 1.1) ; voir notes.md § 1.3.
    return np.exp(np.log(w_net) * lam)


# ---------------------------------------------------------------- barèmes
# 2024 (Bozio-Wasmer 2024, p. 45-46 et 203) : RG jusqu'à 1,6 Smic ; taux au Smic
# 40,15 % toutes réductions (> 50 sal.), dont 6 + 1,8 points de bandeaux, d'où
# T_RG = 32,35 % (> 50) et 31,95 % (< 50, « retrancher 0,4 point »).
# Seuils 2024 gelés : 2,47 Smic (maladie) et 3,46 Smic (famille).
def e2024(w, T, s_mal=2.47, s_fam=3.46):
    rg = np.where(w < 1.6, T / 0.6 * (1.6 / np.maximum(w, 1.0) - 1), 0.0)
    return rg + 0.06 * (w <= s_mal) + 0.018 * (w <= s_fam)


def etarget(w, T, smic_ratio=1.0):
    """Scénario B-W : courbe RG + 7,8 points prolongée jusqu'à extinction (~1,88)."""
    x = w / smic_ratio                  # salaire en multiples du Smic de référence
    tot = T / 0.6 * (1.6 / np.maximum(x, 1.0) - 1) + 0.078
    return np.maximum(tot, 0.0)


# RGDU 2026 (annexe 9 PLFSS 2027, art. 7 : formule et cas-type ; FNTP 2026 :
# Tmin 0,02, Tdelta 0,3781 / 0,3821, P 1,75) : C = Tmin + Tdelta·[½(3·S/R − 1)]^P
def ergdu(w_assiette, Td, smic_ratio=1.0):
    x = w_assiette / smic_ratio
    base = np.clip(0.5 * (3 / np.maximum(x, 1.0) - 1), 0, None)
    return np.where(x < 3, 0.02 + Td * base**1.75, 0.0)


def check_cas_type():
    """Cas-type annexe 9 p. 38 : 22 184 € (1 Smic 2026) -> réduction 8 528,54 €."""
    smic_gele = 1823.03 * 12            # Smic de référence gelé (1/1/2026)
    rem = 22184.0
    c = 0.02 + 0.3781 * (0.5 * (3 * smic_gele / rem - 1)) ** 1.75
    return c * rem                      # attendu 8 528,54 (FNAL 0,1 %)


# ---------------------------------------------------------------- calcul
def integ(rate, w):
    return float(np.mean(rate * w))     # masse d'exonération par unité (Smic×EQTP)


def run(interp="loglin", brut="progressif", s27=0.973, ip_cal=3.3 / 74.735,
        ip_profile=(0.7, 1.3), couverture=1.0, s_mal=2.47, lam=0.9):
    w = quantile_grid(interp=interp, brut=brut, lam=lam)
    T = 0.5 * (0.3235 + 0.3195)
    Td = 0.5 * (0.3781 + 0.3821)
    e24 = e2024(w, T, s_mal)
    et0 = etarget(w, T)
    L = integ(e24 - et0, w)                         # rendement de la ligne (2024)
    rg = np.where(w < 1.6, T / 0.6 * (1.6 / np.maximum(w, 1.0) - 1), 0.0)
    out = {"rg_sur_maladie": integ(rg, w) / integ(0.06 * (w <= s_mal) * (w >= 1.0), w),
           "L_sur_maladie": L / integ(0.06 * (w <= s_mal) * (w >= 1.0), w),
           "fam_sur_mal": integ(0.018 * (w <= 3.46) * (w >= 1), w)
           / integ(0.06 * (w <= s_mal) * (w >= 1), w),
           "part_masse_1_2": float(np.mean(w * ((w >= 1) & (w < 2))) / np.mean(w)),
           "part_etp_sup_3_5": float(np.mean(w > 3.5))}
    # profil de l'intéressement/participation (part du salaire) : intensité relative
    # ip_profile[0] entre 1 et 2 Smic (annexe 9 : 49 % de la masse, ~34 % des sommes
    # => 0,7), ip_profile[1] au-delà de 2 Smic ; niveau calé sur le coût officiel.
    g = np.where(w < 2, ip_profile[0], ip_profile[1])
    cost_rgdu = integ(ergdu(w, Td, s27), w)
    def cost_with(phi0):
        phi = phi0 * g / couverture
        c_cov = integ(ergdu(w * (1 + phi), Td, s27), w)
        return couverture * c_cov + (1 - couverture) * cost_rgdu
    lo, hi = 0.0, 0.5                               # calage : baisse = ip_cal × coût RGDU
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if (cost_rgdu - cost_with(mid)) / cost_rgdu < ip_cal:
            lo = mid
        else:
            hi = mid
    phi0 = lo
    out["phi_moyen_1_3"] = float(np.mean((phi0 * g * w)[(w >= 1) & (w < 3)])
                                 / np.mean(w[(w >= 1) & (w < 3)]))
    out["gel_sur_rgdu"] = 1 - cost_rgdu / integ(ergdu(w, Td, 1.0), w)
    out["rgdu_sur_rg_bandeaux_2024"] = integ(ergdu(w, Td), w) / integ(e24 * (w >= 0), w)

    def remaining(gel, assiette, cible_regles, zone="cap"):
        s = s27 if gel else 1.0
        tot = 0.0
        groups = [(couverture, phi0 * g / couverture), (1 - couverture, 0 * g)] if assiette \
            else [(1.0, 0 * g)]
        for wt, phi in groups:
            if wt == 0:
                continue
            wa = w * (1 + phi)
            eref = ergdu(wa, Td, s)
            et = etarget(wa, T, s) if cible_regles else et0
            zone_mask = (w / (s if cible_regles else 1.0)) >= 1.6
            if zone == "cap":
                tot += wt * integ(np.maximum(eref - et, 0) * zone_mask, w)
            elif zone == "remplacement":
                tot += wt * integ(eref - et, w)
            elif zone == "recouvrement":      # part non obtenue, plafonnée par salaire
                gain_ligne = np.maximum(e24 - et0, 0)
                deja = np.clip(e24 - eref, 0, gain_ligne)
                tot += wt * integ(gain_ligne - deja, w)
        return tot / L

    for name, gel, ass in [("rgdu_seule", False, False), ("rgdu_gel", True, False),
                           ("reference_2027", True, True)]:
        for regles in (False, True):
            for zone in ("cap", "remplacement", "recouvrement"):
                out[f"F_{name}_{'cibleRef' if regles else 'cibleSmic'}_{zone}"] = \
                    remaining(gel, ass, regles, zone)
    return out


if __name__ == "__main__":
    print(f"Cas-type annexe 9 : réduction {check_cas_type():.2f} € (attendu 8 528,54)")
    base = run()
    print("\n== Variante centrale (loglin, brut progressif, lam 0,9, s27=0,973, I/P 3,3 Md€)")
    for k, v in base.items():
        print(f"  {k:45s} {v:7.3f}")
    print("\n== Sensibilités (432 combinaisons de paramètres ; définitions détaillées dans notes.md § 1.4)")
    keys = ["F_rgdu_seule_cibleSmic_cap", "F_rgdu_gel_cibleRef_cap", "F_rgdu_gel_cibleSmic_cap",
            "F_reference_2027_cibleRef_cap", "F_reference_2027_cibleSmic_cap",
            "F_reference_2027_cibleRef_remplacement", "F_reference_2027_cibleRef_recouvrement",
            "F_rgdu_seule_cibleRef_recouvrement", "F_rgdu_gel_cibleRef_recouvrement"]
    res = []
    for interp, brut, s27, ipc, prof, cov, lam in itertools.product(
            ["loglin", "pchip"], ["progressif", "constant"], [0.967, 0.973, 0.976],
            [3.3 / 74.735, 3.7 / 74.735], [(0.7, 1.0), (0.7, 1.3), (0.7, 1.8)],
            [1.0, 0.54], [0.8, 0.9, 1.0]):
        r = run(interp, brut, s27, ipc, prof, cov, 2.47, lam)
        res.append(r)
    print("  (", len(res), "combinaisons )")
    print("\n== Effet de la seule dispersion (lam), autres paramètres centraux")
    for lam in (0.75, 0.8, 0.85, 0.9, 0.95, 1.0):
        r = run(lam=lam)
        print(f"  lam {lam:4.2f}  L/mal {r['L_sur_maladie']:.3f}  fam/mal {r['fam_sur_mal']:.3f}"
              f"  masse 1-2 {r['part_masse_1_2']:.3f}  F_ref_cap {r['F_reference_2027_cibleRef_cap']:.3f}"
              f"  F_ref_cibleSmic {r['F_reference_2027_cibleSmic_cap']:.3f}"
              f"  F_ref_recouv {r['F_reference_2027_cibleRef_recouvrement']:.3f}"
              f"  F_rgdu {r['F_rgdu_seule_cibleSmic_cap']:.3f}")
    for k in keys + ["rg_sur_maladie", "L_sur_maladie", "fam_sur_mal", "part_masse_1_2", "part_etp_sup_3_5",
                     "gel_sur_rgdu"]:
        v = np.array([r[k] for r in res])
        print(f"  {k:45s} min {v.min():.3f}  med {np.median(v):.3f}  max {v.max():.3f}")


# ---------------------------------------------------------------- comparaison avec l'agent A
def comparaison_A(lam=0.9, s=12.02 / 12.31):
    """Isole les écarts : (1) transposition de la cible, (2) distribution, (3) assiette.

    Transpositions de l'agent A (notes_A.md § 1.3) : A = de C_RGDU(1,6) à 0 linéaire en
    1,88 ; B = RGDU inchangée jusqu'à 1,88 puis 0. Distribution de A : effectifs par bande
    (1,6-2 : 14 % ; 2-2,5 : 8,3 % ; 2,5-3 : 5,5 % ; 3-3,5 : 3,5 %), uniforme dans la bande.
    """
    T = 0.5 * (0.3235 + 0.3195)
    Td = 0.5 * (0.3781 + 0.3821)
    def dist_mienne():
        return quantile_grid(lam=lam), None
    def dist_A():
        bands = [(1.6, 2.0, 0.14), (2.0, 2.5, 0.083), (2.5, 3.0, 0.055), (3.0, 3.5, 0.035)]
        ws, wt = [], []
        for a, b, p in bands:
            x = np.linspace(a, b, 4001)[:-1] + (b - a) / 8000
            ws.append(x); wt.append(np.full_like(x, p / len(x)))
        return np.concatenate(ws), np.concatenate(wt)
    def I(rate, w, wt):
        return float(np.sum(rate * w * wt)) if wt is not None else integ(rate, w)
    rows = []
    for dname, dfun in (("mienne (Insee, lam)", dist_mienne), ("agent A (bandes)", dist_A)):
        w, wt = dfun()
        # barèmes de A : bandeaux 2,5 / 3,5 ; les miens : 2,47 / 3,46 -> on garde les miens
        e24 = e2024(w, T) * (w >= 1.6)
        et0 = etarget(w, T) * (w >= 1.6)
        L = I(e24 - et0, w, wt)
        z = w >= 1.6
        for sv, lab in ((1.0, "RGDU seule"), (s, "RGDU + gel")):
            er = ergdu(w, Td, sv)
            c16 = ergdu(np.array([1.6]), Td, sv)[0]
            scA = np.where(w < 1.88, c16 * (1.88 - w) / 0.28, 0.0)
            scB = np.where(w < 1.88, er, 0.0)
            rec = np.maximum(e24 - et0, 0) - np.clip(e24 - er, 0, np.maximum(e24 - et0, 0))
            rows.append((dname, lab,
                         I((er - scA) * z, w, wt) / L, I((er - scB) * z, w, wt) / L,
                         I(np.maximum(er - et0, 0) * z, w, wt) / L, I(rec * z, w, wt) / L))
    return rows


def part_assiette_au_dessus(lam=0.9, s27=0.973, ip_profile=(0.7, 1.3)):
    """Part du coût de l'art. 7 (I/P) qui porte sur les salaires >= 1,6 Smic (modèle)."""
    w = quantile_grid(lam=lam)
    Td = 0.5 * (0.3781 + 0.3821)
    g = np.where(w < 2, ip_profile[0], ip_profile[1])
    base = ergdu(w, Td, s27)
    lo, hi = 0.0, 0.5
    c0 = integ(base, w)
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if (c0 - integ(ergdu(w * (1 + mid * g), Td, s27), w)) / c0 < 3.3 / 74.735:
            lo = mid
        else:
            hi = mid
    d = (base - ergdu(w * (1 + lo * g), Td, s27)) * w
    return float(d[w >= 1.6].sum() / d.sum())


if __name__ == "__main__":
    print("\n== Comparaison avec l'agent A (sans assiette) : A, B = transpositions de A ;"
          " cap = cible B-W absolue ; recouv = part non obtenue")
    for r in comparaison_A():
        print(f"  {r[0]:22s} {r[1]:11s}  A {r[2]:.3f}  B {r[3]:.3f}  cap {r[4]:.3f}  recouv {r[5]:.3f}")
    for lam in (0.8, 0.9, 1.0):
        for prof in ((0.7, 1.0), (0.7, 1.3), (0.7, 1.8)):
            print(f"  part de l'art. 7 (I/P) au-dessus de 1,6 Smic, lam {lam}, profil {prof} :"
                  f" {part_assiette_au_dessus(lam, ip_profile=prof):.2f}")
    w = quantile_grid(lam=0.9)
    for a, b in ((1.6, 2.0), (2.0, 2.5), (2.5, 3.0), (3.0, 3.5)):
        print(f"  part des EQTP entre {a} et {b} Smic (ma distribution, lam 0,9) :"
              f" {np.mean((w >= a) & (w < b)):.3f}")
