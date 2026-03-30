# 🎓 Student Exam Performance Indicator
### End-to-End Machine Learning Project by RM

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask)
![scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?style=for-the-badge&logo=github)

---

## 📌 About The Project

A complete end-to-end Machine Learning web application that **predicts a student's Math score** based on various demographic and academic factors like gender, ethnicity, parental education, lunch type, test preparation course, reading score, and writing score.

> 🏆 Model Accuracy: **88% R² Score**

---

## 🖥️ Live Demo

> Fill in student details → Click Predict → Get Math Score instantly!

---

## 📂 Project Structure

```
mlproject/
├── artifacts/                  # Trained model & preprocessor files
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── data.csv
│   ├── train.csv
│   └── test.csv
├── notebook/                   # EDA & Model Training notebooks
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   ├── 2. MODEL TRAINING.ipynb
│   └── data/stud.csv
├── src/                        # Source code
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
├── templates/                  # HTML frontend
│   ├── index.html
│   └── home.html
├── app.py                      # Flask application
├── requirements.txt
└── setup.py
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.8+ |
| Web Framework | Flask |
| ML Libraries | Scikit-learn, XGBoost, CatBoost |
| Data Processing | Pandas, NumPy |
| Frontend | HTML, CSS |
| Deployment | Render / AWS |

---

## 🚀 How To Run Locally

### Step 1 — Clone the Repository
```bash
git clone https://github.com/Rajesh-Mojumder/mlproject.git
cd mlproject
```

### Step 2 — Create Virtual Environment
```bash
python -m venv venv
```

### Step 3 — Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Mac / Linux:**
```bash
source venv/bin/activate
```

### Step 4 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5 — Train the Model (generates model.pkl & preprocessor.pkl)
```bash
python -m src.components.data_ingestion
```
> ⏳ This will take a few minutes. You will see the R² score printed when done.

### Step 6 — Run the Flask App
```bash
python app.py
```

### Step 7 — Open in Browser
```
http://localhost:5000/predictdata
```

---

## 🔄 How The Pipeline Works

```
Raw Data (stud.csv)
      ↓
Data Ingestion  →  train.csv / test.csv
      ↓
Data Transformation  →  preprocessor.pkl
      ↓
Model Training  →  model.pkl  (Best model selected from 7 algorithms)
      ↓
Flask Web App  →  Predict Math Score
```

---

## 🤖 Models Trained

The pipeline trains and evaluates **7 models** and picks the best one automatically:

- Linear Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- CatBoost
- AdaBoost

---

## 📊 Input Features

| Feature | Description |
|---|---|
| Gender | Male / Female |
| Race or Ethnicity | Group A / B / C / D / E |
| Parental Level of Education | High School → Master's Degree |
| Lunch Type | Standard / Free or Reduced |
| Test Preparation Course | None / Completed |
| Writing Score | 0 – 100 |
| Reading Score | 0 – 100 |

**Output:** Predicted **Math Score** (0 – 100)

---

## ☁️ Deployment (Render - Free)

1. Push code to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repo
4. Set **Build Command:** `pip install -r requirements.txt`
5. Set **Start Command:** `python app.py`
6. Deploy! 🎉

---

## 👨‍💻 Author

**Rajesh Mojumder (RM)**
- GitHub: [@Rajesh-Mojumder](https://github.com/Rajesh-Mojumder)

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
