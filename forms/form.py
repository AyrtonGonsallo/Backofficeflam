from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, HiddenField
from wtforms.validators import DataRequired, Length


class MyForm(FlaskForm):
    form_name = HiddenField(default='connexion')
    identifiant = StringField('Identifiant', validators=[DataRequired()])
    mot_de_passe = PasswordField('Mot de passe', validators=[DataRequired(message="Le mot de passe est requis."),
        Length(min=8, message="Le mot de passe doit contenir au moins 8 caractères.")])
    submit = SubmitField('Se connecter',render_kw={"style": "border:0px;background-color:#e81b20;border-radius:50px;margin-bottom:6px;"})

