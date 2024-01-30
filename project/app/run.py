from flask_bootstrap import Bootstrap
from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'my key'

#create a Form Class
# class NamerForm(FlaskForm):
#     name = StringField('What`s Your Name', validators=[DataRequired()])
#     submit = SubmitField('Submit')

@app.route('/')
def index():
    first_name = 'John'
    stuff = 'This is a bold text'
    
    favourite_pizza = ['Pepperoni', 'Cheese', 'Margarita']
    return render_template('index.html',
                           first_name=first_name,
                           stuff=stuff,
                           favourite_pizza=favourite_pizza)
#localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

#Create Custom Error Pages

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

#Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    #Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('name.html',
                           name=name,
                           form=form)

if __name__ == '__main__':
    app.run(debug=True)
