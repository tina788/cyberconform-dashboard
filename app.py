import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="CyberConform Dashboard",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialiser session state si nécessaire
if 'profil' not in st.session_state:
    st.session_state.profil = {
        'nom': 'Votre organisation',
        'secteur': 'finance',
        'taille': 'medium',
        'ca': '10M$ - 50M$',
        'ca_annuel': 30000000,
        'budget': 'medium',
        'maturite': 'managed'
    }

# Header principal avec branding amélioré
st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2.5rem; border-radius: 12px; margin-bottom: 2rem; text-align: center;">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">🔒</div>
        <h1 style="color: white; margin: 0; font-size: 2.8rem; font-weight: 700;">CyberConform Dashboard</h1>
        <p style="color: #E2E8F0; margin: 0.75rem 0 0 0; font-size: 1.3rem;">Plateforme d'analyse de conformité cybersécurité</p>
    </div>
    """, unsafe_allow_html=True)

# Bandeau d'avertissement si données d'exemple
if st.session_state.profil.get('nom') == 'Votre organisation':
    st.warning("""
    ⚠️ **ATTENTION: DONNÉES D'EXEMPLE AFFICHÉES**
    
    Pour obtenir une **analyse personnalisée** avec vos vraies données:
    
    1. Cliquez sur **"🏢 Profil organisation"** dans le menu de gauche
    2. Configurez votre secteur, CA, budget, etc.
    3. Cliquez sur **"💾 Enregistrer le profil"**
    4. Les autres pages se mettront automatiquement à jour avec vos données!
    """)
    
# Section bienvenue
st.success("""
### 👋 Bienvenue sur CyberConform Dashboard!

Cette plateforme vous aide à **analyser votre conformité cybersécurité** et à **planifier votre mise en conformité** 
selon les réglementations québécoises et internationales.

**🎯 Ce que vous pouvez faire:**
- ⚖️ **Évaluer** votre exposition aux pénalités réglementaires (Loi 25, RGPD, etc.)
- 💰 **Calculer** les risques financiers basés sur votre CA réel  
- 💡 **Obtenir** des recommandations adaptées à VOTRE budget
- 📅 **Planifier** votre projet de conformité sur 18-24 mois
- 📊 **Visualiser** le retour sur investissement (ROI)
- 📄 **Exporter** des rapports PDF professionnels
""")

# Guide de démarrage
col1, col2 = st.columns([2, 1])

with col1:
    st.info("""
    ### 🚀 Guide de démarrage rapide (5 minutes)
    
    **Étape 1: Configurez votre profil** *(2 min)*
    - Cliquez sur **🏢 Profil organisation** dans le menu
    - Entrez votre secteur, CA annuel, budget disponible
    - Sauvegardez
    
    **Étape 2: Analysez vos risques** *(2 min)*
    - Allez dans **⚠️ Analyse de risques**
    - Découvrez votre exposition financière (calculée selon VOTRE CA)
    - Identifiez les référentiels applicables à votre secteur
    
    **Étape 3: Obtenez votre plan d'action** *(1 min)*
    - Consultez **💡 Recommandations**
    - Votre stratégie optimale sera automatiquement recommandée
    - Voyez les actions prioritaires adaptées à votre budget
    
    **Bonus:** Explorez **📅 Calendrier** et **💰 Investissement** pour les détails!
    """)

with col2:
    st.markdown("### 📊 Couverture")
    
    st.metric("Référentiels analysés", "20+", help="Loi 25, RGPD, ISO 27001, PCI DSS, etc.")
    st.metric("Secteurs couverts", "6", help="Santé, Finance, Tech, Public, Retail, Autre")
    st.metric("Économies possibles", "170k$", help="Jusqu'à 170k$ d'économies identifiées")

st.markdown("<br>", unsafe_allow_html=True)

# FAQ rapide
with st.expander("❓ Questions fréquentes"):
    st.markdown("""
    **Q: D'où viennent les montants de pénalités?**  
    R: Calculés selon la législation officielle (Loi 25 Art. 90.1, RGPD Art. 83) et votre CA réel.
    
    **Q: Les recommandations sont-elles adaptées à mon budget?**  
    R: Oui! L'outil propose uniquement les stratégies réalisables avec votre budget déclaré.
    
    **Q: Puis-je exporter les résultats?**  
    R: Oui, chaque page importante a un bouton "📤 Exporter en PDF".
    
    **Q: Les données sont-elles sauvegardées?**  
    R: Oui, durant votre session. Mais aucune donnée n'est envoyée à des serveurs externes.
    
    **Q: C'est fiable?**  
    R: Basé sur les standards ISACA, NIST, budgets moyens du marché québécois 2024-2026.
    """)

# Call to action
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Commencer mon analyse maintenant", type="primary", use_container_width=True):
        st.balloons()
        st.success("""
        **Parfait! Voici vos prochaines étapes:**
        
        1. Utilisez le **menu de gauche** (☰ sur mobile)
        2. Commencez par **🏢 Profil organisation**
        3. Suivez le guide étape par étape!
        """)

# Footer avec crédibilité
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.caption("""
    **📚 Sources:**  
    Loi 25, RGPD, ISO 27001, NIST CSF, PCI DSS
    """)

with col2:
    st.caption("""
    **🏢 Basé sur:**  
    Standards ISACA, budgets réels marché QC
    """)

with col3:
    st.caption("""
    **📅 Mis à jour:**  
    Mars 2026
    """)

st.caption("© 2026 CyberConform Dashboard - Outil d'analyse de conformité cybersécurité")
