import streamlit as st

st.set_page_config(page_title="Profil organisation", page_icon="🏢", layout="wide")

# Initialiser session state
if 'profil' not in st.session_state:
    st.session_state.profil = {
        'nom': 'TechnoQuébec Inc.',
        'secteur': 'finance',
        'taille': 'medium',
        'ca': '10M$ - 50M$',
        'ca_annuel': 30000000,  # Pour calcul pénalités
        'budget': 'medium',
        'maturite': 'managed',
        'infrastructure': 'hybrid',
        'serveurs': 12,
        'instances': 45,
        'endpoints': 234
    }

st.title("🏢 Profil de l'organisation")
st.caption("Configurez les informations de votre organisation pour des recommandations personnalisées")

st.divider()

# Affichage des cartes résumé
col1, col2, col3 = st.columns(3)

with col1:
    st.info(f"**🏢 Secteur d'activité**")
    secteur_labels = {
        'health': 'Santé',
        'finance': 'Services financiers',
        'public': 'Secteur public',
        'tech': 'Technologies',
        'retail': 'Commerce',
        'other': 'Autre'
    }
    current_secteur = st.session_state.profil.get('secteur', 'finance')
    st.metric("", secteur_labels.get(current_secteur, 'Non défini'))

with col2:
    st.success(f"**💰 Chiffre d'affaires**")
    st.metric("", st.session_state.profil.get('ca', 'Non défini'))

with col3:
    st.warning(f"**📈 Niveau de maturité**")
    maturite_labels = {
        'initial': 'Niveau 1 - Initial',
        'managed': 'Niveau 2 - Géré',
        'defined': 'Niveau 3 - Défini',
        'optimized': 'Niveau 4 - Optimisé'
    }
    current_maturite = st.session_state.profil.get('maturite', 'managed')
    st.metric("", maturite_labels.get(current_maturite, 'Non défini'))

st.markdown("<br>", unsafe_allow_html=True)

# Formulaire
st.subheader("Informations générales")

col1, col2 = st.columns(2)

with col1:
    nom_org = st.text_input(
        "Nom de l'organisation",
        value=st.session_state.profil.get('nom', ''),
        help="Nom légal de votre organisation"
    )
    
    secteur = st.selectbox(
        "Secteur d'activité",
        options=['health', 'finance', 'public', 'tech', 'retail', 'other'],
        index=['health', 'finance', 'public', 'tech', 'retail', 'other'].index(st.session_state.profil.get('secteur', 'finance')),
        format_func=lambda x: {
            'health': '🏥 Santé',
            'finance': '💰 Services financiers',
            'public': '🏛️ Secteur public',
            'tech': '💻 Technologies',
            'retail': '🛒 Commerce',
            'other': '📊 Autre'
        }[x]
    )
    
    taille = st.selectbox(
        "Taille de l'organisation (employés)",
        options=['micro', 'small', 'medium', 'large'],
        index=['micro', 'small', 'medium', 'large'].index(st.session_state.profil.get('taille', 'medium')),
        format_func=lambda x: {
            'micro': '👤 Micro (1-10)',
            'small': '👥 Petite (11-49)',
            'medium': '👨‍👩‍👧‍👦 Moyenne (50-199)',
            'large': '🏢 Grande (200+)'
        }[x]
    )

with col2:
    ca = st.selectbox(
        "Chiffre d'affaires annuel",
        options=['< 1M$', '1M$ - 10M$', '10M$ - 50M$', '50M$ - 100M$', '> 100M$'],
        index=['< 1M$', '1M$ - 10M$', '10M$ - 50M$', '50M$ - 100M$', '> 100M$'].index(
            st.session_state.profil.get('ca', '10M$ - 50M$')
        )
    )
    
    # CA numérique pour calculs
    ca_mapping = {
        '< 1M$': 500000,
        '1M$ - 10M$': 5000000,
        '10M$ - 50M$': 30000000,
        '50M$ - 100M$': 75000000,
        '> 100M$': 150000000
    }
    ca_annuel = ca_mapping[ca]
    
    budget = st.selectbox(
        "Budget disponible pour la conformité",
        options=['low', 'medium', 'high'],
        index=['low', 'medium', 'high'].index(st.session_state.profil.get('budget', 'medium')),
        format_func=lambda x: {
            'low': '💰 Limité (< 50k$)',
            'medium': '💰💰 Moyen (50k$ - 200k$)',
            'high': '💰💰💰 Élevé (> 200k$)'
        }[x]
    )
    
    maturite = st.selectbox(
        "Niveau de maturité actuel",
        options=['initial', 'managed', 'defined', 'optimized'],
        index=['initial', 'managed', 'defined', 'optimized'].index(st.session_state.profil.get('maturite', 'managed')),
        format_func=lambda x: {
            'initial': '🌱 Niveau 1 - Initial',
            'managed': '📊 Niveau 2 - Géré',
            'defined': '📈 Niveau 3 - Défini',
            'optimized': '🏆 Niveau 4 - Optimisé'
        }[x]
    )

st.markdown("<br>", unsafe_allow_html=True)

# Infrastructure
st.subheader("🖥️ Infrastructure technologique")

type_infra = st.selectbox(
    "Type d'infrastructure",
    options=['onprem', 'cloud', 'hybrid'],
    index=['onprem', 'cloud', 'hybrid'].index(st.session_state.profil.get('infrastructure', 'hybrid')),
    format_func=lambda x: {
        'onprem': 'Sur site (On-premise)',
        'cloud': 'Cloud public',
        'hybrid': 'Hybride (mix)'
    }[x]
)

col1, col2, col3 = st.columns(3)

with col1:
    serveurs = st.number_input(
        "Serveurs physiques",
        min_value=0,
        value=st.session_state.profil.get('serveurs', 12),
        step=1
    )

with col2:
    instances = st.number_input(
        "Instances cloud",
        min_value=0,
        value=st.session_state.profil.get('instances', 45),
        step=1
    )

with col3:
    endpoints = st.number_input(
        "Points de terminaison",
        min_value=0,
        value=st.session_state.profil.get('endpoints', 234),
        step=1
    )

st.markdown("<br><br>", unsafe_allow_html=True)

# Boutons
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("🔄 Réinitialiser", use_container_width=True):
        # Reset aux valeurs par défaut
        st.session_state.profil = {
            'nom': 'TechnoQuébec Inc.',
            'secteur': 'finance',
            'taille': 'medium',
            'ca': '10M$ - 50M$',
            'ca_annuel': 30000000,
            'budget': 'medium',
            'maturite': 'managed',
            'infrastructure': 'hybrid',
            'serveurs': 12,
            'instances': 45,
            'endpoints': 234
        }
        st.rerun()

with col3:
    if st.button("💾 Enregistrer le profil", type="primary", use_container_width=True):
        # Sauvegarder dans session state
        st.session_state.profil = {
            'nom': nom_org,
            'secteur': secteur,
            'taille': taille,
            'ca': ca,
            'ca_annuel': ca_annuel,
            'budget': budget,
            'maturite': maturite,
            'infrastructure': type_infra,
            'serveurs': serveurs,
            'instances': instances,
            'endpoints': endpoints
        }
        
        st.success("✅ Profil enregistré avec succès!")
        st.balloons()
        
        st.info("🎯 **Les autres pages vont maintenant s'adapter à votre profil!**\n\nAllez voir les pages **Analyse de risques** et **Recommandations** pour voir les changements.")

st.markdown("<br>", unsafe_allow_html=True)

# Afficher le profil actuel (debug)
with st.expander("🔍 Voir le profil actuel (debug)"):
    st.json(st.session_state.profil)
