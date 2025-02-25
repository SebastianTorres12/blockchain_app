# 📌 Blockchain con Flask y Visualización con NetworkX

## 📖 Descripción del Proyecto
Este proyecto es una implementación de una **blockchain simple en Python** con una API en **Flask** para gestionar transacciones y bloques. También incluye un **visualizador interactivo con D3.js, NetworkX y Matplotlib** para representar gráficamente la blockchain.

## 🚀 Características principales
- **Creación y validación de una blockchain**.
- **API Flask para interactuar con la blockchain** (agregar transacciones, minar bloques, validar la cadena).
- **Modificación de bloques con recálculo de hash**.
- **Visualización en tiempo real** con D3.js y NetworkX.
- **Detección de inconsistencias** en la blockchain.
- **Panel lateral interactivo para mostrar detalles de múltiples bloques**.

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
Este proyecto utiliza varias librerías importantes para facilitar la construcción y visualización de la blockchain:

- **Flask**: Se usa para crear una API REST simple que permite interactuar con la blockchain a través de endpoints. Permite realizar operaciones como agregar transacciones, minar bloques y validar la cadena de bloques.
- **Requests**: Se utiliza para hacer llamadas HTTP a la API desde otros scripts o herramientas externas, permitiendo la prueba de los endpoints.
- **NetworkX**: Facilita la representación de la blockchain como un grafo dirigido, permitiendo ver cómo se conectan los bloques.
- **Matplotlib**: Usada para visualizar gráficamente la blockchain generada por NetworkX.
- **D3.js**: Permite crear visualizaciones interactivas en la interfaz web con gráficos dinámicos.
- **Hashlib**: Se emplea para generar hashes SHA-256 de los bloques, asegurando la integridad de la cadena.
- **JSON**: Se usa para serializar y deserializar los datos de la blockchain y permitir su envío en las respuestas de la API.

---

## 🎯 Objetivo de Cada Clase

### **📌 Clase Blockchain**
Esta es la clase principal que modela la funcionalidad de la blockchain. Sus objetivos son:
- Gestionar la estructura de la cadena de bloques.
- Controlar la adición de nuevos bloques.
- Validar la integridad de la cadena.
- Permitir modificaciones y pruebas de seguridad.

#### **Principales métodos:**
- **`__init__()`**: Inicializa la blockchain con el bloque génesis y define la lista de transacciones pendientes.
- **`create_block(proof, previous_hash)`**: Crea un nuevo bloque y lo añade a la blockchain.
- **`add_transaction(sender, receiver, amount)`**: Agrega una transacción a la lista de transacciones pendientes.
- **`last_block`**: Devuelve el último bloque de la blockchain.
- **`proof_of_work(previous_proof)`**: Implementa la prueba de trabajo (PoW) resolviendo un problema computacional para añadir un bloque.
- **`hash_block(block)`**: Genera un hash único para cada bloque usando SHA-256.
- **`validar_blockchain()`**: Revisa que todos los `previous_hash` coincidan con los `hash_actual` para garantizar la integridad.
- **`modificar_bloque(index, campo, nuevo_valor)`**: Modifica un bloque y recalcula su hash sin afectar el previous_hash (para pruebas de seguridad).

### **📌 Clase Flask API**
Se usa para exponer la funcionalidad de la blockchain a través de endpoints REST. Permite que los usuarios interactúen con la blockchain sin necesidad de modificar el código fuente.

#### **Principales endpoints:**
- **`/chain`** (GET): Retorna la blockchain completa.
- **`/transactions/new`** (POST): Agrega una nueva transacción a la lista de pendientes.
- **`/mine`** (GET): Realiza la prueba de trabajo y añade un nuevo bloque a la blockchain.
- **`/validate`** (GET): Verifica la integridad de la blockchain.
- **`/modify_block`** (POST): Modifica un bloque específico para pruebas de seguridad.

### **📌 Visualización Interactiva con D3.js**
Este módulo permite visualizar la blockchain en tiempo real con D3.js.

#### **Objetivo:**
- Representar la blockchain como un grafo, donde cada nodo es un bloque.
- Detectar bloques alterados que no coinciden con el hash previo.
- Permitir que los nodos se puedan mover con el mouse.
- Mostrar detalles de múltiples bloques en un **panel lateral dinámico**.

#### **Principales funcionalidades:**
- **`fetchBlockchain()`**: Obtiene la blockchain desde la API y la dibuja en la interfaz.
- **`drawBlockchain(blockchain)`**: Crea un grafo interactivo en el navegador.
- **`showBlockDetails(block)`**: Muestra la información de un bloque seleccionado en el panel lateral.
- **`closeBlockDetails()`**: Permite cerrar la información de un bloque de manera individual.

---

## 📊 Visualizador de Blockchain
El visualizador usa **D3.js, NetworkX y Matplotlib** para graficar los bloques de la blockchain.

### **1️⃣ Ejecutar el Visualizador**
```bash
python app.py
```

### **2️⃣ Cómo funciona**
- Cada **bloque es un nodo** en el gráfico.
- Se conecta con el anterior **si los hashes coinciden**.
- Si hay inconsistencias, **el bloque aparecerá aislado**.
- Puedes **hacer clic en los nodos** para ver detalles en el panel lateral.

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

