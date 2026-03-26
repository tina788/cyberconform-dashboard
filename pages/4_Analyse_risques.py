import streamlit as st
import plotly.graph_objects as go
import json
import sys
sys.path.append('.')

st.set_page_config(page_title="Analyse de risques", page_icon="⚠️", layout="wide")

# Vérifier si profil configuré
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

# Avertissement si profil non configuré
if profil.get('nom') == 'Votre organisation':
    st.error("""
    ⚠️ **PROFIL NON CONFIGURÉ**
    
    Cette page nécessite que vous configuriez d'abord votre profil organisationnel 
    pour calculer votre exposition réelle aux risques.
    
    **👉 Allez dans "🏢 Profil organisation"** pour commencer.
    """)
    
    if st.button("📋 Aller au Profil organisation", type="primary"):
        st.info("Cliquez sur '🏢 Profil organisation' dans le menu de gauche")
    
    st.stop()

# Charger les référentiels
try:
    with open('data/referentiels.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        referentiels = data['referentiels']
except:
    st.error("❌ Impossible de charger les référentiels")
    st.stop()

# Récupérer le profil
ca_annuel = profil.get('ca_annuel', 30000000)
secteur = profil.get('secteur', 'finance')
maturite = profil.get('maturite', 'managed')

st.title("⚠️ Analyse des risques de non-conformité")
st.caption(f"Évaluation pour: **{profil.get('nom')}** • Secteur: **{secteur}** • CA: **{profil.get('ca')}**")

col1, col2 = st.columns([3, 1])
with col2:
    # Bouton export PDF
    if st.button("📤 Exporter en PDF", use_container_width=True):
        try:
            from utils.pdf_generator import generer_rapport_analyse_risques
            
            pdf_buffer = generer_rapport_analyse_risques(profil)
            
            st.download_button(
                label="💾 Télécharger le PDF",
                data=pdf_buffer,
                file_name=f"analyse_risques_{profil.get('nom', 'rapport').replace(' ', '_')}.pdf",
                mime="application/pdf",
                use_container_width=True
            )
            
            st.success("✅ PDF généré avec succès!")
            
        except Exception as e:
            st.error(f"❌ Erreur lors de la génération du PDF: {str(e)}")
            st.info("💡 Assurez-vous d'avoir installé: pip install reportlab")

st.divider()

# CALCUL DYNAMIQUE DES PÉNALITÉS
def calculer_penalite_loi25(ca_annuel):
    """Loi 25: max(25M$, 4% CA)"""
    penalite_fixe = 25000000
    penalite_pct = ca_annuel * 0.04
    return max(penalite_fixe, penalite_pct)

def calculer_penalite_rgpd(ca_annuel):
    """RGPD: max(20M€, 4% CA mondial)"""
    penalite_fixe = 20000000 * 1.45  # Conversion € vers CAD
    penalite_pct = ca_annuel * 0.04
    return max(penalite_fixe, penalite_pct)

# Calcul des pénalités
penalite_loi25 = calculer_penalite_loi25(ca_annuel)
penalite_rgpd = calculer_penalite_rgpd(ca_annuel)
penalite_pci = 100000 * 12

# Total exposition
total_exposition = penalite_loi25 + penalite_rgpd + penalite_pci

# Probabilité selon maturité
probabilites = {
    'initial': 0.85,
    'managed': 0.65,
    'defined': 0.40,
    'optimized': 0.15
}
probabilite = probabilites.get(maturite, 0.65)

# Alert box avec contexte
st.error(f"""
### ⚠️ Exposition financière critique détectée

Votre organisation est exposée à un risque financier potentiel de **{total_exposition/1000000:.1f} M$** en raison de lacunes 
de conformité identifiées. 

**Probabilité d'incident:** {int(probabilite*100)}% avec votre niveau de maturité actuel ({maturite})

**Détail de l'exposition:**
- **Loi 25 (Québec):** {penalite_loi25/1000000:.1f} M$ (maximum entre 25M$ et 4% de votre CA de {ca_annuel/1000000:.0f}M$)
- **RGPD (si clients UE):** {penalite_rgpd/1000000:.1f} M$
- **PCI DSS (paiements carte):** {penalite_pci/1000:.0f}k$/an
""")

# Interprétation intelligente
st.info(f"""
💡 **Interprétation pour votre organisation:**

Avec un CA de **{ca_annuel/1000000:.0f}M$**, votre exposition Loi 25 est {
    "**au-dessus du minimum de 25M$**" if penalite_loi25 > 25000000 
    else "**égale au minimum de 25M$**"
} car {
    f"4% de votre CA ({ca_annuel*0.04/1000000:.1f}M$) dépasse le minimum fixe" if penalite_loi25 > 25000000
    else "4% de votre CA est inférieur au minimum de 25M$"
}.

**📊 Benchmark secteur {secteur}:**
- Exposition moyenne: 15-30M$
- Votre exposition: **{total_exposition/1000000:.1f}M$** → {"✅ Dans la norme" if total_exposition/1000000 < 30 else "⚠️ Au-dessus de la moyenne"}
- 73% des entreprises similaires ont déjà un projet de conformité en cours

**🎯 Recommandation immédiate:** Consultez la page **Recommandations** pour voir le plan d'action adapté à votre budget.
""")

col1, col2 = st.columns([2, 2])
with col1:
    if st.button("🎯 Voir le plan d'action prioritaire", type="primary", use_container_width=True):
        st.success("👉 Cliquez sur **💡 Recommandations** dans le menu de gauche!")
with col2:
    if st.button("📞 Obtenir de l'aide", use_container_width=True):
        st.info("Contactez un expert en conformité pour une analyse approfondie")

st.markdown("<br>", unsafe_allow_html=True)

# Référentiels applicables
st.subheader("📋 Référentiels applicables à votre organisation")

# Filtrer selon le secteur
refs_applicables = []
for ref_id, ref_data in referentiels.items():
    if secteur in ref_data.get('applicabilite', {}).get('secteurs', []):
        refs_applicables.append((ref_id, ref_data))

# Identifier les obligatoires
refs_obligatoires = [r for r in refs_applicables if secteur in r[1].get('obligatoire_for', [])]

if refs_obligatoires:
    st.warning(f"🔴 **{len(refs_obligatoires)} référentiels OBLIGATOIRES** pour le secteur {secteur}")
    for ref_id, ref_data in refs_obligatoires:
        st.markdown(f"• **{ref_data['name']}** - {ref_data['description']}")
else:
    st.info(f"ℹ️ Aucun référentiel strictement obligatoire identifié pour votre secteur")

st.success(f"📊 **{len(refs_applicables)} référentiels recommandés** au total pour votre profil")

# Expander avec définition des termes
with st.expander("❓ Qu'est-ce qu'un référentiel?"):
    st.markdown("""
    **Définition simple:** Un référentiel est un ensemble de règles et bonnes pratiques 
    pour protéger les données et les systèmes informatiques.
    
    **Exemples:**
    - **Loi 25** = Règles québécoises pour protéger la vie privée
    - **ISO 27001** = Standard international de sécurité de l'information
    - **PCI DSS** = Règles pour protéger les paiements par carte bancaire
    
    **Pourquoi c'est important:** Ne pas respecter ces règles peut entraîner des amendes 
    importantes et nuire à la réputation de votre organisation.
    """)

st.markdown("<br>", unsafe_allow_html=True)

# Graphique exposition
st.subheader("💰 Exposition financière par réglementation")

regulations = ['Loi 25', 'RGPD', 'PCI DSS']
expositions = [penalite_loi25/1000000, penalite_rgpd/1000000, penalite_pci/1000000]
colors_bars = ['#EF4444', '#F59E0B', '#F59E0B']

fig = go.Figure()
fig.add_trace(go.Bar(
    x=regulations,
    y=expositions,
    marker_color=colors_bars,
    text=[f"{e:.1f}M$" for e in expositions],
    textposition='outside',
    textfont=dict(size=14, weight='bold')
))

fig.update_layout(
    height=400,
    yaxis_title="Exposition financière (M$)",
    showlegend=False,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor='#F3F4F6'),
    margin=dict(t=40, b=40, l=60, r=40)
))

st.plotly_chart(fig, use_container_width=True)

# Interprétation du graphique
st.success("""
📊 **Lecture du graphique:**

- Les barres **rouges/oranges** indiquent le niveau de risque élevé
- Plus la barre est haute, plus la pénalité potentielle est importante
- Ces montants sont **cumulatifs** - une seule violation peut déclencher plusieurs pénalités

💡 **Action recommandée:** Priorisez la Loi 25 (la plus élevée et OBLIGATOIRE au Québec)
""")

st.markdown("<br>", unsafe_allow_html=True)

# Pénalités détaillées avec tooltips
st.subheader("📑 Pénalités réglementaires détaillées")

# Loi 25
with st.expander("🔴 **Loi 25 (Québec)** - Jusqu'à 25 M$ ou 4% du CA mondial", expanded=True):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**Pénalités financières**")
        st.caption(f"Probabilité d'incident: {['Faible', 'Moyenne', 'Élevée', 'Très élevée'][min(3, int(probabilite*4))]} ({int(probabilite*100)}%)")
    
    with col2:
        st.metric("Votre exposition", f"{penalite_loi25/1000000:.1f} M$")
        if penalite_loi25 > 25000000:
            st.caption(f"= 4% de {ca_annuel/1000000:.0f}M$ CA")
        else:
            st.caption("= 25M$ (minimum)")
    
    st.markdown("**Détails des sanctions:**")
    st.markdown(f"""
    - 10 M$ ou 2% du CA ({ca_annuel*0.02/1000000:.1f}M$) pour violations moins graves
    - 25 M$ ou 4% du CA ({ca_annuel*0.04/1000000:.1f}M$) pour violations graves
    - Sanctions administratives pécuniaires cumulatives
    - **Votre CA de {ca_annuel/1000000:.0f}M$ vous expose à {penalite_loi25/1000000:.1f}M$**
    """)
    
    # Tooltip sur ÉFVP
    with st.expander("❓ C'est quoi une ÉFVP?"):
        st.markdown("""
        **ÉFVP = Évaluation des Facteurs relatifs à la Vie Privée**
        
        En termes simples: C'est un document qui explique:
        - Quelles données personnelles vous collectez
        - Pourquoi vous les collectez
        - Comment vous les protégez
        - Quels sont les risques pour la vie privée
        
        **Obligatoire selon Loi 25** pour certains traitements de données sensibles.
        """)

# RGPD
with st.expander("🟡 **RGPD (Europe)** - Jusqu'à 20 M€ ou 4% du CA mondial"):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**Amendes administratives**")
        prob_rgpd = probabilite * 0.8 if secteur != 'public' else probabilite * 0.4
        st.caption(f"Probabilité: {['Faible', 'Moyenne', 'Élevée'][min(2, int(prob_rgpd*3))]} ({int(prob_rgpd*100)}%)")
    
    with col2:
        st.metric("Votre exposition", f"{penalite_rgpd/1000000:.1f} M$")
        st.caption("Si clients UE")
    
    st.markdown("**Détails des sanctions:**")
    st.markdown(f"""
    - 10 M€ ou 2% du CA pour certaines violations
    - 20 M€ ou 4% du CA pour violations graves
    - Application extraterritoriale si traitement de données UE
    - **Votre exposition: {penalite_rgpd/1000000:.1f}M$ CAD**
    """)

# PCI DSS
with st.expander("🟡 **PCI DSS** - 5,000$ - 100,000$ par mois"):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**Amendes et restrictions**")
        st.caption("Probabilité: Moyenne (45%)")
    
    with col2:
        st.metric("Pénalité annuelle", f"{penalite_pci/1000:.0f}k$")
        st.caption("= 100k$/mois × 12")
    
    st.markdown("**Détails des sanctions:**")
    st.markdown("""
    - Amendes des réseaux de cartes (Visa, Mastercard)
    - Révocation du droit de traiter les paiements par carte
    - Augmentation des frais de transaction
    - Audits de sécurité obligatoires aux frais du commerçant
    """)

st.markdown("<br><br>", unsafe_allow_html=True)

# Recommandations personnalisées en bas
st.info(f"""
💡 **Recommandation personnalisée pour {profil.get('nom')}:**

Avec un CA de **{profil.get('ca')}** et un niveau de maturité **{maturite}**, votre priorité absolue est:

1. **Se conformer à la Loi 25** (exposition: {penalite_loi25/1000000:.1f}M$)
2. Mettre en place les contrôles de base (MFA, chiffrement)
3. Former vos employés à la cybersécurité

➡️ Consultez la page **💡 Recommandations** pour voir votre plan d'action complet adapté à votre budget de {profil.get('budget')}.
""")

st.success("✅ Cette analyse est basée sur votre profil actuel. Mettez à jour votre profil dans **🏢 Profil organisation** pour recalculer.")
