from flask import Flask, jsonify, request
from flask_cors import CORS
from users import users
from products import products
from cart import cart

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

@app.route('/api/products/<int:id>', methods=['GET'])
def get_product_id(id):
    productFound = [product for product in products if product['id'] == id]
    if (len(productFound) > 0):
        return jsonify({'product': productFound[0]})
    return jsonify({'message': 'Producto no encontrado'})

@app.route('/api/cart', methods=['GET'])
def get_cart():
    return jsonify({'cart': cart})

@app.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product = data.get('product')
    quantity = data.get('quantity')
    
    for item in cart:
        if item['product']['id'] == product['id']:
            item['quantity'] += quantity
            return jsonify({'message': 'Cantidad actualizada en el carrito'})
    cart.append({'product': product, 'quantity': quantity})
    return jsonify({'message': 'Producto agregado al carrito'})

@app.route('/api/cart/remove/<int:id>', methods=['DELETE'])
def remove_from_cart(id):
    for item in cart:
        if item['product']['id'] == id:
            cart.remove(item)
            return jsonify({'message': 'Producto eliminado del carrito'})
    return jsonify({'message': 'Producto no encontrado en el carrito'}, 404)

if __name__ == '__main__':
    app.run(debug=True)