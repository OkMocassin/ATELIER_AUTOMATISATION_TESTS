# API Choice

- Étudiant : GANDON Léo-Paul
- API choisie : Agify
- URL base : https://api.agify.io
- Documentation officielle / README : https://agify.io
- Auth : None

- Endpoints testés :
  - GET /?name=michael
  - GET /?name=invalidname123

- Hypothèses de contrat (champs attendus, types, codes) :
  - Code HTTP attendu : 200 (requête valide)
  - Content-Type : application/json
  - Champs attendus :
    - name : string
    - age : int (ou null si inconnu)
    - count : int
  - Requête invalide (sans paramètre name) :
    - code HTTP attendu : 400 ou réponse JSON partielle

- Limites / rate limiting connu :
  - API gratuite sans authentification
  - Limite implicite sur le nombre de requêtes (non documentée précisément)
  - Risque de réponse lente en cas de forte utilisation

- Risques (instabilité, downtime, CORS, etc.) :
  - API publique → possible indisponibilité temporaire
  - Latence variable selon charge serveur
  - Données statistiques approximatives
  - Pas de garantie de SLA
