import networkx as nx
import matplotlib.pyplot as plt
from blockchain import Blockchain

def draw_blockchain(blockchain):
    G = nx.DiGraph()
    for block in blockchain.chain:
        index = block["index"]
        G.add_node(index, label=f"Bloque {index}\n{block['transactions']}")
        if index > 1:
            G.add_edge(index - 1, index)

    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')

    plt.figure(figsize=(8, 5))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold")
    nx.draw_networkx_labels(G, pos, labels)
    plt.title("Visualización de la Blockchain")
    plt.show()

if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_transaction("Alice", "Bob", 50)

    # CORREGIDO: Minar el bloque correctamente
    previous_hash = blockchain.hash_block(blockchain.last_block)
    proof = blockchain.proof_of_work(blockchain.last_block['index'])
    blockchain.create_block(proof, previous_hash)

    blockchain.add_transaction("Bob", "Charlie", 30)
    
    # CORREGIDO: Minar otro bloque correctamente
    previous_hash = blockchain.hash_block(blockchain.last_block)
    proof = blockchain.proof_of_work(blockchain.last_block['index'])
    blockchain.create_block(proof, previous_hash)

    draw_blockchain(blockchain)
