# 🤖 Multi-Agent Data Analyst System

An **AI-powered Multi-Agent Data Analyst** that analyzes datasets using LLM-driven agents, performs data processing, generates insights, and supports scalable deployment using modern AI engineering practices.

---

## 🚀 Overview

This project implements an **Agentic AI system** where multiple agents collaborate to perform data analysis tasks:

* 📊 Data Analysis (Pandas)
* 📈 Visualization (Matplotlib)
* 🧠 LLM-based reasoning (OpenAI)
* 🔄 Agent orchestration (LangGraph)

---

## 🏗️ Architecture

```
User Query
   ↓
Planner Agent
   ↓
Analyst Agent (Pandas Tool)
   ↓
Visualization Agent
   ↓
Report Agent
   ↓
Final Response
```

---

## ⚙️ Tech Stack

* **Python**
* **FastAPI** – Backend API
* **LangGraph** – Agent orchestration
* **LangChain** – LLM integration
* **OpenAI GPT-4o-mini**
* **Pandas** – Data processing
* **Matplotlib** – Visualization
* **Docker** (planned)
* **AWS EC2 / CI-CD** (planned)

---

## 📁 Project Structure

```
multi-agent-data-analyst/
│
├── app/
│   ├── main.py                # FastAPI entry point
│   ├── agents/               # Agent logic (planned)
│   ├── tools/                # Tools (Pandas, plotting)
│   ├── graph/                # LangGraph workflows
│
├── data/                     # Sample datasets
├── requirements.txt          # Dependencies
├── .env                      # Environment variables (not committed)
├── .gitignore
```

---

## 🔑 Environment Variables

Create a `.env` file in root:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ⚡ Installation

```bash
git clone https://github.com/your-username/multi-agent-data-analyst.git
cd multi-agent-data-analyst
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 API Usage

### Endpoint:

`POST /analyze`

### Input:

* CSV file upload
* Query string

### Example Query:

```
"Find average sales and plot trend"
```

---

## 🎯 Features

✔ Multi-agent architecture
✔ Dataset-driven analysis
✔ API-based interaction
✔ Extensible agent framework
✔ Cloud deployment ready

---

## 🚀 Future Enhancements

* 🔥 Dynamic tool selection using LLM
* 🔥 Memory (Redis / Vector DB)
* 🔥 Multi-agent communication (LangGraph advanced)
* 🔥 Streamlit / React UI
* 🔥 Docker + AWS deployment
* 🔥 CI/CD pipeline integration

---

## 💡 Use Cases

* Business data analysis automation
* AI-powered analytics assistant
* Self-service BI tools
* Data exploration without coding

---

## 🧠 Key Learnings

* Agentic AI architecture design
* LLM tool orchestration
* Scalable AI system deployment
* CI/CD for AI applications

---

## 📌 Author

**Priyanka Bawankar**

---

## ⭐ If you like this project, give it a star!
