import hashlib
import json
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_block(previous_hash="0", proof=100)  # Bloque génesis

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
            'hash_actual': None  # Se calculará después
        }
        self.pending_transactions = []  # Limpiar transacciones pendientes
        
        # Calcular el hash del bloque después de crearlo
        block['hash_actual'] = self.hash_block(block)
        
        self.chain.append(block)
        return block

    def add_transaction(self, sender, receiver, amount):
        self.pending_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        while not hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest().startswith("0000"):
            new_proof += 1
        return new_proof

    def hash_block(self, block):
        """Calcula el hash SHA-256 de un bloque."""
        block_string = json.dumps({k: v for k, v in block.items() if k != 'hash_actual'}, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def validar_blockchain(self):
        """Verifica que cada bloque tenga un `previous_hash` correcto."""

        for i in range(1, len(self.chain)):  # Empezamos desde el bloque 2
            previous_block = self.chain[i - 1]
            current_block = self.chain[i]

            # Obtener el previous_hash del bloque actual
            previous_hash_actual = previous_block["hash_actual"]

            # Verificar si el previous_hash del bloque actual es igual al hash_actual del anterior
            if current_block["previous_hash"] != previous_hash_actual:
                print(f"❌ ERROR en el bloque {current_block['index']}:")
                print(f"🔴 previous_hash almacenado: {current_block['previous_hash']}")
                print(f"🟢 Debió ser: {previous_hash_actual}")
                return False  # La blockchain es inválida

        return True  # La blockchain es válida

    def modificar_bloque(self, index, campo, nuevo_valor):
        """Modifica un bloque sin cambiar su previous_hash y recalcula su hash_actual."""

        # Verificar que el índice sea un número entero
        if not isinstance(index, int):
            return {"message": "El índice debe ser un número entero ❌"}

        # Verificar si el índice está dentro del rango permitido
        if index <= 0 or index >= len(self.chain):
            return {"message": f"Índice fuera de rango ❌ La blockchain tiene {len(self.chain)} bloques."}

        # Obtener el bloque a modificar
        bloque_modificado = self.chain[index - 1]

        # Verificar si el campo existe en el bloque
        if campo not in bloque_modificado:
            return {"message": f"El campo '{campo}' no existe en el bloque ❌"}

        # Modificar el valor del campo
        bloque_modificado[campo] = nuevo_valor

        # Recalcular el hash_actual del bloque modificado
        bloque_modificado["hash_actual"] = self.hash_block(bloque_modificado)

        return {
            "message": "Bloque modificado con éxito ✅",
            "index": bloque_modificado["index"],
            "nuevo_hash": bloque_modificado["hash_actual"]
        }
