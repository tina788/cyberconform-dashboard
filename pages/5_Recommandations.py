import streamlit as st
import sys
sys.path.append('.')

st.set_page_config(page_title="Recommandations", page_icon="💡", layout="wide")

# Initialiser profil si nécessaire
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

# CONVERTIR LE BUDGET EN MONTANT RÉEL
def get_budget_montant(budget_niveau):
    """Convertir le niveau de budget en montant maximum disponible"""
    budgets = {
        'low': 50000,      # < 50k$
        'medium': 200000,  # 50k$ - 200k$
        'high': 500000     # > 200k$ (on met un plafond raisonnable)
    }
    return budgets.get(budget_niveau, 200000)

budget_disponible = get_budget_montant(budget)

st.title("💡 Recommandations stratégiques")
st.caption(f"Plan d'action pour: **{profil.get('nom')}** • {secteur} • Budget disponible: **{budget_disponible/1000:.0f}k$**")

# Alerte budget
if budget == 'low':
    st.warning(f"""
    ⚠️ **Budget limité détecté ({budget_disponible/1000:.0f}k$)**
    
    Avec ce budget, vous ne pourrez atteindre qu'une conformité partielle. Nous vous recommandons de:
    - Prioriser uniquement les référentiels OBLIGATOIRES (Loi 25)
    - Commencer par les Quick Wins pour réduire les risques critiques
    - Planifier un budget additionnel pour l'année suivante
    """)

col1, col2 = st.columns([3, 1])
with col2:
    # Bouton export PDF
    if st.button("📤 Exporter en PDF", use_container_width=True):
        try:
            from utils.pdf_generator import generer_rapport_recommandations
            
            # Générer le PDF
            pdf_buffer = generer_rapport_recommandations(profil)
            
            # Bouton de téléchargement
            st.download_button(
                label="💾 Télécharger le PDF",
                data=pdf_buffer,
                file_name=f"recommandations_{profil.get('nom', 'rapport').replace(' ', '_')}.pdf",
                mime="application/pdf",
                use_container_width=True
            )
            
            st.success("✅ PDF généré avec succès!")
            
        except Exception as e:
            st.error(f"❌ Erreur lors de la génération du PDF: {str(e)}")
            st.info("💡 Assurez-vous d'avoir installé: pip install reportlab")

st.divider()

# STRATÉGIES ADAPTÉES AU BUDGET
def generer_strategies_selon_budget(budget_disponible, taille):
    """Génère les stratégies possibles selon le budget disponible"""
    
    strategies = []
    
    # Stratégie MINIMALE (30-100k$)
    cout_minimal_base = 80000
    multiplicateurs = {'micro': 0.4, 'small': 0.7, 'medium': 1.0, 'large': 1.5}
    cout_minimal = int(cout_minimal_base * multiplicateurs.get(taille, 1.0))
    
    if budget_disponible >= cout_minimal:
        strategies.append({
            'nom': 'minimale',
            'titre': '💰 Approche minimale - Conformité essentielle',
            'duree': '12-18 mois',
            'cout': cout_minimal,
            'risque': 'Élevé',
            'complexite': 'Faible',
            'description': 'Focus sur Loi 25 uniquement, contrôles critiques seulement',
            'phases': [
                {'nom': 'Conformité Loi 25', 'duree': '8 mois', 'budget': int(cout_minimal * 0.7)},
                {'nom': 'Ajustements', 'duree': '4 mois', 'budget': int(cout_minimal * 0.3)}
            ],
            'objectifs': [
                'Conformité minimale Loi 25',
                'Contrôles de sécurité de base',
                'Réduction des risques critiques'
            ],
            'limitations': [
                'Pas de certification ISO 27001',
                'Couverture partielle seulement',
                'Risques résiduels élevés'
            ]
        })
    
    # Stratégie PROGRESSIVE (150-400k$)
    cout_progressif_base = 300000
    cout_progressif = int(cout_progressif_base * multiplicateurs.get(taille, 1.0))
    
    if budget_disponible >= cout_progressif:
        strategies.append({
            'nom': 'progressive',
            'titre': '📈 Approche progressive - Équilibrée',
            'duree': '18-24 mois',
            'cout': cout_progressif,
            'risque': 'Moyen',
            'complexite': 'Moyenne',
            'description': 'Implémentation par phases avec amélioration continue',
            'phases': [
                {'nom': 'Fondations', 'duree': '6 mois', 'budget': int(cout_progressif * 0.35)},
                {'nom': 'Renforcement', 'duree': '8 mois', 'budget': int(cout_progressif * 0.40)},
                {'nom': 'Optimisation', 'duree': '6 mois', 'budget': int(cout_progressif * 0.25)}
            ],
            'objectifs': [
                'Conformité Loi 25 complète',
                'Préparation ISO 27001',
                'Contrôles avancés',
                'Processus matures'
            ],
            'limitations': [
                'Durée plus longue',
                'Certification ISO en fin de parcours'
            ]
        })
    
    # Stratégie ACCÉLÉRÉE (400k$+)
    cout_accelere_base = 500000
    cout_accelere = int(cout_accelere_base * multiplicateurs.get(taille, 1.0))
    
    if budget_disponible >= cout_accelere:
        strategies.append({
            'nom': 'acceleree',
            'titre': '🎯 Approche accélérée - Rapide',
            'duree': '9-12 mois',
            'cout': cout_accelere,
            'risque': 'Faible',
            'complexite': 'Élevée',
            'description': 'Déploiement rapide avec ressources dédiées',
            'phases': [
                {'nom': 'Déploiement rapide', 'duree': '4 mois', 'budget': int(cout_accelere * 0.55)},
                {'nom': 'Consolidation', 'duree': '5 mois', 'budget': int(cout_accelere * 0.45)}
            ],
            'objectifs': [
                'Conformité complète en < 1 an',
                'Certification ISO 27001',
                'Équipe externe dédiée',
                'Tous les référentiels couverts'
            ],
            'limitations': [
                'Coût élevé',
                'Stress organisationnel',
                'Nécessite engagement fort de la direction'
            ]
        })
    
    return strategies

strategies_disponibles = generer_strategies_selon_budget(budget_disponible, taille)

# Message si aucune stratégie n'est possible
if not strategies_disponibles:
    st.error(f"""
    ❌ **Budget insuffisant**
    
    Votre budget de **{budget_disponible/1000:.0f}k$** est inférieur au minimum requis pour une mise en conformité même partielle.
    
    **Minimum absolu:** 30k$ - 50k$ pour la conformité Loi 25 de base seulement.
    
    **Options:**
    1. Augmenter le budget à au moins 50k$
    2. Concentrer uniquement sur la politique de confidentialité (5-10k$)
    3. Étaler sur 2-3 ans avec budget annuel de 20-30k$
    """)
    st.stop()

# Déterminer la stratégie recommandée
strategie_recommandee = strategies_disponibles[-1]['nom']  # La plus complète possible dans le budget

st.success(f"""
✅ **Recommandation pour votre budget de {budget_disponible/1000:.0f}k$:**

Nous vous recommandons l'**approche {strategie_recommandee}** qui correspond à votre budget disponible.
""")

# Tabs
tab1, tab2, tab3 = st.tabs(["🎯 Stratégies disponibles", "⚡ Actions prioritaires", "🏆 Quick Wins"])

with tab1:
    st.subheader(f"Stratégies adaptées à votre budget ({budget_disponible/1000:.0f}k$)")
    
    for i, strategie in enumerate(strategies_disponibles):
        # Indicateur si c'est la recommandée
        if strategie['nom'] == strategie_recommandee:
            st.success("⭐ **RECOMMANDÉE POUR VOTRE BUDGET**")
        
        st.subheader(strategie['titre'])
        
        # Vérifier si ça rentre dans le budget
        dans_budget = strategie['cout'] <= budget_disponible
        
        if not dans_budget:
            st.error(f"❌ Cette stratégie dépasse votre budget de {(strategie['cout'] - budget_disponible)/1000:.0f}k$")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("⏱️ Durée", strategie['duree'])
        with col2:
            st.metric("💰 Coût total", f"{strategie['cout']/1000:.0f}k$")
        with col3:
            st.metric("⚠️ Risque", strategie['risque'])
        with col4:
            st.metric("🔧 Complexité", strategie['complexite'])
        
        st.markdown(f"**Description:** {strategie['description']}")
        
        # Phases
        with st.expander("📅 Détail des phases", expanded=(strategie['nom'] == strategie_recommandee)):
            for phase in strategie['phases']:
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.markdown(f"**{phase['nom']}** ({phase['duree']})")
                with col2:
                    st.metric("Budget", f"{phase['budget']/1000:.0f}k$")
                st.divider()
        
        # Objectifs
        with st.expander("🎯 Objectifs et limitations"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**✅ Objectifs:**")
                for obj in strategie['objectifs']:
                    st.markdown(f"• {obj}")
            
            with col2:
                st.markdown("**⚠️ Limitations:**")
                for lim in strategie['limitations']:
                    st.markdown(f"• {lim}")
        
        if strategie['nom'] == strategie_recommandee and dans_budget:
            st.button(
                "✅ Sélectionner cette stratégie", 
                type="primary", 
                use_container_width=True,
                key=f"select_{strategie['nom']}"
            )
        
        st.markdown("<br>", unsafe_allow_html=True)
    
    # Comparaison
    if len(strategies_disponibles) > 1:
        st.subheader("📊 Tableau comparatif")
        
        data = [["Critère"] + [s['titre'].split('-')[0].strip() for s in strategies_disponibles]]
        data.append(["💰 Coût"] + [f"{s['cout']/1000:.0f}k$" for s in strategies_disponibles])
        data.append(["⏱️ Durée"] + [s['duree'] for s in strategies_disponibles])
        data.append(["⚠️ Risque"] + [s['risque'] for s in strategies_disponibles])
        data.append(["✅ Conformité"] + [
            "Partielle (Loi 25)" if s['nom'] == 'minimale' else 
            "Élevée" if s['nom'] == 'progressive' else 
            "Complète" for s in strategies_disponibles
        ])
        
        # Afficher comme tableau
        import pandas as pd
        df = pd.DataFrame(data[1:], columns=data[0])
        st.dataframe(df, use_container_width=True)

with tab2:
    st.subheader(f"Actions prioritaires (budget: {budget_disponible/1000:.0f}k$)")
    
    # Actions avec coûts réels
    actions_essentielles = [
        {
            'titre': 'Politique de confidentialité Loi 25',
            'delai': '2 semaines',
            'cout': 5000,
            'impact': '85%',
            'description': 'OBLIGATOIRE - Mise à jour conforme Loi 25',
            'priorite': 'critique'
        },
        {
            'titre': 'Registre des traitements de données',
            'delai': '4 semaines',
            'cout': 15000,
            'impact': '70%',
            'description': 'Documentation complète des traitements',
            'priorite': 'haute'
        },
        {
            'titre': 'ÉFVP (Évaluation facteurs vie privée)',
            'delai': '6 semaines',
            'cout': 25000,
            'impact': '75%',
            'description': 'Analyse d\'impact obligatoire Loi 25',
            'priorite': 'haute'
        },
        {
            'titre': 'Formation cybersécurité employés',
            'delai': '2 semaines',
            'cout': 5000,
            'impact': '50%',
            'description': 'Sensibilisation et réduction risque humain',
            'priorite': 'moyenne'
        },
        {
            'titre': 'Contrôles d\'accès et MFA',
            'delai': '3 semaines',
            'cout': 8000,
            'impact': '75%',
            'description': 'Authentification renforcée',
            'priorite': 'haute'
        }
    ]
    
    # Calculer le budget cumulé
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
    💡 Avec votre budget de **{budget_disponible/1000:.0f}k$**, vous pouvez réaliser **{len(actions_dans_budget)}** actions prioritaires 
    pour un total de **{budget_cumule/1000:.0f}k$**.
    
    Budget restant: **{(budget_disponible - budget_cumule)/1000:.0f}k$**
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
            st.metric("📉 Impact", action['impact'])
        
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
    
    quick_wins = [
        {
            'titre': 'Activer MFA sur comptes administrateurs',
            'duree': '3 jours',
            'cout': 500,
            'impact': '60%',
            'description': 'Protection immédiate des comptes critiques'
        },
        {
            'titre': 'Révision des droits d\'accès',
            'duree': '1 semaine',
            'cout': 2000,
            'impact': '50%',
            'description': 'Supprimer les accès obsolètes'
        },
        {
            'titre': 'Politique de mots de passe renforcée',
            'duree': '2 jours',
            'cout': 0,
            'impact': '40%',
            'description': 'Mise à jour des exigences (gratuit)'
        },
        {
            'titre': 'Sensibilisation email phishing',
            'duree': '1 journée',
            'cout': 1000,
            'impact': '35%',
            'description': 'Formation courte de 2h pour tous'
        }
    ]
    
    st.success("✨ Ces actions rapides peuvent être réalisées immédiatement avec un impact significatif")
    
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

# Résumé final
st.success(f"""
✅ **Plan d'action recommandé pour votre budget de {budget_disponible/1000:.0f}k$:**

1. **Stratégie:** {strategie_recommandee.upper()} ({strategies_disponibles[-1]['cout']/1000:.0f}k$)
2. **Actions immédiates:** {len(actions_dans_budget)} actions prioritaires ({budget_cumule/1000:.0f}k$)
3. **Quick Wins:** {len([q for q in quick_wins if q['cout'] <= budget_disponible])} actions rapides ({sum(q['cout'] for q in quick_wins if q['cout'] <= budget_disponible)/1000:.1f}k$)

**Budget total utilisé:** {(strategies_disponibles[-1]['cout'] if strategies_disponibles else 0)/1000:.0f}k$ / {budget_disponible/1000:.0f}k$

💡 Consultez **Calendrier** pour la timeline et **Investissement** pour le détail des coûts.
""")

if actions_hors_budget:
    st.warning(f"""
    ⚠️ **{len(actions_hors_budget)} actions différées** faute de budget suffisant.  
    Budget additionnel requis: {sum(a['cout'] for a in actions_hors_budget)/1000:.0f}k$
    """)
