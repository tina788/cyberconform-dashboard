import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="Tableau de bord", page_icon="📊", layout="wide")

# Initialiser profil
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

profil = st.session_state.profil
ca_annuel = profil.get('ca_annuel', 30000000)
secteur = profil.get('secteur', 'finance')
maturite = profil.get('maturite', 'managed')
budget_niveau = profil.get('budget', 'medium')

# Header
st.title("📊 Tableau de bord CyberConform")

# Avertissement si profil non configuré
if profil.get('nom') == 'Votre organisation':
    st.warning("⚠️ **Profil non configuré** - Les données ci-dessous sont des exemples. Allez dans **Profil organisation** pour voir VOS données réelles.")

st.caption(f"Vue d'ensemble pour: **{profil.get('nom')}** • Dernière mise à jour: {datetime.now().strftime('%d/%m/%Y à %H:%M')}")
st.divider()

# CALCULS DYNAMIQUES (recalculés à chaque affichage)
penalite_loi25 = max(25000000, ca_annuel * 0.04)
penalite_rgpd = max(29000000, ca_annuel * 0.04)
total_exposition = penalite_loi25 + penalite_rgpd + 1200000

probabilites = {'initial': 0.85, 'managed': 0.65, 'defined': 0.40, 'optimized': 0.15}
probabilite = probabilites.get(maturite, 0.65)

budgets = {'low': 50000, 'medium': 200000, 'high': 500000}
budget_disponible = budgets.get(budget_niveau, 200000)

# Score de conformité DYNAMIQUE
scores_conformite = {'initial': 25, 'managed': 55, 'defined': 75, 'optimized': 95}
score_conformite = scores_conformite.get(maturite, 55)

# MÉTRIQUES PRINCIPALES
st.subheader("🎯 Métriques clés")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Exposition totale",
        f"{total_exposition/1000000:.1f} M$",
        f"-{int(probabilite*100)}% si conformité",
        delta_color="inverse",
        help="Risque financier total auquel vous êtes exposé"
    )

with col2:
    couleur_score = "🔴" if score_conformite < 50 else "🟡" if score_conformite < 75 else "🟢"
    st.metric(
        f"{couleur_score} Score de conformité",
        f"{score_conformite}%",
        f"+{100-score_conformite}% à atteindre",
        help=f"Basé sur votre maturité '{maturite}': initial=25%, managed=55%, defined=75%, optimized=95%"
    )

with col3:
    st.metric(
        "📅 Délai recommandé",
        "18 mois",
        "Conformité complète",
        help="Temps estimé pour atteindre la conformité complète"
    )

with col4:
    roi = total_exposition / budget_disponible if budget_disponible > 0 else 0
    st.metric(
        "📈 ROI estimé",
        f"{roi:.0f}:1",
        f"Protection de {total_exposition/1000000:.0f}M$",
        help="Chaque dollar investi protège contre X$ de risques"
    )

st.markdown("<br>", unsafe_allow_html=True)

# GUIDE DE DÉMARRAGE (sans emojis ni minutes)
st.info("""
**Guide de démarrage rapide**

**Étape 1: Configurez votre profil**
• Cliquez sur Profil organisation dans le menu
• Entrez votre secteur, CA annuel, budget disponible
• Sauvegardez

**Étape 2: Analysez vos risques**
• Allez dans Analyse de risques
• Découvrez votre exposition financière (calculée selon VOTRE CA)
• Identifiez les référentiels applicables à votre secteur

**Étape 3: Obtenez votre plan d'action**
• Consultez Recommandations
• Votre stratégie optimale sera automatiquement recommandée
• Voyez les actions prioritaires adaptées à votre budget

**Bonus:** Explorez Calendrier et Investissement pour les détails!
""")

st.markdown("<br>", unsafe_allow_html=True)

# ALERTES
st.subheader("🚨 Alertes prioritaires")

col1, col2 = st.columns([2, 1])

with col1:
    if score_conformite < 75:
        st.error(f"""
**🔴 URGENT: Conformité Loi 25 requise**

Exposition: {penalite_loi25/1000000:.1f}M$ • Probabilité: {int(probabilite*100)}%

Actions immédiates requises dans les 30 prochains jours.
""")
    
    if budget_disponible < 100000:
        st.warning("**⚠️ Budget limité détecté** - Votre budget de conformité pourrait être insuffisant pour une couverture complète.")

with col2:
    st.info("**💡 Actions rapides:** Configurer profil • Voir recommandations • Télécharger rapport")

st.markdown("<br>", unsafe_allow_html=True)

# GRAPHIQUES
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Exposition par réglementation")
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=['Loi 25', 'RGPD', 'PCI DSS'],
        y=[penalite_loi25/1000000, penalite_rgpd/1000000, 1.2],
        marker_color=['#EF4444', '#F59E0B', '#F59E0B'],
        text=[f"{penalite_loi25/1000000:.1f}M$", f"{penalite_rgpd/1000000:.1f}M$", "1.2M$"],
        textposition='outside'
    ))
    
    fig.update_layout(
        height=300,
        yaxis_title="Exposition (M$)",
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=20, b=40, l=40, r=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.caption("💡 Loi 25 = priorité absolue (OBLIGATOIRE au Québec)")

with col2:
    st.subheader("🎯 Progression de conformité")
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=score_conformite,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Score actuel"},
        delta={'reference': 100, 'increasing': {'color': "green"}},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "#2563EB"},
            'steps': [
                {'range': [0, 50], 'color': "#FEE2E2"},
                {'range': [50, 75], 'color': "#FEF3C7"},
                {'range': [75, 100], 'color': "#D1FAE5"}
            ],
            'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 95}
        }
    ))
    
    fig.update_layout(height=300, margin=dict(t=40, b=20, l=20, r=20))
    st.plotly_chart(fig, use_container_width=True)
    st.caption(f"💡 {100-score_conformite}% restant pour conformité complète")

st.markdown("<br>", unsafe_allow_html=True)

# TIMELINE
st.subheader("📅 Timeline de mise en conformité")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("**Phase 1: Fondations**\n\n0-6 mois\n\n• Politique Loi 25\n• MFA et chiffrement\n• Formation employés\n\nBudget: 105k$")

with col2:
    st.info("**Phase 2: Renforcement**\n\n6-14 mois\n\n• SIEM et monitoring\n• Audits réguliers\n• Processus matures\n\nBudget: 120k$")

with col3:
    st.info("**Phase 3: Optimisation**\n\n14-18 mois\n\n• Certification ISO\n• Tests avancés\n• Automatisation\n\nBudget: 75k$")

st.caption("💡 Consultez Calendrier pour la timeline détaillée")
st.markdown("<br>", unsafe_allow_html=True)

# ACTIONS RAPIDES AVEC NAVIGATION DIRECTE
st.subheader("⚡ Actions rapides disponibles")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📋 Configurer profil", use_container_width=True):
        st.switch_page("pages/2_Profil_organisation.py")

with col2:
    if st.button("⚠️ Voir les risques", use_container_width=True):
        st.switch_page("pages/4_Analyse_risques.py")

with col3:
    if st.button("💡 Plan d'action", use_container_width=True):
        st.switch_page("pages/5_Recommandations.py")

with col4:
    if st.button("📤 Exporter rapport", use_container_width=True):
        st.switch_page("pages/9_Synthese_executive.py")

st.markdown("<br>", unsafe_allow_html=True)

# RÉSUMÉ EXÉCUTIF
st.subheader("📄 Résumé exécutif")

st.success(f"""
### Situation actuelle de {profil.get('nom')}

**🎯 Score de conformité:** {score_conformite}% ({maturite})

**💰 Exposition financière:** {total_exposition/1000000:.1f}M$ de risques potentiels

**📊 Recommandation:** Approche {"minimale" if budget_disponible < 100000 else "progressive" if budget_disponible < 400000 else "accélérée"}

**⏱️ Délai:** 18-24 mois pour conformité complète

**💵 Investissement:** {budget_disponible/1000:.0f}k$ disponibles ({"suffisant" if budget_disponible >= 200000 else "limité - budget additionnel requis"})

**📈 ROI:** {roi:.0f}:1 - Protection de {total_exposition/1000000:.1f}M$ pour {budget_disponible/1000:.0f}k$ investis

**🚀 Prochaine étape:** Consulter les Recommandations pour le plan d'action détaillé
""")

st.divider()

# Footer
st.caption("""
💡 **Conseil:** Configurez votre profil dans Profil organisation pour voir vos données réelles.

📊 Ce tableau de bord se met à jour automatiquement selon votre profil.

**Comment le score de conformité est calculé:**
• Initial (ad-hoc): 25% • Géré (processus de base): 55% • Défini (processus documentés): 75% • Optimisé (amélioration continue): 95%
""")
