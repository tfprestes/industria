# app/routes/call_routes.py
from flask import Blueprint, render_template, request, redirect, url_for

call_bp = Blueprint('calls', __name__)

@call_bp.route('/')
def list_calls():
    calls = [] # Placeholder
    return render_template('calls/list.html', calls=calls)
