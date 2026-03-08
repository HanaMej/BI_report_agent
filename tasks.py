# tasks.py
from crewai import Task
from agents import researcher, analyst, writer
 
# ─────────────────────────────────────────────
# TASK 1: Research Task
# ─────────────────────────────────────────────
research_task = Task(
    description=(
        'Research {company} thoroughly using web search. '
        'Collect and organize the following information:\n'
        '1. Company overview (founded, HQ, size, industry)\n'
        '2. Key financial metrics (revenue, profit, growth rate if available)\n'
        '3. Main products and services\n'
        '4. Market position and key competitors\n'
        '5. Recent news and strategic developments (last 6 months)\n'
        '6. Known challenges or controversies\n'
        'Provide all information with source references where possible.'
    ),
    expected_output=(
        'A structured document with clearly labeled sections for each '
        'of the 6 research areas above. Include factual data, numbers, '
        'and dates where available. Minimum 400 words.'
    ),
    agent=researcher,
)
 
# ─────────────────────────────────────────────
# TASK 2: Analysis Task
# ─────────────────────────────────────────────
analysis_task = Task(
    description=(
        'Using the research report provided, analyze {company} from a '
        'business intelligence perspective. Produce:\n'
        '1. A full SWOT analysis (Strengths, Weaknesses, Opportunities, Threats)\n'
        '2. Key Business KPIs and what they indicate\n'
        '3. Competitive positioning assessment (vs top 2-3 competitors)\n'
        '4. Top 3 strategic recommendations for management\n'
        'Base all analysis on facts from the research. Be specific.'
    ),
    expected_output=(
        'A structured analysis with: SWOT table, KPI commentary, '
        'competitive positioning summary, and 3 numbered strategic recommendations. '
        'Each section clearly labeled. Minimum 300 words.'
    ),
    agent=analyst,
    context=[research_task],  # Analyst receives researcher output as context
)
 
# ─────────────────────────────────────────────
# TASK 3: Report Writing Task
# ─────────────────────────────────────────────
writing_task = Task(
    description=(
        'Write a complete, professional Business Intelligence Report about {company} '
        'using the research and analysis provided. '
        'Structure the report with these sections:\n'
        '# Business Intelligence Report: {company}\n'
        '## 1. Executive Summary\n'
        '## 2. Company Overview\n'
        '## 3. Financial Performance\n'
        '## 4. Products & Services\n'
        '## 5. Competitive Landscape\n'
        '## 6. SWOT Analysis\n'
        '## 7. Key KPIs & Metrics\n'
        '## 8. Strategic Recommendations\n'
        '## 9. Conclusion\n'
        'Use professional business language. Format in clean markdown.'
    ),
    expected_output=(
        'A complete, well-structured business intelligence report in markdown format. '
        'All 9 sections present. Professional tone. Minimum 600 words. '
        'Ready to be converted to a PDF for C-suite presentation.'
    ),
    agent=writer,
    context=[research_task, analysis_task],  # Writer sees both outputs
    output_file='output/report.md',          # Auto-save to file
)
