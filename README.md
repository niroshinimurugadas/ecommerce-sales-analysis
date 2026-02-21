# 📦 Ecommerce Sales Analysis

A simple Streamlit dashboard for exploring sales data from an online store.  
This project loads a CSV of product sales, calculates revenue and popularity metrics, and visualises the results in an interactive web app.

This project uses a publicly available ecommerce dataset from Kaggle or a similar open data source for educational purposes.

---

## 🚀 Features

- 💰 **Total sales revenue** metric
- 🔥 **Most popular product category**
- 📈 **Bar chart of revenue by product category**
- 📋 **Revenue table with drill‑down details**

All calculations are done with **Pandas**, and visualisations use **Seaborn** and **Matplotlib** via **Streamlit**.

---

## 🛠️ Requirements

- Python 3.8+
- Virtual environment (recommended)

Install dependencies:

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

pip install pandas seaborn matplotlib streamlit

## 📁 Project Structure

```
salesanalysis/
├── ecommerce_dashboard.py   # Streamlit app
└── ecommerce_sales_analysis.csv  # Sample dataset
```

## ▶️ Running the Dashboard

From the project root:

streamlit run ecommerce_dashboard.py


Open the URL shown in your browser (default `http://localhost:8501`).

---

## 🤝 Contributing

1. Fork the repo  
2. Create a feature branch  
3. Commit your changes  
4. Submit a pull request

Please include tests or screenshots for new visual features.

---

## 📄 License

This project is available under the **MIT License** .

> Feel free to adapt the dashboard for your own ecommerce data!

---

Happy analyzing! 🎯
