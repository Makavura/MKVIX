#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

orders = [
    {
        'id': 1,
        'meal': 'ugali',
        'price': 700,
        'description': 'staple meal',
        'address': 'sete street',
        'delivered': False
    },
    {
        'id': 2,
        'meal': 'sphagetti',
        'price': 550,
        'delivered': False,
        'description': 'chakula ya watoto',
        'address': 'Yoyo street'
    }
]


@app.route('/')
def index():
    return "Welcome To Fast Food Fast - A Delivery Service App!"


@app.route('/orders/api/v1/orders/', methods=['GET'])
def get_orders():
    return make_response(jsonify({'orders': orders}), 200)


@app.route('/orders/api/v1/orders/<int:order_id>/', methods=['GET'])
def get_order(order_id):
    order = [order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    return make_response(jsonify({'order': order[0]}), 200)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/orders/api/v1/orders/', methods=['POST'])
def create_order():
    if not request.json or not 'meal' in request.json:
        abort(400)
    order = {
        'id': orders[-1]['id'] + 1,
        'meal': request.json['meal'],
        'price': request.json.get('price', ""),
        'delivered': False
    }
    orders.append(order)
    return make_response(jsonify({'order': order}), 201)


@app.route('/orders/api/v1/orders/<int:order_id>/', methods=['PUT'])
def update_order(order_id):
    order = [order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'price' in request.json and type(request.json['price']) != int:
        return make_response(jsonify({'please input a valid price, integers only, in json format'}))
    if 'meal' in request.json and type(request.json['meal']) != unicode:
        return make_response(jsonify({'please input a meal in json format'}))
    if 'address' in request.json and type(request.json['adress']) is not unicode:
        return make_response(jsonify({'Please input a valid address in json format'}))
    if 'delivered' in request.json and type(request.json['delivered']) is not bool:
        return make_response(jsonify({'Please input either true or false'}))
    order[0]['meal'] = request.json.get('meal', order[0]['meal'])
    order[0]['description'] = request.json.get(
        'description', order[0]['description'])
    return make_response(jsonify({'order': order[0]}), 200)


@app.route('/orders/api/v1.0/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = [order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        return make_response(jsonify({'order cannot be empty'}))
    orders.remove(order[0])
    return make_response(jsonify, ({'Order Deletion Succesful'}), 200)


if __name__ == '__main__':
    app.run(debug=True)
