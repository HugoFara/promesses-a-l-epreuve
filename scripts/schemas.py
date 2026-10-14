"""Schémas des CSV sources (data/raw/). Une classe par fichier ; build.py les applique à chaque ligne."""
from typing import Annotated, Literal, Optional
from pydantic import BaseModel, BeforeValidator, ConfigDict, field_validator


def _vide_none(v):
    return None if isinstance(v, str) and v.strip() == "" else v


OptFloat = Annotated[Optional[float], BeforeValidator(_vide_none)]
OptInt = Annotated[Optional[int], BeforeValidator(_vide_none)]
OptStr = Annotated[Optional[str], BeforeValidator(_vide_none)]
Confiance = Literal["high", "medium", "low"]
Url = Annotated[str, BeforeValidator(lambda v: v.strip())]


class Ligne(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    @field_validator("url", "source_ex_ante", "source_ex_post", "source", check_fields=False)
    @classmethod
    def _url(cls, v):
        if v and v.startswith("http") and " " in v and cls.__name__ != "Historique":  # historique : texte libre
            raise ValueError(f"URL avec espace : {v}")
        return v


class MesureCout(Ligne):
    id: str; mesure: str; annee: int; sens: Literal["cout", "economie"]; indicateur: str
    ex_ante: float; estimateur_ex_ante: str
    ex_post_bas: float; ex_post_central: float; ex_post_haut: float; estimateur_ex_post: str
    cause_principale: str; confiance: Confiance; source_ex_ante: Url; source_ex_post: Url; note: OptStr = None
    note_confiance: OptStr = None
    citation_ex_ante: OptStr = None; page_ex_ante: OptStr = None
    citation_ex_post: OptStr = None; page_ex_post: OptStr = None
    deflateur_ex_ante: float = 1.0; type_ex_post: Literal["observe", "administratif", "reestimation"] = "observe"
    inclus_stats: Literal[0, 1] = 1

    @field_validator("inclus_stats", mode="before")
    @classmethod
    def _int(cls, v):
        return int(v)

    @field_validator("ex_post_haut")
    @classmethod
    def _ordre(cls, v, info):
        d = info.data
        if "ex_post_bas" in d and "ex_post_central" in d and not d["ex_post_bas"] <= d["ex_post_central"] <= v:
            raise ValueError("ex_post_bas ≤ central ≤ haut non respecté")
        return v


class MesureEffet(Ligne):
    id: str; mesure: str; effet: str; annonce: str; mesure_ex_post: str; ratio_central: OptFloat = None
    verdict: str; source_ex_ante: Url; source_ex_post: Url
    citation_ex_ante: OptStr = None; page_ex_ante: OptStr = None; citation_ex_post: OptStr = None
    page_ex_post: OptStr = None; note: OptStr = None; note_confiance: OptStr = None
    confiance: Annotated[Optional[Confiance], BeforeValidator(_vide_none)] = None


class ProgrammeStabilite(Ligne):
    millesime: str; annee_t1: int; prev_t1: float; real_t1: float
    annee_t3: OptInt = None; prev_t3: OptFloat = None; real_t3: OptFloat = None
    confiance: Confiance; source: Url; note_confiance: OptStr = None


class PaireFS(Ligne):
    pays: str; erreur_1an: float; erreur_2ans: float; erreur_3ans: float


class RegleCalibration(Ligne):
    id: str; categorie: str; correction_2027: str; base_empirique: str


class Regle(Ligne):
    regle: str; facteur: OptFloat = None; variable: bool; references: OptStr = None; base: str


Methode = Literal["Quasi-expérience", "Expérimentation aléatoire", "Modèle", "Méta-analyse ou revue", "Descriptif"]


class Elasticite(Ligne):
    id: str; domaine: str; parametre: str; valeur_centrale: str; fourchette: str; pays_periode: str
    methode: Methode; usage_2027: str; source: str; url: Url; confiance: Confiance
    # Valeurs numériques (T4) : facultatives tant que la saisie n'est pas complète
    val_bas: OptFloat = None; val_central: OptFloat = None; val_haut: OptFloat = None
    unite: OptStr = None; type: OptStr = None; note_num: OptStr = None
    citation: OptStr = None; page: OptStr = None; note_confiance: OptStr = None

    @field_validator("val_haut")
    @classmethod
    def _ordre(cls, v, info):
        d = info.data
        if v is not None and d.get("val_bas") is not None and d.get("val_central") is not None:
            lo, hi = sorted((d["val_bas"], v))
            if not lo <= d["val_central"] <= hi:
                raise ValueError("val_central hors de [val_bas, val_haut]")
        return v


class Hypothese(Ligne):
    id: str; levier: str; hypothese: str; effet_chiffrage: str; references: str


Statut = Literal["votée", "proposée", "absente", "partielle"]


class LigneApplication(Ligne):
    id: str; programme: str; ligne: str
    type: Literal["Dépense", "Recette", "Économie", "Effet promis", "Charge d'intérêts"]
    annonce_parti: OptFloat = None; independant: float; source_independant: str; autres_estimations: str
    regle: str; facteur: float; justification: str; url: Url; confiance: Confiance
    statut_reference: Optional[Statut] = None; source_reference: OptStr = None
    facteur_reference: float = 1.0; note_reference: OptStr = None; confiance_reference: Annotated[Optional[Confiance], BeforeValidator(_vide_none)] = None; note_confiance: OptStr = None
    facteur_reference_bas: OptFloat = None; facteur_reference_haut: OptFloat = None; facteur_reference_2028: OptFloat = None
    facteur_interaction: OptFloat = None; facteur_interaction_bas: OptFloat = None; facteur_interaction_haut: OptFloat = None
    recours_complet_suppose: Annotated[Optional[Literal["oui", "non"]], BeforeValidator(_vide_none)] = None
    source_recours: OptStr = None


class ProgrammeApplication(Ligne):
    id: str; programme: str; solde_annonce: OptFloat = None; solde_montaigne: float
    position_parti: str; chiffrages_independants: str


class Parametre(Ligne):
    id: str; valeur: float; description: str; url: OptStr = None


class LignePanier(Ligne):
    id: str; variantes: str; role: Literal["Mesure phare", "Financement", "Investissement (règle d'or)"]
    ligne: str; statique: float; facteur: float; regle: str; incertitude: str; qui_paie: str
    source: str; url: Url; confiance: Confiance
    statut_reference: Optional[Statut] = None; source_reference: OptStr = None
    facteur_reference: float = 1.0; note_reference: OptStr = None; confiance_reference: Annotated[Optional[Confiance], BeforeValidator(_vide_none)] = None; note_confiance: OptStr = None
    facteur_reference_bas: OptFloat = None; facteur_reference_haut: OptFloat = None; facteur_reference_2028: OptFloat = None
    facteur_interaction: OptFloat = None; facteur_interaction_bas: OptFloat = None; facteur_interaction_haut: OptFloat = None
    recours_complet_suppose: Annotated[Optional[Literal["oui", "non"]], BeforeValidator(_vide_none)] = None
    source_recours: OptStr = None


class MoteurRegle(Ligne):
    regle: str
    formule: Literal["fixe", "complement", "taxe_elasticite", "semi_elasticite", "semi_elasticite_taux", "accise", "smic", "montant", "emploi_smic", "assiette_reduite_nette", "ligne"]
    parametres: OptStr = None; justification_ecart: OptStr = None


class MoteurParametre(Ligne):
    id: str; val_bas: OptFloat = None; val_central: float; val_haut: OptFloat = None; unite: str
    source_type: Literal["constante", "elasticite", "backtest", "url", "calcul", "bareme"]; source_ref: OptStr = None
    confiance: Confiance; note: OptStr = None


class ChiffrageInstitut(Ligne):
    id_ligne: str; programme: str; chiffreur: str; valeur: float
    usage: Literal["ligne", "recettes_du_parti", "composante", "hors_lignes", "partisan"]
    horizon: OptStr = None; perimetre: OptStr = None; url: Url; citation: OptStr = None; page: OptStr = None
    confiance: Confiance; note: OptStr = None


class TotalInstitut(Ligne):
    programme: str; chiffreur: str; solde_total: OptFloat = None; horizon: OptStr = None; url: Url
    citation: OptStr = None; confiance: Confiance; note: OptStr = None


class StatutReference2027(Ligne):
    fichier: Literal["application_lignes", "paniers"]; id_ligne: str; ligne: str; statut_reference: Statut
    texte: OptStr = None; montant_reference_2027: OptFloat = None; facteur_suggere: float; url: OptStr = None
    citation: OptStr = None; page: OptStr = None; confiance: Confiance; note: str


class ParametreBareme(Ligne):
    id: str; parametre: str; val_bas: OptFloat = None; val_central: OptFloat = None; val_haut: OptFloat = None
    unite: str; annee: OptStr = None; url: OptStr = None; citation: OptStr = None; page: OptStr = None
    confiance: Confiance; note: OptStr = None


class ProjectionReference(Ligne):
    annee: int; croissance_reelle: OptFloat = None; deflateur: OptFloat = None; pib: OptFloat = None
    solde_pct: float; dette_pct: OptFloat = None; sfa_pct: OptFloat = None; extrapole: Literal[0, 1]
    source: OptStr = None; note: OptStr = None

    @field_validator("extrapole", mode="before")
    @classmethod
    def _bool(cls, v):
        return int(v)


class RendementLevier(Ligne):
    id: str; levier: str; rendement_md: float; unite: str; annee: OptStr = None; url: Url
    citation: OptStr = None; page: OptStr = None; confiance: Confiance; note: OptStr = None


class PosteIfrap(Ligne):
    type: str; mesure: str; montant_md: float; asterisque: OptStr = None; url: Url; page: OptStr = None
    confiance: Confiance; note: OptStr = None


class CalibrationInstitut(Ligne):
    campagne: str; mesure: str; chiffreur: str; chiffrage_campagne: OptFloat = None; horizon: OptStr = None
    cout_realise: OptFloat = None; source_realise: OptStr = None; ecart_pct: OptFloat = None
    url_chiffrage: OptStr = None; citation_chiffrage: OptStr = None; url_realise: OptStr = None
    citation_realise: OptStr = None; confiance: Confiance; note: OptStr = None; page_chiffrage: OptStr = None
    page_realise: OptStr = None; inclus_stats: str; date_acces: OptStr = None


class ReformeDistributive(Ligne):
    id: str; libelle: str; type: Literal["parametre", "option_bareme_capital", "smic_net_cible", "gel_pensions"]
    cible: OptStr = None; valeur: OptStr = None; ligne_liee: str; url: Url; confiance: Confiance; note: OptStr = None


class VarianteSensibilite(Ligne):
    variante: str; libelle: str; fichier: Literal["application_lignes", "paniers"]; id: str; colonne: str
    valeur: float; source: str; note: OptStr = None


class AttributionValidation(Ligne):
    fichier: Literal["mesures_officielles", "effets_annonces", "chiffrages_campagne"]; id: str; regle: str
    justification: str; issue_connue: Literal["oui", "non"]


class Historique(Ligne):
    date: str; fichier: str; id: str; colonne: str; ancienne: OptStr = None; nouvelle: OptStr = None
    raison: str; source: OptStr = None


SCHEMAS = {
    "mesures_cout": MesureCout,
    "mesures_effets": MesureEffet,
    "programmes_stabilite_fr": ProgrammeStabilite,
    "pairs_frankel_schreger": PaireFS,
    "regles_calibration": RegleCalibration,
    "regles": Regle,
    "elasticites": Elasticite,
    "hypotheses_defaut": Hypothese,
    "application_lignes": LigneApplication,
    "application_programmes": ProgrammeApplication,
    "application_parametres": Parametre,
    "paniers": LignePanier,
    "moteur_regles": MoteurRegle,
    "moteur_parametres": MoteurParametre,
    "chiffrages_instituts": ChiffrageInstitut,
    "totaux_instituts": TotalInstitut,
    "statut_reference_2027": StatutReference2027,
    "parametres_bareme": ParametreBareme,
    "projection_reference": ProjectionReference,
    "projection_parametres": Parametre,
    "rendements_leviers": RendementLevier,
    "ifrap_nfp_2024": PosteIfrap,
    "calibration_instituts": CalibrationInstitut,
    "distributif_reformes": ReformeDistributive,
    "variantes_sensibilite": VarianteSensibilite,
    "validation_attribution": AttributionValidation,
    "historique": Historique,
}
