from flask import Flask, jsonify, request, render_template
from blockchain import Blockchain

app = Flask(__name__, template_folder="templates", static_folder="static")  # Agregar carpetas para HTML y JS
blockchain = Blockchain()

@app.route('/')
def index():
    """Carga la interfaz gráfica en el navegador."""
    return render_template('index.html')  # Servir HTML

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    data = request.get_json()
    index = blockchain.add_transaction(data['sender'], data['receiver'], data['amount'])
    return jsonify({'message': f'Transacción añadida al bloque {index}'}), 201

@app.route('/mine', methods=['GET'])
def mine_block():
    last_block = blockchain.last_block
    proof = blockchain.proof_of_work(last_block['index'])
    previous_hash = blockchain.hash_block(last_block)
    block = blockchain.create_block(proof, previous_hash)
    return jsonify(block), 200

@app.route('/chain', methods=['GET'])
def get_chain():
    # Agregar el hash calculado de cada bloque
    chain_data = [
        {
            **block,
            "hash": blockchain.hash_block(block)  # Añadir el hash del bloque
        } for block in blockchain.chain
    ]
    return jsonify({'chain': chain_data, 'length': len(chain_data)}), 200


@app.route('/validate', methods=['GET'])
def validate_blockchain():
    is_valid = blockchain.validar_blockchain()
    if is_valid:
        return jsonify({'message': 'La blockchain es válida ✅'}), 200
    else:
        return jsonify({'message': '⚠️ La blockchain ha sido modificada ❌'}), 400

@app.route('/modify_block', methods=['POST'])
def modify_block():
    data = request.get_json()
    if not all(k in data for k in ["index", "campo", "nuevo_valor"]):
        return jsonify({"message": "Faltan parámetros en la solicitud ❌"}), 400

    resultado = blockchain.modificar_bloque(data["index"], data["campo"], data["nuevo_valor"])
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
