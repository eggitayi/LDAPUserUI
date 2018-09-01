from flask_user.forms import FlaskForm,StringField,validators,SubmitField,_

class EditUserProfileForm(FlaskForm):

    displayName = StringField(_('Display Name'), validators=[validators.DataRequired()])

    submit = SubmitField(_('Update'))