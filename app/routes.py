from flask import render_template, redirect, url_for, session
from .forms import LoginForm
from .models import User, Question
from werkzeug.security import check_password_hash
from .app_init import db


# Déplacer l'import de db dans les fonctions de route pour éviter l'import circulaire
def login():
    form = LoginForm()  # Créer une instance du formulaire
    if form.validate_on_submit():  # Si le formulaire est validé
        user = User.query.filter_by(username=form.username.data).first()  # Rechercher l'utilisateur par son nom d'utilisateur
        if user and check_password_hash(user.password, form.password.data):  # Vérifier le mot de passe
            session['user'] = user.username  # Stocker le nom de l'utilisateur dans la session
            return redirect(url_for('quiz'))  # Rediriger vers la page du quiz
        else:
            # Si l'utilisateur ou le mot de passe est incorrect
            return render_template('login.html', form=form, error="Identifiants incorrects.")
    return render_template('login.html', form=form)  # Afficher le formulaire de connexion

def quiz():
    from .app_init import db  # Import de db ici aussi
    question = Question.query.first()
    return render_template('quiz.html', question=question)

def result():
    return render_template('result.html')
