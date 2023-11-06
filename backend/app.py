from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from users import users
from products import products

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    for user in users:
        if user['username'] == username and user['password'] == password:
            return jsonify({'message': 'Inicio de sesión exitoso'})

    return jsonify({'message': 'Datos Incorrectos'}), 401

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify({'products': products})

# @app.route('/api/products/<category>', methods=['GET'])
# def filter_products(category):
#     filtered_products = [product for product in products if product['category'] == category]
#     return jsonify({'products': filtered_products})

@app.route('/api/products/filter', methods=['POST'])
def filter_products():
    data = request.get_json()
    search_term = data.get('searchTerm', '').lower()
    
    filtered_products = [product for product in products if search_term in product['name'].lower()]

    return jsonify(filtered_products)


if __name__ == '__main__':
    app.run(debug=True)
