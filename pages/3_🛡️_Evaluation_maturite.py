import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Évaluation maturité", page_icon="🛡️", layout="wide")

# Header
st.markdown("""
<div class="page-header">
    <h1>Évaluation de la maturité</h1>
    <p>Analyse détaillée de votre posture de sécurité selon les 10 domaines ISO 27001</p>
</div>
""", unsafe_allow_html=True)

# Score global (grand box bleu style Figma)
st.markdown("""
<div style="background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%); 
            padding: 3rem 2rem; border-radius: 1.5rem; color: white; margin-bottom: 2rem;
            box-shadow: 0 10px 30px rgba(37,99,235,0.3);">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <div style="font-size: 1.1rem; font-weight: 600; opacity: 0.9; margin-bottom: 1rem;">Score de maturité global</div>
            <div style="display: flex; align-items: baseline; gap: 1rem;">
                <div style="font-size: 5rem; font-weight: 800; line-height: 1;">69</div>
                <div style="font-size: 2rem; opacity: 0.8;">/ 100</div>
            </div>
            <div style="margin-top: 1rem; background: rgba(0,0,0,0.2); height: 8px; border-radius: 1rem; overflow: hidden;">
                <div style="background: white; height: 100%; width: 69%;"></div>
            </div>
        </div>
        <div style="background: white; color: #2563EB; padding: 1rem 2rem; border-radius: 1rem; font-weight: 700;">
            <div style="font-size: 0.85rem; opacity: 0.7;">Niveau actuel</div>
            <div style="font-size: 1.5rem;">Niveau 2 - Géré</div>
            <div style="font-size: 0.85rem; margin-top: 0.5rem; color: #10B981;">
                Progression vers Niveau 3: 52%
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Vue d'ensemble par domaine
st.markdown("## Vue d'ensemble par domaine")

# Radar chart
categories = [
    'Gouvernance',
    'Gestion des risques',
    'Sécurité des actifs',
    'Contrôle d\'accès',
    'Cryptographie',
    'Sécurité physique',
    'Sécurité opérationnelle',
    'Sécurité réseau',
    'Continuité d\'activité',
    'Conformité'
]

values = [100, 75, 50, 25, 0, 75, 50, 75, 50, 100]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=values,
    theta=categories,
    fill='toself',
    fillcolor='rgba(37,99,235,0.3)',
    line=dict(color='#2563EB', width=2),
    marker=dict(size=8, color='#2563EB'),
    name='Score actuel'
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100],
            gridcolor='#E5E7EB'
        ),
        angularaxis=dict(
            gridcolor='#E5E7EB'
        )
    ),
    showlegend=True,
    height=500,
    margin=dict(t=40, b=40, l=80, r=80),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# Détails par domaine
st.markdown("## Détails par domaine")

# Domaine 1 - Gouvernance
with st.expander("**Gouvernance de la sécurité** - 75%", expanded=True):
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%); 
                padding: 1rem; border-radius: 0.75rem; border-left: 4px solid #10B981; margin-bottom: 1rem;">
        <div style="font-weight: 600; color: #065F46; margin-bottom: 0.5rem;">
            <span style="background: #10B981; color: white; padding: 0.25rem 0.75rem; border-radius: 1rem; font-size: 0.75rem; margin-right: 0.5rem;">Niveau 3 - Défini</span>
            Score: 75/100
        </div>
        <div style="background: rgba(16,185,129,0.2); height: 6px; border-radius: 1rem; overflow: hidden;">
            <div style="background: #10B981; height: 100%; width: 75%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### ✅ Points forts")
        st.markdown("""
        - Politique de sécurité documentée et approuvée
        - Comité de sécurité actif avec réunions régulières
        - Rôles et responsabilités clairement définis
        """)
    
    with col2:
        st.markdown("##### ⚠️ Axes d'amélioration")
        st.markdown("""
        - Absence d'indicateurs de performance (KPI) de sécurité
        - Révision annuelle des politiques non systématique
        """)

# Domaine 2 - Gestion des risques
with st.expander("**Gestion des risques** - 60%"):
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%); 
                padding: 1rem; border-radius: 0.75rem; border-left: 4px solid #F59E0B; margin-bottom: 1rem;">
        <div style="font-weight: 600; color: #78350F; margin-bottom: 0.5rem;">
            <span style="background: #F59E0B; color: white; padding: 0.25rem 0.75rem; border-radius: 1rem; font-size: 0.75rem; margin-right: 0.5rem;">Niveau 2 - Géré</span>
            Score: 60/100
        </div>
        <div style="background: rgba(245,158,11,0.2); height: 6px; border-radius: 1rem; overflow: hidden;">
            <div style="background: #F59E0B; height: 100%; width: 60%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### ✅ Points forts")
        st.markdown("""
        - Registre des risques existant
        - Évaluations ponctuelles réalisées
        """)
    
    with col2:
        st.markdown("##### ⚠️ Axes d'amélioration")
        st.markdown("""
        - Pas de méthodologie formelle d'analyse de risques
        - Absence de revue périodique des risques
        - Manque de quantification des impacts financiers
        """)

# Domaine 3 - Contrôle d'accès
with st.expander("**Contrôle d'accès** - 70%"):
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%); 
                padding: 1rem; border-radius: 0.75rem; border-left: 4px solid #10B981; margin-bottom: 1rem;">
        <div style="font-weight: 600; color: #065F46; margin-bottom: 0.5rem;">
            <span style="background: #10B981; color: white; padding: 0.25rem 0.75rem; border-radius: 1rem; font-size: 0.75rem; margin-right: 0.5rem;">Niveau 3 - Défini</span>
            Score: 70/100
        </div>
        <div style="background: rgba(16,185,129,0.2); height: 6px; border-radius: 1rem; overflow: hidden;">
            <div style="background: #10B981; height: 100%; width: 70%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### ✅ Points forts")
        st.markdown("""
        - Authentification multi-facteurs déployée
        - Gestion centralisée des identités
        - Révocation d'accès automatisée
        """)
    
    with col2:
        st.markdown("##### ⚠️ Axes d'amélioration")
        st.markdown("""
        - Revue des droits d'accès non périodique
        - Comptes privilégiés insuffisamment surveillés
        """)

# Domaine 4 - Continuité d'activité
with st.expander("**Continuité d'activité** - 50%"):
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FEE2E2 0%, #FECACA 100%); 
                padding: 1rem; border-radius: 0.75rem; border-left: 4px solid #EF4444; margin-bottom: 1rem;">
        <div style="font-weight: 600; color: #991B1B; margin-bottom: 0.5rem;">
            <span style="background: #EF4444; color: white; padding: 0.25rem 0.75rem; border-radius: 1rem; font-size: 0.75rem; margin-right: 0.5rem;">Niveau 2 - Géré</span>
            Score: 50/100
        </div>
        <div style="background: rgba(239,68,68,0.2); height: 6px; border-radius: 1rem; overflow: hidden;">
            <div style="background: #EF4444; height: 100%; width: 50%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### ✅ Points forts")
        st.markdown("""
        - Plan de Continuité d'Activité (PCA) documenté pour systèmes critiques
        """)
    
    with col2:
        st.markdown("##### ⚠️ Axes d'amélioration")
        st.markdown("""
        - Absence de tests réguliers du PRA
        - RTO et RPO non définis pour tous les systèmes
        - Plan de communication de crise incomplet
        - Sauvegarde hors site non validée
        """)
