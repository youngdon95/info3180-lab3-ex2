"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for,flash
from forms import UserForm
import smtplib
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

   
@app.route('/contact/',methods=['GET','POST'])
def contact():
    user_form = UserForm()
    #form = ContactForm(csrf_enabled=False)
    if request.method=='POST':
         if user_form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html',form=user_form)

         else:
            fromname = user_form.name.data
            fromaddr = user_form.email.data
            subject = user_form.subject.data
            msg = user_form.message.data
            send_email(fromname,fromaddr,subject,msg)
            message1="Messgae was sent %s"%fromname
            return render_template('home.html',message1=message1)
            
            
    elif request.method=='GET':
         return render_template('contact.html', form=user_form)
   
def send_email(from_name, from_email, subject, msg):
    
    receivers = 'romarioomartin@gmail.com'

    to_name="AlkaVybz"
    message = """From: {} <{}>
To: {} <{}> 
Subject: {}
{}
""" 

    #message_to_send1 = message.format(from_name,from_email,to_name,receivers,subject,msg) 
    message_to_send3 = message.format(

                             from_name,

                             from_email,

                             to_name,

                             receivers,

                             subject,

                             msg)

    username = ''
    password = ''   
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, receivers, message_to_send3)
   
    server.quit()
    
# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
    
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
