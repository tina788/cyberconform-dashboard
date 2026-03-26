import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Évaluation Maturité", page_icon="🛡️", layout="wide")

# Initialiser profil
if 'profil' not in st.session_state:
    st.session_state.profil = {
        'nom': 'Votre organisation',
        'maturite': 'managed'
    }

st.title("🛡️ Évaluation de la maturité cybersécurité")
st.caption("Comprenez votre niveau actuel et ce que vous devez améliorer")

st.divider()

# SECTION 1: EXPLICATION
st.markdown("## 📚 Qu'est-ce que la maturité cybersécurité?")

st.info("""
**Définition simple:**

La maturité cybersécurité mesure **à quel point votre organisation est structurée et organisée** 
pour protéger ses données et systèmes informatiques.

**Analogie:** C'est comme la différence entre:
- 🔴 Une maison sans alarme ni serrure (Initial)
- 🟡 Une maison avec serrures basiques (Géré)
- 🟢 Une maison avec alarme et caméras (Défini)
- 🔵 Une maison avec système de sécurité complet 24/7 (Optimisé)

**Pourquoi c'est important?**
- Plus votre maturité est élevée, moins vous avez de risques d'incident
- Les assurances et partenaires regardent votre niveau de maturité
- Ça détermine la probabilité qu'une cyberattaque réussisse
""")

st.markdown("<br>", unsafe_allow_html=True)

# SECTION 2: LES 4 NIVEAUX DÉTAILLÉS
st.markdown("## 🎯 Les 4 niveaux de maturité expliqués")

st.success("""
**Comment utiliser cette section:**

Lisez chaque niveau ci-dessous et identifiez celui qui correspond le mieux à VOTRE situation actuelle.

Soyez honnête - c'est pour VOUS aider à vous améliorer, pas pour impressionner qui que ce soit!
""")

st.markdown("<br>", unsafe_allow_html=True)

# NIVEAU 1: INITIAL
with st.expander("🔴 **NIVEAU 1: INITIAL (Ad-hoc, Réactif)** - Cliquez pour voir les détails", expanded=False):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Caractéristiques principales:
        
        **En bref:** Vous réagissez aux problèmes quand ils arrivent, sans vrai plan.
        
        **Vous êtes à ce niveau si:**
        - ❌ Pas de politiques de sécurité écrites
        - ❌ Pas de responsable sécurité désigné
        - ❌ Les employés ne sont jamais formés à la cybersécurité
        - ❌ Pas de sauvegardes régulières (ou vous ne savez pas)
        - ❌ Chacun gère sa sécurité comme il veut
        - ❌ Vous découvrez les problèmes par hasard
        
        **Exemples concrets:**
        - "On installe l'antivirus quand quelqu'un a un virus"
        - "Les mots de passe? Chacun met ce qu'il veut"
        - "On n'a jamais testé nos sauvegardes"
        - "Sécurité? C'est le problème du gars IT quand il a le temps"
        
        **Ce qui pourrait arriver:**
        - Employé clique sur phishing → Tout le réseau infecté
        - Serveur tombe en panne → Aucune sauvegarde récente
        - Ex-employé garde accès aux systèmes pendant des mois
        - Violation de données découverte 6 mois trop tard
        """)
    
    with col2:
        st.error("""
        **📊 Statistiques:**
        
        **Probabilité d'incident:** 85%
        
        **Score conformité:** 25%
        
        **Coût moyen incident:** 500k$ - 2M$
        
        **Temps de détection:** 6-12 mois
        """)
        
        st.warning("""
        **⚠️ Actions urgentes:**
        
        1. Nommer un responsable sécurité
        2. Mettre des sauvegardes automatiques
        3. Formation employés de base
        4. Politique mots de passe minimum
        """)

# NIVEAU 2: GÉRÉ
with st.expander("🟡 **NIVEAU 2: GÉRÉ (Processus de base)** - Cliquez pour voir les détails", expanded=False):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Caractéristiques principales:
        
        **En bref:** Vous avez mis quelques bases en place, mais ce n'est pas encore systématique.
        
        **Vous êtes à ce niveau si:**
        - ✅ Antivirus installé sur tous les postes
        - ✅ Sauvegardes faites régulièrement (hebdo/mensuel)
        - ✅ Quelques politiques écrites (mais pas toujours suivies)
        - ✅ Formation occasionnelle des employés
        - ✅ Quelqu'un s'occupe de la sécurité (mais pas à temps plein)
        - ⚠️ Mais tout n'est pas documenté ni testé
        
        **Exemples concrets:**
        - "On a une politique de mots de passe écrite quelque part"
        - "Les sauvegardes tournent, mais on ne les a jamais testées"
        - "On fait une formation cybersécurité tous les 2-3 ans"
        - "Le responsable IT gère la sécurité quand il a le temps"
        - "On a un antivirus, mais les mises à jour ne sont pas forcées"
        
        **Ce qui pourrait arriver:**
        - Ransomware détecté rapidement grâce à l'antivirus
        - Mais les sauvegardes ne fonctionnent pas complètement
        - Employés formés mais formation datée (phishing moderne passe)
        - Incident détecté en quelques semaines (vs 6 mois niveau 1)
        """)
    
    with col2:
        st.warning("""
        **📊 Statistiques:**
        
        **Probabilité d'incident:** 65%
        
        **Score conformité:** 55%
        
        **Coût moyen incident:** 200k$ - 800k$
        
        **Temps de détection:** 2-4 mois
        """)
        
        st.info("""
        **💡 Prochaines étapes:**
        
        1. Documenter tous les processus
        2. Tests réguliers des sauvegardes
        3. Formation annuelle obligatoire
        4. Audits de sécurité trimestriels
        5. MFA sur comptes critiques
        """)

# NIVEAU 3: DÉFINI
with st.expander("🟢 **NIVEAU 3: DÉFINI (Processus documentés)** - Cliquez pour voir les détails", expanded=False):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Caractéristiques principales:
        
        **En bref:** Vous avez des processus clairs, documentés et suivis par tous.
        
        **Vous êtes à ce niveau si:**
        - ✅ Toutes les politiques écrites, à jour et suivies
        - ✅ Équipe sécurité dédiée (au moins 1 personne à temps plein)
        - ✅ Formation cybersécurité annuelle obligatoire
        - ✅ Sauvegardes testées régulièrement (tous les trimestres)
        - ✅ Plan de réponse aux incidents documenté et testé
        - ✅ Audits internes réguliers
        - ✅ MFA activé partout
        - ✅ Logs et monitoring en place
        
        **Exemples concrets:**
        - "On a un RSSI (Responsable Sécurité) à temps plein"
        - "Tous les employés font 2h de formation cyber par an"
        - "On teste nos sauvegardes tous les 3 mois avec succès"
        - "On a un plan d'incident: tout le monde sait quoi faire"
        - "Tous les accès ont MFA (code SMS + mot de passe)"
        - "On fait des audits internes chaque trimestre"
        
        **Ce qui pourrait arriver:**
        - Tentative de phishing détectée et bloquée automatiquement
        - Incident contenu en quelques heures grâce au plan
        - Sauvegarde restaurée en < 24h si besoin
        - Audit externe: Peu de correctifs à faire
        """)
    
    with col2:
        st.success("""
        **📊 Statistiques:**
        
        **Probabilité d'incident:** 40%
        
        **Score conformité:** 75%
        
        **Coût moyen incident:** 50k$ - 200k$
        
        **Temps de détection:** Quelques jours
        """)
        
        st.info("""
        **🎯 Pour aller plus loin:**
        
        1. Certification ISO 27001
        2. SIEM 24/7
        3. Tests de pénétration annuels
        4. Automatisation processus
        5. Threat intelligence
        """)

# NIVEAU 4: OPTIMISÉ
with st.expander("🔵 **NIVEAU 4: OPTIMISÉ (Amélioration continue)** - Cliquez pour voir les détails", expanded=False):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Caractéristiques principales:
        
        **En bref:** Vous avez une machine bien huilée qui s'améliore en permanence.
        
        **Vous êtes à ce niveau si:**
        - ✅ Certification ISO 27001 obtenue et maintenue
        - ✅ SIEM avec monitoring 24/7
        - ✅ Tests de pénétration réguliers (2x/an minimum)
        - ✅ Processus d'amélioration continue documenté
        - ✅ Équipe sécurité complète et formée
        - ✅ Automatisation maximale
        - ✅ Intelligence de menaces active
        - ✅ Bug bounty program ou red team
        - ✅ Métriques de sécurité suivies et analysées
        
        **Exemples concrets:**
        - "On a ISO 27001 depuis 3 ans, re-certifié chaque année"
        - "Notre SOC (Security Operations Center) surveille 24/7"
        - "On fait des pentests tous les 6 mois + bug bounty"
        - "Chaque incident est analysé et améliore nos processus"
        - "95% de nos processus sont automatisés"
        - "On participe à des groupes de partage de menaces"
        - "Notre équipe sécu a 5 personnes + consultants"
        
        **Ce qui pourrait arriver:**
        - Attaque détectée et bloquée en temps réel (minutes)
        - Zero-day découvert et patché avant exploitation
        - Incident majeur contenu en < 1h
        - Conformité à tous les référentiels pertinents
        """)
    
    with col2:
        st.success("""
        **📊 Statistiques:**
        
        **Probabilité d'incident:** 15%
        
        **Score conformité:** 95%
        
        **Coût moyen incident:** < 50k$
        
        **Temps de détection:** Temps réel
        """)
        
        st.success("""
        **🏆 Excellence:**
        
        Vous êtes dans le top 5% des organisations!
        
        Continuez à:
        - Innover
        - Partager vos pratiques
        - Former l'industrie
        - Rester vigilant
        """)

st.markdown("<br>", unsafe_allow_html=True)

# SECTION 3: QUIZ D'AUTO-ÉVALUATION
st.markdown("## ❓ Quiz d'auto-évaluation rapide")

st.warning("""
**Instructions:**

Répondez honnêtement aux 10 questions ci-dessous.

À la fin, vous saurez exactement à quel niveau vous êtes!
""")

# Questions du quiz
questions = {
    "Q1": {
        "question": "Avez-vous une politique de sécurité écrite et à jour?",
        "reponses": {
            "Non, rien d'écrit": 1,
            "Oui, mais ancienne (> 3 ans)": 2,
            "Oui, à jour et suivie": 3,
            "Oui, avec revue annuelle et amélioration continue": 4
        }
    },
    "Q2": {
        "question": "Qui est responsable de la cybersécurité?",
        "reponses": {
            "Personne en particulier": 1,
            "Le responsable IT quand il a le temps": 2,
            "Une personne dédiée (50%+ de son temps)": 3,
            "Équipe sécurité complète": 4
        }
    },
    "Q3": {
        "question": "À quelle fréquence formez-vous vos employés à la cybersécurité?",
        "reponses": {
            "Jamais": 1,
            "Tous les 2-3 ans ou quand on y pense": 2,
            "Annuellement, obligatoire": 3,
            "Annuellement + tests réguliers (phishing simulé)": 4
        }
    },
    "Q4": {
        "question": "Vos sauvegardes:",
        "reponses": {
            "On n'en fait pas ou très rarement": 1,
            "Automatiques mais jamais testées": 2,
            "Testées tous les trimestres avec succès": 3,
            "Testées mensuellement + plan de restauration < 24h": 4
        }
    },
    "Q5": {
        "question": "Authentification multi-facteurs (MFA/2FA):",
        "reponses": {
            "Pas utilisée": 1,
            "Sur quelques comptes seulement": 2,
            "Sur tous les comptes administrateurs": 3,
            "Sur tous les comptes sans exception": 4
        }
    },
    "Q6": {
        "question": "Avez-vous un plan de réponse aux incidents?",
        "reponses": {
            "Non": 1,
            "Oui, mais jamais testé": 2,
            "Oui, testé annuellement": 3,
            "Oui, testé 2x/an avec amélioration continue": 4
        }
    },
    "Q7": {
        "question": "Monitoring et détection:",
        "reponses": {
            "On découvre les problèmes par hasard": 1,
            "Antivirus basique": 2,
            "Logs centralisés + alertes": 3,
            "SIEM avec surveillance 24/7": 4
        }
    },
    "Q8": {
        "question": "Audits de sécurité:",
        "reponses": {
            "Jamais fait": 1,
            "Occasionnellement (tous les 2-3 ans)": 2,
            "Annuellement (interne)": 3,
            "2x/an (interne + externe) + pentest": 4
        }
    },
    "Q9": {
        "question": "Gestion des accès:",
        "reponses": {
            "Pas de processus, chacun gère": 1,
            "Liste Excel des accès": 2,
            "Processus documenté + revue annuelle": 3,
            "Automatisé + revue trimestrielle + révocation immédiate": 4
        }
    },
    "Q10": {
        "question": "Certifications:",
        "reponses": {
            "Aucune": 1,
            "En cours de préparation": 2,
            "ISO 27001 ou équivalent": 3,
            "ISO 27001 + autres (SOC 2, etc.)": 4
        }
    }
}

# Interface du quiz
score_total = 0
reponses = {}

for q_id, q_data in questions.items():
    reponse = st.radio(
        f"**{q_id}.** {q_data['question']}",
        options=list(q_data['reponses'].keys()),
        index=0,
        key=q_id
    )
    reponses[q_id] = q_data['reponses'][reponse]
    score_total += q_data['reponses'][reponse]

st.markdown("<br>", unsafe_allow_html=True)

# Résultats du quiz
if st.button("📊 Voir mon résultat", type="primary", use_container_width=True):
    st.markdown("---")
    st.subheader("🎯 Votre résultat")
    
    # Calculer le niveau
    score_moyen = score_total / 10
    
    if score_moyen < 1.5:
        niveau = "INITIAL"
        couleur = "error"
        emoji = "🔴"
        conformite = 25
        probabilite = 85
    elif score_moyen < 2.5:
        niveau = "GÉRÉ"
        couleur = "warning"
        emoji = "🟡"
        conformite = 55
        probabilite = 65
    elif score_moyen < 3.5:
        niveau = "DÉFINI"
        couleur = "success"
        emoji = "🟢"
        conformite = 75
        probabilite = 40
    else:
        niveau = "OPTIMISÉ"
        couleur = "info"
        emoji = "🔵"
        conformite = 95
        probabilite = 15
    
    # Afficher le résultat
    if couleur == "error":
        st.error(f"""
        ## {emoji} Niveau: {niveau}
        
        **Score:** {score_total}/40 points
        
        **Score de conformité:** {conformite}%
        
        **Probabilité d'incident:** {probabilite}%
        """)
    elif couleur == "warning":
        st.warning(f"""
        ## {emoji} Niveau: {niveau}
        
        **Score:** {score_total}/40 points
        
        **Score de conformité:** {conformite}%
        
        **Probabilité d'incident:** {probabilite}%
        """)
    elif couleur == "success":
        st.success(f"""
        ## {emoji} Niveau: {niveau}
        
        **Score:** {score_total}/40 points
        
        **Score de conformité:** {conformite}%
        
        **Probabilité d'incident:** {probabilite}%
        """)
    else:
        st.info(f"""
        ## {emoji} Niveau: {niveau}
        
        **Score:** {score_total}/40 points
        
        **Score de conformité:** {conformite}%
        
        **Probabilité d'incident:** {probabilite}%
        """)
    
    # Recommandations personnalisées
    st.markdown("### 💡 Recommandations pour vous:")
    
    if niveau == "INITIAL":
        st.error("""
        **Actions URGENTES (30 jours):**
        
        1. 🔴 **Nommer un responsable sécurité** (même à temps partiel)
        2. 🔴 **Mettre en place sauvegardes automatiques** hebdomadaires
        3. 🔴 **Formation de base** pour tous les employés (2h)
        4. 🔴 **Politique mots de passe** minimum (12 caractères)
        5. 🔴 **Antivirus** sur tous les postes
        
        **Budget estimé:** 10-20k$ pour démarrer
        
        **Priorité #1:** Éviter un incident majeur imminent (85% de risque!)
        """)
    
    elif niveau == "GÉRÉ":
        st.warning("""
        **Actions prioritaires (3-6 mois):**
        
        1. 🟡 **Documenter tous les processus** de sécurité
        2. 🟡 **Tester les sauvegardes** tous les trimestres
        3. 🟡 **MFA sur comptes critiques** (admins, finances)
        4. 🟡 **Formation annuelle** obligatoire
        5. 🟡 **Audit interne** pour identifier les trous
        
        **Budget estimé:** 50-100k$ pour passer au niveau Défini
        
        **Objectif:** Atteindre 75% de conformité
        """)
    
    elif niveau == "DÉFINI":
        st.success("""
        **Prochaines étapes (6-12 mois):**
        
        1. 🟢 **Certification ISO 27001** (reconnaissance internationale)
        2. 🟢 **SIEM** pour monitoring avancé
        3. 🟢 **Tests de pénétration** annuels
        4. 🟢 **Automatisation** des processus
        5. 🟢 **Amélioration continue** formalisée
        
        **Budget estimé:** 100-200k$ pour optimiser
        
        **Objectif:** Atteindre 95% et excellence
        """)
    
    else:  # OPTIMISÉ
        st.info("""
        **Maintenir l'excellence:**
        
        1. 🔵 **Innovation continue** et veille technologique
        2. 🔵 **Partage des bonnes pratiques** avec l'industrie
        3. 🔵 **Formation avancée** de l'équipe
        4. 🔵 **Bug bounty** ou red team régulier
        5. 🔵 **Rester vigilant** - les menaces évoluent!
        
        **Félicitations:** Vous êtes dans le top 5%!
        """)
    
    # Bouton pour sauvegarder dans le profil
    if st.button("💾 Sauvegarder ce niveau dans mon profil", use_container_width=True):
        niveau_code = {'INITIAL': 'initial', 'GÉRÉ': 'managed', 'DÉFINI': 'defined', 'OPTIMISÉ': 'optimized'}
        st.session_state.profil['maturite'] = niveau_code[niveau]
        st.success("✅ Niveau de maturité sauvegardé! Toutes les analyses seront mises à jour.")
        st.balloons()

st.divider()

# Footer
st.caption("""
💡 **Conseil:** Refaites ce quiz tous les 6 mois pour suivre votre progression!

🎯 **Objectif:** Passer au niveau supérieur en 12-18 mois avec le bon plan d'action.

📊 **Source:** Basé sur les frameworks CMMI, NIST CSF et ISO 27001.
""")
