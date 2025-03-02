from flask import Blueprint, render_template
from app.models import Men, Women, Kids, Accessories, Shoes  # Correct import

# Define Blueprint for views
views_bp = Blueprint('views', __name__)

# Index route to display products
@views_bp.route('/')
def index():
    # Query all products from different categories
    products_men = Men.query.all()
    products_women = Women.query.all()
    products_kids = Kids.query.all()
    products_accessories = Accessories.query.all()
    products_shoes = Shoes.query.all()  # Correct Shoes model reference

    # Combine all products into one list
    all_products = products_men + products_women + products_kids + products_accessories + products_shoes

    # Render the homepage template and pass the products to the template
    return render_template('index.html', products=all_products)

@views_bp.route('/men')
def men():
    products_men = Men.query.all()
    return render_template('men.html', products=products_men, category="Men")

@views_bp.route('/women')
def women():
    products_women = Women.query.all()
    return render_template('women.html', products=products_women, category="Women")

@views_bp.route('/kids')
def kids():
    products_kids = Kids.query.all()
    return render_template('kids.html', products=products_kids, category="Kids")

@views_bp.route('/accessories')
def accessories():
    products_accessories = Accessories.query.all()
    return render_template('accessories.html', products=products_accessories, category="Accessories")

@views_bp.route('/shoes')
def shoes():
    products_shoes = Shoes.query.all()  # Correct query
    return render_template('shoes.html', products=products_shoes, category="Shoes")




