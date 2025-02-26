from flask import Blueprint, render_template
from .models import Product

 # Import your Product model
from apps import db  # Import database instance

views_bp = Blueprint('views', __name__, template_folder='templates')

@views_bp.route('/')
def index():
    
    products = Product.query.all()  # Fetch all products
    return render_template('index.html', products=products)

@views_bp.route('/women')
def women():
   
    products = Product.query.filter_by(category='Women').all()
    return render_template('women.html', products=products)

@views_bp.route('/wishlist')
def wishlist():
   
    wishlist_items = Product.query.filter(Product.sale == True).all()  # Example: fetching sale items
    return render_template('wishlist.html', products=wishlist_items)

@views_bp.route('/product/<int:product_id>')
def product_detail(product_id):
   
    product = Product.query.get_or_404(product_id)
    return render_template('productdetail.html', product=product)


 
