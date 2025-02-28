from flask import Blueprint, render_template
from app.models import db, Product  # Import db and Product from models
import time

views_bp = Blueprint('views', __name__, template_folder='templates')

@views_bp.route('/')
def index():
    return render_template('index.html',now=int(time.time()))

@views_bp.route('/women')
def women():
    
    return render_template("women.html")

@views_bp.route('/men')
def men():
    
    return render_template("men.html")


@views_bp.route('/kids')
def kids():
    
    return render_template("kids.html")


@views_bp.route('/accessories')
def accessories():
    
    return render_template("accessories.html")


@views_bp.route('/shoes')
def shoes():
    
    return render_template("kids.html")



