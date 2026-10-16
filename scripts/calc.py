import pandas as pd, numpy as np, json
c=pd.read_csv('mesures_cout.csv')
# écart sur le solde public (Md€/an): + = mieux que prévu pour les finances publiques
# ex ante ramené à la base de prix de l'ex post (deflateur_ex_ante, 1 par défaut)
c['ex_ante_comparable']=c.ex_ante*c.deflateur_ex_ante
a=c.ex_ante_comparable
c['ratio']=c.ex_post_central/a
c['ecart_solde']=np.where(c.sens=='cout', a-c.ex_post_central, c.ex_post_central-a)
c['ecart_pct']=np.where(c.sens=='cout',(a-c.ex_post_central)/a,(c.ex_post_central-a)/a)*100
print(c[['id','ex_ante_comparable','ex_post_central','ratio','ecart_pct','cause_principale','type_ex_post','inclus_stats']].round(2).to_string())
# Statistique principale : mesures incluses (hors dispositifs énergie exclus) ; variantes pour la sensibilité.
# Les mesures de T18 (selection = test_regles) ont été choisies parce qu'une règle de comportement s'y applique : elles
# ne représentent pas l'ensemble des chiffrages officiels et restent hors de la statistique principale.
gen=c.selection=='generale'
echantillons={'principal (inclus_stats = 1)': (c.inclus_stats==1)&gen, 'toutes (hors test des règles)': gen,
              'ex post observés seulement': (c.inclus_stats==1)&gen&(c.type_ex_post=='observe'),
              'y compris mesures choisies pour tester les règles': c.inclus_stats==1}
stats=[]
for nom,m in echantillons.items():
    e=c.ecart_pct[m].abs()
    stats.append({'echantillon':nom,'n':int(m.sum()),'erreur_abs_mediane_pct':round(e.median(),1),
                  'a_15pct':int((e<=15).sum()),'erreur_abs_moyenne_pct':round(e.mean(),1)})
    print(f"{nom:<32} n={int(m.sum()):>2}  erreur absolue médiane {e.median():5.1f} %  à ±15 % : {(e<=15).sum()}/{int(m.sum())}")
pd.DataFrame(stats).to_csv('couche1_stats.csv',index=False)
c_all=c
c=c[(c.inclus_stats==1)&(c.selection=='generale')]
p=pd.read_csv('programmes_stabilite_fr.csv')
p['e1']=p.real_t1-p.prev_t1; p['e3']=p.real_t3-p.prev_t3
print(p[['millesime','e1','e3']].round(2).to_string())
crisis1={2009,2020}; crisis3={2009,2010,2020,2021}
print('t1 mean all',p.e1.mean().round(2),len(p.e1))
m=~p.annee_t1.isin(crisis1); print('t1 hors crise',p.e1[m].mean().round(2),m.sum(),'median',p.e1[m].median())
q=p.dropna(subset=['e3']); print('t3 all',q.e3.mean().round(2),len(q))
m3=~q.annee_t3.isin(crisis3); print('t3 hors crise',q.e3[m3].mean().round(2),m3.sum(),'median',q.e3[m3].median(), 'share pessimistic', (q.e3[m3]<0).mean())
print('t1 share optimistic hors crise',(p.e1[m]<0).mean())
c_all.to_csv('mesures_cout_calc.csv',index=False); p.to_csv('ps_calc.csv',index=False)
# Erreurs par cause d'écart (couche 1) : biais signé (+ = mieux que prévu pour le solde) et erreur absolue
par_cause = c.groupby('cause_principale').agg(n=('id', 'size'), biais_median_pct=('ecart_pct', 'median'),
                                               erreur_abs_mediane_pct=('ecart_pct', lambda s: s.abs().median()),
                                               mesures=('id', lambda s: ' '.join(s))).round(1).sort_values('n', ascending=False)
par_cause.to_csv('couche1_par_cause.csv')
print(par_cause.drop(columns='mesures').to_string())
