import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Calendrier", page_icon="📅", layout="wide")

st.title("📅 Calendrier d'implémentation")
st.caption("Feuille de route détaillée sur 18 mois (approche progressive)")

col1, col2 = st.columns([3, 1])
with col2:
    st.button("📤 Exporter le calendrier", use_container_width=True)

st.divider()

# Métriques du projet
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📅 Durée totale", "18 mois")

with col2:
    st.metric("💰 Budget total", "600k$")

with col3:
    st.metric("👥 Équipes impliquées", "6")

with col4:
    st.metric("🎯 Jalons majeurs", "12")

st.markdown("<br>", unsafe_allow_html=True)

# Référentiels à implémenter
st.subheader("Référentiels à implémenter")

tab1, tab2, tab3, tab4 = st.tabs([
    "📋 Loi 25 (Québec)", 
    "🔒 ISO 27001:2022", 
    "🌐 RGPD",
    "💳 PCI DSS"
])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Loi 25 (Québec)")
        st.caption("Loi modernisant des dispositions législatives en matière de protection des RP")
        
        st.markdown("**Statut:** 🟡 En cours")
        st.markdown("**Échéance:** Septembre 2024 (déjà en vigueur)")
        st.markdown("**Priorité:** 🔴 Obligatoire • Critique")
    
    with col2:
        st.metric("Progression", "65%")
        st.progress(0.65)
    
    st.markdown("**Exigences principales:**")
    st.markdown("""
    - Désignation d'un responsable de la protection des RP
    - Évaluation des facteurs relatifs à la vie privée (ÉFVP)
    - Registre des incidents de confidentialité
    - Politiques et pratiques de gouvernance documentées
    - Notification des incidents (72h)
    - Formulaires de consentement conformes
    """)

with tab2:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### ISO 27001:2022")
        st.caption("Norme internationale pour les systèmes de management de la sécurité")
        
        st.markdown("**Statut:** 🔵 Planifié")
        st.markdown("**Échéance:** T4 2026")
        st.markdown("**Priorité:** 🟡 Recommandé fortement • Haute")
    
    with col2:
        st.metric("Progression", "35%")
        st.progress(0.35)
    
    st.markdown("**Exigences principales:**")
    st.markdown("""
    - Système de management de la sécurité (SMSI)
    - Déclaration d'applicabilité (SoA)
    - Audits internes et revues de direction
    - Analyse de risques formelle
    - 93 contrôles de sécurité (Annexe A)
    - Documentation complète du SMSI
    """)

with tab3:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### RGPD (si applicable)")
        st.caption("Règlement Général sur la Protection des Données (UE)")
        
        st.markdown("**Statut:** 🟢 Partiellement conforme")
        st.markdown("**Échéance:** En vigueur")
        st.markdown("**Priorité:** 🟡 Obligatoire si clients UE • Haute")
    
    with col2:
        st.metric("Progression", "55%")
        st.progress(0.55)
    
    st.markdown("**Exigences principales:**")
    st.markdown("""
    - Base légale pour le traitement des données
    - Analyse d'impact sur la vie privée (AIPD)
    - Délégué à la Protection des Données (DPO) si requis
    - Registre des activités de traitement
    - Droit à l'effacement et à la portabilité
    - Notification des violations (72h)
    """)

with tab4:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### PCI DSS 4.0")
        st.caption("Payment Card Industry Data Security Standard")
        
        st.markdown("**Statut:** ⚪ Non démarré")
        st.markdown("**Échéance:** T2 2027")
        st.markdown("**Priorité:** 🟡 Obligatoire si paiements • Moyenne")
    
    with col2:
        st.metric("Progression", "0%")
        st.progress(0.0)
    
    st.markdown("**Exigences principales:**")
    st.markdown("""
    - Sécuriser le réseau et les systèmes
    - Protéger les données des titulaires de carte
    - Maintenir un programme de gestion des vulnérabilités
    - Mettre en œuvre des mesures de contrôle d'accès strictes
    - Surveiller et tester régulièrement les réseaux
    - Maintenir une politique de sécurité de l'information
    """)

st.markdown("<br><br>", unsafe_allow_html=True)

# Timeline détaillée
st.subheader("Timeline détaillée par trimestre")

timeline_data = [
    {
        "trimestre": "T1 2026 (Mars-Mai)",
        "budget": "150k$",
        "phase": "Phase 1: Fondations critiques",
        "items": [
            "Sem 1-4: Gouvernance et organisation",
            "Sem 5-8: Inventaire et classification",
            "Sem 9-12: Politiques et procédures Loi 25"
        ]
    },
    {
        "trimestre": "T2 2026 (Juin-Août)",
        "budget": "125k$",
        "phase": "Phase 1 suite: Sécurité de base",
        "items": [
            "Sem 13-16: Contrôles d'accès renforcés",
            "Sem 17-20: Chiffrement et protection données"
        ]
    },
    {
        "trimestre": "T3 2026 (Sept-Nov)",
        "budget": "175k$",
        "phase": "Phase 2: Renforcement",
        "items": [
            "Sem 25-28: Gestion des risques formelle",
            "Sem 29-32: Surveillance et détection",
            "Sem 33-36: Continuité d'activité"
        ]
    },
    {
        "trimestre": "T4 2026 (Déc-Fév 2027)",
        "budget": "150k$",
        "phase": "Phase 2 suite: Certification",
        "items": [
            "Sem 37-40: Audit interne et préparation",
            "Sem 41-44: Tests et exercices",
            "Sem 45-48: Certification ISO 27001"
        ]
    }
]

for i, t in enumerate(timeline_data, 1):
    with st.expander(f"**{t['trimestre']}** - {t['budget']}", expanded=(i==1)):
        st.subheader(t['phase'])
        
        for item in t['items']:
            st.markdown(f"• {item}")
        
        # Progress bar
        progress = i / len(timeline_data)
        st.progress(progress, text=f"{int(progress * 100)}% complété")

st.markdown("<br>", unsafe_allow_html=True)

# Jalons clés
st.subheader("🎯 Jalons clés")

jalons = [
    ("Nomination du responsable conformité", "Semaine 2", "✅"),
    ("Politique de confidentialité publiée", "Semaine 6", "✅"),
    ("Inventaire des actifs complet", "Semaine 10", "🔵"),
    ("MFA déployé à 100%", "Semaine 14", "🔵"),
    ("Formation employés complétée", "Semaine 18", "⚪"),
    ("ÉFVP processus critiques", "Semaine 24", "⚪"),
    ("SIEM opérationnel", "Semaine 30", "⚪"),
    ("PCA testé et validé", "Semaine 36", "⚪"),
    ("Audit interne ISO 27001", "Semaine 40", "⚪"),
    ("Pentest externe réalisé", "Semaine 44", "⚪"),
    ("Certification ISO 27001 obtenue", "Semaine 48", "⚪"),
    ("Revue post-implémentation", "Semaine 52", "⚪")
]

for jalon, timing, statut in jalons:
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        st.markdown(f"**{jalon}**")
    with col2:
        st.caption(timing)
    with col3:
        st.markdown(statut)

st.success("✅ Consultez **Investissement** pour voir le détail des coûts par phase!")
