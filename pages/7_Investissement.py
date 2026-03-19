import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Investissement", page_icon="💰", layout="wide")

# Initialiser profil
if 'profil' not in st.session_state:
    st.session_state.profil = {
        'nom': 'Votre organisation',
        'budget': 'medium'
    }

profil = st.session_state.profil
budget_niveau = profil.get('budget', 'medium')

# Convertir budget en montant
def get_budget_montant(budget_niveau):
    budgets = {
        'low': 50000,
        'medium': 200000,
        'high': 500000
    }
    return budgets.get(budget_niveau, 200000)

budget_disponible = get_budget_montant(budget_niveau)

st.title("💰 Investissement requis")
st.caption(f"Plan d'investissement adapté à votre budget de **{budget_disponible/1000:.0f}k$**")

col1, col2 = st.columns([3, 1])
with col2:
    st.button("📤 Exporter en PDF", use_container_width=True)

st.divider()

# Calculer l'investissement optimal selon budget
investissement_optimal = min(budget_disponible, 300000)  # Cap à 300k pour l'exemple

# Répartition
capex = int(investissement_optimal * 0.40)
opex_initial = int(investissement_optimal * 0.60)
opex_annuel = int(investissement_optimal * 0.35)

# ROI estimé
ca_annuel = profil.get('ca_annuel', 30000000)
penalite_evitee = max(25000000, ca_annuel * 0.04)
roi_3ans = penalite_evitee + (2000000)  # Pénalités + gains opérationnels
ratio_roi = roi_3ans / investissement_optimal if investissement_optimal > 0 else 0

# Grandes cartes métriques
col1, col2 = st.columns(2)

with col1:
    st.info(f"**Investissement total adapté à votre budget**")
    st.metric(
        label="💰 Budget utilisé",
        value=f"{investissement_optimal/1000:.0f}k$",
        delta=f"sur {budget_disponible/1000:.0f}k$ disponibles"
    )
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("CapEx", f"{capex/1000:.0f}k$")
    with col_b:
        st.metric("OpEx initial", f"{opex_initial/1000:.0f}k$")
    with col_c:
        st.metric("OpEx/an", f"{opex_annuel/1000:.0f}k$")

with col2:
    st.success("**ROI estimé**")
    st.metric(
        label="📈 Retour sur investissement",
        value=f"{roi_3ans/1000000:.0f}M$",
        delta="Risques évités sur 3 ans"
    )
    
    st.metric(
        label="Ratio ROI",
        value=f"{ratio_roi:.0f}:1",
        help="Chaque dollar investi protège contre X$ de risques"
    )

# Alerte budget
if budget_disponible < 100000:
    st.warning(f"""
    ⚠️ **Budget limité ({budget_disponible/1000:.0f}k$)**
    
    Votre budget permet uniquement une conformité **partielle**. Vous pourrez:
    - ✅ Mettre en place la politique Loi 25 (essentiel)
    - ✅ Implémenter quelques contrôles de base
    - ❌ PAS de certification ISO 27001
    - ❌ Couverture incomplète des risques
    
    **Recommandation:** Planifiez un budget additionnel de {(200000-budget_disponible)/1000:.0f}k$ pour l'année suivante.
    """)

st.markdown("<br>", unsafe_allow_html=True)

# Graphiques
col1, col2 = st.columns(2)

with col1:
    st.subheader("Répartition par catégorie")
    
    # Adapter les catégories selon le budget
    if budget_disponible >= 200000:
        categories = ['Technologie', 'Conseil', 'Formation', 'Certification', 'RH']
        values = [
            investissement_optimal * 0.40,
            investissement_optimal * 0.25,
            investissement_optimal * 0.15,
            investissement_optimal * 0.10,
            investissement_optimal * 0.10
        ]
        colors_cat = ['#2563EB', '#A855F7', '#10B981', '#F59E0B', '#EF4444']
    else:
        # Budget limité: focus sur l'essentiel
        categories = ['Conseil (GAP)', 'Politiques', 'Formation base', 'Outils essentiels']
        values = [
            investissement_optimal * 0.35,
            investissement_optimal * 0.25,
            investissement_optimal * 0.20,
            investissement_optimal * 0.20
        ]
        colors_cat = ['#2563EB', '#A855F7', '#10B981', '#F59E0B']
    
    fig = go.Figure(data=[go.Pie(
        labels=categories,
        values=values,
        hole=.6,
        marker=dict(colors=colors_cat),
        textinfo='label+percent',
        textfont=dict(size=11),
        hovertemplate='<b>%{label}</b><br>%{value:$,.0f}<br>%{percent}<extra></extra>'
    )])
    
    fig.update_layout(
        height=350,
        showlegend=True,
        legend=dict(orientation="v", yanchor="middle", y=0.5),
        margin=dict(t=20, b=20, l=20, r=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Budget par phase")
    
    # Adapter les phases selon budget
    if budget_disponible >= 200000:
        phases = ['Phase 1:\nFondations', 'Phase 2:\nRenforcement', 'Phase 3:\nOptimisation']
        budgets_phases = [
            investissement_optimal * 0.40,
            investissement_optimal * 0.35,
            investissement_optimal * 0.25
        ]
    else:
        phases = ['Phase 1:\nConformité Loi 25', 'Phase 2:\nContrôles base']
        budgets_phases = [
            investissement_optimal * 0.70,
            investissement_optimal * 0.30
        ]
    
    fig = go.Figure(data=[
        go.Bar(
            x=phases,
            y=budgets_phases,
            marker=dict(color=['#2563EB', '#3B82F6', '#60A5FA'][:len(phases)]),
            text=[f"{b/1000:.0f}k$" for b in budgets_phases],
            textposition='outside',
            textfont=dict(size=14, weight='bold')
        )
    ])
    
    fig.update_layout(
        height=350,
        yaxis_title="Budget ($)",
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#F3F4F6'),
        margin=dict(t=40, b=40, l=60, r=40)
    )
    
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# Investissements détaillés selon budget
st.subheader("💻 Détail des investissements")

if budget_disponible >= 200000:
    # Budget moyen/élevé: investissements complets
    tab1, tab2, tab3 = st.tabs(["Technologies", "Services", "Formation"])
    
    with tab1:
        st.markdown("### Solutions technologiques")
        
        tech_items = [
            ("Firewall NGFW", "CapEx", 45000),
            ("Antivirus/EDR entreprise", "OpEx/an", 35000),
            ("SIEM", "OpEx/an", 50000),
            ("Solution MFA", "OpEx/an", 15000),
            ("Chiffrement bases de données", "CapEx", 25000),
            ("Sauvegarde sécurisée", "OpEx/an", 40000),
        ]
        
        budget_tech_total = 0
        for nom, type_cout, cout in tech_items:
            if budget_tech_total + cout <= investissement_optimal * 0.40:
                col1, col2, col3 = st.columns([2, 1, 1])
                with col1:
                    st.markdown(f"**{nom}**")
                with col2:
                    st.caption(type_cout)
                with col3:
                    st.metric("", f"{cout/1000:.0f}k$")
                st.divider()
                budget_tech_total += cout
            else:
                break
    
    with tab2:
        st.markdown("### Services professionnels")
        
        services = [
            ("Analyse GAP complète", "2 semaines", 25000),
            ("Analyse de risques", "4 semaines", 35000),
            ("Audit ISO 27001", "3 semaines", 40000),
            ("Tests pénétration", "1 semaine", 20000),
        ]
        
        for nom, duree, cout in services:
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                st.markdown(f"**{nom}**")
            with col2:
                st.caption(duree)
            with col3:
                st.markdown(f"**{cout/1000:.0f}k$**")
            st.divider()
    
    with tab3:
        st.markdown("### Formation et ressources")
        
        st.markdown("""
        - Formation cybersécurité employés: **35k$/an**
        - Formation Loi 25 (2 jours): **25k$**
        - Responsable conformité (6 mois): **60k$**
        """)

else:
    # Budget limité: focus essentiel
    st.warning(f"**Avec un budget de {budget_disponible/1000:.0f}k$, voici les investissements prioritaires:**")
    
    investissements_essentiels = [
        {
            'categorie': '📋 Analyse et conseil',
            'items': [
                ('Analyse GAP Loi 25', 15000, 'Identifier les écarts critiques'),
                ('Rédaction politique confidentialité', 5000, 'Document obligatoire'),
                ('Registre des traitements', 10000, 'Documentation RP'),
            ]
        },
        {
            'categorie': '🔒 Contrôles de base',
            'items': [
                ('Solution MFA', 3000, 'Authentification renforcée'),
                ('Formation sensibilisation', 5000, 'Tous les employés'),
                ('Chiffrement données', 8000, 'Protection de base'),
            ]
        }
    ]
    
    budget_utilise = 0
    
    for inv in investissements_essentiels:
        st.markdown(f"### {inv['categorie']}")
        
        for nom, cout, description in inv['items']:
            if budget_utilise + cout <= budget_disponible:
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**{nom}**")
                    st.caption(description)
                with col2:
                    st.metric("", f"{cout/1000:.0f}k$")
                
                budget_utilise += cout
                st.divider()
    
    st.info(f"**Budget utilisé:** {budget_utilise/1000:.0f}k$ / {budget_disponible/1000:.0f}k$")
    
    if budget_utilise < budget_disponible:
        st.success(f"✅ Budget restant: {(budget_disponible - budget_utilise)/1000:.0f}k$ pour actions additionnelles")

st.markdown("<br>", unsafe_allow_html=True)

# Coûts récurrents
st.warning("**💼 Coûts récurrents annuels (après implémentation)**")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Licences", f"{opex_annuel/1000:.0f}k$/an")

with col2:
    audits_annuels = min(50000, budget_disponible * 0.20)
    st.metric("Audits", f"{audits_annuels/1000:.0f}k$/an")

with col3:
    formation_annuelle = min(30000, budget_disponible * 0.15)
    st.metric("Formation", f"{formation_annuelle/1000:.0f}k$/an")

with col4:
    total_annuel = opex_annuel + audits_annuels + formation_annuelle
    st.metric("TOTAL", f"{total_annuel/1000:.0f}k$/an")

st.caption("Coûts de maintien de la conformité après implémentation initiale")

st.markdown("<br>", unsafe_allow_html=True)

# Analyse ROI
st.subheader("📊 Analyse du retour sur investissement")

col1, col2 = st.columns(2)

with col1:
    st.success("**Bénéfices attendus**")
    st.markdown(f"""
    - **Pénalités évitées**: {penalite_evitee/1000000:.0f}M$ (Très élevé)
    - **Réduction coûts incidents**: 500k$ - 2M$ (Élevé)
    - **Économie primes assurance**: 50k$/an (Moyen)
    - **Gains productivité**: Non quantifiable
    """)

with col2:
    st.info("**Résumé financier**")
    st.metric("Investissement", f"{investissement_optimal/1000:.0f}k$")
    st.metric("Risques évités", f"{roi_3ans/1000000:.0f}M$")
    st.metric("ROI sur 3 ans", f"{ratio_roi:.0f}:1")
    
    if ratio_roi >= 40:
        st.success("✅ ROI excellent!")
    elif ratio_roi >= 20:
        st.success("✅ ROI très bon")
    else:
        st.warning("⚠️ ROI acceptable")

# Message final
if budget_disponible < 100000:
    st.error(f"""
    ⚠️ **ATTENTION: Budget insuffisant**
    
    Votre budget actuel de {budget_disponible/1000:.0f}k$ permet uniquement une conformité **partielle**.
    
    **Pour une conformité complète**, un budget minimal de **200k$** est recommandé.
    
    **Options:**
    1. Augmenter le budget à 200k$ pour couvrir tous les essentiels
    2. Échelonner sur 2-3 ans (70-100k$/an)
    3. Se concentrer uniquement sur Loi 25 cette année
    """)
else:
    st.success(f"""
    ✅ **Votre budget de {budget_disponible/1000:.0f}k$ permet une mise en conformité solide!**
    
    - Protection contre {penalite_evitee/1000000:.0f}M$ de pénalités
    - ROI de {ratio_roi:.0f}:1 sur 3 ans
    - Conformité Loi 25 complète
    """ + ("- Certification ISO 27001 possible" if budget_disponible >= 300000 else ""))
