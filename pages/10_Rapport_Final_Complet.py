import streamlit as st
from datetime import datetime
import sys
sys.path.append('.')

st.set_page_config(page_title="Rapport Final", page_icon="📋", layout="wide")

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

st.title("📋 Génération du Rapport Final Complet")
st.caption("Compilez tous les apports de votre analyse dans un seul document PDF professionnel")

st.divider()

# Vérifier si profil configuré
if profil.get('nom') == 'Votre organisation':
    st.error("""
    ⚠️ **Profil non configuré**
    
    Pour générer un rapport personnalisé, vous devez d'abord configurer votre profil organisationnel.
    
    👉 Allez dans **Profil organisation** pour commencer.
    """)
    
    if st.button("📋 Aller au Profil organisation", type="primary"):
        st.switch_page("pages/2_Profil_organisation.py")
    
    st.stop()

# Afficher le profil actuel
st.success(f"""
### ✅ Profil configuré: {profil.get('nom')}

**Secteur:** {profil.get('secteur')}  
**CA annuel:** {profil.get('ca')}  
**Budget conformité:** {profil.get('budget')}  
**Maturité:** {profil.get('maturite')}
""")

st.divider()

# Description du rapport
st.markdown("## 📄 Contenu du Rapport Final")

st.info("""
Le rapport final PDF inclut **TOUTES les sections** de votre analyse:

1. ✅ **Page de garde professionnelle**
2. ✅ **Table des matières**
3. ✅ **Résumé exécutif** (1 page synthétique)
4. ✅ **Profil de votre organisation**
5. ✅ **Évaluation de la maturité cybersécurité**
6. ✅ **Analyse détaillée des risques** (pénalités, exposition)
7. ✅ **Recommandations stratégiques** (triées par budget disponible)
8. ✅ **Calendrier de mise en conformité** (18-24 mois)
9. ✅ **Budget et ROI détaillés**
10. ✅ **Synthèse et décision requise**
11. ✅ **Annexes** (références, définitions, contacts)

**Format:** PDF professionnel de 15-20 pages  
**Langue:** Français  
**Audience:** Direction, comité de pilotage, conseil d'administration
""")

st.markdown("<br>", unsafe_allow_html=True)

# Preview du contenu
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Métriques incluses")
    
    # Calculs
    ca_annuel = profil.get('ca_annuel', 30000000)
    penalite_loi25 = max(25000000, ca_annuel * 0.04)
    total_exposition = penalite_loi25 + 30000000
    
    budgets = {'low': 50000, 'medium': 200000, 'high': 500000}
    budget_disponible = budgets.get(profil.get('budget', 'medium'), 200000)
    
    scores = {'initial': 25, 'managed': 55, 'defined': 75, 'optimized': 95}
    score_conformite = scores.get(profil.get('maturite', 'managed'), 55)
    
    roi = total_exposition / budget_disponible if budget_disponible > 0 else 0
    
    st.metric("Exposition totale", f"{total_exposition/1000000:.1f} M$")
    st.metric("Score conformité", f"{score_conformite}%")
    st.metric("ROI estimé", f"{roi:.0f}:1")
    st.metric("Budget requis", "300k$")

with col2:
    st.markdown("### 🎯 Apports principaux")
    st.markdown("""
    - **Analyse des risques** avec calculs précis selon VOTRE CA
    - **Recommandations triées** par faisabilité budgétaire
    - **Actions prioritaires** que vous pouvez faire MAINTENANT
    - **Calendrier réaliste** sur 18-24 mois
    - **ROI chiffré** pour justifier l'investissement
    - **Décision claire** à présenter à la direction
    """)

st.markdown("<br>", unsafe_allow_html=True)

# Options de génération
st.markdown("## ⚙️ Options de génération")

col1, col2 = st.columns(2)

with col1:
    inclure_annexes = st.checkbox("Inclure les annexes détaillées", value=True, 
                                  help="Références réglementaires, définitions, contacts")

with col2:
    inclure_signatures = st.checkbox("Inclure espace pour signatures", value=True,
                                     help="Espace pour signature du responsable IT/Conformité")

format_export = st.radio(
    "Format d'export",
    options=["PDF (recommandé)", "PDF + Version imprimable"],
    help="Version imprimable optimisée pour impression papier"
)

st.markdown("<br>", unsafe_allow_html=True)

# Bouton de génération
st.markdown("## 📥 Génération du rapport")

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("🎯 Générer le Rapport Final Complet", type="primary", use_container_width=True):
        
        with st.spinner("Génération du rapport en cours... Veuillez patienter."):
            try:
                # Import du générateur
                from generer_rapport_final import generer_rapport_final_complet
                
                # Générer le PDF
                pdf_buffer = generer_rapport_final_complet(profil)
                
                # Nom du fichier
                nom_fichier = f"Rapport_Final_Complet_{profil.get('nom', 'Organisation').replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.pdf"
                
                # Succès
                st.success("✅ Rapport généré avec succès!")
                st.balloons()
                
                # Bouton de téléchargement
                st.download_button(
                    label="💾 Télécharger le Rapport Final (PDF)",
                    data=pdf_buffer,
                    file_name=nom_fichier,
                    mime="application/pdf",
                    use_container_width=True,
                    type="primary"
                )
                
                # Statistiques
                st.info(f"""
                **📊 Rapport généré:**
                
                - **Nom:** {nom_fichier}
                - **Pages:** ~15-20 pages
                - **Taille:** ~500-800 KB
                - **Date:** {datetime.now().strftime('%d/%m/%Y à %H:%M')}
                - **Organisation:** {profil.get('nom')}
                """)
                
                # Prochaines étapes
                st.markdown("### 🚀 Prochaines étapes")
                
                st.success("""
                **Après avoir téléchargé le rapport:**
                
                1. ✅ **Lisez** le résumé exécutif (page 3)
                2. ✅ **Vérifiez** les recommandations triées par budget (page 8)
                3. ✅ **Présentez** le rapport à votre direction
                4. ✅ **Planifiez** une réunion de décision (2 semaines max)
                5. ✅ **Lancez** le projet de mise en conformité
                
                **💡 Conseil:** Imprimez le résumé exécutif (pages 3-4) pour la réunion avec la direction.
                """)
                
            except Exception as e:
                st.error(f"""
                ❌ **Erreur lors de la génération du rapport**
                
                Détails: {str(e)}
                
                **Solutions:**
                1. Vérifiez que votre profil est complet
                2. Assurez-vous que `reportlab` est installé: `pip install reportlab`
                3. Réessayez dans quelques instants
                """)
                
                st.info("💡 Si l'erreur persiste, contactez le support technique.")

st.markdown("<br>", unsafe_allow_html=True)

# Conseils d'utilisation
with st.expander("💡 Conseils pour présenter le rapport à votre direction"):
    st.markdown("""
    ### 📋 Préparation de la présentation
    
    **AVANT la réunion:**
    1. Imprimez le résumé exécutif pour chaque participant
    2. Préparez une présentation PowerPoint (5-10 slides max) avec les points clés
    3. Identifiez les objections potentielles et préparez vos réponses
    
    **PENDANT la réunion (30 min recommandé):**
    
    **Minutes 0-5:** Introduction
    - Contexte: Pourquoi cette analyse maintenant?
    - Objectif: Obtenir approbation budgétaire
    
    **Minutes 5-15:** Présentation des constats
    - Exposition: "Nous sommes exposés à X M$ de risques"
    - Conformité: "Notre score actuel est Y%"
    - Obligation: "Loi 25 est OBLIGATOIRE"
    
    **Minutes 15-25:** Recommandations
    - Plan: "Approche progressive sur 18 mois"
    - Budget: "300k$ pour protection de X M$"
    - ROI: "Ratio de 15:1"
    - Actions: "Voici ce qu'on peut faire dans notre budget"
    
    **Minutes 25-30:** Décision
    - Question claire: "Approuvez-vous le budget de 300k$?"
    - Timeline: "Décision requise dans 2 semaines"
    - Prochaines étapes: "Si oui, on lance dans 30 jours"
    
    **ARGUMENTS CLÉS à utiliser:**
    - ✅ "C'est OBLIGATOIRE (Loi 25)"
    - ✅ "ROI de 15:1 - chaque dollar protège 15$ de risques"
    - ✅ "65% de probabilité d'incident SANS action"
    - ✅ "Actions triées par budget - on fait ce qu'on peut"
    - ✅ "Délai 18 mois - plan réaliste et progressif"
    
    **RÉPONSES aux objections courantes:**
    
    **"C'est trop cher!"**
    → "Comparé au risque de 55M$, 300k$ c'est 0.5%. Un seul incident coûte 500k$-2M$."
    
    **"On n'a pas le temps!"**
    → "C'est précisément pourquoi on a un plan étalé sur 18 mois avec des ressources externes."
    
    **"On verra l'année prochaine."**
    → "Chaque mois de retard augmente le risque. Loi 25 est déjà en vigueur - on est en retard."
    
    **"Est-ce qu'on peut faire moins cher?"**
    → "Oui - approche minimale à 80k$. Mais couverture partielle seulement (Loi 25 uniquement)."
    """)

with st.expander("📧 Exemple d'email pour envoyer le rapport"):
    st.code("""
Objet: Rapport d'analyse cybersécurité - Décision requise

Bonjour [Nom du directeur],

Suite à notre discussion sur la conformité cybersécurité, 
j'ai le plaisir de vous transmettre le rapport d'analyse complet.

📋 RÉSUMÉ EXÉCUTIF:
• Exposition actuelle: 55M$ de risques réglementaires
• Conformité Loi 25: OBLIGATOIRE - non atteinte actuellement
• Investissement recommandé: 300k$ sur 18 mois
• ROI: 15:1 (chaque dollar investi protège 15$ de risques)

🎯 RECOMMANDATION:
Approche progressive en 3 phases sur 18-24 mois.
Le rapport détaille les actions prioritaires triées par notre 
budget disponible.

📅 PROCHAINES ÉTAPES:
1. Lecture du résumé exécutif (pages 3-4 du rapport)
2. Réunion de décision dans les 2 prochaines semaines
3. Lancement du projet si approbation

Le rapport complet (15 pages) est joint à cet email.

Je reste à votre disposition pour toute question.

Cordialement,
[Votre nom]
[Votre titre]
    """, language="text")

st.divider()

# Footer
st.caption("""
💡 **Note:** Ce rapport est généré automatiquement à partir de votre profil configuré. 
Assurez-vous que toutes les informations sont à jour avant de le présenter.

📊 **Source:** CyberConform Dashboard - Analyse de conformité cybersécurité
""")
