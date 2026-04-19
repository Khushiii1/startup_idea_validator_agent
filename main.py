import asyncio
import prompts
import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from google.adk.integrations.langchain import LangchainTool
from langchain_tavily import TavilySearch

load_dotenv()
import logging
logging.basicConfig(level=logging.ERROR, filename='adk_debug.log', filemode='a')

APP_NAME = "startup_validator"
USER_ID = "arindam_1729"
SESSION_ID = "startup_validation_session"

# Gemini model - ADK natively supports Gemini, no wrapper needed
GEMINI_MODEL = "gemini-flash-latest"


async def run_validation(idea: str):

    # LangChain TavilySearch tool wrapped for ADK
    # Gemini handles tool calling natively, so this works reliably
    tavily_tool_instance = TavilySearch(
        max_results=3,
        search_depth="basic",
        include_answer=True,
        include_raw_content=False,
        include_images=False,
    )
    tavily_search = LangchainTool(tool=tavily_tool_instance)

    idea_clarifier_agent = LlmAgent(
        name="IdeaClarifierAgent",
        model=GEMINI_MODEL,
        instruction=prompts.IDEA_PROMPT,
        description="Helps clarify and refine the startup idea.",
        output_key="clarified_idea"
    )
    market_research_agent = LlmAgent(
        name="MarketResearchAgent",
        model=GEMINI_MODEL,
        instruction=prompts.MARKET_RESEARCH_PROMPT,
        description="Conducts market research for the startup idea.",
        tools=[tavily_search],
        output_key="market_research"
    )
    competitor_analysis_agent = LlmAgent(
        name="CompetitorAnalysisAgent",
        model=GEMINI_MODEL,
        instruction=prompts.COMPETITOR_ANALYSIS_PROMPT,
        description="Conducts competitor analysis for the startup idea.",
        tools=[tavily_search],
        output_key="competitor_analysis"
    )
    report_agent = LlmAgent(
        name="ReportAgent",
        model=GEMINI_MODEL,
        instruction=prompts.REPORT_PROMPT,
        description="Generates a report based on the analysis findings.",
        output_key="validation_report"
    )

    startup_validation_agent = SequentialAgent(
        name="StartupValidationAgent",
        sub_agents=[
            idea_clarifier_agent,
            market_research_agent,
            competitor_analysis_agent,
            report_agent
        ],
        description="Validates startup ideas through a structured analysis process."
    )

    initial_state = {"idea": idea}
    session_service = InMemorySessionService()

    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state
    )

    runner = Runner(
        agent=startup_validation_agent,
        app_name=APP_NAME,
        session_service=session_service
    )

    content = types.Content(role="user", parts=[types.Part(text=idea)])
    events = runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=content
    )

    for event in events:
        if event.is_final_response():
            print(event.content.parts[0].text)

    session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    clarified_idea      = session.state.get("clarified_idea", "Not available")
    market_research     = session.state.get("market_research", "Not available")
    competitor_analysis = session.state.get("competitor_analysis", "Not available")
    validation_report   = session.state.get("validation_report", "Not available")

    summary = f"""
STARTUP IDEA VALIDATION COMPLETED!

Clarified Idea:
{clarified_idea}

Market Research:
{market_research}

Competitor Analysis:
{competitor_analysis}

Final Validation Report:
{validation_report}

Disclaimer: For informational purposes only.
"""
    print(summary)
    return summary


if __name__ == "__main__":
    asyncio.run(run_validation("A CodeReview Agent that reviews your code in each PR"))
