from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, EmailField, SelectMultipleField
from wtforms.validators import DataRequired
from wtforms.widgets import CheckboxInput, ListWidget

class FormEditUser(FlaskForm):
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
    role = SelectField('Role',choices=[ ] ,validators=[DataRequired()])
    submit = SubmitField('Modifier')
