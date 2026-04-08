AI Sentiment Analysis (Flask + Docker)

A simple yet powerful AI-based Sentiment Analysis web application built using **Flask** and **TextBlob**, fully containerized with **Docker** and ready for cloud deployment.

---

Features

* 🔍 Analyze text sentiment (Positive / Negative / Neutral)
* 🌐 Clean and interactive web UI
* 🐳 Dockerized for easy deployment
* ☁️ Cloud-ready (Azure / AWS / Render)
* ⚡ Fast and lightweight

---

Tech Stack

* **Backend:** Flask (Python)
* **NLP:** TextBlob
* **Frontend:** HTML, CSS (Bootstrap)
* **Containerization:** Docker

---

Demo

1. Enter your text
2. Click **Analyze**
3. Get instant sentiment result

---

Run Locally

### Clone the repository

```bash
git clone https://github.com/ritikbatho16/ai-sentiment-analysis.git
cd ai-sentiment-analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the app

```bash
python app.py
```

Open in browser:

```
http://localhost:5000
```

---

Run with Docker

Build Docker image

```bash
docker build -t ai-sentiment-app .
```

Run container

```bash
docker run -d -p 5000:5000 --name ai-app ai-sentiment-app
```

Open:

```
http://localhost:5000
```

---

Deployment

This project can be deployed on:

* Microsoft Azure (App Service / Container)
* AWS EC2 / ECS
* Render / Railway

---

Project Structure

```
.
├── app.py
├── requirements.txt
├── Dockerfile
├── templates/
│   └── index.html
```

---

Future Improvements

* 🤖 Advanced ML model (HuggingFace / Transformers)
* 📊 Sentiment visualization (charts)
* 🔐 User authentication
* 🌍 Multi-language support

---

Author

**ritik batho**
GitHub: https://github.com/ritikbatho16


