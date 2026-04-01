# Masar.AI

### 🧭 B2B AI-Powered Tourist Routing Platform

![MVP](https://img.shields.io/badge/Status-MVP-orange)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![Vue.js](https://img.shields.io/badge/Vue.js-3-42b883)
![Mapbox](https://img.shields.io/badge/Mapbox-GL%20JS-000000)
![License](https://img.shields.io/badge/License-MIT-green)

Masar.AI is a hackathon MVP helping tourism businesses design smarter, data-driven routes with AI recommendations and interactive map navigation.

## 🚧 MVP Status

This repository contains the first MVP release focused on rapid validation, demo readiness, and iterative feature expansion.

## ❗ The Problem

Tourism operators often rely on manual planning, static maps, and fragmented data, making route creation time-consuming, inconsistent, and difficult to optimize.

## ✅ The Solution

Masar.AI combines machine learning clustering and map-based directions to propose intelligent tourist routing paths that reduce planning effort and improve operational decisions for B2B tourism teams.

## 🏗️ Architecture

### Frontend Layer
- Vue.js 3
- Tailwind CSS
- Mapbox GL JS
- Mapbox Directions API

### Backend Layer
- FastAPI
- Pandas
- Scikit-learn (K-Means)

### Data Layer
- `masar_ai_dataset_v3_kaggle.csv`

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-org/masar-ai.git
cd masar-ai
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install backend dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a local `.env` file based on `.env.example` and set your Mapbox token.

```env
MAPBOX_ACCESS_TOKEN=your_real_mapbox_token
```

### 5. Run the backend API

```bash
uvicorn api:app --reload
```

Backend endpoints:
- `http://127.0.0.1:8000`
- `http://127.0.0.1:8000/docs`

### 6. Open the frontend

Open `index.html` in your browser, or use a local static server:

```bash
python -m http.server 5500
```

Then visit:
- `http://127.0.0.1:5500`

## 👥 Team

- Member 1 — TSETSE Komla Edem Wilfried / AI-enginner | Web Developper / k.tsetse0026@uca.ac.ma
- Member 2 — Anas ELATIFI / AI-Enginner / a.elatifi4901@uca.ac.ma
- Member 3 — Marouane Bakrim / AI-enginner / m.bakrim2741@uca.ac.ma

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.
