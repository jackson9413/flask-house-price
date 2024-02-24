from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class UserInputForm(FlaskForm):
    num_bedrooms = IntegerField('Number of Bedrooms', validators=[DataRequired()])
    num_bathrooms = IntegerField('Number of Bathrooms', validators=[DataRequired()])
    sqft_living = IntegerField('Square Footage of Living Space', validators=[DataRequired()])
    sqft_above = IntegerField('Square Footage of Lot', validators=[DataRequired()])
    sqft_basement = IntegerField('Square Footage of Basement', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit')
    