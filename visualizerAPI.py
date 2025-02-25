import requests
import networkx as nx
import matplotlib.pyplot as plt

# URL de la API Flask
API_URL = "http://127.0.0.1:5000/chain"

def fetch_chain():
    """Obtiene la blockchain desde la API Flask."""
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()["chain"]
    else:
        print("Error al obtener la blockchain:", response.text)
        return []

def draw_blockchain(blockchain):
    """Dibuja la blockchain como un grafo de NetworkX, sin unir nodos con hashes inconsistentes."""
    G = nx.DiGraph()

    for i, block in enumerate(blockchain):
        index = block["index"]
        transactions = block["transactions"]
        G.add_node(index, label=f"Bloque {index}\n{transactions}")

        # No unir nodos si el previous_hash no coincide con el hash_actual del anterior
        if i > 0:
            prev_block = blockchain[i - 1]
            if block["previous_hash"] == prev_block["hash_actual"]:
                G.add_edge(prev_block["index"], index)  # 🔗 Conectar si los hashes coinciden
            else:
                print(f"⚠️ Advertencia: El bloque {index} no coincide con el hash del anterior. ❌")

    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=2500, node_color="lightblue", font_size=10, font_weight="bold")
    nx.draw_networkx_labels(G, pos, labels)
    plt.title("Blockchain en Tiempo Real (con verificación de integridad)")
    plt.show()

if __name__ == "__main__":
    blockchain = fetch_chain()  # Obtiene la blockchain desde la API
    if blockchain:
        draw_blockchain(blockchain)  # Dibuja el grafo si hay bloques en la cadena
    else:
        print("No se pudo obtener la blockchain.")
