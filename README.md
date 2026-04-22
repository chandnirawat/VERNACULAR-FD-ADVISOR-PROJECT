# VERNACULAR-FD-ADVISOR-PROJECT
<br>
#  Vernacular FD Advisor

###  Smart Fixed Deposit Recommendation System with Multilingual Support

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![Uvicorn](https://img.shields.io/badge/Uvicorn-Server-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-blue)

---

##  Overview

**Vernacular FD Advisor** is a smart financial assistant that helps users choose the best Fixed Deposit (FD) plan based on their investment preferences.

It also supports **Hindi language output** and includes a **chatbot** for answering FD-related queries — making it beginner-friendly and accessible.

---

##  Features

*  Secure Login & Registration System
*  FD Recommendation Engine
*  Risk-based Suggestions (Low / Medium / High)
*  Multilingual Support (English + Hindi)
*  Built-in Chatbot Assistant
*  Clean Dashboard UI
*  Fast API performance with FastAPI

---

##  UI Preview

###  Login Page

```
+------------------------+
|        LOGIN           |
| Username [______]      |
| Password [______]      |
| [ Login ]              |
| New user? Register     |
+------------------------+
```

###  Dashboard

```
+----------------------------------+
|  FD Advisor Dashboard          |
| Amount: [____]                   |
| Duration: [____]                 |
| Risk: [Low | Medium | High]      |
| Language: [EN | HI]              |
| [ Recommend ]                    |
|                                  |
|  Result: Bank + Interest       |
|                                  |
|  Chatbot: Ask anything...      |
+----------------------------------+
```

---

##  Tech Stack

| Layer    | Technology    |
| -------- | ------------- |
| Backend  | FastAPI       |
| Frontend | HTML (Jinja2) |
| Server   | Uvicorn       |
| Language | Python        |

---

##  Project Structure

```bash
Vernacular FD Advisor/
│── main.py
│── auth.py
│── recommendation.py
│── chatbot.py
│── translator.py
│
└── templates/
     ├── login.html
     ├── register.html
     └── dashboard.html
```

---

## ⚙️ Setup & Installation

### 1️ Clone Repository

```bash
git clone https://github.com/your-username/vernacular-fd-advisor.git
cd vernacular-fd-advisor
```

###  Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️ Install Dependencies

```bash
pip install fastapi uvicorn jinja2
```

###  Run Server

```bash
uvicorn main:app --reload
```

###  Open Browser

```
http://127.0.0.1:8000
```

---

##  How It Works

1. User logs in or registers
2. Inputs:

   * Investment amount
   * Duration
   * Risk level
3. System calculates best FD option
4. Result displayed instantly
5. Chatbot handles queries
6. Optional Hindi translation applied

---

##  Future Enhancements

*  Live bank interest rate APIs
*  Mobile responsive UI
*  Voice assistant integration
*  Multi-language expansion
*  JWT Authentication

---

##  Sample Output

```
Bank: SBI | Interest: ₹12,450
```

Hindi:

```
बैंक: SBI | ब्याज: ₹12,450
```

---

##  Contributing

Contributions are welcome!
Feel free to fork, improve, and submit a pull request.

---

##  Author

**Chandni Rawat**

---

##  Support

If you found this project helpful:

 Give it a  on GitHub
 Share with others

---

##  License

This project is licensed under the MIT License.
