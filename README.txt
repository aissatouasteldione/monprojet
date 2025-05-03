Instructions d'installation du projet Quiz

1. Crée un environnement virtuel :
   python -m venv venv

2. Active-le :
   - Windows : venv\Scripts\activate
   - Linux/macOS : source venv/bin/activate

3. Installe les dépendances :
   pip install -r requirements.txt

4. Initialise la base :
   flask db init
   flask db migrate -m "Initial"
   flask db upgrade

5. Lance le serveur :
   flask run

Accède à : http://localhost:5000
