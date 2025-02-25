# 📌 Blockchain con Flask y Visualización con NetworkX

## 📖 Descripción del Proyecto
Este proyecto es una implementación de una **blockchain simple en Python** con una API en **Flask** para gestionar transacciones y bloques. También incluye un **visualizador con NetworkX y Matplotlib** para representar gráficamente la blockchain.

## 🚀 Características principales
- **Creación y validación de una blockchain**.
- **API Flask para interactuar con la blockchain** (agregar transacciones, minar bloques, validar la cadena).
- **Modificación de bloques con recalculo de hash**.
- **Visualización en tiempo real** con NetworkX.
- **Detección de inconsistencias** en la blockchain.

---

## 📦 Instalación y Configuración

### **1️⃣ Requisitos Previos**
Asegúrate de tener instalado **Python 3.8+** y **pip**.

### **2️⃣ Clonar el Repositorio**
```bash
git clone https://github.com/tu_usuario/blockchain-flask
cd blockchain-flask
```

### **3️⃣ Crear y Activar el Entorno Virtual en Python**
Este proyecto utiliza un **entorno virtual** en Python para aislar las dependencias y evitar conflictos con otros proyectos. Para crear y activar el entorno virtual:
```bash
python -m venv .venv
# En Windows (PowerShell):
.venv\Scripts\activate
# En Linux/macOS:
source .venv/bin/activate
```

### **4️⃣ Instalar Dependencias**
```bash
pip install -r requirements.txt
```

---

## 🛠 Uso de Librerías
Este proyecto utiliza varias librerías importantes:

- **Flask**: Proporciona una API web para interactuar con la blockchain mediante endpoints REST.
- **Requests**: Permite hacer solicitudes HTTP para interactuar con la API desde otros scripts.
- **NetworkX**: Facilita la representación de la blockchain como un grafo dirigido.
- **Matplotlib**: Usada para visualizar gráficamente la blockchain generada.
- **Hashlib**: Se utiliza para generar hashes SHA-256 y asegurar la integridad de los bloques.
- **JSON**: Para la serialización y deserialización de datos en la API.

---

## 🔗 API Flask - Endpoints y Objetivo Educativo

### **1️⃣ Iniciar el Servidor Flask**
```bash
python app.py
```
Por defecto, se ejecutará en `http://127.0.0.1:5000/`

### **2️⃣ Endpoints Disponibles y su Objetivo Educativo**

| Método | Ruta | Descripción | Objetivo Educativo |
|--------|------|-------------|--------------------|
| `GET`  | `/chain` | Obtener la blockchain completa | Visualizar cómo se encadenan los bloques |
| `POST` | `/transactions/new` | Agregar una nueva transacción | Entender la creación y registro de transacciones |
| `GET`  | `/mine` | Minar un nuevo bloque | Introducir el concepto de prueba de trabajo (PoW) |
| `GET`  | `/validate` | Validar la integridad de la blockchain | Demostrar cómo se detectan alteraciones en la blockchain |
| `POST` | `/modify_block` | Modificar un bloque | Experimentar con ataques a la blockchain y ver su efecto |

### **Ejemplo de Uso**
📌 **Agregar una transacción**
```bash
curl -X POST http://127.0.0.1:5000/transactions/new -H "Content-Type: application/json" -d '{"sender": "Alice", "receiver": "Bob", "amount": 100}'
```
📌 **Minar un nuevo bloque**
```bash
curl -X GET http://127.0.0.1:5000/mine
```
📌 **Verificar la blockchain**
```bash
curl -X GET http://127.0.0.1:5000/chain
```
📌 **Validar la blockchain**
```bash
curl -X GET http://127.0.0.1:5000/validate
```
📌 **Modificar un bloque**
```bash
curl -X POST http://127.0.0.1:5000/modify_block -H "Content-Type: application/json" -d '{"index": 2, "campo": "transactions", "nuevo_valor": [{"sender": "Hacker", "receiver": "Alice", "amount": 999999}]}'
```

---

## 🏗️ Componentes de la Clase Blockchain
La clase `Blockchain` gestiona toda la lógica de la cadena de bloques. Sus principales componentes son:

- **`__init__()`**: Inicializa la blockchain con el bloque génesis y define la lista de transacciones pendientes.
- **`create_block(proof, previous_hash)`**: Crea un nuevo bloque, lo añade a la blockchain y calcula su hash.
- **`add_transaction(sender, receiver, amount)`**: Agrega una transacción a la lista de transacciones pendientes.
- **`last_block`**: Devuelve el último bloque de la blockchain.
- **`proof_of_work(previous_proof)`**: Implementa el mecanismo de **Prueba de Trabajo (PoW)** para minar bloques.
- **`hash_block(block)`**: Genera un **hash SHA-256** del bloque.
- **`validar_blockchain()`**: Revisa que todos los `previous_hash` coincidan con los `hash_actual`, garantizando la integridad.
- **`modificar_bloque(index, campo, nuevo_valor)`**: Permite modificar un bloque y recalcular su hash (para simular ataques y pruebas de seguridad).

---

## 📊 Visualizador de Blockchain
El visualizador usa **NetworkX** y **Matplotlib** para graficar los bloques de la blockchain.

### **1️⃣ Ejecutar el Visualizador**
```bash
python visualizer.py
```

### **2️⃣ Cómo funciona**
- Cada **bloque es un nodo** en el gráfico.
- Se conecta con el anterior **si los hashes coinciden**.
- Si hay inconsistencias, **el bloque aparecerá aislado**.

### **Ejemplo de visualización:**
🟦 Bloques conectados = **Blockchain válida** ✅  
🔴 Bloques desconectados = **Blockchain alterada** ❌

---

## 🏆 Contribuciones
Si deseas mejorar este proyecto:
1. Haz un fork del repositorio.
2. Crea una rama nueva (`git checkout -b feature-nueva`).
3. Envía un Pull Request.

¡Gracias por tu interés en este proyecto! 🚀
