from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField, SelectMultipleField
from wtforms.validators import DataRequired


class FormAddCours(FlaskForm):
    heure = TimeField('heure', validators=[DataRequired()])
    jour = SelectField('jour',choices=[("Lundi", "Lundi"), ("Mardi", "Mardi"), ("Mercredi", "Mercredi"),
                 ("Jeudi", "Jeudi"), ("Vendredi", "Vendredi"), ("Samedi", "Samedi"),
                 ("Dimanche", "Dimanche")],validators=[DataRequired()])
    dojoId = SelectField('dojo', choices=[],coerce=int, validators=[DataRequired()])
    profsId = SelectMultipleField(
        'professeurs',
        choices=[],  # rempli dynamiquement dans ta vue
        coerce=int,  # important pour recevoir des entiers
        validators=[DataRequired()]
    )
    categorie_age = SelectMultipleField(
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
