''' Log in form '''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """When the browser sends the POST request as a result of pressing submit,
    form.validate_on_submit() gathers all the data, runs the validators,
    and  will return True, indicating that the data is valid.
    If one field fails validation, then the function will return False,
    causing the form to be rendered back to the user, like with GET."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
