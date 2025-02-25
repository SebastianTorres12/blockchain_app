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
- **`create_block(proof, previous_hash)`**: Crea un nuevo bloque con una prueba de trabajo y lo añade a la blockchain.
- **`add_transaction(sender, receiver, amount)`**: Agrega una nueva transacción a la lista de transacciones pendientes.
- **`last_block`**: Devuelve el último bloque de la blockchain.
- **`proof_of_work(previous_proof)`**: Implementa el algoritmo de prueba de trabajo (PoW) resolviendo un problema computacional basado en el valor cuadrático de los proof previos.
- **`hash_block(block)`**: Genera un hash único para cada bloque usando el algoritmo SHA-256, garantizando la seguridad de la información.
- **`validar_blockchain()`**: Revisa que todos los `previous_hash` coincidan con los `hash_actual` de los bloques anteriores para garantizar la integridad de la cadena.
- **`modificar_bloque(index, campo, nuevo_valor)`**: Modifica el contenido de un bloque específico y recalcula su hash sin afectar el `previous_hash` de los siguientes bloques para pruebas de seguridad.

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

## 🎯 Conceptos Claves de Blockchain

### 🔹 **Bloques y Transacciones**

Cada bloque en la blockchain contiene un conjunto de transacciones. Estas transacciones representan el envío de valores o información entre usuarios.

- **Transacción**: Representa la acción de enviar datos o valores de un emisor a un receptor.
- **Bloque**: Contiene múltiples transacciones agrupadas y validadas mediante un proceso de minería.
- **Previous Hash**: Cada bloque contiene un hash del bloque anterior, lo que garantiza la integridad de la cadena.

### 🔹 **Minado y Prueba de Trabajo (PoW)**

El proceso de **minado** en la blockchain consiste en resolver un problema matemático complejo para validar y agregar nuevos bloques a la cadena. En este proyecto, se usa un método de **Prueba de Trabajo (PoW)** para garantizar la seguridad de la red:

1. Se genera un nuevo bloque con las transacciones pendientes.
2. Se busca un **número de prueba (proof)** que satisfaga una condición establecida (por ejemplo, un hash que empiece con ciertos ceros).
3. Una vez encontrada la prueba, se añade el bloque a la blockchain y se comparte con la red.

Este método **asegura que cada bloque requiere un esfuerzo computacional para ser validado**, evitando ataques y alteraciones maliciosas.

### 🔹 **Validación de Blockchain**

Para verificar que la blockchain no ha sido manipulada, se realiza un proceso de validación que revisa dos aspectos clave:

- **El `previous_hash` de cada bloque debe coincidir con el `hash_actual` del bloque anterior.**
- **El proceso de minería (PoW) debe ser válido y cumplir con las condiciones establecidas.**

Si alguna de estas condiciones falla, se considera que la blockchain ha sido alterada.

---

## 🏆 Contribuciones
Si deseas mejorar este proyecto:
1. Haz un fork del repositorio.
2. Crea una rama nueva (`git checkout -b feature-nueva`).
3. Envía un Pull Request.

¡Gracias por tu interés en este proyecto! 🚀

