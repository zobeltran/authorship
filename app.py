from flask import Flask, request, render_template
from flask_mail import Mail, Message
from os import getenv

app = Flask(__name__)
mail = Mail(app)

# mailServer = getenv('MAIL_SERVER')
# mailPort = getenv('MAIL_PORT')
# mailSSL = getenv('MAIL_USE_SSL')
# mailTSL = getenv('MAIL_USE_TSL')
# mailUsername = getenv('MAIL_USERNAME')
# mailPassword = getenv('MAIL_PASSWORD')
# mailSender = getenv('MAIL_DEFAULT_SENDER')

app.config['MAIL_SERVER'] = 'mail.ideafy-it.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TSL'] = False
app.config['MAIL_USERNAME'] = 'renzobeltran@ideafy-it.com'
app.config['MAIL_PASSWORD'] = 'P@55w0rd1'
app.config['MAIL_DEFAULT_SENDER'] = 'renzobeltran@ideafy-it.com'


@app.route('/', methods=['GET', 'POST'])
def Register():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        msg = Message(("Hi " + name + "<br>" + "<a href='127.0.0.1:5000/registration/confirmpage'>Click here to Confirm</a>"),
                      recipients=[email])
        mail.send(msg)
        return print(email)
        return print(name)
    return render_template('register.html')


@app.route('/sendEmail', methods=['GET', 'POST'])
def sendEmail():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        msg = Message(("Hi " + name + "<br>" + "<a href='127.0.0.1:5000/registration/confirmpage'>Click here to Confirm</a>"),
                      recipients=[email])
        mail.send(msg)
        print(email)
        print(name)
    return render_template('register.html')


@app.route('/registration/confirmpage', methods=['GET', 'POST'])
def confirm():
    return render_template('confirmpage.html')


if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run()