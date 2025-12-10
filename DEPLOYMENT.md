# 🚀 Deployment Guide — Diabetes Prediction + RAG + LLM System

This guide explains how to deploy the production API using:

- Docker (local or server)
- Render
- AWS EC2
- Azure App Service
- Google Cloud Run

Your project ships as a **containerized FastAPI service** with optional **RAG + LLM explainability** integrated.

---

# 🐳 1. Local Deployment with Docker

## **Build the image**
```bash
docker build -t diabetes-api .
docker run -p 8000:8000 diabetes-api
http://localhost:8000/docs
2. Run Without Docker (Local FastAPI)

Install dependencies:

pip install -r requirements.txt


Start server:

uvicorn src.api.main:app --reload

🌐 3. Deployment on Render (Free Tier Compatible)
1. Create a new Web Service

From your GitHub repo → “Deploy Web Service”

2. Choose environment

Runtime: Docker

Build Command: (leave blank — Docker auto-handled)

Start Command:

uvicorn src.api.main:app --host 0.0.0.0 --port 10000

3. Add environment variables

Go to Render → Environment → Add Variables:

OPENAI_API_KEY=your_key
RAG_ENABLED=true

4. Deploy

Render automatically builds the Dockerfile and exposes your API.

☁️ 4. Deployment on AWS EC2 (Production Ready)
1. Launch EC2 Instance

Amazon Linux 2023 or Ubuntu 22.04

t2.medium or better recommended

2. Install Docker
sudo yum install docker -y
sudo service docker start
sudo usermod -aG docker ec2-user

3. Pull your image from GitHub Container Registry (optional)
docker pull ghcr.io/trojan3877/diabetes-api:latest

4. Run Container
docker run -d -p 80:8000 \
  -e OPENAI_API_KEY=your_key \
  ghcr.io/trojan3877/diabetes-api:latest


API now available at:

http://your-ec2-public-ip/docs

🔵 5. Deployment on Azure App Service
1. Create Resource → Web App

Publish: Docker Container

OS: Linux

SKU: B1 or higher

2. Configure Container

Use:

trojan3877/diabetes-api:latest

3. Add App Settings
OPENAI_API_KEY=your_key
RAG_ENABLED=true

4. Restart the app

Your API is now running on Azure.

🟡 6. Deployment on Google Cloud Run (Most Beginner-Friendly Cloud Option)
1. Install Google Cloud CLI
gcloud init

2. Build & push container
gcloud builds submit --tag gcr.io/YOUR_PROJECT/diabetes-api

3. Deploy
gcloud run deploy diabetes-api \
    --image gcr.io/YOUR_PROJECT/diabetes-api \
    --platform managed \
    --allow-unauthenticated


Cloud Run gives you a public URL immediately.

🔑 7. Required Environment Variables

Create a .env file:

OPENAI_API_KEY=your_key
EMBEDDING_MODEL=text-embedding-3-small
LLM_MODEL=gpt-4o-mini
RAG_ENABLED=true


Load automatically via:

from dotenv import load_dotenv
load_dotenv()

🗂 8. Directory Structure (Deployment Relevant)
src/
 ├── api/
 │    └── main.py
 ├── models/
 │    └── model.pkl
 ├── rag/
 │    ├── retriever.py
 │    └── explain.py
 ├── preprocessing/
 ├── training/
Dockerfile
requirements.txt

🧾 9. Dockerfile Overview (Already Included)
FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]

🧠 10. Testing the API After Deployment
GET https://your-url/ping

POST https://your-url/predict
{
  "Pregnancies": 2,
  "Glucose": 130,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 80,
  "BMI": 30.5,
  "DiabetesPedigreeFunction": 0.45,
  "Age": 34
}
