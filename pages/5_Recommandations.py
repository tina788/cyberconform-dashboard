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
    st.warning("""
    ⚠️ **Profil non configuré**
    
    Les recommandations ci-dessous sont basées sur un profil générique.
    
    **Pour des recommandations personnalisées**, configurez d'abord votre profil dans **🏢 Profil organisation**.
    """)

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
    - 🟢 Faible = Très bien protégé
    - 🟡 Moyen = Protection acceptable
    - ⚠️ Élevé = Vulnérabilités subsistent
    
    **🎯 Conformité atteinte:** Niveau de couverture des référentiels
    - Partielle = Loi 25 uniquement
    - Élevée = Loi 25 + principaux référentiels
    - Complète = Tous les référentiels pertinents
    
    **🔧 Complexité:** Niveau de difficulté d'implémentation
    
    **👥 Ressources externes:** Besoin de consultants/experts externes
    
    **📜 ISO 27001:** Certification internationale de sécurité de l'information
    """)

st.markdown("<br>", unsafe_allow_html=True)

# TABS pour détails
tab1, tab2, tab3 = st.tabs(["🎯 Détail des approches", "⚡ Actions prioritaires", "🏆 Quick Wins"])

with tab1:
    st.subheader("Approches détaillées")
    
    # APPROCHE PROGRESSIVE
    if strategie_recommandee == 'progressive':
        st.success("⭐ **RECOMMANDÉE POUR VOUS**")
    
    st.markdown("### 📈 Approche progressive")
    
    budget_progressif = adapter_budget(300000, taille)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("⏱️ Durée", "18-24 mois")
    with col2:
        st.metric("💰 Budget", f"{budget_progressif/1000:.0f}k$")
    with col3:
        dans_budget = budget_progressif <= budget_disponible
        st.metric("📊 Status", "✅ Dans budget" if dans_budget else "❌ Hors budget")
    
    if not dans_budget:
        st.error(f"""
        ⚠️ **Budget insuffisant**
        
        Cette approche nécessite {budget_progressif/1000:.0f}k$ mais votre budget est de {budget_disponible/1000:.0f}k$.
        
        **Déficit:** {(budget_progressif - budget_disponible)/1000:.0f}k$
        
        → Considérez l'approche **Minimale** ou augmentez votre budget.
        """)
    
    with st.expander("📘 Détail des phases", expanded=True):
        st.markdown(f"""
        **Phase 1: Fondations (6 mois • {int(budget_progressif*0.35)/1000:.0f}k$)**
        
        *Que va-t-on faire concrètement?*
        - Analyser vos systèmes actuels (où sont les données? qui y accède?)
        - Créer votre politique de confidentialité conforme Loi 25
        - Former vos employés (2h de formation interactive)
        - Installer l'authentification à deux facteurs (MFA) sur tous les comptes
        - Chiffrer vos bases de données sensibles
        
        **Résultat:** Conformité minimale Loi 25 atteinte ✅
        
        ---
        
        **Phase 2: Renforcement (8 mois • {int(budget_progressif*0.40)/1000:.0f}k$)**
        
        *Que va-t-on faire concrètement?*
        - Installer un système de monitoring (SIEM) pour détecter les incidents
        - Mettre en place des sauvegardes automatiques sécurisées
        - Auditer régulièrement vos systèmes (tests tous les 3 mois)
        - Créer un plan de réponse aux incidents
        
        **Résultat:** Préparation pour certification ISO 27001 ✅
        
        ---
        
        **Phase 3: Optimisation (6 mois • {int(budget_progressif*0.25)/1000:.0f}k$)**
        
        *Que va-t-on faire concrètement?*
        - Passer l'audit de certification ISO 27001
        - Faire tester votre sécurité par des hackers éthiques (pentest)
        - Former votre équipe aux techniques avancées
        - Automatiser les processus de conformité
        
        **Résultat:** Certification ISO 27001 obtenue! 🏆
        """)
    
    if strategie_recommandee == 'progressive' and dans_budget:
        if st.button("✅ Sélectionner l'approche progressive", type="primary", use_container_width=True):
            st.balloons()
            st.success("""
            **Excellent choix!**
            
            Prochaines étapes:
            1. Téléchargez le rapport PDF complet
            2. Présentez-le à votre direction pour approbation
            3. Commencez par les Quick Wins (onglet ci-dessus)
            """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # APPROCHE ACCÉLÉRÉE
    if strategie_recommandee == 'acceleree':
        st.success("⭐ **RECOMMANDÉE POUR VOUS**")
    
    st.markdown("### 🎯 Approche accélérée")
    
    budget_accelere = adapter_budget(500000, taille)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("⏱️ Durée", "9-12 mois")
    with col2:
        st.metric("💰 Budget", f"{budget_accelere/1000:.0f}k$")
    with col3:
        dans_budget_acc = budget_accelere <= budget_disponible
        st.metric("📊 Status", "✅ Dans budget" if dans_budget_acc else "❌ Hors budget")
    
    with st.expander("Détail de l'approche accélérée"):
        st.markdown(f"""
        **Pourquoi choisir cette approche?**
        - Vous avez une échéance serrée
        - Votre exposition au risque est critique
        - Vous avez le budget nécessaire
        
        **Ce qui change:**
        - Équipe de consultants dédiée à temps plein
        - Toutes les phases en parallèle (au lieu de séquentiel)
        - Certification obtenue en < 1 an
        
        **Coût supplémentaire:** +{(budget_accelere - budget_progressif)/1000:.0f}k$ vs Progressive
        
        **Attention:** Demande un engagement fort de toute l'organisation
        """)
    
    # APPROCHE MINIMALE
    if strategie_recommandee == 'minimale':
        st.success("⭐ **RECOMMANDÉE POUR VOUS**")
    
    st.markdown("### 💰 Approche minimale")
    
    budget_minimal = adapter_budget(80000, taille)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("⏱️ Durée", "12-18 mois")
    with col2:
        st.metric("💰 Budget", f"{budget_minimal/1000:.0f}k$")
    with col3:
        dans_budget_min = budget_minimal <= budget_disponible
        st.metric("📊 Status", "✅ Dans budget" if dans_budget_min else "❌ Hors budget")
    
    with st.expander("Détail de l'approche minimale"):
        st.markdown(f"""
        **Pour qui?**
        - Petites entreprises
        - Budget limité (< 100k$)
        - Besoin de se conformer à la Loi 25 uniquement
        
        **Ce qui est inclus:**
        - Conformité Loi 25 (OBLIGATOIRE)
        - Contrôles de sécurité de base
        - Formation minimale
        
        **Ce qui n'est PAS inclus:**
        - Certification ISO 27001
        - SIEM et outils avancés
        - Audits complets
        
        **⚠️ Attention:** Risque résiduel élevé
        
        **Recommandation:** Planifiez un budget additionnel pour l'année suivante
        """)

with tab2:
    st.subheader(f"Actions prioritaires pour le secteur {secteur}")
    
    # Actions essentielles
    actions_essentielles = [
        {'titre': 'Politique de confidentialité Loi 25', 'delai': '2 semaines', 'cout': 5000, 'impact': '85%', 'description': '🔴 OBLIGATOIRE - Mise à jour conforme Loi 25', 'priorite': 'critique'},
        {'titre': 'Registre des traitements de données', 'delai': '4 semaines', 'cout': 15000, 'impact': '70%', 'description': 'Documentation complète des traitements', 'priorite': 'haute'},
        {'titre': 'ÉFVP (Évaluation vie privée)', 'delai': '6 semaines', 'cout': 25000, 'impact': '75%', 'description': "Analyse d'impact obligatoire Loi 25", 'priorite': 'haute'},
        {'titre': 'Formation cybersécurité employés', 'delai': '2 semaines', 'cout': 5000, 'impact': '50%', 'description': 'Sensibilisation et réduction risque humain', 'priorite': 'moyenne'},
        {'titre': "Contrôles d'accès et MFA", 'delai': '3 semaines', 'cout': 8000, 'impact': '75%', 'description': 'Authentification renforcée', 'priorite': 'haute'}
    ]
    
    # Calculer budget cumulé
    budget_cumule = 0
    actions_dans_budget = []
    actions_hors_budget = []
    
    for action in actions_essentielles:
        if budget_cumule + action['cout'] <= budget_disponible:
            actions_dans_budget.append(action)
            budget_cumule += action['cout']
        else:
            actions_hors_budget.append(action)
    
    st.info(f"""
    💡 Avec votre budget de **{budget_disponible/1000:.0f}k$**, vous pouvez réaliser **{len(actions_dans_budget)} actions prioritaires** pour un total de **{budget_cumule/1000:.0f}k$**.
    
    **Budget restant:** {(budget_disponible - budget_cumule)/1000:.0f}k$
    """)
    
    # Actions dans le budget
    st.markdown("### ✅ Actions à réaliser (dans votre budget)")
    
    for i, action in enumerate(actions_dans_budget, 1):
        if action['priorite'] == 'critique':
            st.error(f"**{i}. {action['titre']}** - {action['cout']/1000:.0f}k$")
        elif action['priorite'] == 'haute':
            st.warning(f"**{i}. {action['titre']}** - {action['cout']/1000:.0f}k$")
        else:
            st.info(f"**{i}. {action['titre']}** - {action['cout']/1000:.0f}k$")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("⏱️ Délai", action['delai'])
        with col2:
            st.metric("💰 Coût", f"{action['cout']/1000:.0f}k$")
        with col3:
            st.metric("📉 Réduction risque", action['impact'])
        
        st.caption(action['description'])
        st.divider()
    
    # Actions hors budget
    if actions_hors_budget:
        st.markdown("### ⏸️ Actions différées (hors budget actuel)")
        
        st.warning(f"""
        Ces actions nécessitent un budget additionnel de **{sum(a['cout'] for a in actions_hors_budget)/1000:.0f}k$**.
        Planifiez-les pour l'année suivante ou augmentez votre budget.
        """)
        
        for i, action in enumerate(actions_hors_budget, 1):
            with st.expander(f"{action['titre']} - {action['cout']/1000:.0f}k$"):
                st.markdown(f"""
                **Délai:** {action['delai']}  
                **Impact:** {action['impact']}  
                **Description:** {action['description']}
                """)

with tab3:
    st.subheader("Quick Wins - Actions immédiates")
    
    st.success("✨ Ces actions peuvent être réalisées rapidement (< 1 mois) avec un impact immédiat")
    
    quick_wins = [
        {'titre': 'Activer MFA sur comptes administrateurs', 'duree': '3 jours', 'cout': {'micro': 500, 'small': 1500, 'medium': 3000, 'large': 8000}[taille], 'impact': '60%', 'description': 'Protection immédiate contre 80% des attaques par mot de passe. MFA = Code SMS/App en plus du mot de passe.'},
        {'titre': "Révision des droits d'accès", 'duree': '1 semaine', 'cout': {'micro': 1000, 'small': 2000, 'medium': 4000, 'large': 10000}[taille], 'impact': '50%', 'description': 'Supprimer les accès obsolètes (ex-employés, accès non nécessaires)'},
        {'titre': 'Politique de mots de passe renforcée', 'duree': '2 jours', 'cout': 0, 'impact': '40%', 'description': 'Mise à jour gratuite: min 12 caractères, pas de mots communs, changement tous les 90 jours'},
        {'titre': 'Sensibilisation email phishing', 'duree': '1 journée', 'cout': {'micro': 500, 'small': 1000, 'medium': 2000, 'large': 5000}[taille], 'impact': '35%', 'description': 'Formation courte de 2h pour reconnaître les emails frauduleux'}
    ]
    
    budget_quick_wins = sum(qw['cout'] for qw in quick_wins)
    
    if budget_quick_wins <= budget_disponible:
        st.info(f"💡 Toutes les Quick Wins rentrent dans votre budget! Total: {budget_quick_wins/1000:.1f}k$")
    
    for i, qw in enumerate(quick_wins, 1):
        avec_budget = qw['cout'] <= budget_disponible
        
        with st.expander(f"**{i}. {qw['titre']}** - {qw['cout']/1000:.1f}k$ {'✅' if avec_budget else '⏸️'}", expanded=(i==1)):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("⏱️ Durée", qw['duree'])
            with col2:
                st.metric("💰 Coût", f"{qw['cout']/1000:.1f}k$" if qw['cout'] > 0 else "Gratuit")
            with col3:
                st.metric("📈 Impact", qw['impact'])
            
            st.caption(qw['description'])
            
            if not avec_budget and qw['cout'] > 0:
                st.warning("⚠️ Budget insuffisant pour cette action")

st.markdown("<br>", unsafe_allow_html=True)

# RÉSUMÉ FINAL
st.success(f"""
✅ **Plan d'action recommandé pour votre budget de {budget_disponible/1000:.0f}k$:**

1. **Stratégie:** {strategie_recommandee.upper()}
2. **Actions immédiates:** {len(actions_dans_budget)} actions prioritaires ({budget_cumule/1000:.0f}k$)
3. **Quick Wins:** {len([q for q in quick_wins if q['cout'] <= budget_disponible])} actions rapides

**Budget total utilisé:** {budget_cumule/1000:.0f}k$ / {budget_disponible/1000:.0f}k$

💡 Consultez **📅 Calendrier** pour la timeline et **💰 Investissement** pour le détail des coûts.
""")

if actions_hors_budget:
    st.warning(f"""
    ⚠️ **{len(actions_hors_budget)} actions différées** faute de budget suffisant.  
    Budget additionnel requis: {sum(a['cout'] for a in actions_hors_budget)/1000:.0f}k$
    """)
