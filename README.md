
## 🔍 Hybrid Log Classification System

A powerful and flexible system for classifying software-generated log messages using a hybrid approach combining **Regex**, **BERT**, and **LLM** (Groq API). Designed to support multiple log sources with custom logic for each, including legacy systems.

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Folder Structure](#folder-structure)
- [Setup Instructions](#setup-instructions)
- [How It Works](#how-it-works)
- [Sample Prompt](#sample-prompt)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 Project Overview

This system intelligently classifies log messages using a **tiered fallback strategy**:
1. **Regex-based classification** (fast and rule-based)
2. **BERT embeddings + ML classifier** (semantic understanding)
3. **LLM-based classification via Groq API** (for complex cases, especially for `LegacyCRM`)

It ensures robust classification even when traditional or ML-based models fail.

---

## 🧰 Tech Stack

| Component         | Tech Used                          |
|------------------|-------------------------------------|
| Language         | Python 3.10                         |
| ML Model         | BERT (`all-MiniLM-L6-v2`)           |
| API Client       | Groq API (LLM integration)          |
| Packaging        | Joblib, SentenceTransformers        |
| Environment      | `virtualenv`, `.env`                |

---

## 📁 Folder Structure

```

HybridLogAnalyzer/
│
├── classify.py                # Main script to classify logs
├── processor\_llm.py          # Groq-based LLM classifier
├── processor\_regex.py        # Regex-based classifier
├── processor\_bert.py         # BERT-based classifier
├── models/
│   └── log\_classifier.joblib # Trained ML model
├── .env                      # Environment variables (API keys etc.)
├── requirements.txt          # Python dependencies
├── logenv/                   # Virtual environment (excluded via .gitignore)

````

---

## 🚀 Setup Instructions

```bash
# Step 1: Clone the repository
git clone https://github.com/yourusername/hybrid-log-classifier.git
cd hybrid-log-classifier

# Step 2: Set up a virtual environment
python -m venv logenv
source logenv/bin/activate  # On Windows: logenv\Scripts\activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Add your API key in the .env file
GROQ_API_KEY=your_key_here
````

---

## 🧠 How It Works

```python
def classify_log(source, log_msg):
    if source != "LegacyCRM":
        label = classify_with_regex(log_msg)
        if not label:
            label = classify_with_bert(log_msg)
        if not label:
            label = classify_with_llm(log_msg)
    else:
        label = classify_with_regex(log_msg)
        if not label:
            label = classify_with_bert(log_msg)
        if not label:
            label = classify_with_llm(log_msg)
    return label
```

---

## ✨ Sample Prompt (for LLM)

```plaintext
Classify the following log message into one of the categories: "Bug", "Info", "Warning", "Security", "Database", "UserAction".

Log: "Error 503 while accessing /api/v1/users due to timeout from upstream server."
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork this repository
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -m "Added feature"`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request

---

## 📄 License

This project is licensed under the **Apache 2.0 License**. See `LICENSE` file for more details.

---

## 👨‍💻 Author

Developed by **Onkar Lonsane**

[🔗 LinkedIn](https://www.linkedin.com/in/onkar-lonsane)  |  ✉️ Email: [onkarlonsane@gmail.com](mailto:onkarlonsane@gmail.com)

```

---

Let me know if you want:
- Badges (Python version, license, etc.)
- GitHub Action for deployment or testing
- A sample `.env.example` file

I can also convert this to a downloadable `.md` or `.pdf` if you want.
```
