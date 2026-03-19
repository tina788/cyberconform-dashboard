# 🔒 CyberConform - Dashboard de Conformité Cybersécurité

Dashboard professionnel multi-pages inspiré du design Figma AI - Style Salesforce/HubSpot

## 📋 Contenu du projet

```
cyberconform-dashboard/
├── app.py                          # Page d'accueil et navigation
├── requirements.txt                # Dépendances Python
├── data/
│   └── referentiels.json          # Base de données (6 référentiels + 10 économies)
├── utils/
│   └── calculations.py            # Fonctions de calcul
└── pages/
    ├── 1_📊_Tableau_de_bord.py    # Dashboard avec métriques + graphiques
    ├── 2_🏢_Profil_organisation.py # Formulaire profil
    ├── 3_🛡️_Evaluation_maturite.py # Score maturité + radar chart
    ├── 4_⚠️_Analyse_risques.py     # Pénalités + exposition financière
    ├── 5_💡_Recommandations.py     # 3 stratégies d'implémentation
    ├── 6_📅_Calendrier.py          # Timeline d'implémentation
    ├── 7_💰_Investissement.py      # Détails coûts + ROI
    └── 8_⚙️_Parametres.py          # Paramètres de l'application
```

## 🚀 Installation

### 1. Créer un environnement virtuel

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Lancer l'application

```bash
streamlit run app.py
```

L'application sera accessible à: **http://localhost:8501**

## 🎨 Fonctionnalités

### ✅ Pages implémentées

- **📊 Tableau de bord** - Métriques clés + graphiques + activités récentes
- **🏢 Profil organisation** - 3 grandes cartes colorées + formulaire
- **🛡️ Évaluation maturité** - Score 69/100 + radar chart 10 domaines
- **⚠️ Analyse de risques** - Alert rouge + pénalités Loi 25/RGPD/PCI DSS
- **💡 Recommandations** - 3 stratégies (Progressive/Accélérée/Minimale)
- **📅 Calendrier** - Timeline implémentation + référentiels
- **💰 Investissement** - Détails coûts + ROI + graphiques
- **⚙️ Paramètres** - Général/Notifications/Sécurité/Équipe

### 🎯 Données intégrées

**6 Référentiels:**
- Loi 25 (Québec)
- NIST Cybersecurity Framework
- ISO/IEC 27001:2022
- LPRPSP (fédérale)
- CSA Cloud Controls Matrix
- ISO/IEC 27018

**10 Économies:**
- Gouvernance (4): Politique existante, Responsable sécurité, Formation, Évaluations
- Sécurité (4): Antivirus/EDR, MFA, Sauvegardes, Pare-feu
- Processus (2): Inventaire actifs, Gestion incidents

### 💎 Style & Design

- **Palette:** #2563EB (bleu), #10B981 (vert), #F59E0B (orange), #EF4444 (rouge), #A855F7 (violet)
- **Fonts:** Inter (texte) + Poppins (titres)
- **Composants:** Metric cards, glassmorphism, badges colorés, progress bars, alerts
- **Graphiques:** Plotly (barres, donut, radar)

## 📦 Déploiement sur Streamlit Cloud

1. Pushez le code sur GitHub
2. Allez sur https://streamlit.io/cloud
3. Connectez votre repo
4. Deploy!

## 🔧 Personnalisation

### Modifier les couleurs

Éditez le CSS dans `app.py`:

```python
:root {
    --primary-blue: #2563EB;
    --success-green: #10B981;
    --warning-orange: #F59E0B;
    --danger-red: #EF4444;
    --purple: #A855F7;
}
```

### Ajouter des données

Modifiez `data/referentiels.json`:

```json
{
  "referentiels": {
    "nouveau_ref": {
      "name": "Nouveau Référentiel",
      "description": "Description...",
      ...
    }
  }
}
```

## 📞 Support

Pour toute question, contactez l'équipe CyberConform.

---

**© 2026 CyberConform - Assistant de conformité cybersécurité**
