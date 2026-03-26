"""
Module de génération de rapports PDF pour CyberConform Dashboard
Génère des rapports professionnels pour analyse, recommandations et présentation
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from io import BytesIO
from datetime import datetime

def generer_rapport_analyse_risques(profil):
    """Génère rapport PDF analyse des risques"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    # Titre
    story.append(Paragraph("Rapport d'Analyse des Risques", styles['Title']))
    story.append(Paragraph(f"Organisation: {profil.get('nom', 'N/A')}", styles['Normal']))
    story.append(Paragraph(f"Date: {datetime.now().strftime('%d/%m/%Y')}", styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    # Calculs
    ca_annuel = profil.get('ca_annuel', 30000000)
    penalite_loi25 = max(25000000, ca_annuel * 0.04)
    total_exposition = penalite_loi25 + 30000000
    
    # Contenu
    story.append(Paragraph("Résumé Exécutif", styles['Heading2']))
    resume = f"Exposition totale: {total_exposition/1000000:.1f} M$. Loi 25: {penalite_loi25/1000000:.1f}M$. Actions immédiates requises."
    story.append(Paragraph(resume, styles['Normal']))
    
    doc.build(story)
    buffer.seek(0)
    return buffer

def generer_rapport_recommandations(profil):
    """Génère rapport PDF recommandations"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    story.append(Paragraph("Plan d'Action Stratégique", styles['Title']))
    story.append(Paragraph(f"Organisation: {profil.get('nom', 'N/A')}", styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    plan = "Phase 1 (6m): 105k$. Phase 2 (8m): 120k$. Phase 3 (6m): 75k$. Total: 300k$ sur 18 mois."
    story.append(Paragraph(plan, styles['Normal']))
    
    doc.build(story)
    buffer.seek(0)
    return buffer

def generer_rapport_complet(profil):
    """Génère rapport PDF complet"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    story.append(Paragraph("Rapport de Conformité Complet", styles['Title']))
    story.append(Paragraph(f"{profil.get('nom', 'Votre Organisation')}", styles['Heading2']))
    story.append(Paragraph(f"Date: {datetime.now().strftime('%d/%m/%Y')}", styles['Normal']))
    story.append(PageBreak())
    
    ca_annuel = profil.get('ca_annuel', 30000000)
    penalite = max(25000000, ca_annuel * 0.04)
    
    story.append(Paragraph("Résumé Exécutif", styles['Heading2']))
    resume = f"Exposition: {(penalite+30000000)/1000000:.1f}M$. ROI: 15:1. Durée: 18 mois. Budget: 300k$."
    story.append(Paragraph(resume, styles['Normal']))
    
    doc.build(story)
    buffer.seek(0)
    return buffer

def generer_presentation_directeur(profil):
    """Génère présentation PDF pour directeur"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('CustomTitle', parent=styles['Title'], alignment=TA_CENTER)
    
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("Présentation Cybersécurité", title_style))
    story.append(Paragraph(f"{profil.get('nom', 'Votre Organisation')}", styles['Heading2']))
    story.append(PageBreak())
    
    story.append(Paragraph("Situation", styles['Heading2']))
    story.append(Paragraph(f"Risques: {max(25000000, profil.get('ca_annuel', 30000000)*0.04)/1000000:.1f}M$", styles['Normal']))
    story.append(PageBreak())
    
    story.append(Paragraph("Recommandation", styles['Heading2']))
    story.append(Paragraph("Approche progressive 18 mois - 300k$. ROI: 15:1.", styles['Normal']))
    
    doc.build(story)
    buffer.seek(0)
    return buffer
