import streamlit as st
import json
from pathlib import Path
import sys

# Configuration de la page
st.set_page_config(
    page_title="CyberConform - Assistant Pro",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Encodage UTF-8 pour Windows
if sys.platform == "win32":
    import locale
    locale.setlocale(locale.LC_ALL, '')

# CSS Global - Design Figma
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Variables */
:root {
    --sidebar-dark: #1E293B;
    --primary-blue: #2563EB;
    --success-green: #10B981;
    --warning-orange: #F59E0B;
    --danger-red: #EF4444;
    --purple: #A855F7;
    --bg-light: #F8FAFC;
}

* {
    font-family: 'Inter', -apple-system, sans-serif;
}

/* Hide Streamlit defaults */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background: var(--sidebar-dark);
    padding-top: 0;
}

[data-testid="stSidebar"] .block-container {
    padding-top: 1rem;
}

/* Logo header dans sidebar */
.sidebar-logo {
    background: var(--sidebar-dark);
    padding: 1.5rem 1rem;
    margin: 0 -1rem 2rem -1rem;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    text-align: center;
}

.sidebar-logo h1 {
    color: white;
    font-size: 1.5rem;
    margin: 0;
    font-weight: 700;
}

.sidebar-logo p {
    color: rgba(255,255,255,0.7);
    font-size: 0.9rem;
    margin: 0.25rem 0 0 0;
}

/* Navigation links */
.stRadio > div {
    gap: 0.25rem;
}

.stRadio label {
    background: transparent !important;
    color: rgba(255,255,255,0.8) !important;
    padding: 0.75rem 1rem !important;
    border-radius: 0.5rem !important;
    transition: all 0.2s ease !important;
    font-weight: 500 !important;
}

.stRadio label:hover {
    background: rgba(255,255,255,0.1) !important;
    color: white !important;
}

.stRadio div[role="radiogroup"] label[data-selected="true"] {
    background: var(--primary-blue) !important;
    color: white !important;
}

/* Help box */
.help-box {
    background: linear-gradient(135deg, #0EA5E9 0%, #2563EB 100%);
    border-radius: 1rem;
    padding: 1.5rem;
    margin: 2rem 0 1rem 0;
    color: white;
}

.help-box h3 {
    color: white;
    font-size: 1.1rem;
    margin: 0 0 0.5rem 0;
}

.help-box p {
    color: rgba(255,255,255,0.9);
    font-size: 0.9rem;
    margin: 0 0 1rem 0;
    line-height: 1.5;
}

/* Main content */
.main {
    background: var(--bg-light);
}

/* Header */
.page-header {
    background: white;
    padding: 1.5rem 2rem;
    border-radius: 1rem;
    margin-bottom: 2rem;
    border-bottom: 1px solid #E5E7EB;
}

.page-header h1 {
    font-size: 2rem;
    font-weight: 700;
    color: #0A0A0A;
    margin: 0 0 0.5rem 0;
}

.page-header p {
    color: #6B7280;
    font-size: 1rem;
    margin: 0;
}

/* Metric cards */
.metric-card {
    background: white;
    border-radius: 1rem;
    padding: 1.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    border: 1px solid #E8E8E8;
    transition: all 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

/* Buttons */
.stButton > button {
    background: var(--primary-blue);
    color: white;
    border: none;
    border-radius: 0.75rem;
    padding: 0.75rem 1.5rem;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(37,99,235,0.2);
}

.stButton > button:hover {
    background: #1D4ED8;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(37,99,235,0.3);
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "Tableau de bord"

# Sidebar avec logo
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔒</div>
        <h1>CyberConform</h1>
        <p>Assistant Pro</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    pages = {
        "📊 Tableau de bord": "1_📊_Tableau_de_bord",
        "🏢 Profil organisation": "2_🏢_Profil_organisation",
        "🛡️ Évaluation maturité": "3_🛡️_Evaluation_maturite",
        "⚠️ Analyse de risques": "4_⚠️_Analyse_risques",
        "💡 Recommandations": "5_💡_Recommandations",
        "📅 Calendrier": "6_📅_Calendrier",
        "💰 Investissement": "7_💰_Investissement",
        "⚙️ Paramètres": "8_⚙️_Parametres"
    }
    
    selected = st.radio("Navigation", list(pages.keys()), label_visibility="collapsed")
    
    # Help box
    st.markdown("""
    <div class="help-box">
        <h3>Besoin d'aide?</h3>
        <p>Consultez notre guide de conformité cybersécurité</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Voir le guide", use_container_width=True):
        st.info("Guide de conformité à venir!")

# Message de bienvenue si c'est le tableau de bord
if selected == "📊 Tableau de bord":
    st.markdown("""
    <div class="page-header">
        <h1>Tableau de bord</h1>
        <p>Vue d'ensemble de votre conformité cybersécurité</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("👉 **Utilisez le menu de gauche pour naviguer entre les sections**")
    
    st.markdown("""
    ## 🚀 Commencez par:
    
    1. **🏢 Profil organisation** - Configurez les informations de base
    2. **🛡️ Évaluation maturité** - Évaluez votre niveau actuel
    3. **💡 Recommandations** - Obtenez un plan personnalisé
    """)
else:
    st.info(f"📄 Page: **{selected}**\n\nContenu détaillé à venir dans les prochains fichiers.")

# Footer
st.markdown("---")
st.caption("© 2026 CyberConform - Assistant de conformité cybersécurité")
