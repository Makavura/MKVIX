#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

orders = [
    {
        'id': 1,
        'meal': 'ugali',
        'description': 'staple meal',
        'delivered': 'False'
    },
    {
        'id': 2,
        'meal': 'sphagetti',
        'description': 'chakula ya watoto',
        'delivered': 'True'
    }
]


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
        'description': request.json.get('description', ""),
        'delivered': False
    }
    orders.append(order)
    return make_response(jsonify({'order': order}), 201)


@app.route('/orders/api/v1/orders/<int:order_id>/', methods=['PUT'])
def update_order(order_id):
    order = [order for order in orders if order['id'] == order_id]
    if 'delivered' in request.json and type(request.json['delivered']) is not bool:
        abort(400)
    order[0]['meal'] = request.json.get('meal', order[0]['meal'])
    order[0]['description'] = request.json.get(
        'description', order[0]['description'])
    order[0]['delivered'] = request.json.get(
        'delivered', order[0]['delivered'])
    return make_response(jsonify({'order': order[0]}), 200)

if __name__ == '__main__':
    app.run(debug=True)
