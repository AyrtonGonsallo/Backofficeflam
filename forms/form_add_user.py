from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, EmailField, SelectMultipleField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import CheckboxInput, ListWidget


class FormAddUser(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    prenom = StringField('prenom', validators=[DataRequired()])
    email = EmailField('email', )
    dojos = SelectMultipleField(
        'Dojo(s)',
        choices=[],  # à remplir dans la vue
        coerce=int,  # valeurs numériques
        option_widget=CheckboxInput(),
        widget=ListWidget(prefix_label=False)
    )
    mot_de_passe = PasswordField('Mot de passe', validators=[DataRequired(message="Le mot de passe est requis."),
        Length(min=8, message="Le mot de passe doit contenir au moins 8 caractères.")])
    role = SelectField('Role',choices=[ ] ,validators=[DataRequired()])
    submit = SubmitField('Ajouter')
