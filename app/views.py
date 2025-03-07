from flask import Blueprint, render_template, request, redirect, url_for
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
    products_shoes = Shoes.query.all()

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
    products_shoes = Shoes.query.all()
    return render_template('shoes.html', products=products_shoes, category="Shoes")

@views_bp.route('/product/<int:product_id>')
def product_details(product_id):
    # Check all tables for the product
    product = (Men.query.get(product_id) or
               Women.query.get(product_id) or
               Kids.query.get(product_id) or
               Accessories.query.get(product_id) or
               Shoes.query.get(product_id))

    if not product:
        return render_template('404.html'), 404  # Return a 404 error if the product is not found

    return render_template('productdetails.html', product=product)

@views_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').strip().lower()
    if not query:
        return redirect(url_for('views.index'))

    # Fetch all products from different categories
    products_men = Men.query.filter(Men.name.ilike(f"%{query}%") | Men.description.ilike(f"%{query}%")).all()
    products_women = Women.query.filter(Women.name.ilike(f"%{query}%") | Women.description.ilike(f"%{query}%")).all()
    products_kids = Kids.query.filter(Kids.name.ilike(f"%{query}%") | Kids.description.ilike(f"%{query}%")).all()
    products_accessories = Accessories.query.filter(Accessories.name.ilike(f"%{query}%") | Accessories.description.ilike(f"%{query}%")).all()
    products_shoes = Shoes.query.filter(Shoes.name.ilike(f"%{query}%") | Shoes.description.ilike(f"%{query}%")).all()

    # Combine results
    all_products = products_men + products_women + products_kids + products_accessories + products_shoes

    return render_template('search.html', query=query, products=all_products)
