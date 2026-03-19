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

st.title("💡 Recommandations stratégiques")
st.caption(f"Plan d'action personnalisé pour: **{profil.get('nom')}** • {secteur} • Budget: {budget} • Maturité: {maturite}")

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

# Déterminer la stratégie recommandée selon le profil
def determiner_strategie(budget, taille, maturite):
    """Détermine la stratégie recommandée selon le profil"""
    
    # Si budget faible ou micro entreprise -> Minimale
    if budget == 'low' or taille == 'micro':
        return 'minimale'
    
    # Si budget élevé et grande entreprise -> Accélérée
    if budget == 'high' and taille == 'large':
        return 'acceleree'
    
    # Sinon -> Progressive (par défaut)
    return 'progressive'

strategie_recommandee = determiner_strategie(budget, taille, maturite)

# Adapter les budgets selon la taille
def adapter_budget(base, taille):
    """Adapte le budget selon la taille"""
    multiplicateurs = {
        'micro': 0.3,
        'small': 0.6,
        'medium': 1.0,
        'large': 1.8
    }
    mult = multiplicateurs.get(taille, 1.0)
    return int(base * mult)

# Tabs
tab1, tab2, tab3 = st.tabs(["🎯 Stratégies d'implémentation", "⚡ Actions prioritaires", "🏆 Quick Wins"])

with tab1:
    st.subheader("Recommandation basée sur votre profil")
    
    # Message personnalisé
    taille_labels = {'micro': 'micro-entreprise', 'small': 'petite entreprise', 'medium': 'moyenne entreprise', 'large': 'grande entreprise'}
    budget_labels = {'low': 'limité', 'medium': 'moyen', 'high': 'élevé'}
    
    st.info(f"""
    Pour une **{taille_labels.get(taille)}** du secteur **{secteur}** avec un budget 
    de conformité **{budget_labels.get(budget)}** et une maturité **{maturite}**, nous recommandons 
    **l'approche {strategie_recommandee}**. 
    
    Cette stratégie est optimisée pour votre situation et offre le meilleur équilibre coût/risque.
    """)
    
    # Approche PROGRESSIVE
    if strategie_recommandee == 'progressive':
        st.success("⭐ **RECOMMANDÉE POUR VOTRE ORGANISATION**")
    
    st.subheader("📈 Approche progressive (Recommandée pour la plupart)")
    
    budget_progressif = adapter_budget(550000, taille)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("⏱️ Durée", "18-24 mois")
    with col2:
        st.metric("💰 Investissement", f"{budget_progressif/1000:.0f}k$")
    with col3:
        st.metric("⚠️ Risque", "Faible", delta="Complexité Moyenne")
    
    st.markdown("---")
    
    phase1 = int(budget_progressif * 0.35)
    phase2 = int(budget_progressif * 0.40)
    phase3 = int(budget_progressif * 0.25)
    
    with st.expander("📘 Phase 1: Fondations (6 mois)", expanded=True):
        st.markdown(f"""
        **Budget: {phase1/1000:.0f}k$**
        
        - Analyse GAP complète de vos systèmes actuels
        - Documentation et politiques de base (Loi 25 prioritaire)
        - Formation de l'équipe interne
        - Mise en place des contrôles essentiels (MFA, chiffrement)
        
        **Objectif:** Conformité minimale Loi 25 atteinte
        """)
    
    with st.expander("📗 Phase 2: Renforcement (8 mois)"):
        st.markdown(f"""
        **Budget: {phase2/1000:.0f}k$**
        
        - Implémentation des contrôles avancés
        - Intégration des outils de sécurité (SIEM, EDR)
        - Audits internes réguliers
        - Amélioration continue des processus
        
        **Objectif:** Préparation certification ISO 27001
        """)
    
    with st.expander("📕 Phase 3: Optimisation (6 mois)"):
        st.markdown(f"""
        **Budget: {phase3/1000:.0f}k$**
        
        - Certification ISO 27001
        - Tests de pénétration
        - Formation avancée
        - Automatisation et optimisation
        
        **Objectif:** Certification obtenue, processus matures
        """)
    
    if strategie_recommandee == 'progressive':
        st.button("✅ Sélectionner cette stratégie", type="primary", use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Approche ACCÉLÉRÉE
    if strategie_recommandee == 'acceleree':
        st.success("⭐ **RECOMMANDÉE POUR VOTRE ORGANISATION**")
    
    st.subheader("🎯 Approche accélérée")
    
    budget_accelere = adapter_budget(750000, taille)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("⏱️ Durée", "9-12 mois")
    with col2:
        st.metric("💰 Budget", f"{budget_accelere/1000:.0f}k$")
    with col3:
        st.metric("⚠️ Risque", "Moyen", delta="Complexité Élevée")
    
    with st.expander("Détails de l'approche accélérée"):
        st.markdown(f"""
        **Phase 1: Déploiement rapide (4 mois • {int(budget_accelere*0.5)/1000:.0f}k$)**
        - Équipe externe dédiée à temps plein
        - Déploiement parallèle de tous les contrôles
        - Formation intensive
        
        **Phase 2: Consolidation (5 mois • {int(budget_accelere*0.5)/1000:.0f}k$)**
        - Tests et ajustements
        - Certification rapide
        
        **Avantages:**
        - Conformité atteinte rapidement
        - Ressources externes dédiées
        
        **Inconvénients:**
        - Coût élevé (+{int((budget_accelere-budget_progressif)/1000)}k$)
        - Stress organisationnel important
        """)
    
    if strategie_recommandee == 'acceleree':
        st.button("✅ Sélectionner cette stratégie", type="primary", use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Approche MINIMALE
    if strategie_recommandee == 'minimale':
        st.success("⭐ **RECOMMANDÉE POUR VOTRE ORGANISATION**")
    
    st.subheader("💰 Approche minimale (Budget limité)")
    
    budget_minimal = adapter_budget(300000, taille)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("⏱️ Durée", "12-18 mois")
    with col2:
        st.metric("💰 Budget", f"{budget_minimal/1000:.0f}k$")
    with col3:
        st.metric("⚠️ Risque", "Élevé", delta="Complexité Faible")
    
    with st.expander("Détails de l'approche minimale"):
        st.markdown(f"""
        **Phase 1: Conformité essentielle (8 mois • {int(budget_minimal*0.7)/1000:.0f}k$)**
        - Focus uniquement sur Loi 25 (obligatoire)
        - Contrôles critiques seulement
        - Formation de base
        
        **Phase 2: Ajustements (6 mois • {int(budget_minimal*0.3)/1000:.0f}k$)**
        - Corrections suite aux audits
        - Optimisations ponctuelles
        
        **Avantages:**
        - Coût minimal
        - Approche pragmatique et réaliste
        
        **Inconvénients:**
        - Risque résiduel élevé
        - Pas de certification ISO 27001
        - Manque de profondeur
        """)
    
    if strategie_recommandee == 'minimale':
        st.button("✅ Sélectionner cette stratégie", type="primary", use_container_width=True)

with tab2:
    st.subheader(f"Actions prioritaires pour le secteur {secteur}")
    
    # Actions spécifiques au secteur
    actions_secteur = {
        'finance': [
            ("Conformité OSFI B-13", "4 semaines", "50k$", "95%", "OBLIGATOIRE pour institutions financières fédérales"),
            ("Politique de confidentialité Loi 25", "2 semaines", "5k$", "85%", "OBLIGATOIRE - Réduction immédiate du risque"),
            ("Registre des traitements de données", "4 semaines", "15k$", "70%", "Documentation complète requise")
        ],
        'health': [
            ("Conformité LPRPSP (santé Québec)", "6 semaines", "35k$", "95%", "OBLIGATOIRE secteur santé"),
            ("Politique de confidentialité Loi 25", "2 semaines", "5k$", "85%", "OBLIGATOIRE - Protection RP"),
            ("Chiffrement des dossiers patients", "3 semaines", "25k$", "90%", "Protection données sensibles santé")
        ],
        'tech': [
            ("Certification SOC 2 Type II", "12 semaines", "65k$", "80%", "Requis pour clients SaaS B2B"),
            ("Politique de confidentialité Loi 25", "2 semaines", "5k$", "85%", "OBLIGATOIRE au Québec"),
            ("Sécurité cloud (ISO 27017)", "6 semaines", "30k$", "75%", "Essentiel pour services cloud")
        ],
        'retail': [
            ("Conformité PCI DSS 4.0", "8 semaines", "55k$", "90%", "OBLIGATOIRE si paiements par carte"),
            ("Politique de confidentialité Loi 25", "2 semaines", "5k$", "85%", "OBLIGATOIRE - Protection clients"),
            ("Sécurité des transactions", "4 semaines", "20k$", "80%", "Protection paiements en ligne")
        ],
        'public': [
            ("Politique de confidentialité Loi 25", "2 semaines", "5k$", "85%", "OBLIGATOIRE secteur public"),
            ("Conformité NIST CSF", "8 semaines", "35k$", "80%", "Recommandé infrastructures critiques"),
            ("Gestion des identités (IAM)", "6 semaines", "40k$", "75%", "Contrôle accès citoyens")
        ]
    }
    
    actions = actions_secteur.get(secteur, actions_secteur['finance'])
    
    st.info(f"🎯 Ces actions sont spécifiquement recommandées pour le secteur **{secteur}**")
    
    for i, (titre, delai, cout, reduction, description) in enumerate(actions, 1):
        if i == 1:
            st.error(f"**{i}. {titre}**")
        elif i == 2:
            st.warning(f"**{i}. {titre}**")
        else:
            st.info(f"**{i}. {titre}**")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("⏱️ Délai", delai)
        with col2:
            st.metric("💰 Coût", cout)
        with col3:
            st.metric("📉 Réduction risque", reduction)
        
        st.caption(description)
        st.divider()

with tab3:
    st.subheader("Quick Wins - Résultats immédiats")
    
    st.success("✨ Ces actions peuvent être complétées rapidement avec un impact immédiat")
    
    # Quick wins adaptés à la taille
    quick_wins_base = [
        {
            "titre": "Activer MFA (authentification multi-facteurs)",
            "duree": "1 semaine",
            "cout_micro": "500$",
            "cout_small": "1500$",
            "cout_medium": "3000$",
            "cout_large": "8000$",
            "impact": "75%",
            "description": "Protection immédiate contre 80% des attaques par mot de passe"
        },
        {
            "titre": "Formation sensibilisation cybersécurité",
            "duree": "2 semaines",
            "cout_micro": "1000$",
            "cout_small": "2500$",
            "cout_medium": "5000$",
            "cout_large": "15000$",
            "impact": "50%",
            "description": "Réduction des incidents causés par erreur humaine"
        },
        {
            "titre": "Chiffrement des bases de données",
            "duree": "3 semaines",
            "cout_micro": "3000$",
            "cout_small": "6000$",
            "cout_medium": "12000$",
            "cout_large": "25000$",
            "impact": "80%",
            "description": "Protection des données au repos contre les violations"
        },
        {
            "titre": "Révision des droits d'accès",
            "duree": "2 semaines",
            "cout_micro": "1000$",
            "cout_small": "2000$",
            "cout_medium": "4000$",
            "cout_large": "10000$",
            "impact": "60%",
            "description": "Élimination des accès non nécessaires et obsolètes"
        }
    ]
    
    for i, qw in enumerate(quick_wins_base, 1):
        cout = qw[f'cout_{taille}']
        
        with st.expander(f"**{i}. {qw['titre']}** - {cout}"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("⏱️ Durée", qw['duree'])
            with col2:
                st.metric("💰 Coût", cout)
            with col3:
                st.metric("📈 Impact", qw['impact'])
            
            st.caption(qw['description'])

st.success(f"""
✅ **Prochaines étapes recommandées:**

1. Sélectionnez l'approche **{strategie_recommandee}** (budget: {adapter_budget(550000 if strategie_recommandee == 'progressive' else 750000 if strategie_recommandee == 'acceleree' else 300000, taille)/1000:.0f}k$)
2. Commencez par les Quick Wins (résultats en 2-3 semaines)
3. Consultez le **Calendrier** pour la timeline détaillée
4. Consultez **Investissement** pour le détail des coûts

💡 Ces recommandations sont personnalisées selon votre profil. Mettez à jour votre **Profil organisation** pour recalculer.
""")
