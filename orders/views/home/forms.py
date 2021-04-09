
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
    BooleanField,
    SelectField,
    RadioField,
)
from wtforms.fields.html5 import DateField, TimeField, IntegerField
from wtforms.widgets.html5 import NumberInput
from wtforms.validators import DataRequired, Length

class OrderForm(FlaskForm):
    vendor  = SelectField('Vendors', choices=[])
    part = StringField("Part / Model #", validators=[DataRequired(), Length(min=2, max=50)])
    quantity = IntegerField('Quantity', widget=NumberInput(min=1, max=1000))
    enduser = StringField("Specific End User")
    extra_details = TextAreaField("Extra Details")
    specs = TextAreaField("Specification Requirements")
    submit2 = SubmitField("Submit")


