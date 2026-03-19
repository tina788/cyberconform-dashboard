import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Tableau de bord", page_icon="📊", layout="wide")

# Header
st.title("📊 Tableau de bord")
st.caption("Vue d'ensemble de votre conformité cybersécurité")

# Bouton export
col1, col2, col3 = st.columns([3, 1, 1])
with col3:
    st.button("📥 Exporter PDF", use_container_width=True)

st.divider()

# Métriques principales (4 cards)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="🛡️ Score de conformité global",
        value="87%",
        delta="+5% mois dernier"
    )

with col2:
    st.metric(
        label="✅ Contrôles actifs",
        value="156",
        delta="+12 mois dernier"
    )

with col3:
    st.metric(
        label="⚠️ Risques identifiés",
        value="88",
        delta="-8 mois dernier"
    )

with col4:
    st.metric(
        label="📈 Taux de résolution",
        value="94%",
        delta="+7% mois dernier"
    )

st.markdown("<br>", unsafe_allow_html=True)

# Section principale
col1, col2, col3 = st.columns([2, 2, 2])

with col1:
    st.subheader("Actions rapides")
    
    st.button("🔍 Nouvelle évaluation", use_container_width=True)
    st.button("📥 Générer rapport", use_container_width=True)
    st.button("👥 Inviter utilisateur", use_container_width=True)
    st.button("🔄 Synchroniser", use_container_width=True)

with col2:
    st.subheader("Tâches de conformité")
    
    # Tâche 1
    with st.container():
        st.markdown("**Mettre à jour la politique de confidentialité**")
        col_a, col_b = st.columns([3, 1])
        with col_a:
            st.caption("Loi 25 • Échéance: 7 mars 2026")
        with col_b:
            st.markdown("🔴 **Haute**")
    
    st.divider()
    
    # Tâche 2
    with st.container():
        st.markdown("**Réviser les contrôles d'accès**")
        col_a, col_b = st.columns([3, 1])
        with col_a:
            st.caption("ISO 27001 • Échéance: 12 mars 2026")
        with col_b:
            st.markdown("🟡 **Moyenne**")
    
    st.divider()
    
    # Tâche 3
    with st.container():
        st.markdown("**Formation cybersécurité employés**")
        col_a, col_b = st.columns([3, 1])
        with col_a:
            st.caption("SOC 2 • Échéance: 20 mars 2026")
        with col_b:
            st.markdown("🟢 **Moyenne**")

with col3:
    st.subheader("Activités récentes")
    
    st.markdown("✅ **Évaluation ISO 27001 complétée**")
    st.caption("Score de conformité: 92% • Il y a 2 heures")
    
    st.divider()
    
    st.markdown("⚠️ **Nouvelle vulnérabilité détectée**")
    st.caption("Système de gestion des accès • Il y a 4 heures")
    
    st.divider()
    
    st.markdown("📄 **Politique de sécurité mise à jour**")
    st.caption("Politique de mots de passe v2.1 • Hier")
    
    st.divider()
    
    st.markdown("🕐 **Révision trimestrielle en attente**")
    st.caption("Date limite: 15 mars 2026 • Il y a 2 jours")

st.markdown("<br><br>", unsafe_allow_html=True)

# Graphiques
col1, col2 = st.columns(2)

with col1:
    st.subheader("Conformité par réglementation")
    
    # Graphique barres
    fig = go.Figure()
    
    regulations = ['Loi 25', 'ISO 27001', 'RGPD', 'PCI DSS', 'SOC 2']
    scores = [85, 92, 78, 88, 95]
    colors = ['#EF4444', '#10B981', '#F59E0B', '#3B82F6', '#A855F7']
    
    fig.add_trace(go.Bar(
        x=regulations,
        y=scores,
        marker_color=colors,
        text=[f"{s}%" for s in scores],
        textposition='outside',
        textfont=dict(size=14, weight='bold'),
        hovertemplate='<b>%{x}</b><br>Score: %{y}%<extra></extra>'
    ))
    
    fig.update_layout(
        height=350,
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#F3F4F6', range=[0, 100]),
        margin=dict(t=20, b=20, l=20, r=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Distribution des risques")
    
    # Graphique donut
    fig = go.Figure()
    
    labels = ['Critique', 'Élevé', 'Moyen', 'Faible']
    values = [3, 12, 28, 45]
    colors = ['#EF4444', '#F59E0B', '#F59E0B', '#10B981']
    
    fig.add_trace(go.Pie(
        labels=labels,
        values=values,
        hole=0.6,
        marker=dict(colors=colors),
        textinfo='label+percent',
        textfont=dict(size=12, weight='bold'),
        hovertemplate='<b>%{label}</b><br>%{value} risques<br>%{percent}<extra></extra>'
    ))
    
    fig.update_layout(
        height=350,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        margin=dict(t=20, b=20, l=20, r=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)

st.success("✅ Votre tableau de bord est à jour!")
