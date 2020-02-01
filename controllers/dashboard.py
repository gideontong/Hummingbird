from flask import Blueprint, render_template, abort

dashboard = Blueprint('dashboard', __name__,
                        template_folder='templates')

@dashboard.route('/dashboard')
def show():
    return render_template('pages/dashboard.html', size = 500, mfRatio = 99, meanTc = 5000000)