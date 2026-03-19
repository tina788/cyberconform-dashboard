"""
Module de génération de rapports PDF pour CyberConform
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfgen import canvas
from datetime import datetime
import io

class PDFGenerator:
    """Générateur de rapports PDF pour CyberConform"""
    
    def __init__(self, filename="rapport_cyberconform.pdf"):
        self.filename = filename
        self.buffer = io.BytesIO()
        self.doc = SimpleDocTemplate(
            self.buffer,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18,
        )
        self.styles = getSampleStyleSheet()
        self.story = []
        
        # Styles personnalisés
        self.create_custom_styles()
    
    def create_custom_styles(self):
        """Créer des styles personnalisés"""
        
        # Titre principal
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1E293B'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Sous-titre
        self.styles.add(ParagraphStyle(
            name='CustomSubtitle',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#2563EB'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        ))
        
        # Section
        self.styles.add(ParagraphStyle(
            name='CustomSection',
            parent=self.styles['Heading3'],
            fontSize=14,
            textColor=colors.HexColor('#374151'),
            spaceAfter=8,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        ))
        
        # Alerte
        self.styles.add(ParagraphStyle(
            name='Alert',
            parent=self.styles['BodyText'],
            fontSize=12,
            textColor=colors.HexColor('#DC2626'),
            leftIndent=20,
            rightIndent=20,
            spaceAfter=12,
            fontName='Helvetica-Bold'
        ))
    
    def add_header(self, titre, sous_titre=""):
        """Ajouter l'en-tête du rapport"""
        
        # Titre
        self.story.append(Paragraph(titre, self.styles['CustomTitle']))
        
        if sous_titre:
            self.story.append(Paragraph(sous_titre, self.styles['Normal']))
            
        # Date
        date_str = datetime.now().strftime("%d/%m/%Y à %H:%M")
        date_para = Paragraph(f"Généré le {date_str}", self.styles['Normal'])
        self.story.append(date_para)
        
        self.story.append(Spacer(1, 0.3*inch))
    
    def add_section(self, titre):
        """Ajouter une section"""
        self.story.append(Paragraph(titre, self.styles['CustomSubtitle']))
        self.story.append(Spacer(1, 0.1*inch))
    
    def add_subsection(self, titre):
        """Ajouter une sous-section"""
        self.story.append(Paragraph(titre, self.styles['CustomSection']))
    
    def add_paragraph(self, texte, style='BodyText'):
        """Ajouter un paragraphe"""
        self.story.append(Paragraph(texte, self.styles[style]))
        self.story.append(Spacer(1, 0.1*inch))
    
    def add_alert(self, texte):
        """Ajouter une alerte"""
        self.story.append(Paragraph(f"⚠️ ALERTE: {texte}", self.styles['Alert']))
        self.story.append(Spacer(1, 0.2*inch))
    
    def add_table(self, data, col_widths=None, style='default'):
        """Ajouter un tableau"""
        
        if not col_widths:
            col_widths = [2*inch] * len(data[0])
        
        table = Table(data, colWidths=col_widths)
        
        # Styles de tableau
        if style == 'default':
            table_style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2563EB')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F9FAFB')])
            ])
        elif style == 'simple':
            table_style = TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                ('TOPPADDING', (0, 0), (-1, -1), 6),
                ('LINEBELOW', (0, 0), (-1, 0), 1, colors.black),
            ])
        
        table.setStyle(table_style)
        self.story.append(table)
        self.story.append(Spacer(1, 0.2*inch))
    
    def add_metrics_row(self, metrics):
        """Ajouter une ligne de métriques"""
        data = []
        row = []
        
        for label, value in metrics:
            row.append(f"{label}\n{value}")
        
        data.append(row)
        
        col_widths = [6.5*inch / len(metrics)] * len(metrics)
        table = Table(data, colWidths=col_widths)
        
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#EFF6FF')),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 12),
            ('BOX', (0, 0), (-1, -1), 2, colors.HexColor('#2563EB')),
        ]))
        
        self.story.append(table)
        self.story.append(Spacer(1, 0.2*inch))
    
    def add_page_break(self):
        """Ajouter un saut de page"""
        self.story.append(PageBreak())
    
    def generate(self):
        """Générer le PDF et retourner le buffer"""
        self.doc.build(self.story)
        self.buffer.seek(0)
        return self.buffer


def generer_rapport_analyse_risques(profil):
    """Générer un rapport d'analyse de risques en PDF"""
    
    pdf = PDFGenerator("analyse_risques.pdf")
    
    # En-tête
    pdf.add_header(
        "📊 Rapport d'analyse de risques",
        f"Organisation: {profil.get('nom', 'N/A')} • Secteur: {profil.get('secteur', 'N/A')}"
    )
    
    # Métriques clés
    ca_annuel = profil.get('ca_annuel', 30000000)
    penalite_loi25 = max(25000000, ca_annuel * 0.04)
    penalite_rgpd = max(29000000, ca_annuel * 0.04)
    
    pdf.add_metrics_row([
        ("Exposition totale", f"{(penalite_loi25 + penalite_rgpd)/1000000:.1f} M$"),
        ("CA annuel", f"{ca_annuel/1000000:.0f} M$"),
        ("Secteur", profil.get('secteur', 'N/A')),
        ("Maturité", profil.get('maturite', 'N/A'))
    ])
    
    # Alerte
    pdf.add_alert(
        f"Votre organisation est exposée à un risque financier de {(penalite_loi25 + penalite_rgpd)/1000000:.1f}M$ en raison de lacunes de conformité."
    )
    
    # Section pénalités
    pdf.add_section("💰 Pénalités financières détaillées")
    
    penalites_data = [
        ["Réglementation", "Pénalité maximale", "Votre exposition", "Probabilité"],
        ["Loi 25 (Québec)", "25M$ ou 4% CA", f"{penalite_loi25/1000000:.1f} M$", "Élevée (85%)"],
        ["RGPD (Europe)", "20M€ ou 4% CA", f"{penalite_rgpd/1000000:.1f} M$", "Moyenne (65%)"],
        ["PCI DSS", "100k$/mois", "1.2 M$/an", "Moyenne (45%)"],
    ]
    
    pdf.add_table(penalites_data, col_widths=[1.8*inch, 1.6*inch, 1.6*inch, 1.5*inch])
    
    # Risques encourus
    pdf.add_section("⚠️ Risques encourus")
    
    pdf.add_subsection("Risques financiers")
    pdf.add_paragraph("""
    • Amendes réglementaires jusqu'à 25 M$ (Loi 25)<br/>
    • Coûts de remédiation: 500k$ - 2M$<br/>
    • Perte de revenus pendant incident: 50k$ - 500k$ par jour<br/>
    • Augmentation des primes d'assurance cyber: +150%
    """)
    
    pdf.add_subsection("Risques réputationnels")
    pdf.add_paragraph("""
    • Perte de confiance client: baisse de 25-40% des ventes<br/>
    • Couverture médiatique négative<br/>
    • Impact sur la valeur boursière<br/>
    • Difficulté à recruter des talents
    """)
    
    # Recommandations
    pdf.add_page_break()
    pdf.add_section("💡 Recommandations prioritaires")
    
    recommandations_data = [
        ["Action", "Délai", "Coût", "Impact"],
        ["Politique de confidentialité Loi 25", "2 semaines", "5k$", "85%"],
        ["Registre des traitements", "4 semaines", "15k$", "70%"],
        ["Activer MFA", "1 semaine", "3k$", "75%"],
        ["Formation cybersécurité", "2 semaines", "5k$", "50%"],
    ]
    
    pdf.add_table(recommandations_data, col_widths=[2.5*inch, 1.3*inch, 1.2*inch, 1.5*inch])
    
    pdf.add_paragraph("""
    <b>Prochaines étapes recommandées:</b><br/>
    1. Mettre en place la politique de confidentialité Loi 25 (priorité absolue)<br/>
    2. Activer l'authentification multi-facteurs (MFA) pour tous les utilisateurs<br/>
    3. Créer le registre des traitements de données<br/>
    4. Planifier une formation de sensibilisation cybersécurité
    """)
    
    return pdf.generate()


def generer_rapport_recommandations(profil):
    """Générer un rapport de recommandations en PDF"""
    
    pdf = PDFGenerator("recommandations.pdf")
    
    # En-tête
    pdf.add_header(
        "💡 Plan d'action stratégique",
        f"Organisation: {profil.get('nom', 'N/A')} • Budget: {profil.get('budget', 'N/A')}"
    )
    
    # Stratégie recommandée
    budget = profil.get('budget', 'medium')
    taille = profil.get('taille', 'medium')
    
    strategie = 'progressive'
    if budget == 'low' or taille == 'micro':
        strategie = 'minimale'
    elif budget == 'high' and taille == 'large':
        strategie = 'acceleree'
    
    pdf.add_section(f"🎯 Approche recommandée: {strategie.upper()}")
    
    if strategie == 'progressive':
        pdf.add_paragraph("""
        <b>Approche progressive (18-24 mois • 450-650k$)</b><br/><br/>
        Cette stratégie offre le meilleur équilibre entre coût, risque et délai pour votre organisation.
        """)
        
        phases_data = [
            ["Phase", "Durée", "Budget", "Objectifs clés"],
            ["Fondations", "6 mois", "150-200k$", "Conformité Loi 25 de base"],
            ["Renforcement", "8 mois", "200-300k$", "Contrôles avancés, SIEM"],
            ["Optimisation", "6 mois", "100-150k$", "Certification ISO 27001"],
        ]
        
        pdf.add_table(phases_data, col_widths=[1.5*inch, 1.3*inch, 1.5*inch, 2.2*inch])
    
    # Quick Wins
    pdf.add_section("🏆 Quick Wins - Résultats immédiats")
    
    quick_wins_data = [
        ["Action", "Durée", "Coût", "Impact"],
        ["Activer MFA", "1 semaine", "3k$", "75%"],
        ["Formation cybersécurité", "2 semaines", "5k$", "50%"],
        ["Chiffrement bases de données", "3 semaines", "12k$", "80%"],
        ["Révision droits d'accès", "2 semaines", "4k$", "60%"],
    ]
    
    pdf.add_table(quick_wins_data, col_widths=[2.5*inch, 1.3*inch, 1.2*inch, 1.5*inch])
    
    # Timeline
    pdf.add_page_break()
    pdf.add_section("📅 Timeline d'implémentation")
    
    timeline_data = [
        ["Trimestre", "Phase", "Budget", "Livrables"],
        ["T1 2026", "Fondations", "150k$", "Politiques, Inventaire, MFA"],
        ["T2 2026", "Fondations", "125k$", "Chiffrement, Contrôles d'accès"],
        ["T3 2026", "Renforcement", "175k$", "SIEM, Gestion risques"],
        ["T4 2026", "Optimisation", "150k$", "Certification ISO 27001"],
    ]
    
    pdf.add_table(timeline_data, col_widths=[1.3*inch, 1.5*inch, 1.3*inch, 2.4*inch])
    
    pdf.add_paragraph("""
    <b>Note importante:</b> Cette timeline est indicative et peut être ajustée selon vos contraintes 
    opérationnelles et budgétaires. Un suivi mensuel est recommandé pour s'assurer du respect des jalons.
    """)
    
    return pdf.generate()


def generer_rapport_complet(profil):
    """Générer un rapport complet incluant tout"""
    
    pdf = PDFGenerator("rapport_complet_cyberconform.pdf")
    
    # Page de garde
    pdf.add_header(
        "🔒 CyberConform",
        "Rapport complet d'analyse de conformité cybersécurité"
    )
    
    pdf.add_paragraph(f"""
    <b>Organisation:</b> {profil.get('nom', 'N/A')}<br/>
    <b>Secteur d'activité:</b> {profil.get('secteur', 'N/A')}<br/>
    <b>Chiffre d'affaires:</b> {profil.get('ca', 'N/A')}<br/>
    <b>Taille:</b> {profil.get('taille', 'N/A')}<br/>
    <b>Niveau de maturité:</b> {profil.get('maturite', 'N/A')}
    """, 'BodyText')
    
    pdf.add_page_break()
    
    # Table des matières
    pdf.add_section("📑 Table des matières")
    pdf.add_paragraph("""
    1. Résumé exécutif<br/>
    2. Profil de l'organisation<br/>
    3. Analyse des risques<br/>
    4. Pénalités et exposition financière<br/>
    5. Recommandations stratégiques<br/>
    6. Plan d'action détaillé<br/>
    7. Timeline d'implémentation<br/>
    8. Budget et investissements<br/>
    9. Annexes
    """)
    
    pdf.add_page_break()
    
    # Résumé exécutif
    pdf.add_section("📊 1. Résumé exécutif")
    
    ca_annuel = profil.get('ca_annuel', 30000000)
    penalite_totale = max(25000000, ca_annuel * 0.04) + max(29000000, ca_annuel * 0.04)
    
    pdf.add_alert(
        f"Exposition financière totale estimée: {penalite_totale/1000000:.1f} M$"
    )
    
    pdf.add_paragraph(f"""
    Ce rapport présente une analyse complète de la conformité cybersécurité de {profil.get('nom', 'votre organisation')}.
    <br/><br/>
    <b>Constats principaux:</b><br/>
    • Exposition financière significative aux pénalités réglementaires<br/>
    • Conformité Loi 25 (Québec) requise de manière urgente<br/>
    • Plusieurs quick wins identifiés pour réduction rapide des risques<br/>
    • Investissement recommandé: 450-650k$ sur 18-24 mois
    """)
    
    pdf.add_page_break()
    
    # Profil organisation
    pdf.add_section("🏢 2. Profil de l'organisation")
    
    profil_data = [
        ["Caractéristique", "Valeur"],
        ["Nom", profil.get('nom', 'N/A')],
        ["Secteur", profil.get('secteur', 'N/A')],
        ["Taille", profil.get('taille', 'N/A')],
        ["Chiffre d'affaires", profil.get('ca', 'N/A')],
        ["Budget conformité", profil.get('budget', 'N/A')],
        ["Niveau de maturité", profil.get('maturite', 'N/A')],
        ["Type infrastructure", profil.get('infrastructure', 'N/A')],
    ]
    
    pdf.add_table(profil_data, col_widths=[2.5*inch, 4*inch], style='simple')
    
    # Suite du rapport...
    # (Ajoutez les autres sections ici)
    
    return pdf.generate()
