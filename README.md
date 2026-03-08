# Multi-Agent Business Report Generator


A CrewAI-powered system where three specialized AI agents collaborate
to automatically generate a professional business intelligence report
for any company.

---

##  System Architecture

| Agent | Role | Tools |
|-------|------|-------|
| Researcher | Gathers factual data via web search | SerperDevTool |
| Analyst | Produces SWOT, KPIs, strategic insights | None (reasoning) |
| Writer | Compiles full BI report in markdown | None (writing) |

---

##  Project Structure
```
bi_report_agent/
├── .env                  # API keys (never committed)
├── main.py               # Entry point
├── agents.py             # Agent definitions
├── tasks.py              # Task definitions
├── tools.py              # Web search tool
└── output/
    └── report.md         # Generated report
```

##  Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/bi_report_agent.git
cd bi_report_agent
```

### 2. Create virtual environment
```bash
python3.11 -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install crewai crewai-tools python-dotenv
```

### 4. Configure API keys
Create a `.env` file in the project root:
```
OPENAI_API_KEY=sk-your-openai-key
SERPER_API_KEY=your-serper-key
OPENAI_MODEL_NAME=gpt-4o-mini
```
Get your free Serper key at: https://serper.dev

### 5. Run
```bash
mkdir output
python main.py
```
Enter a company name when prompted (e.g. `Tesla`, `Samsung`, `Airbus`).
The report will be saved to `output/report.md`.

---

##  Sample Output

The system generates a structured report with 9 sections:
1. Executive Summary
2. Company Overview
3. Financial Performance
4. Products & Services
5. Competitive Landscape
6. SWOT Analysis
7. Key KPIs & Metrics
8. Strategic Recommendations
9. Conclusion

---

##  Built With
- [CrewAI](https://crewai.com)
- [OpenAI GPT-4o-mini](https://openai.com)
- [Serper API](https://serper.dev)

---

##  Author
**Hana Mejdi** 
```

---

## Step 2 — Create a .gitignore file

Create a file called `.gitignore` in the project root. This prevents secrets and junk from being uploaded:
```
# API keys — NEVER upload this
.env

# Virtual environment
venv/
venv311/
__pycache__/
*.pyc

# Generated output (optional — remove this line if you want to include reports)
output/