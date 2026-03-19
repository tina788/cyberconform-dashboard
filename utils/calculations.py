"""
Fonctions de calcul pour l'assistant de conformité cybersécurité
"""

def formater_cout(montant):
    """Formate un montant en dollars canadiens"""
    if montant >= 1000000:
        return f"{montant / 1000000:.1f}M$"
    elif montant >= 1000:
        return f"{montant / 1000:.0f}K$"
    else:
        return f"{montant:.0f}$"

def calculer_economies(economies_selectionnees, economies_data):
    """Calcule le total des économies"""
    total = 0
    for key in economies_selectionnees:
        if key in economies_data:
            total += economies_data[key]['economie']
    return total

def filtrer_referentiels_applicables(referentiels_data, profil):
    """Filtre les référentiels applicables selon le profil"""
    secteur = profil['secteur']
    taille = profil['taille']
    
    obligatoires = []
    optionnels = []
    
    for ref_id, ref in referentiels_data.items():
        # Vérifier si obligatoire
        if secteur in ref['obligatoire_pour']:
            obligatoires.append({
                'id': ref_id,
                'name': ref['name'],
                'description': ref['description'],
                'cout_minimal': ref['couts']['minimal'],
                'cout_standard': ref['couts']['standard'],
                'cout_maximal': ref['couts']['maximal']
            })
        # Vérifier si applicable (optionnel)
        elif (secteur in ref['applicabilite']['secteurs'] and 
              taille in ref['applicabilite']['tailles']):
            optionnels.append({
                'id': ref_id,
                'name': ref['name'],
                'description': ref['description'],
                'cout_minimal': ref['couts']['minimal'],
                'cout_standard': ref['couts']['standard'],
                'cout_maximal': ref['couts']['maximal']
            })
    
    return obligatoires, optionnels

def calculer_budget_disponible(niveau_budget):
    """Retourne le montant de budget selon le niveau"""
    budgets = {
        'low': 50000,
        'medium': 150000,
        'high': 300000
    }
    return budgets.get(niveau_budget, 50000)

def generer_recommandations(obligatoires, optionnels, economies, budget_niveau):
    """Génère les recommandations personnalisées"""
    
    # Calculer les totaux
    total_minimal = sum(ref['cout_minimal'] for ref in obligatoires) - economies
    total_standard = sum(ref['cout_standard'] for ref in obligatoires) - economies
    total_maximal = sum(ref['cout_maximal'] for ref in obligatoires) - economies
    
    # Ajuster si négatif
    total_minimal = max(0, total_minimal)
    total_standard = max(0, total_standard)
    total_maximal = max(0, total_maximal)
    
    # Budget disponible
    budget_montant = calculer_budget_disponible(budget_niveau)
    
    # Calculer ce qui reste ou dépasse
    reste_minimal = budget_montant - total_minimal
    reste_standard = budget_montant - total_standard
    reste_maximal = budget_montant - total_maximal
    
    recommandations = {
        'obligatoires': obligatoires,
        'optionnels': optionnels,
        'totaux': {
            'minimal': total_minimal,
            'standard': total_standard,
            'maximal': total_maximal
        },
        'budget': {
            'montant': budget_montant,
            'minimal': {
                'reste': max(0, reste_minimal),
                'montant_depassement': max(0, -reste_minimal),
                'depasse': reste_minimal < 0
            },
            'standard': {
                'reste': max(0, reste_standard),
                'montant_depassement': max(0, -reste_standard),
                'depasse': reste_standard < 0
            },
            'maximal': {
                'reste': max(0, reste_maximal),
                'montant_depassement': max(0, -reste_maximal),
                'depasse': reste_maximal < 0
            }
        }
    }
    
    return recommandations
