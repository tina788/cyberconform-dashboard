import streamlit as st

st.set_page_config(page_title="Profil Organisation", page_icon="🏢", layout="wide")

# Initialiser profil
if 'profil' not in st.session_state:
    st.session_state.profil = {
        'nom': 'Votre organisation',
        'secteur': 'finance',
        'taille': 'medium',
        'ca': '10M$ - 50M$',
        'ca_annuel': 30000000,
        'budget': 'medium',
        'maturite': 'managed',
        'infrastructure': 'cloud_hybride'
    }

st.title("🏢 Profil de votre organisation")
st.caption("Configurez les informations de base pour personnaliser toutes les analyses")

# Message d'aide
st.info("""
💡 **Pourquoi configurer votre profil?**

Toutes les analyses, calculs de pénalités, recommandations et budgets sont adaptés selon VOS données.
Plus votre profil est précis, plus les recommandations seront pertinentes.

⏱️ **Temps estimé:** 2-3 minutes
""")

st.divider()

# Afficher profil actuel si configuré
if st.session_state.profil.get('nom') != 'Votre organisation':
    with st.expander("📋 Voir le profil actuel", expanded=False):
        st.success(f"""
        **Nom:** {st.session_state.profil.get('nom')}  
        **Secteur:** {st.session_state.profil.get('secteur')}  
        **Taille:** {st.session_state.profil.get('taille')}  
        **CA:** {st.session_state.profil.get('ca')}  
        **Budget conformité:** {st.session_state.profil.get('budget')}  
        **Maturité:** {st.session_state.profil.get('maturite')}
        """)
        
        if st.button("🔄 Réinitialiser le profil"):
            st.session_state.profil = {
                'nom': 'Votre organisation',
                'secteur': 'finance',
                'taille': 'medium',
                'ca': '10M$ - 50M$',
                'ca_annuel': 30000000,
                'budget': 'medium',
                'maturite': 'managed',
                'infrastructure': 'cloud_hybride'
            }
            st.rerun()

st.markdown("### 📝 Informations de base")

col1, col2 = st.columns(2)

with col1:
    nom = st.text_input(
        "Nom de l'organisation *",
        value=st.session_state.profil.get('nom', ''),
        help="Le nom de votre entreprise ou organisation",
        placeholder="ex: Acme Corporation"
    )
    
    if nom and nom != st.session_state.profil.get('nom'):
        if len(nom) < 2:
            st.warning("⚠️ Le nom doit contenir au moins 2 caractères")
        else:
            st.success("✅ Nom valide")

with col2:
    secteur = st.selectbox(
        "Secteur d'activité *",
        options=['finance', 'health', 'tech', 'retail', 'public', 'autre'],
        format_func=lambda x: {
            'finance': '🏦 Finance et services financiers',
            'health': '🏥 Santé',
            'tech': '💻 Technologie et SaaS',
            'retail': '🛒 Commerce et retail',
            'public': '🏛️ Secteur public',
            'autre': '🏢 Autre'
        }[x],
        index=['finance', 'health', 'tech', 'retail', 'public', 'autre'].index(
            st.session_state.profil.get('secteur', 'finance')
        ),
        help="Votre secteur d'activité détermine les référentiels applicables"
    )
    
    # Aide contextuelle par secteur
    secteur_info = {
        'finance': "📋 Référentiels: OSFI B-13, PCI DSS, Loi 25",
        'health': "📋 Référentiels: LPRPSP, HIPAA, Loi 25",
        'tech': "📋 Référentiels: SOC 2, ISO 27001, Loi 25",
        'retail': "📋 Référentiels: PCI DSS, Loi 25",
        'public': "📋 Référentiels: NIST CSF, Loi 25"
    }
    if secteur in secteur_info:
        st.caption(secteur_info[secteur])

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    taille = st.selectbox(
        "Taille de l'organisation *",
        options=['micro', 'small', 'medium', 'large'],
        format_func=lambda x: {
            'micro': '👤 Micro (1-10 employés)',
            'small': '👥 Petite (11-50 employés)',
            'medium': '👨‍👩‍👧‍👦 Moyenne (51-250 employés)',
            'large': '🏢 Grande (250+ employés)'
        }[x],
        index=['micro', 'small', 'medium', 'large'].index(
            st.session_state.profil.get('taille', 'medium')
        ),
        help="Le nombre d'employés influence les coûts de mise en conformité"
    )

with col2:
    ca = st.selectbox(
        "Chiffre d'affaires annuel *",
        options=['< 1M$', '1M$ - 10M$', '10M$ - 50M$', '50M$ - 100M$', '> 100M$'],
        index=['< 1M$', '1M$ - 10M$', '10M$ - 50M$', '50M$ - 100M$', '> 100M$'].index(
            st.session_state.profil.get('ca', '10M$ - 50M$')
        ),
        help="Utilisé pour calculer les pénalités (Loi 25 = max(25M$, 4% CA))"
    )
    
    # Calculer CA numérique
    ca_map = {
        '< 1M$': 500000,
        '1M$ - 10M$': 5000000,
        '10M$ - 50M$': 30000000,
        '50M$ - 100M$': 75000000,
        '> 100M$': 150000000
    }
    ca_annuel = ca_map.get(ca, 30000000)
    
    # Preview pénalité
    penalite_loi25 = max(25000000, ca_annuel * 0.04)
    st.caption(f"💡 Pénalité Loi 25 calculée: {penalite_loi25/1000000:.1f}M$")

st.markdown("### 💰 Budget et maturité")

col1, col2 = st.columns(2)

with col1:
    budget = st.selectbox(
        "Budget de conformité disponible *",
        options=['low', 'medium', 'high'],
        format_func=lambda x: {
            'low': '💰 Limité (< 50k$)',
            'medium': '💰💰 Moyen (50k$ - 200k$)',
            'high': '💰💰💰 Élevé (> 200k$)'
        }[x],
        index=['low', 'medium', 'high'].index(
            st.session_state.profil.get('budget', 'medium')
        ),
        help="Budget disponible pour le projet de mise en conformité"
    )
    
    # Preview stratégie
    budget_montants = {'low': 50000, 'medium': 200000, 'high': 500000}
    strategie_suggeree = {
        'low': "Approche minimale recommandée",
        'medium': "Approche progressive recommandée",
        'high': "Approche accélérée possible"
    }
    st.caption(f"💡 {strategie_suggeree[budget]} ({budget_montants[budget]/1000:.0f}k$)")

with col2:
    maturite = st.selectbox(
        "Niveau de maturité cybersécurité *",
        options=['initial', 'managed', 'defined', 'optimized'],
        format_func=lambda x: {
            'initial': '🔴 Initial (ad-hoc, réactif)',
            'managed': '🟡 Géré (processus de base)',
            'defined': '🟢 Défini (processus documentés)',
            'optimized': '🔵 Optimisé (amélioration continue)'
        }[x],
        index=['initial', 'managed', 'defined', 'optimized'].index(
            st.session_state.profil.get('maturite', 'managed')
        ),
        help="Votre niveau actuel de maturité en cybersécurité"
    )
    
    # Preview probabilité
    probabilites = {'initial': 85, 'managed': 65, 'defined': 40, 'optimized': 15}
    st.caption(f"💡 Probabilité d'incident: {probabilites[maturite]}%")

# Tooltip aide maturité
with st.expander("❓ Comment évaluer ma maturité?"):
    st.markdown("""
    **🔴 Initial (ad-hoc):**
    - Pas de processus formels
    - Réaction aux incidents uniquement
    - Pas de responsable sécurité dédié
    
    **🟡 Géré (processus de base):**
    - Quelques politiques en place
    - Sauvegardes régulières
    - Antivirus installé
    - Formation occasionnelle
    
    **🟢 Défini (processus documentés):**
    - Politiques écrites et suivies
    - Audits réguliers
    - Équipe sécurité dédiée
    - Plan de réponse aux incidents
    
    **🔵 Optimisé (amélioration continue):**
    - Processus matures et automatisés
    - Monitoring 24/7
    - Tests réguliers (pentest)
    - Certifications obtenues (ISO 27001)
    """)

st.markdown("### ☁️ Infrastructure (optionnel)")

infrastructure = st.selectbox(
    "Type d'infrastructure",
    options=['on_premise', 'cloud_public', 'cloud_hybride'],
    format_func=lambda x: {
        'on_premise': '🏢 Sur site (serveurs internes)',
        'cloud_public': '☁️ Cloud public (AWS, Azure, GCP)',
        'cloud_hybride': '🔄 Hybride (mix sur site + cloud)'
    }[x],
    index=['on_premise', 'cloud_public', 'cloud_hybride'].index(
        st.session_state.profil.get('infrastructure', 'cloud_hybride')
    )
)

st.markdown("<br>", unsafe_allow_html=True)

# Boutons d'action
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("💾 Enregistrer le profil", type="primary", use_container_width=True):
        # Validation
        if not nom or nom == 'Votre organisation':
            st.error("❌ Veuillez entrer le nom de votre organisation")
        elif len(nom) < 2:
            st.error("❌ Le nom doit contenir au moins 2 caractères")
        else:
            # Sauvegarder
            st.session_state.profil = {
                'nom': nom,
                'secteur': secteur,
                'taille': taille,
                'ca': ca,
                'ca_annuel': ca_annuel,
                'budget': budget,
                'maturite': maturite,
                'infrastructure': infrastructure
            }
            
            st.success("✅ Profil enregistré avec succès!")
            st.balloons()
            
            # Preview de l'impact
            st.info(f"""
            **📊 Votre profil a été enregistré. Impact:**
            
            • **Analyse de risques:** Pénalités calculées selon CA de {ca_annuel/1000000:.0f}M$
            • **Recommandations:** Stratégie adaptée à budget {budget}
            • **Calendrier:** Timeline personnalisée
            • **Investissement:** Coûts ajustés à taille {taille}
            
            👉 Consultez maintenant **⚠️ Analyse de risques** pour voir vos données!
            """)

with col2:
    if st.button("🔄 Réinitialiser", use_container_width=True):
        st.session_state.profil = {
            'nom': 'Votre organisation',
            'secteur': 'finance',
            'taille': 'medium',
            'ca': '10M$ - 50M$',
            'ca_annuel': 30000000,
            'budget': 'medium',
            'maturite': 'managed',
            'infrastructure': 'cloud_hybride'
        }
        st.rerun()

with col3:
    if st.button("❓ Aide", use_container_width=True):
        st.info("Besoin d'aide? Contactez votre équipe IT")

st.markdown("<br>", unsafe_allow_html=True)

# Résumé visuel si profil configuré
if st.session_state.profil.get('nom') != 'Votre organisation':
    st.markdown("### 📊 Résumé de votre profil")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Organisation",
            st.session_state.profil.get('nom')[:20] + "..." if len(st.session_state.profil.get('nom', '')) > 20 else st.session_state.profil.get('nom'),
            delta=secteur.upper()
        )
    
    with col2:
        st.metric(
            "Exposition Loi 25",
            f"{penalite_loi25/1000000:.1f}M$",
            delta=f"4% de {ca_annuel/1000000:.0f}M$ CA"
        )
    
    with col3:
        st.metric(
            "Budget disponible",
            f"{budget_montants[budget]/1000:.0f}k$",
            delta=budget.upper()
        )
    
    with col4:
        st.metric(
            "Probabilité incident",
            f"{probabilites[maturite]}%",
            delta=maturite.upper(),
            delta_color="inverse"
        )

st.divider()

st.caption("""
💡 **Conseil:** Mettez à jour votre profil régulièrement pour maintenir les analyses à jour.

🔒 **Confidentialité:** Vos données restent dans votre session et ne sont pas envoyées à des serveurs externes.
""")
