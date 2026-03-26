"""
Script de génération du RAPPORT FINAL COMPLET
Compile tous les apports de l'analyse dans un seul PDF professionnel
"""

import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from io import BytesIO
from datetime import datetime

def generer_rapport_final_complet(profil):
    """
    Génère le rapport final PDF complet avec TOUS les apports
    
    Sections:
    1. Page de garde
    2. Table des matières
    3. Résumé exécutif
    4. Profil organisation
    5. Évaluation maturité
    6. Analyse des risques
    7. Recommandations (triées par budget)
    8. Calendrier détaillé
    9. Budget et ROI
    10. Synthèse et décision
    11. Annexes
    """
    
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.75*inch, bottomMargin=0.75*inch)
    story = []
    styles = getSampleStyleSheet()
    
    # ============================================
    # STYLES PERSONNALISÉS
    # ============================================
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=28,
        textColor=colors.HexColor('#1e40af'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    section_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#1e40af'),
        spaceAfter=15,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    # ============================================
    # 1. PAGE DE GARDE
    # ============================================
    
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("RAPPORT FINAL", title_style))
    story.append(Paragraph("Analyse de Conformité Cybersécurité", styles['Heading2']))
    story.append(Spacer(1, 0.5*inch))
    
    story.append(Paragraph(f"<b>{profil.get('nom', 'Votre Organisation')}</b>", ParagraphStyle('OrgName', parent=styles['Normal'], fontSize=16, alignment=TA_CENTER)))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(f"Secteur: {profil.get('secteur', 'N/A').upper()}", ParagraphStyle('Sector', parent=styles['Normal'], alignment=TA_CENTER)))
    story.append(Spacer(1, 1*inch))
    
    story.append(Paragraph(f"Date: {datetime.now().strftime('%d %B %Y')}", ParagraphStyle('Date', parent=styles['Normal'], alignment=TA_CENTER)))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("CONFIDENTIEL", ParagraphStyle('Confidential', parent=styles['Normal'], textColor=colors.red, fontSize=14, alignment=TA_CENTER, fontName='Helvetica-Bold')))
    
    story.append(PageBreak())
    
    # ============================================
    # 2. TABLE DES MATIÈRES
    # ============================================
    
    story.append(Paragraph("Table des Matières", section_style))
    story.append(Spacer(1, 0.2*inch))
    
    toc = """
    <b>1.</b> Résumé Exécutif ................................................... 3<br/>
    <b>2.</b> Profil de l'Organisation ......................................... 4<br/>
    <b>3.</b> Évaluation de la Maturité Cybersécurité .......................... 5<br/>
    <b>4.</b> Analyse des Risques ............................................... 6<br/>
    <b>5.</b> Recommandations Stratégiques (Triées par Budget) ................. 8<br/>
    <b>6.</b> Calendrier de Mise en Conformité ................................. 10<br/>
    <b>7.</b> Budget et Retour sur Investissement .............................. 12<br/>
    <b>8.</b> Synthèse et Décision Requise ..................................... 13<br/>
    <b>9.</b> Annexes ........................................................... 14
    """
    story.append(Paragraph(toc, styles['Normal']))
    story.append(PageBreak())
    
    # ============================================
    # 3. RÉSUMÉ EXÉCUTIF
    # ============================================
    
    story.append(Paragraph("1. Résumé Exécutif", section_style))
    
    # Calculs
    ca_annuel = profil.get('ca_annuel', 30000000)
    penalite_loi25 = max(25000000, ca_annuel * 0.04)
    penalite_rgpd = max(29000000, ca_annuel * 0.04)
    total_exposition = penalite_loi25 + penalite_rgpd + 1200000
    
    budgets = {'low': 50000, 'medium': 200000, 'high': 500000}
    budget_disponible = budgets.get(profil.get('budget', 'medium'), 200000)
    
    scores_maturite = {'initial': 25, 'managed': 55, 'defined': 75, 'optimized': 95}
    score_conformite = scores_maturite.get(profil.get('maturite', 'managed'), 55)
    
    roi = total_exposition / budget_disponible if budget_disponible > 0 else 0
    
    resume_exec = f"""
    Ce rapport présente une analyse complète de la conformité cybersécurité de <b>{profil.get('nom', 'votre organisation')}</b>
    et propose un plan d'action détaillé adapté à votre budget.
    <br/><br/>
    <b>CONSTATS PRINCIPAUX:</b><br/>
    • Exposition financière totale: <b>{total_exposition/1000000:.1f} M$</b> de risques potentiels<br/>
    • Score de conformité actuel: <b>{score_conformite}%</b> (niveau: {profil.get('maturite', 'managed')})<br/>
    • Conformité Loi 25: <b>REQUISE IMMÉDIATEMENT</b> (exposition {penalite_loi25/1000000:.1f}M$)<br/>
    • Budget disponible: <b>{budget_disponible/1000:.0f}k$</b><br/>
    <br/>
    <b>RECOMMANDATION STRATÉGIQUE:</b><br/>
    Approche <b>{"minimale" if budget_disponible < 100000 else "progressive" if budget_disponible < 400000 else "accélérée"}</b> sur 18-24 mois
    <br/><br/>
    <b>RETOUR SUR INVESTISSEMENT:</b><br/>
    • Protection: {total_exposition/1000000:.1f}M$ de risques évités<br/>
    • Ratio ROI: <b>{roi:.0f}:1</b><br/>
    • Période de retour: < 6 mois<br/>
    <br/>
    <b>DÉCISION REQUISE:</b> Approbation budgétaire et lancement dans les 30 jours.
    """
    story.append(Paragraph(resume_exec, styles['Normal']))
    story.append(PageBreak())
    
    # ============================================
    # 4. PROFIL ORGANISATION
    # ============================================
    
    story.append(Paragraph("2. Profil de l'Organisation", section_style))
    
    profil_data = [
        ['Critère', 'Valeur'],
        ['Nom de l\'organisation', profil.get('nom', 'N/A')],
        ['Secteur d\'activité', profil.get('secteur', 'N/A')],
        ['Taille', profil.get('taille', 'N/A')],
        ['Chiffre d\'affaires annuel', profil.get('ca', 'N/A')],
        ['Budget conformité disponible', profil.get('budget', 'N/A')],
        ['Niveau de maturité cybersécurité', profil.get('maturite', 'N/A')],
        ['Type d\'infrastructure', profil.get('infrastructure', 'N/A')]
    ]
    
    t = Table(profil_data, colWidths=[3*inch, 3.5*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e40af')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t)
    story.append(PageBreak())
    
    # ============================================
    # 5. ÉVALUATION MATURITÉ
    # ============================================
    
    story.append(Paragraph("3. Évaluation de la Maturité Cybersécurité", section_style))
    
    maturite_text = f"""
    <b>Niveau actuel:</b> {profil.get('maturite', 'managed').upper()}<br/>
    <b>Score de conformité:</b> {score_conformite}%<br/>
    <b>Probabilité d'incident:</b> {['85%', '65%', '40%', '15%'][['initial', 'managed', 'defined', 'optimized'].index(profil.get('maturite', 'managed'))]}
    <br/><br/>
    <b>Signification:</b><br/>
    """
    
    maturite_descriptions = {
        'initial': 'Organisation réactive sans processus formels. Risque élevé (85% probabilité incident).',
        'managed': 'Processus de base en place mais non documentés. Risque moyen-élevé (65% probabilité).',
        'defined': 'Processus documentés et suivis. Équipe sécurité dédiée. Risque modéré (40% probabilité).',
        'optimized': 'Excellence opérationnelle. Certification ISO 27001. Risque faible (15% probabilité).'
    }
    
    maturite_text += maturite_descriptions.get(profil.get('maturite', 'managed'), '')
    
    story.append(Paragraph(maturite_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>Recommandation:</b> Objectif d'atteindre le niveau DÉFINI (75% conformité) dans les 18 prochains mois.", styles['Normal']))
    story.append(PageBreak())
    
    # ============================================
    # 6. ANALYSE DES RISQUES
    # ============================================
    
    story.append(Paragraph("4. Analyse des Risques de Non-Conformité", section_style))
    
    risques_text = f"""
    <b>EXPOSITION FINANCIÈRE TOTALE: {total_exposition/1000000:.1f} M$</b>
    <br/><br/>
    <b>Détail par réglementation:</b><br/>
    <br/>
    <b>1. Loi 25 (Québec) - {penalite_loi25/1000000:.1f} M$</b><br/>
    • Pénalité maximale: Maximum entre 25M$ et 4% du CA mondial<br/>
    • Votre exposition: {penalite_loi25/1000000:.1f}M$ (CA {ca_annuel/1000000:.0f}M$ × 4% = {ca_annuel*0.04/1000000:.1f}M$)<br/>
    • <b>STATUT: OBLIGATOIRE</b> - Conformité requise immédiatement<br/>
    <br/>
    <b>2. RGPD (Europe) - {penalite_rgpd/1000000:.1f} M$</b><br/>
    • Si clients ou opérations en Union Européenne<br/>
    • Pénalité: Maximum entre 20M€ et 4% du CA mondial<br/>
    • Application extraterritoriale<br/>
    <br/>
    <b>3. PCI DSS (Paiements carte) - 1.2 M$/an</b><br/>
    • Si traitement de paiements par carte<br/>
    • Amendes: 5,000$ - 100,000$ par mois<br/>
    • Révocation possible du droit de traiter les paiements<br/>
    <br/>
    <b>CONSÉQUENCES D'UN INCIDENT:</b><br/>
    • Coûts directs: Amendes réglementaires<br/>
    • Coûts indirects: Perte de revenus (50k$-500k$/jour d'arrêt)<br/>
    • Réputation: Perte de confiance clients (-25% ventes)<br/>
    • Assurance: Augmentation primes (+150%)<br/>
    <br/>
    <b>RECOMMANDATION:</b> Prioriser la mise en conformité Loi 25 (exposit ion {penalite_loi25/1000000:.1f}M$).
    """
    story.append(Paragraph(risques_text, styles['Normal']))
    story.append(PageBreak())
    
    # ============================================
    # 7. RECOMMANDATIONS (TRIÉES PAR BUDGET)
    # ============================================
    
    story.append(Paragraph("5. Recommandations Stratégiques", section_style))
    story.append(Paragraph("(Actions triées par faisabilité budgétaire)", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph(f"<b>Budget disponible: {budget_disponible/1000:.0f}k$</b>", styles['Normal']))
    story.append(Spacer(1, 0.15*inch))
    
    # Actions prioritaires
    actions = [
        ('Politique confidentialité Loi 25', '2 sem', 5, 'Critique'),
        ('Formation employés cybersécurité', '2 sem', 5, 'Haute'),
        ('MFA + Contrôles d\'accès', '3 sem', 8, 'Critique'),
        ('Registre traitements données', '4 sem', 15, 'Haute'),
        ('ÉFVP (Évaluation vie privée)', '6 sem', 25, 'Haute'),
        ('Audit sécurité externe', '1 mois', 30, 'Moyenne'),
        ('Déploiement SIEM', '3 mois', 45, 'Moyenne'),
        ('Plan réponse incidents', '1 mois', 12, 'Haute')
    ]
    
    # Séparer actions dans budget
    budget_cumule = 0
    actions_ok = []
    actions_ko = []
    
    for action in sorted(actions, key=lambda x: x[2]):  # Tri par coût
        if budget_cumule + action[2]*1000 <= budget_disponible:
            actions_ok.append(action)
            budget_cumule += action[2]*1000
        else:
            actions_ko.append(action)
    
    # Tableau actions DANS budget
    story.append(Paragraph(f"<b>ACTIONS RÉALISABLES (dans budget {budget_disponible/1000:.0f}k$):</b>", styles['Normal']))
    story.append(Spacer(1, 0.1*inch))
    
    actions_table_data = [['#', 'Action', 'Délai', 'Coût (k$)', 'Priorité']]
    for i, action in enumerate(actions_ok, 1):
        actions_table_data.append([str(i), action[0], action[1], str(action[2]), action[3]])
    
    t = Table(actions_table_data, colWidths=[0.4*inch, 2.8*inch, 0.8*inch, 0.8*inch, 0.8*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#10b981')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgreen),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph(f"<b>Budget utilisé: {budget_cumule/1000:.0f}k$ / {budget_disponible/1000:.0f}k$</b>", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Actions HORS budget
    if actions_ko:
        story.append(Paragraph(f"<b>ACTIONS DIFFÉRÉES (budget additionnel requis: {sum(a[2] for a in actions_ko):.0f}k$):</b>", styles['Normal']))
        story.append(Spacer(1, 0.1*inch))
        
        for action in actions_ko:
            story.append(Paragraph(f"• {action[0]} ({action[2]}k$) - {action[3]}", styles['Normal']))
    
    story.append(PageBreak())
    
    # ============================================
    # 8. CALENDRIER
    # ============================================
    
    story.append(Paragraph("6. Calendrier de Mise en Conformité", section_style))
    
    calendrier_text = """
    <b>DURÉE TOTALE: 18-24 mois</b>
    <br/><br/>
    <b>Phase 1: FONDATIONS (Mois 0-6) - 105k$</b><br/>
    • Analyse GAP et évaluation initiale<br/>
    • Politique de confidentialité Loi 25<br/>
    • Formation sensibilisation employés<br/>
    • Déploiement MFA et chiffrement<br/>
    • Registre des traitements de données<br/>
    <b>Livrable clé:</b> Conformité minimale Loi 25 atteinte<br/>
    <br/>
    <b>Phase 2: RENFORCEMENT (Mois 6-14) - 120k$</b><br/>
    • Déploiement SIEM et monitoring<br/>
    • Audits de sécurité réguliers<br/>
    • Plan de réponse aux incidents<br/>
    • Processus matures et documentés<br/>
    <b>Livrable clé:</b> Contrôles avancés opérationnels<br/>
    <br/>
    <b>Phase 3: OPTIMISATION (Mois 14-18) - 75k$</b><br/>
    • Préparation certification ISO 27001<br/>
    • Tests de pénétration<br/>
    • Automatisation des processus<br/>
    • Amélioration continue<br/>
    <b>Livrable clé:</b> Certification ISO 27001 obtenue<br/>
    <br/>
    <b>JALONS IMPORTANTS:</b><br/>
    • Mois 6: Conformité Loi 25 ✓<br/>
    • Mois 12: Contrôles complets ✓<br/>
    • Mois 18: Certification ISO ✓
    """
    story.append(Paragraph(calendrier_text, styles['Normal']))
    story.append(PageBreak())
    
    # ============================================
    # 9. BUDGET ET ROI
    # ============================================
    
    story.append(Paragraph("7. Budget et Retour sur Investissement", section_style))
    
    budget_table_data = [
        ['Phase', 'Durée', 'Budget', '% Total'],
        ['Phase 1: Fondations', '6 mois', '105k$', '35%'],
        ['Phase 2: Renforcement', '8 mois', '120k$', '40%'],
        ['Phase 3: Optimisation', '6 mois', '75k$', '25%'],
        ['TOTAL', '18-24 mois', '300k$', '100%']
    ]
    
    t = Table(budget_table_data, colWidths=[2.2*inch, 1.2*inch, 1.2*inch, 1*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e40af')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#fef3c7')),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.3*inch))
    
    roi_text = f"""
    <b>RETOUR SUR INVESTISSEMENT (ROI):</b><br/>
    <br/>
    • Investissement total: <b>300k$</b> sur 18 mois<br/>
    • Risques évités: <b>{total_exposition/1000000:.1f}M$</b><br/>
    • Ratio ROI: <b>{roi:.0f}:1</b><br/>
    • Période de retour: <b>< 6 mois</b><br/>
    <br/>
    <b>BÉNÉFICES ADDITIONNELS:</b><br/>
    • Réduction prime d'assurance: -30% à -50%<br/>
    • Confiance clients renforcée<br/>
    • Avantage concurrentiel (certification)<br/>
    • Conformité réglementaire assurée<br/>
    • Réduction probabilité d'incident: 65% → 15%
    """
    story.append(Paragraph(roi_text, styles['Normal']))
    story.append(PageBreak())
    
    # ============================================
    # 10. SYNTHÈSE ET DÉCISION
    # ============================================
    
    story.append(Paragraph("8. Synthèse et Décision Requise", section_style))
    
    synthese_text = f"""
    <b>SITUATION ACTUELLE:</b><br/>
    {profil.get('nom', 'Votre organisation')} est exposé à {total_exposition/1000000:.1f}M$ de risques de non-conformité,
    avec une probabilité d'incident de 65% au niveau de maturité actuel.
    <br/><br/>
    <b>RECOMMANDATION STRATÉGIQUE:</b><br/>
    Approche progressive sur 18-24 mois avec investissement de 300k$.
    Cette stratégie maximise le ROI ({roi:.0f}:1) tout en respectant les contraintes budgétaires.
    <br/><br/>
    <b>ACTIONS IMMÉDIATES (30 JOURS):</b><br/>
    1. <b>Approbation budgétaire:</b> 300k$ sur 18 mois<br/>
    2. <b>Nomination sponsor exécutif:</b> Membre direction engagé<br/>
    3. <b>Lancement projet:</b> Analyse GAP et Quick Wins<br/>
    4. <b>Constitution équipe:</b> Responsable projet + équipe IT<br/>
    <br/>
    <b>CONSÉQUENCES DE L'INACTION:</b><br/>
    • Exposition continue à {total_exposition/1000000:.1f}M$ de risques<br/>
    • Probabilité d'incident maintenue à 65%<br/>
    • Non-conformité Loi 25 (pénalités jusqu'à {penalite_loi25/1000000:.1f}M$)<br/>
    • Perte potentielle de clients et partenaires<br/>
    <br/>
    <b>DÉCISION REQUISE:</b><br/>
    Ce rapport nécessite une décision de la direction dans les <b>2 prochaines semaines</b>.
    Chaque mois de retard augmente l'exposition aux risques et les coûts de mise en conformité.
    """
    story.append(Paragraph(synthese_text, styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    # Signature
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("_" * 50, styles['Normal']))
    story.append(Paragraph("Signature du responsable IT / Conformité", styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Date: _______________", styles['Normal']))
    
    story.append(PageBreak())
    
    # ============================================
    # 11. ANNEXES
    # ============================================
    
    story.append(Paragraph("9. Annexes", section_style))
    
    annexes_text = """
    <b>A. Références réglementaires</b><br/>
    • Loi 25 (Québec): Loi modernisant des dispositions législatives en matière de protection des renseignements personnels<br/>
    • RGPD: Règlement Général sur la Protection des Données (UE)<br/>
    • ISO 27001: Norme internationale de gestion de la sécurité de l'information<br/>
    • NIST CSF: Framework de cybersécurité du National Institute of Standards and Technology<br/>
    <br/>
    <b>B. Définitions</b><br/>
    • <b>ÉFVP:</b> Évaluation des Facteurs relatifs à la Vie Privée<br/>
    • <b>MFA:</b> Multi-Factor Authentication (authentification à plusieurs facteurs)<br/>
    • <b>SIEM:</b> Security Information and Event Management<br/>
    • <b>ROI:</b> Return On Investment (retour sur investissement)<br/>
    • <b>Pentest:</b> Test de pénétration (simulation d'attaque)<br/>
    <br/>
    <b>C. Contacts</b><br/>
    Pour toute question sur ce rapport, contactez:<br/>
    • Responsable IT / Conformité de l'organisation<br/>
    • Email: [à compléter]<br/>
    • Téléphone: [à compléter]<br/>
    <br/>
    <b>D. Sources des données</b><br/>
    • Profil organisationnel: Configuré par l'utilisateur<br/>
    • Pénalités réglementaires: Textes officiels Loi 25 et RGPD<br/>
    • Budgets estimés: Moyennes marché québécois 2024-2025<br/>
    • Probabilités d'incident: CMMI et NIST frameworks<br/>
    • ROI: Calculs basés sur exposition vs investissement<br/>
    <br/>
    <b>FIN DU RAPPORT</b>
    """
    story.append(Paragraph(annexes_text, styles['Normal']))
    
    # Footer final
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("_" * 80, styles['Normal']))
    story.append(Paragraph(f"Rapport généré par CyberConform Dashboard - {datetime.now().strftime('%d/%m/%Y à %H:%M')}", 
                          ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, textColor=colors.grey)))
    story.append(Paragraph("© 2026 - Document confidentiel", 
                          ParagraphStyle('Footer2', parent=styles['Normal'], fontSize=8, textColor=colors.grey)))
    
    # Générer le PDF
    doc.build(story)
    buffer.seek(0)
    return buffer
