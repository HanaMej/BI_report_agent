# tools.py
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv
 
load_dotenv()
 
# Initialize the web search tool
# The tool will automatically use SERPER_API_KEY from .env
search_tool = SerperDevTool()
