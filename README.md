# GitHub Webhook Activity Tracker

## 📌 Overview

This project captures GitHub repository events (**Push, Pull Request, and Merge**) using GitHub Webhooks and stores only the minimal required data in MongoDB.

The UI polls the backend every 15 seconds and displays the latest repository activity in a clean and minimal format as required in the assignment.

---

## 🏗 Architecture Flow

GitHub (action-repo)  
→ Webhook  
→ Flask Backend (webhook-repo)  
→ MongoDB  
→ UI (Polling every 15 seconds)

---

## 🚀 Repositories

### 1️⃣ action-repo
This is the dummy repository where Push, Pull Request, and Merge events are generated.

### 2️⃣ webhook-repo
This repository contains:
- Flask webhook endpoint
- MongoDB integration
- UI for displaying repository activity

---

## 📦 Tech Stack

- Python (Flask)
- MongoDB
- GitHub Webhooks
- HTML, CSS, JavaScript
- ngrok (for local webhook testing)

---

## 📂 Project Structure

webhook-repo/
│
├── app.py
├── routes.py
├── models.py
├── requirements.txt
├── .env
│
├── templates/
│   └── index.html
│
└── static/
    └── styles.css

---

## ⚙️ Setup Instructions 

1️⃣ Clone the repository

```bash
git clone https://github.com/Kartikmanth19/webhook-repo.git
cd webhook-repo
```

2️⃣ Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Start MongoDB

```bash
mongod
```

5️⃣ Create `.env` file

```
MONGO_URI=mongodb://localhost:27017/
DATABASE_NAME=github_events
```

6️⃣ Run Flask app

```bash
python app.py
```

7️⃣ Start ngrok

```bash
ngrok http 5000
```

8️⃣ Configure GitHub Webhook in action-repo

- Payload URL: `https://your-ngrok-url/webhook`
- Content type: `application/json`
- Select events:
  - ✔ Push
  - ✔ Pull requests

Done ✅

---


## 👨‍💻 Author

Kartik Manthanwar  
GitHub: https://github.com/Kartikmanth19
