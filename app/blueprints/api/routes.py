from flask import jsonify, request
from sympy import Product
from app.models import User
from . import bp as api
from datetime import 

new_user = User(**data)
    eturn jsonify(new_user.to_dict())

@api.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])


@api.route('/users/<id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@api.route('/users', methods=['POST'])
def create_user():
    data = request.json
   
    for field in ['username', 'email', 'password']:
        if field not in data:
            return jsonify({'error': f"You are missing the {field} field"}), 400

    username = data['username']
    email = data['email']
    password = data['password']

    user_exists = User.query.filter((User.username == username)|(User.email == email)).all()
    if user_exists:
        return jsonify({'error': f"User with username {username} or email {email} already exists"}), 400
        
@api.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    if current_user.id != id:
        return jsonify({'error': 'You do not have access to delete this user'}), 403
    user_to_delete = User.query.get_or_404(id)
    user_to_delete.delete()
    return jsonify({}), 204

@api.route('/products')
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@api.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
     if current_user.id != id:
        return jsonify({'error': 'You do not have access to delete this product'}), 403
    product = Product.query.get_or_404(id)
    product.delete()
    return jsonify({}), 204

@api.route('/users/<int:id>', methods=['PUT'])
def updated_user(id):
     if current_user.id != id:
        return jsonify({'error': 'You do not have access to update this user'}), 403
    user = User.query.get_or_404(id)
    data = request.json
    user.update(data)
    return jsonify(user.to_dict())
