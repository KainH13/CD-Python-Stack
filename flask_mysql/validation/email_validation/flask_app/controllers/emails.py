# name should be plural
from flask_app import app
from flask import  render_template, redirect, request, session, flash
from flask_app.models.email import Email

@app.route('/')
def email_form():
    return render_template('email_form.html')

@app.route('/validate', methods=["POST"])
def validate():
    data = {
        "email": request.form["email"]
    }
    emails = Email.get_all()
    used_emails = []
    for entry in emails:
        print(entry.email)
        used_emails.append(entry.email)
    if not Email.validate_email(request.form, used_emails):
        return redirect('/')
    Email.create(data)
    return redirect('/success')

@app.route('/success')
def success_page():
    emails = Email.get_all()
    return render_template('success.html', emails=emails)

@app.route('/delete', methods=['POST'])
def delete_email():
    data = {
        "id": request.form['id']
    }
    Email.remove(data)
    return redirect('/success')