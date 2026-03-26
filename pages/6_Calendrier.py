import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import pandas as pd

st.set_page_config(page_title="Calendrier", page_icon="📅", layout="wide")

# Initialiser profil
if 'profil' not in st.session_state:
    st.session_state.profil = {'nom': 'Votre organisation', 'budget': 'medium', 'taille': 'medium'}

profil = st.session_state.profil
budget = profil.get('budget', 'medium')
taille = profil.get('taille', 'medium')

st.title("📅 Calendrier de mise en conformité")
st.caption("Timeline détaillée avec jalons et livrables")

col1, col2 = st.columns([3, 1])
with col2:
    if st.button("📤 Exporter Timeline PDF", use_container_width=True):
        st.info("Export PDF disponible bientôt")

st.divider()

# Dates
date_debut = datetime.now()
date_fin = date_debut + timedelta(days=540)  # 18 mois

# TIMELINE GANTT INTERACTIF
st.subheader("📊 Timeline visuelle (18 mois)")

# Données pour le Gantt
tasks = []

# Phase 1: Fondations
tasks.append(dict(Task="Phase 1: Fondations", Start=date_debut, Finish=date_debut + timedelta(days=180), Resource="Critique"))
tasks.append(dict(Task="  └ Analyse GAP", Start=date_debut, Finish=date_debut + timedelta(days=30), Resource="Deliverable"))
tasks.append(dict(Task="  └ Politique Loi 25", Start=date_debut + timedelta(days=15), Finish=date_debut + timedelta(days=45), Resource="Deliverable"))
tasks.append(dict(Task="  └ Formation employés", Start=date_debut + timedelta(days=30), Finish=date_debut + timedelta(days=60), Resource="Deliverable"))
tasks.append(dict(Task="  └ MFA + Chiffrement", Start=date_debut + timedelta(days=45), Finish=date_debut + timedelta(days=90), Resource="Deliverable"))
tasks.append(dict(Task="  └ Registre traitements", Start=date_debut + timedelta(days=60), Finish=date_debut + timedelta(days=120), Resource="Deliverable"))

# Phase 2: Renforcement
tasks.append(dict(Task="Phase 2: Renforcement", Start=date_debut + timedelta(days=180), Finish=date_debut + timedelta(days=420), Resource="Important"))
tasks.append(dict(Task="  └ SIEM", Start=date_debut + timedelta(days=180), Finish=date_debut + timedelta(days=270), Resource="Deliverable"))
tasks.append(dict(Task="  └ Audits internes", Start=date_debut + timedelta(days=210), Finish=date_debut + timedelta(days=420), Resource="Deliverable"))
tasks.append(dict(Task="  └ Plan réponse incidents", Start=date_debut + timedelta(days=240), Finish=date_debut + timedelta(days=300), Resource="Deliverable"))

# Phase 3: Optimisation
tasks.append(dict(Task="Phase 3: Optimisation", Start=date_debut + timedelta(days=420), Finish=date_debut + timedelta(days=540), Resource="Optionnel"))
tasks.append(dict(Task="  └ Préparation ISO 27001", Start=date_debut + timedelta(days=420), Finish=date_debut + timedelta(days=480), Resource="Deliverable"))
tasks.append(dict(Task="  └ Audit certification", Start=date_debut + timedelta(days=480), Finish=date_debut + timedelta(days=510), Resource="Deliverable"))
tasks.append(dict(Task="  └ Pentest", Start=date_debut + timedelta(days=500), Finish=date_debut + timedelta(days=530), Resource="Deliverable"))

df = pd.DataFrame(tasks)

# Couleurs par type
colors = {
    'Critique': '#EF4444',
    'Important': '#F59E0B', 
    'Optionnel': '#3B82F6',
    'Deliverable': '#10B981'
}

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource",
                  color_discrete_map=colors)

fig.update_yaxes(categoryorder="array", categoryarray=df["Task"].tolist()[::-1])
fig.update_layout(
    height=600,
    showlegend=True,
    xaxis_title="Période",
    yaxis_title="",
    hovermode='closest'
)

st.plotly_chart(fig, use_container_width=True)

st.caption("""
💡 **Légende:** 
🔴 Critique (Phase 1) • 🟡 Important (Phase 2) • 🔵 Optionnel (Phase 3) • 🟢 Livrables
""")

st.markdown("<br>", unsafe_allow_html=True)

# JALONS IMPORTANTS
st.subheader("🎯 Jalons importants")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(f"""
    **🏁 Mois 6**
    
    {(date_debut + timedelta(days=180)).strftime('%B %Y')}
    
    ✅ **Conformité Loi 25 atteinte**
    
    Livrables:
    • Politique confidentialité
    • Registre traitements
    • ÉFVP complétée
    • MFA activé
    • Formation complète
    """)

with col2:
    st.info(f"""
    **🏁 Mois 12**
    
    {(date_debut + timedelta(days=360)).strftime('%B %Y')}
    
    ✅ **Contrôles avancés en place**
    
    Livrables:
    • SIEM opérationnel
    • Processus matures
    • Audits réguliers
    • Plan incident actif
    """)

with col3:
    st.info(f"""
    **🏁 Mois 18**
    
    {(date_debut + timedelta(days=540)).strftime('%B %Y')}
    
    ✅ **Certification ISO 27001**
    
    Livrables:
    • Audit réussi
    • Pentest complété
    • Optimisations finales
    • Certification obtenue
    """)

st.markdown("<br>", unsafe_allow_html=True)

# DÉTAIL PAR TRIMESTRE
st.subheader("📆 Planning par trimestre")

trimestres = [
    {
        'nom': 'T1 2026 (Mois 1-3)',
        'phase': 'Phase 1: Fondations',
        'objectif': 'Démarrage et Quick Wins',
        'actions': [
            '✅ Analyse GAP complète (Semaine 1-4)',
            '✅ Politique Loi 25 rédigée et approuvée (Semaine 3-6)',
            '✅ MFA déployé sur comptes critiques (Semaine 7-10)',
            '✅ Formation sensibilisation (Semaine 5-8)',
            '✅ Début registre traitements (Semaine 9-12)'
        ],
        'budget': '105k$',
        'couleur': 'success'
    },
    {
        'nom': 'T2 2026 (Mois 4-6)',
        'phase': 'Phase 1: Fondations',
        'objectif': 'Conformité Loi 25',
        'actions': [
            '✅ Finalisation registre traitements',
            '✅ ÉFVP complétée',
            '✅ Chiffrement bases de données',
            '✅ Contrôles d\'accès renforcés',
            '🎯 Conformité Loi 25 ATTEINTE'
        ],
        'budget': '50k$',
        'couleur': 'success'
    },
    {
        'nom': 'T3 2026 (Mois 7-9)',
        'phase': 'Phase 2: Renforcement',
        'objectif': 'Outils avancés',
        'actions': [
            '🔧 Déploiement SIEM',
            '🔧 Mise en place sauvegardes sécurisées',
            '🔧 Premier audit interne',
            '🔧 Formation avancée équipe IT',
            '🔧 Documentation processus'
        ],
        'budget': '120k$',
        'couleur': 'info'
    },
    {
        'nom': 'T4 2026 (Mois 10-12)',
        'phase': 'Phase 2: Renforcement',
        'objectif': 'Processus matures',
        'actions': [
            '🔧 SIEM opérationnel 24/7',
            '🔧 Plan réponse incidents actif',
            '🔧 Audits trimestriels programmés',
            '🔧 Tests de restauration',
            '🔧 Préparation pré-certification'
        ],
        'budget': '75k$',
        'couleur': 'info'
    },
    {
        'nom': 'T1 2027 (Mois 13-15)',
        'phase': 'Phase 3: Optimisation',
        'objectif': 'Certification',
        'actions': [
            '🎯 Préparation documentation ISO 27001',
            '🎯 Audit blanc (interne)',
            '🎯 Corrections audit blanc',
            '🎯 Formation certification',
            '🎯 Lancement audit officiel'
        ],
        'budget': '60k$',
        'couleur': 'warning'
    },
    {
        'nom': 'T2 2027 (Mois 16-18)',
        'phase': 'Phase 3: Optimisation',
        'objectif': 'Finalisation',
        'actions': [
            '🎯 Audit certification ISO 27001',
            '🎯 Tests de pénétration',
            '🎯 Corrections post-audit',
            '🎯 Automatisation processus',
            '🏆 CERTIFICATION OBTENUE'
        ],
        'budget': '40k$',
        'couleur': 'warning'
    }
]

for trim in trimestres:
    with st.expander(f"**{trim['nom']}** - {trim['phase']}", expanded=False):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"**🎯 Objectif:** {trim['objectif']}")
            st.markdown("**Actions:**")
            for action in trim['actions']:
                st.markdown(f"- {action}")
        
        with col2:
            st.metric("Budget", trim['budget'])
            
            if '✅' in trim['actions'][0]:
                st.success("Phase critique")
            elif '🔧' in trim['actions'][0]:
                st.info("Phase importante")
            else:
                st.warning("Phase finale")

st.markdown("<br>", unsafe_allow_html=True)

# RESSOURCES
st.subheader("👥 Ressources requises")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Ressources internes:**")
    st.markdown("""
    - **Sponsor exécutif:** 10% temps (suivi mensuel)
    - **Responsable projet:** 50% temps (6-12 mois)
    - **Équipe IT:** 2-3 personnes, 25% temps
    - **RH/Formation:** Support ponctuel
    - **Juridique:** Review politiques (10-20h)
    """)

with col2:
    st.markdown("**Ressources externes:**")
    st.markdown("""
    - **Consultant conformité:** 3-6 mois
    - **Auditeur ISO 27001:** Ponctuel (mois 12-18)
    - **Pentest:** 1-2 semaines (mois 17)
    - **Formation externe:** Selon besoins
    - **Support technique:** Selon outils
    """)

st.markdown("<br>", unsafe_allow_html=True)

# RISQUES
st.subheader("⚠️ Risques du planning")

st.warning("""
**Risques pouvant retarder le projet:**

🔴 **Risques critiques:**
- Manque de sponsoring direction → Délai: +2-4 mois
- Budget insuffisant → Blocage possible
- Turnover équipe clé → Délai: +1-3 mois

🟡 **Risques modérés:**
- Résistance au changement → Formation additionnelle requise
- Complexité technique sous-estimée → Budget +10-20%
- Disponibilité consultants → Délai: +1-2 mois

💡 **Mitigation:** Revue mensuelle du planning, budget contingence 15%, sponsor engagé
""")

st.markdown("<br>", unsafe_allow_html=True)

# RÉSUMÉ
st.success(f"""
### ✅ Résumé du calendrier

**📅 Durée totale:** 18 mois ({date_debut.strftime('%B %Y')} → {date_fin.strftime('%B %Y')})

**🎯 Jalons clés:**
- Mois 6: Conformité Loi 25 ✅
- Mois 12: Contrôles avancés ✅
- Mois 18: Certification ISO 27001 ✅

**💰 Budget total:** 450k$ (réparti sur 18 mois)

**👥 Ressources:** 2-3 personnes internes + consultants externes

**⚠️ Points d'attention:** Sponsoring direction + budget stable + disponibilité équipe

**📊 Suivi:** Revue mensuelle recommandée avec comité de pilotage
""")

st.divider()

st.caption("""
💡 **Conseil:** Ce calendrier est indicatif et doit être adapté selon vos contraintes.

📅 **Flexibilité:** Les phases peuvent être ajustées selon votre rythme et vos priorités.
""")
