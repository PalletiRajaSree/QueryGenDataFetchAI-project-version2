# QueryGen – AI-Powered English to SQL Query Generator

## About the Project

QueryGen is a Python-based application that converts natural language questions into SQL queries using Google's Gemini API and executes them against an SQLite database.

It helps users retrieve database information without needing to write SQL queries manually.

## Features

* **Natural Language to SQL:** Convert English questions into SQL queries.
* **AI-Powered Query Generation:** Use Google's Gemini API to generate SQL.
* **SQLite Database Integration:** Execute queries against a local database.
* **Interactive Web Interface:** Enter questions and view results using Streamlit.
* **Dynamic Data Retrieval:** Display database results directly in the application.

## Tech Stack

* Python
* Streamlit
* Google Gemini API
* SQLite
* SQL
* python-dotenv

## Project Structure

```text
QueryGen/
├── app.py
├── student.db
├── .env
├── .gitignore
└── README.md
```

**Note:** `.env` contains your API key and should never be committed to GitHub. The `env/` virtual environment directory should also be excluded from version control. Include `student.db` in the repository only if you intend to share the sample database.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/PalletiRajaSree/QueryGenDataFetchAI-project-version2.git
cd QueryGenDataFetchAI-project-version2
```

### 2. Create a virtual environment

```bash
python -m venv env
```

Activate it on Windows PowerShell:

```powershell
.\env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install streamlit python-dotenv google-generativeai
```

### 4. Configure the API key

Create a `.env` file in the project directory:

```text
GOOGLE_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own valid API key. Never publish the actual key.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## How It Works

1. The user enters a question in English.
2. The Gemini API generates an SQL query.
3. The application executes the query against the SQLite database.
4. The query results are displayed in the Streamlit interface.

## Example

**Input:**

```text
How many student records are present?
```

**Generated SQL:**

```sql
SELECT COUNT(*) FROM STUDENT;
```

**Output:** The total number of student records in the database.

## Future Enhancements

* Support for more database systems.
* Improved SQL validation and error handling.
* Query history and downloadable results.
* Enhanced interface and data visualizations.

## Author

**Palleti Raja Sree**

GitHub: [PalletiRajaSree](https://github.com/PalletiRajaSree)

---

If you find this project useful, feel free to explore the repository and suggest improvements.
