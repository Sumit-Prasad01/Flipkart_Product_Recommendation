# 🛒 Flipkart Product Recommendation System (RAG + LLM)

A **production-ready Product Recommendation System** for Flipkart-like e-commerce platforms built using **LangChain + Hugging Face + AstraDB + Groq** with a **Flask backend** and a modern **TailwindCSS frontend**.

This project implements a **Retrieval-Augmented Generation (RAG)** based recommendation engine that retrieves relevant product information from a vector database and generates **context-aware recommendations** using an LLM.

It also includes **full DevOps + Monitoring setup** with **Docker, Kubernetes (Minikube), kubectl, Prometheus, and Grafana**, deployed on a **GCP VM**.

---

## 🚀 Features

✅ Flipkart product recommendation using **RAG pipeline**  
✅ Vector database storage with **AstraDB (Cassandra + Vector Search)**  
✅ Embeddings powered by **Hugging Face models**  
✅ LLM inference powered by **Groq API** (fast responses)  
✅ Flask backend with modular structure  
✅ Clean HTML UI using **TailwindCSS + JavaScript**  
✅ Dockerized application for production deployment  
✅ Kubernetes deployment via **Minikube + kubectl**  
✅ Monitoring with **Prometheus + Grafana dashboards**  
✅ Logging system with custom exception handling  

---

## 🏗️ Tech Stack

### 🔥 Backend
- **Python**
- **Flask**
- **LangChain**
- **Groq LLM API**
- **Hugging Face Embeddings**
- **AstraDB Vector Database**

### 🎨 Frontend
- **HTML**
- **TailwindCSS**
- **JavaScript**

### ☁️ Deployment & DevOps
- **GCP VM (Google Cloud Platform)**
- **Docker**
- **Kubernetes (Minikube)**
- **kubectl**
- **YAML deployments**

### 📊 Monitoring & Observability
- **Prometheus**
- **Grafana**
- Logs + Custom Exception Handling

---

## 📂 Project Structure

```bash
Flipkart_Product_Recommendation/
│── config/                       # Configuration files
│── data/                         # Dataset storage
│── grafana/
│   └── grafana-deployment.yaml    # Grafana K8s deployment
│── logs/                          # Application logs
│── prometheus/
│   ├── prometheus-configmap.yaml  # Prometheus configuration
│   └── prometheus-deployment.yaml # Prometheus K8s deployment
│── src/
│   ├── data_converter.py          # Data preprocessing + conversion
│   ├── data_ingestion.py          # Data ingestion pipeline
│   ├── download_data.py           # Download dataset script
│   ├── rag_chain.py               # LangChain RAG pipeline
│── templates/
│   └── index.html                 # UI page
│── utils/
│   ├── custom_exception.py        # Custom exception handler
│   ├── logger.py                  # Logging module
│── app.py                         # Flask main app
│── Dockerfile                     # Docker build file
│── flask-deployment.yaml          # Flask K8s deployment
│── requirements.txt               # Dependencies
│── setup.py                       # Package setup
│── README.md                      # Documentation
│── .env                           # Environment variables
│── .gitignore
```

---

## ⚙️ How It Works (Architecture)

This project follows a **RAG-based Recommendation Workflow**:

1. **Product Dataset Download**
2. **Data Cleaning & Preprocessing**
3. **Embedding Generation (Hugging Face)**
4. **Store Vectors in AstraDB**
5. **User Query (Product Need / Search Text)**
6. **Retriever pulls similar product vectors**
7. **Groq LLM generates final recommendation response**
8. **Flask API serves result to UI**
9. **Monitoring tracked via Prometheus + Grafana**

---

## 🧠 RAG Pipeline (LangChain Flow)

```text
User Query → HuggingFace Embeddings → AstraDB Retriever → Context Retrieved
→ Groq LLM → Recommendation Response
```

---

## 🔑 Environment Variables (.env)

Create a `.env` file in the root directory:

```ini
ASTRA_DB_API_ENDPOINT=your_astra_endpoint
ASTRA_DB_APPLICATION_TOKEN=your_astra_token
ASTRA_DB_KEYSPACE=your_keyspace

GROQ_API_KEY=your_groq_api_key

HF_TOKEN=your_huggingface_token
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

---

## 🛠️ Installation & Setup (Local)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Sumit-Prasad01/Flipkart_Product_Recommendation.git
cd Flipkart_Product_Recommendation
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Flask App
```bash
python app.py
```

App will run at:
```
http://127.0.0.1:5000
```

---

## 🧪 Running the Data Pipeline

### 📥 Download Dataset
```bash
python src/download_data.py
```

### 🧹 Convert & Preprocess Data
```bash
python src/data_converter.py
```

### 📌 Ingest Data into AstraDB
```bash
python src/data_ingestion.py
```

---

## 🌐 Using the Web Application

- Open the browser at: `http://127.0.0.1:5000`
- Enter query like:
  - **"Recommend me best gaming laptops under 60000"**
  - **"Suggest best smartphones with good camera"**
  - **"I want running shoes for men"**

The system will generate smart recommendations based on retrieved Flipkart product context.

---

## 🐳 Docker Setup

### 1️⃣ Build Docker Image
```bash
docker build -t flipkart-recommendation .
```

### 2️⃣ Run Docker Container
```bash
docker run -p 5000:5000 --env-file .env flipkart-recommendation
```

---

## ☸️ Kubernetes Deployment (Minikube)

### 1️⃣ Start Minikube
```bash
minikube start
```

### 2️⃣ Apply Flask Deployment
```bash
kubectl apply -f flask-deployment.yaml
```

### 3️⃣ Apply Prometheus Deployment
```bash
kubectl apply -f prometheus/prometheus-configmap.yaml
kubectl apply -f prometheus/prometheus-deployment.yaml
```

### 4️⃣ Apply Grafana Deployment
```bash
kubectl apply -f grafana/grafana-deployment.yaml
```

### 5️⃣ Check Running Pods
```bash
kubectl get pods
```

### 6️⃣ Expose Flask Service
```bash
minikube service flask-service
```

---

## 📊 Monitoring with Prometheus + Grafana

### Prometheus
- Collects metrics from Flask service and Kubernetes resources.

### Grafana
- Visualizes Prometheus metrics with dashboards.

To access Grafana:
```bash
minikube service grafana-service
```

Default credentials (if not customized):
```
username: admin
password: admin
```

---

## ☁️ Deployment on GCP VM

### Steps Summary
1. Create a **GCP VM instance**
2. Install:
   - Docker
   - Minikube
   - kubectl
3. Clone repository
4. Run Kubernetes YAML deployments
5. Open firewall ports for:
   - Flask (5000)
   - Grafana (3000)
   - Prometheus (9090)

---

## 🧾 API Endpoint

### 🔹 Recommendation Endpoint
`POST /get`

Example payload:
```json
{
  "query": "Recommend me best headphones under 2000"
}
```

Example response:
```json
{
  "recommendations": "Here are some of the best headphones under 2000..."
}
```

---

## 📝 Logging & Exception Handling

- Logs stored in `/logs/`
- Custom exceptions handled via `utils/custom_exception.py`
- Logger defined in `utils/logger.py`

---

## 📌 Future Enhancements

🚀 Add user personalization (collaborative filtering + hybrid search)  
🚀 Add product image embeddings for multimodal search  
🚀 Deploy on GKE instead of Minikube  
🚀 Add CI/CD using GitHub Actions  
🚀 Add Redis caching for faster recommendations  
🚀 Improve UI with React / Next.js  

---



