from flask import render_template, abort
from flask_login import login_required, current_user

from . import admin

@admin.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_admin:
        abort(403)

    return render_template('admin/dashboard.html', title="Admin Dashboard")