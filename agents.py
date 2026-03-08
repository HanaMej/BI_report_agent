# agents.py
from crewai import Agent
from tools import search_tool
 
# ─────────────────────────────────────────────
# AGENT 1: The Researcher
# Gathers factual data about the target company
# ─────────────────────────────────────────────
researcher = Agent(
    role='Senior Business Researcher',
    goal=(
        'Conduct thorough research on {company} and collect factual data: '
        'company overview, key financials, market position, recent news, '
        'major products/services, competitors, and strategic challenges.'
    ),
    backstory=(
        'You are an experienced business analyst at a top consulting firm. '
        'You are known for your ability to find reliable, up-to-date information '
        'quickly and summarize it in a structured, professional format.'
    ),
    tools=[search_tool],
    verbose=True,          # Print agent's reasoning to console
    allow_delegation=False # This agent does not assign tasks to others
)
 
# ─────────────────────────────────────────────
# AGENT 2: The Analyst
# Interprets research data and extracts insights
# ─────────────────────────────────────────────
analyst = Agent(
    role='Business Intelligence Analyst',
    goal=(
        'Analyze the research provided about {company}. '
        'Identify key performance indicators, competitive advantages, '
        'risks, opportunities, and provide a SWOT analysis.' #(Strenght weakness opportunities threats
    ),
    backstory=(
        'You are a BI analyst with 10 years of experience in strategic consulting. '
        'You excel at transforming raw data into actionable business intelligence. '
        'Your analyses are always data-driven, structured, and insightful.'
    ),
    tools=[],              # Analyst reasons only — no external tools needed
    verbose=True,
    allow_delegation=False
)
 
# ─────────────────────────────────────────────
# AGENT 3: The Writer
# Compiles everything into a professional report
# ─────────────────────────────────────────────
writer = Agent(
    role='Business Report Writer',
    goal=(
        'Write a comprehensive, professional business intelligence report '
        'about {company} using the research and analysis provided. '
        'The report must be well-structured, readable by a C-suite executive, '
        'and saved in clean markdown format.'
    ),
    backstory=(
        'You are a senior business writer at McKinsey. You specialize in '
        'turning complex analytical findings into clear, compelling reports '
        'that executives can act on. You always use professional language.'
    ),
    tools=[],
    verbose=True,
    allow_delegation=False
)
