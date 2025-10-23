from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField, SelectMultipleField, EmailField, DateField
from wtforms.validators import DataRequired, Regexp


class FormAddAdherent(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    prenom = StringField('prenom', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    telephone = StringField('telephone', validators=[DataRequired(),Regexp(
            r'^(0|\+33)*[1-9](\d{2}){4}$',
            message="Numéro de téléphone invalide. Format attendu : 0601020304 ou +33601020304"
        )])
    date_inscription = DateField('date d\'inscription', validators=[DataRequired()])
    dojoId = SelectField('dojo', choices=[],coerce=int, validators=[DataRequired()])
    coursId = SelectMultipleField(
        'cours',
        choices=[],  # rempli dynamiquement dans ta vue
        coerce=int,  # important pour recevoir des entiers
        validators=[DataRequired()]
    )
    categorie_age = SelectField(
        "catégorie d'âge",
        choices=[
            ("baby", "Baby"),
            ("éveil", "Éveil"),
            ("mini-poussins", "Mini-Poussins"),
            ("poussins", "Poussins"),
            ("benjamins", "Benjamins"),
            ("minimes", "Minimes"),
            ("kick-boxing-enfants", "Kick-Boxing Enfants"),
            ("boxe-anglaise-enfants", "Boxe Anglaise Enfants"),

            # Adultes
            ("kick-boxing-mixte", "Kick-Boxing Mixte"),
            ("kick-boxing-femmes", "Kick-Boxing Femmes"),
            ("kick-boxing-hommes", "Kick-Boxing Hommes"),
            ("boxe-anglaise", "Boxe Anglaise"),
            ("judo-adultes", "Judo Adultes"),
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Ajouter')
