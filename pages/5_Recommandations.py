import streamlit as st
import pandas as pd
import sys
sys.path.append('.')

st.set_page_config(page_title="Recommandations", page_icon="💡", layout="wide")

# Initialiser profil
if 'profil' not in st.session_state:
    st.session_state.profil = {
        'nom': 'Votre organisation',
        'secteur': 'finance',
        'taille': 'medium',
        'ca': '10M$ - 50M$',
        'budget': 'medium',
        'maturite': 'managed'
    }

profil = st.session_state.profil
secteur = profil.get('secteur', 'finance')
budget = profil.get('budget', 'medium')
taille = profil.get('taille', 'medium')
maturite = profil.get('maturite', 'managed')

# Avertissement si profil non configuré
if profil.get('nom') == 'Votre organisation':
    st.warning("⚠️ **Profil non configuré** - Les recommandations ci-dessous sont basées sur un profil générique. Pour des recommandations personnalisées, configurez d'abord votre profil dans **Profil organisation**.")

st.title("💡 Recommandations stratégiques")
st.caption(f"Plan d'action pour: **{profil.get('nom')}** • {secteur} • Budget: {budget} • Maturité: {maturite}")

col1, col2 = st.columns([3, 1])
with col2:
    if st.button("📤 Exporter en PDF", use_container_width=True):
        try:
            from utils.pdf_generator import generer_rapport_recommandations
            pdf_buffer = generer_rapport_recommandations(profil)
            
            st.download_button(
                label="💾 Télécharger le PDF",
                data=pdf_buffer,
                file_name=f"recommandations_{profil.get('nom', 'rapport').replace(' ', '_')}.pdf",
                mime="application/pdf",
                use_container_width=True
            )
            st.success("✅ PDF généré!")
        except Exception as e:
            st.error(f"❌ Erreur: {str(e)}")

st.divider()

# Convertir budget en montant
def get_budget_montant(budget_niveau):
    budgets = {'low': 50000, 'medium': 200000, 'high': 500000}
    return budgets.get(budget_niveau, 200000)

budget_disponible = get_budget_montant(budget)

# Déterminer stratégie recommandée
def determiner_strategie(budget, taille, maturite):
    if budget == 'low' or taille == 'micro':
        return 'minimale'
    if budget == 'high' and taille == 'large':
        return 'acceleree'
    return 'progressive'

strategie_recommandee = determiner_strategie(budget, taille, maturite)

# Adapter budgets selon taille
def adapter_budget(base, taille):
    multiplicateurs = {'micro': 0.3, 'small': 0.6, 'medium': 1.0, 'large': 1.8}
    mult = multiplicateurs.get(taille, 1.0)
    return int(base * mult)

# Message personnalisé
taille_labels = {'micro': 'micro-entreprise', 'small': 'petite entreprise', 'medium': 'moyenne entreprise', 'large': 'grande entreprise'}
budget_labels = {'low': 'limité (< 50k$)', 'medium': 'moyen (50-200k$)', 'high': 'élevé (> 200k$)'}

st.success(f"""
### ✅ Recommandation basée sur votre profil

Pour une **{taille_labels.get(taille)}** du secteur **{secteur}** avec un budget de conformité **{budget_labels.get(budget)}** et une maturité **{maturite}**, nous recommandons **l'approche {strategie_recommandee.upper()}**.

Cette stratégie est optimisée pour maximiser votre conformité tout en respectant votre budget de **{budget_disponible/1000:.0f}k$**.
""")

st.markdown("<br>", unsafe_allow_html=True)

# TABLEAU COMPARATIF DES 3 APPROCHES
st.subheader("📊 Tableau comparatif des approches")

comparaison_data = {
    'Critère': [
        '💰 Coût total',
        '⏱️ Durée',
        '📅 Nombre de phases',
        '⚠️ Niveau de risque',
        '🎯 Conformité atteinte',
        '🔧 Complexité',
        '👥 Ressources externes',
        '📜 Certification ISO 27001',
        '✅ Loi 25 couverte'
    ],
    'Minimale': [
        f"{adapter_budget(80000, taille)/1000:.0f}k$",
        '12-18 mois',
        '2 phases',
        '⚠️ Élevé',
        'Partielle (Loi 25)',
        '🟢 Faible',
        'Minimales',
        '❌ Non incluse',
        '✅ Oui'
    ],
    'Progressive': [
        f"{adapter_budget(300000, taille)/1000:.0f}k$",
        '18-24 mois',
        '3 phases',
        '🟡 Moyen',
        'Élevée',
        '🟡 Moyenne',
        'Modérées',
        '✅ En fin de parcours',
        '✅ Oui'
    ],
    'Accélérée': [
        f"{adapter_budget(500000, taille)/1000:.0f}k$",
        '9-12 mois',
        '2 phases',
        '🟢 Faible',
        'Complète',
        '🔴 Élevée',
        'Importantes',
        '✅ Oui',
        '✅ Oui'
    ]
}

df_comparaison = pd.DataFrame(comparaison_data)
st.dataframe(df_comparaison, use_container_width=True, hide_index=True)

# Légende
col1, col2, col3 = st.columns(3)
with col1:
    if strategie_recommandee == 'minimale':
        st.success("⭐ **MINIMALE** recommandée pour vous")
with col2:
    if strategie_recommandee == 'progressive':
        st.success("⭐ **PROGRESSIVE** recommandée pour vous")
with col3:
    if strategie_recommandee == 'acceleree':
        st.success("⭐ **ACCÉLÉRÉE** recommandée pour vous")

# TOOLTIP: Définitions
with st.expander("❓ Définitions des termes du tableau"):
    st.markdown("""
    **💰 Coût total:** Budget total nécessaire pour le projet complet
    
    **⏱️ Durée:** Temps nécessaire du début à la fin du projet
    
    **📅 Phases:** Étapes distinctes du projet (ex: Fondations, Renforcement, Optimisation)
    
    **⚠️ Niveau de risque:** Risque résiduel après l'implémentation
    
    **🎯 Conformité atteinte:** Niveau de couverture des référentiels
    
    **🔧 Complexité:** Niveau de difficulté d'implémentation
    
    **👥 Ressources externes:** Besoin de consultants/experts externes
    
    **📜 ISO 27001:** Certification internationale de sécurité de l'information
    """)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================
# SECTION ACTIONS PRIORITAIRES - TRI PAR BUDGET
# ============================================

st.subheader(f"⚡ Actions prioritaires pour le secteur {secteur}")

# IMPORTANT: Afficher CLAIREMENT le budget disponible
st.info(f"""
💰 **Votre budget disponible: {budget_disponible/1000:.0f}k$**

Les actions sont triées par **faisabilité budgétaire** - les actions que vous pouvez faire MAINTENANT sont affichées en premier.
""")

# Actions essentielles
actions_essentielles = [
    {'titre': 'Politique de confidentialité Loi 25', 'delai': '2 semaines', 'cout': 5000, 'impact': '85%', 'description': '🔴 OBLIGATOIRE - Mise à jour conforme Loi 25', 'priorite': 'critique'},
    {'titre': 'Formation cybersécurité employés', 'delai': '2 semaines', 'cout': 5000, 'impact': '50%', 'description': 'Sensibilisation et réduction risque humain', 'priorite': 'haute'},
    {'titre': "Contrôles d'accès et MFA", 'delai': '3 semaines', 'cout': 8000, 'impact': '75%', 'description': 'Authentification renforcée', 'priorite': 'critique'},
    {'titre': 'Registre des traitements de données', 'delai': '4 semaines', 'cout': 15000, 'impact': '70%', 'description': 'Documentation complète des traitements', 'priorite': 'haute'},
    {'titre': 'ÉFVP (Évaluation vie privée)', 'delai': '6 semaines', 'cout': 25000, 'impact': '75%', 'description': "Analyse d'impact obligatoire Loi 25", 'priorite': 'haute'},
    {'titre': 'Audit de sécurité externe', 'delai': '1 mois', 'cout': 30000, 'impact': '60%', 'description': 'Identification des vulnérabilités', 'priorite': 'moyenne'},
    {'titre': 'Déploiement SIEM', 'delai': '3 mois', 'cout': 45000, 'impact': '80%', 'description': 'Monitoring et détection avancés', 'priorite': 'moyenne'},
    {'titre': 'Plan de réponse aux incidents', 'delai': '1 mois', 'cout': 12000, 'impact': '65%', 'description': 'Procédures documentées et testées', 'priorite': 'haute'}
]

# TRI PAR BUDGET: Séparer actions dans budget vs hors budget
budget_cumule = 0
actions_dans_budget = []
actions_hors_budget = []

# IMPORTANT: Trier d'abord par coût croissant pour maximiser le nombre d'actions
actions_triees = sorted(actions_essentielles, key=lambda x: x['cout'])

for action in actions_triees:
    if budget_cumule + action['cout'] <= budget_disponible:
        actions_dans_budget.append(action)
        budget_cumule += action['cout']
    else:
        actions_hors_budget.append(action)

# Re-trier les actions dans budget par priorité
ordre_priorite = {'critique': 1, 'haute': 2, 'moyenne': 3}
actions_dans_budget = sorted(actions_dans_budget, key=lambda x: ordre_priorite.get(x['priorite'], 4))

# AFFICHAGE: D'ABORD LES ACTIONS DANS LE BUDGET
st.success(f"""
✅ **Vous pouvez réaliser {len(actions_dans_budget)} actions prioritaires** avec votre budget de {budget_disponible/1000:.0f}k$

**Budget utilisé:** {budget_cumule/1000:.0f}k$ / {budget_disponible/1000:.0f}k$  
**Budget restant:** {(budget_disponible - budget_cumule)/1000:.0f}k$
""")

st.markdown("### ✅ Actions à réaliser MAINTENANT (dans votre budget)")

for i, action in enumerate(actions_dans_budget, 1):
    if action['priorite'] == 'critique':
        st.error(f"**{i}. {action['titre']}** - {action['cout']/1000:.0f}k$ ✅ DANS BUDGET")
    elif action['priorite'] == 'haute':
        st.warning(f"**{i}. {action['titre']}** - {action['cout']/1000:.0f}k$ ✅ DANS BUDGET")
    else:
        st.info(f"**{i}. {action['titre']}** - {action['cout']/1000:.0f}k$ ✅ DANS BUDGET")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("⏱️ Délai", action['delai'])
    with col2:
        st.metric("💰 Coût", f"{action['cout']/1000:.0f}k$")
    with col3:
        st.metric("📉 Réduction risque", action['impact'])
    
    st.caption(action['description'])
    st.divider()

# AFFICHAGE: ENSUITE LES ACTIONS HORS BUDGET
if actions_hors_budget:
    st.markdown("### ⏸️ Actions différées (hors budget actuel)")
    
    budget_manquant = sum(a['cout'] for a in actions_hors_budget)
    
    st.warning(f"""
    Ces **{len(actions_hors_budget)} actions** nécessitent un budget additionnel de **{budget_manquant/1000:.0f}k$**.
    
    **Options:**
    1. Les planifier pour l'année suivante
    2. Augmenter le budget de {budget_manquant/1000:.0f}k$ cette année
    3. Les prioriser selon l'urgence
    """)
    
    for i, action in enumerate(actions_hors_budget, 1):
        with st.expander(f"⏸️ {action['titre']} - {action['cout']/1000:.0f}k$ (HORS BUDGET)", expanded=False):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("⏱️ Délai", action['delai'])
            with col2:
                st.metric("💰 Coût", f"{action['cout']/1000:.0f}k$")
            with col3:
                st.metric("📉 Impact", action['impact'])
            
            st.caption(action['description'])
            st.error(f"⚠️ Budget insuffisant - Manque: {action['cout'] - (budget_disponible - budget_cumule):.0f}$")

st.markdown("<br>", unsafe_allow_html=True)

# QUICK WINS
st.subheader("🏆 Quick Wins - Actions immédiates")

st.success("✨ Ces actions peuvent être réalisées rapidement (< 1 mois) avec un impact immédiat")

quick_wins = [
    {'titre': 'Activer MFA sur comptes administrateurs', 'duree': '3 jours', 'cout': {'micro': 500, 'small': 1500, 'medium': 3000, 'large': 8000}[taille], 'impact': '60%', 'description': 'Protection immédiate contre 80% des attaques par mot de passe. MFA = Code SMS/App en plus du mot de passe.'},
    {'titre': "Révision des droits d'accès", 'duree': '1 semaine', 'cout': {'micro': 1000, 'small': 2000, 'medium': 4000, 'large': 10000}[taille], 'impact': '50%', 'description': 'Supprimer les accès obsolètes (ex-employés, accès non nécessaires)'},
    {'titre': 'Politique de mots de passe renforcée', 'duree': '2 jours', 'cout': 0, 'impact': '40%', 'description': 'Mise à jour gratuite: min 12 caractères, pas de mots communs, changement tous les 90 jours'},
    {'titre': 'Sensibilisation email phishing', 'duree': '1 journée', 'cout': {'micro': 500, 'small': 1000, 'medium': 2000, 'large': 5000}[taille], 'impact': '35%', 'description': 'Formation courte de 2h pour reconnaître les emails frauduleux'}
]

# Trier Quick Wins aussi par budget
quick_wins_budget = []
quick_wins_hors_budget = []

for qw in quick_wins:
    if qw['cout'] <= (budget_disponible - budget_cumule):
        quick_wins_budget.append(qw)
    else:
        quick_wins_hors_budget.append(qw)

if quick_wins_budget:
    st.info(f"💡 **{len(quick_wins_budget)} Quick Wins** rentrent dans votre budget restant ({(budget_disponible - budget_cumule)/1000:.1f}k$)")

for i, qw in enumerate(quick_wins_budget, 1):
    with st.expander(f"✅ {i}. {qw['titre']} - {qw['cout']/1000:.1f}k$", expanded=(i==1)):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("⏱️ Durée", qw['duree'])
        with col2:
            st.metric("💰 Coût", f"{qw['cout']/1000:.1f}k$" if qw['cout'] > 0 else "Gratuit")
        with col3:
            st.metric("📈 Impact", qw['impact'])
        
        st.caption(qw['description'])
        st.success("✅ Action DANS BUDGET - À faire immédiatement!")

if quick_wins_hors_budget:
    st.warning(f"⏸️ {len(quick_wins_hors_budget)} Quick Wins hors budget")
    for qw in quick_wins_hors_budget:
        with st.expander(f"⏸️ {qw['titre']} - {qw['cout']/1000:.1f}k$ (DIFFÉRÉ)"):
            st.caption(qw['description'])

st.markdown("<br>", unsafe_allow_html=True)

# RÉSUMÉ FINAL
st.success(f"""
✅ **Plan d'action recommandé pour votre budget de {budget_disponible/1000:.0f}k$:**

**Actions réalisables immédiatement:**
1. **{len(actions_dans_budget)} actions prioritaires** ({budget_cumule/1000:.0f}k$)
2. **{len(quick_wins_budget)} Quick Wins** (impact rapide)

**Budget total utilisé:** {budget_cumule/1000:.0f}k$ / {budget_disponible/1000:.0f}k$  
**Budget restant:** {(budget_disponible - budget_cumule)/1000:.0f}k$

💡 Consultez **Calendrier** pour la timeline et **Synthèse exécutive** pour la présentation au directeur.
""")

if actions_hors_budget:
    st.warning(f"""
    ⚠️ **{len(actions_hors_budget)} actions différées** faute de budget suffisant.  
    Budget additionnel requis: {sum(a['cout'] for a in actions_hors_budget)/1000:.0f}k$
    
    **Recommandation:** Priorisez les actions dans budget cette année, puis planifiez les autres pour l'année suivante.
    """)

st.divider()

st.caption("""
💡 **Astuce:** Les actions sont triées pour maximiser l'utilisation de votre budget disponible.

📊 **Priorité:** Actions DANS budget affichées en premier, triées par criticité.
""")
