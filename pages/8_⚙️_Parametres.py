import streamlit as st

st.set_page_config(page_title="Paramètres", page_icon="⚙️", layout="wide")

st.markdown("""
<div class="page-header">
    <h1>Paramètres</h1>
    <p>Gérez les paramètres de votre compte et de l'application</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🌐 Général", "🔔 Notifications", "🔒 Sécurité", "👥 Équipe"])

with tab1:
    st.markdown("## Préférences générales")
    
    col1, col2 = st.columns(2)
    
    with col1:
        langue = st.selectbox(
            "Langue de l'interface",
            ["Français", "English"],
            index=0
        )
        
        fuseau = st.selectbox(
            "Fuseau horaire",
            ["America/Montreal (EST)", "America/Toronto (EST)", "America/Vancouver (PST)"],
            index=0
        )
        
        format_date = st.selectbox(
            "Format de date",
            ["JJ-MM-AAAA", "MM-JJ-AAAA", "AAAA-MM-JJ"],
            index=0
        )
    
    with col2:
        st.markdown("### Préférences d'affichage")
        
        theme = st.radio(
            "Thème de l'application",
            ["🌞 Clair", "🌙 Sombre", "🌓 Automatique"],
            index=0
        )
        
        densite = st.radio(
            "Densité d'affichage",
            ["Compact", "Normal", "Spacieux"],
            index=1
        )

    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("Enregistrer", type="primary", use_container_width=True):
            st.success("✅ Paramètres enregistrés!")

with tab2:
    st.markdown("## Notifications")
    
    st.markdown("### Notifications par email")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.checkbox("Alertes de sécurité critiques", value=True)
        st.checkbox("Mises à jour de conformité", value=True)
        st.checkbox("Échéances approchantes", value=True)
        st.checkbox("Rapport hebdomadaire", value=False)
    
    with col2:
        st.checkbox("Nouvelles fonctionnalités", value=False)
        st.checkbox("Newsletters mensuelles", value=False)
        st.checkbox("Invitations à des webinaires", value=False)
        st.checkbox("Enquêtes de satisfaction", value=False)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### Fréquence des notifications")
    
    frequence = st.radio(
        "Fréquence des emails récapitulatifs",
        ["Temps réel", "Quotidien", "Hebdomadaire", "Mensuel"],
        index=2
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("Enregistrer notifications", type="primary", use_container_width=True):
            st.success("✅ Préférences de notification mises à jour!")

with tab3:
    st.markdown("## Sécurité et confidentialité")
    
    st.markdown("### Authentification")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Authentification multi-facteurs (MFA)**")
        mfa_enabled = st.toggle("Activer le MFA", value=False)
        
        if mfa_enabled:
            st.info("🔐 Le MFA ajoute une couche de sécurité supplémentaire à votre compte.")
            if st.button("Configurer le MFA"):
                st.success("✅ Vérifiez votre email pour compléter la configuration MFA")
    
    with col2:
        st.markdown("**Gestion du mot de passe**")
        if st.button("Changer le mot de passe", use_container_width=True):
            st.info("📧 Un lien de réinitialisation a été envoyé à votre email")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("**Sessions actives**")
        st.caption("Vous êtes connecté sur 2 appareils")
        if st.button("Déconnecter tous les appareils", use_container_width=True):
            st.warning("⚠️ Vous serez déconnecté de tous les appareils")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### Confidentialité des données")
    
    st.checkbox("Permettre l'analyse anonyme d'utilisation", value=True)
    st.checkbox("Partager les rapports de conformité avec l'équipe", value=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### Exportation et suppression des données")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📥 Exporter mes données", use_container_width=True):
            st.info("📧 Un fichier d'export sera envoyé à votre email")
    
    with col2:
        if st.button("🗑️ Supprimer mon compte", use_container_width=True):
            st.error("⚠️ Cette action est irréversible!")
    
    with col3:
        if st.button("🔄 Réinitialiser l'app", use_container_width=True):
            st.warning("⚠️ Toutes les données seront effacées")

with tab4:
    st.markdown("## Gestion de l'équipe")
    
    st.markdown("### Membres actuels")
    
    membres = [
        {"nom": "Jean Tremblay", "email": "jean.tremblay@entreprise.ca", "role": "Administrateur", "statut": "Actif"},
        {"nom": "Marie Dubois", "email": "marie.dubois@entreprise.ca", "role": "Éditeur", "statut": "Actif"},
        {"nom": "Pierre Lavoie", "email": "pierre.lavoie@entreprise.ca", "role": "Lecteur", "statut": "Invité"}
    ]
    
    for membre in membres:
        st.markdown(f"""
        <div class="metric-card" style="margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; gap: 1.5rem; align-items: center; flex: 1;">
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 1.5rem; font-weight: 700;">
                        {membre['nom'][0]}
                    </div>
                    <div>
                        <div style="font-weight: 600; font-size: 1.1rem;">{membre['nom']}</div>
                        <div style="color: #6B7280; font-size: 0.9rem;">{membre['email']}</div>
                    </div>
                </div>
                <div style="display: flex; gap: 1rem; align-items: center;">
                    <span style="background: #DBEAFE; color: #1E40AF; padding: 0.4rem 1rem; border-radius: 1rem; font-size: 0.9rem; font-weight: 600;">{membre['role']}</span>
                    <span style="background: #DCFCE7; color: #065F46; padding: 0.4rem 1rem; border-radius: 1rem; font-size: 0.9rem; font-weight: 600;">{membre['statut']}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### Inviter un nouveau membre")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        email_invite = st.text_input("Email du membre", placeholder="utilisateur@entreprise.ca")
    
    with col2:
        role_invite = st.selectbox("Rôle", ["Lecteur", "Éditeur", "Administrateur"])
    
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("📧 Envoyer l'invitation", type="primary", use_container_width=True):
            if email_invite:
                st.success(f"✅ Invitation envoyée à {email_invite}")
            else:
                st.error("⚠️ Veuillez entrer un email")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### Permissions par rôle")
    
    permissions = {
        "Lecteur": ["Voir les rapports", "Exporter les données"],
        "Éditeur": ["Voir les rapports", "Exporter les données", "Modifier les données", "Créer des rapports"],
        "Administrateur": ["Voir les rapports", "Exporter les données", "Modifier les données", "Créer des rapports", "Gérer l'équipe", "Modifier les paramètres"]
    }
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 📖 Lecteur")
        for perm in permissions["Lecteur"]:
            st.caption(f"✓ {perm}")
    
    with col2:
        st.markdown("#### ✏️ Éditeur")
        for perm in permissions["Éditeur"]:
            st.caption(f"✓ {perm}")
    
    with col3:
        st.markdown("#### 👑 Administrateur")
        for perm in permissions["Administrateur"]:
            st.caption(f"✓ {perm}")
