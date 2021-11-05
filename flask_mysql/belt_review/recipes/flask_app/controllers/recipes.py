from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/dashboard')
def success_page():
    if 'user_id' not in session:
        return redirect('user/logout')
    data = {
            "id": session['user_id']
        }
    user = User.get_user_by_id(data)
    return render_template('dashboard.html', user=user[0])
