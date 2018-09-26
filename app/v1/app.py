from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

orders = [] 

@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders': orders})


@app.route('/api/v1/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = [order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    return jsonify({'order': order[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v1/orders', methods=['POST'])
def create_order():
    if not request.json or not 'meal' in request.json:
        abort(400)
    order = {
        'id': orders[-1]['id'] + 1,
        'meal': request.json['meal'],
        'address': request.json.get('address', ""),
        'delivered': False
    }
    orders.append(order)
    return jsonify({'order': order}), 201


@app.route('/api/v1/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = [order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'meal' in request.json and type(request.json['meal']) != unicode:
        abort(400)
    if 'address' in request.json and type(request.json['address']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    order[0]['meal'] = request.json.get('meal', order[0]['meal'])
    order[0]['address'] = request.json.get('address', order[0]['address'])
    order[0]['done'] = request.json.get('done', order[0]['done'])
    return jsonify({'order': order[0]})


@app.route('/api/v1/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = [order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    orders.remove(order[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
