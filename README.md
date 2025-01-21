# Godot DWH Project

## Outil utilisé pour la collecte des données
- **Outil choisi** : GitHub API REST
- **Documentation officielle** : [GitHub REST API](https://docs.github.com/fr/rest)

## Sources de données identifiées
1. **Stars**  
   - Endpoint : `GET /repos/{owner}/{repo}`
   - Description : Récupération du nombre total d'étoiles sur le dépôt.

2. **Forks**  
   - Endpoint : `GET /repos/{owner}/{repo}`
   - Description : Récupération du nombre total de forks.

3. **Contributeurs actifs**  
   - Endpoint : `GET /repos/{owner}/{repo}/contributors`
   - Description : Récupération des contributeurs actifs et de leur nombre de contributions.

4. **Releases (Versions)**  
   - Endpoint : `GET /repos/{owner}/{repo}/releases`
   - Description : Récupération des versions publiées et de leurs descriptions.

5. **Téléchargements des assets**  
   - Endpoint : `GET /repos/{owner}/{repo}/releases/assets`
   - Description : Récupération du nombre de téléchargements pour chaque asset publié.

6. **Commits**  
   - Endpoint : `GET /repos/{owner}/{repo}/commits`
   - Description : Récupération des commits et de leurs métadonnées.

7. **Issues**  
   - Endpoint : `GET /repos/{owner}/{repo}/issues`
   - Description : Récupération des issues ouvertes et fermées.

8. **Trafic des visiteurs**  
   - Endpoint : `GET /repos/{owner}/{repo}/traffic/views`
   - Description : Récupération du trafic des visiteurs du dépôt.

9. **Pull Requests**  
   - Endpoint : `GET /repos/{owner}/{repo}/pulls`
   - Description : Récupération des pull requests et de leurs métadonnées.
