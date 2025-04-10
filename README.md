# Revellabs_project1

# 🧠 Natural Language to SQL Query Generation  
### Using Google Gemini API & SQLite

---

## 📌 Overview

This project bridges the gap between **natural language** and **SQL** by using **Google Gemini** to interpret user questions and generate corresponding SQL queries, which are then executed on a **SQLite** database.

> 💡 Goal: Enable non-technical users to access data insights through plain English queries.

---

## ⚙️ How It Works

1. **User Input**  
   A user asks a question in plain English (e.g., *"How many customers are from India?"*).

2. **Gemini API Processing**  
   The input is sent to Google Gemini, which returns a SQL query based on the question.

3. **SQLite Execution**  
   The generated SQL query runs on a local database of customer data.

4. **Output Display**  
   The result is displayed to the user.

---

## 🗂️ Tech Stack

- **Language:** Python  
- **Database:** SQLite  
- **AI Model:** Google Gemini (via API)  
- **UI (Coming Soon):** Streamlit  
- **Libraries:** `google-generativeai`, `sqlite3`, `python-dotenv`

---

## 🧾 Dataset Info

**Source:** `Customer Data.csv`  
**Table:** `CustomerData`  
**Columns:**
- `CustomerID`
- `Name`
- `Segment`
- `Country`
- `City`

The data is imported into `database.db` (SQLite) for processing.

---

## 📁 Project Structure

```
Gemini-SQL-Project/
├── app.py              # Main application logic
├── sql.py              # CSV to SQLite conversion script
├── Customer Data.csv   # Input dataset
├── database.db         # SQLite DB file
├── .env                # API key file
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🚀 Setup Instructions

1. Clone the repository  
2. Add your Google API key to a `.env` file:
   ```
   GOOGLE_API_KEY="your-api-key-here"
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run `sql.py` to create and populate the database  
5. Run `app.py` to start querying



## ✅ Features

- Natural Language to SQL conversion via Gemini
- Real-time SQL execution on customer database
- Expandable for more complex queries and datasets


