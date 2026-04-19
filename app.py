import streamlit as st
import os
import asyncio
from dotenv import load_dotenv
import base64
import nest_asyncio

nest_asyncio.apply()

st.set_page_config(page_title="Startup Idea Validator Agent", layout="wide")

load_dotenv() 

# Load images safely
def load_image_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return None

adk_base64 = load_image_base64("./assets/adk.png")
tavily_base64 = load_image_base64("./assets/tavily.png")

title_html = f"""
<div style="display: flex; width: 100%;">
    <h1 style="margin: 0; padding: 0; font-size: 2.5rem; font-weight: bold;">
        🏢 Startup Idea Validator with
        {f'<img src="data:image/png;base64,{adk_base64}" style="height: 80px; vertical-align: middle;"/>' if adk_base64 else ''}
        Google ADK &
        {f'<img src="data:image/png;base64,{tavily_base64}" style="height: 60px; vertical-align: middle;"/>' if tavily_base64 else ''}
    </h1>
</div>
"""
st.markdown(title_html, unsafe_allow_html=True)
st.markdown("**Discover the perfect startup ideas with AI-powered validation and comprehensive analysis capabilities**")

with st.sidebar:
    google_key = st.text_input("Enter your Google API key", value=os.getenv("GOOGLE_API_KEY", ""), type="password")

    tavily_key = st.text_input("Enter your Tavily API key", value=os.getenv("TAVILY_API_KEY", ""), type="password")

    if st.button("Save Keys", use_container_width=True):
        if google_key:
            os.environ["GOOGLE_API_KEY"] = google_key
        if tavily_key:
            os.environ["TAVILY_API_KEY"] = tavily_key
        st.success("API keys saved successfully!")

    st.markdown("---")
    st.header("About")
    st.markdown(
        """
        This application is powered by a set of advanced AI agents:
        - **Idea Clarifier**: Refines and clarifies your startup idea.
        - **Market Researcher**: Analyzes market potential, size, and customer segments.
        - **Competitor Analyst**: Evaluates competitors and market positioning.
        - **Report Generator**: Synthesizes all findings into a comprehensive validation report.
        """
    )
    st.markdown("---")
    st.markdown("[⭐ View Source Code on GitHub](https://github.com/Khushiii1/startup_idea_validator_agent)")
idea = st.chat_input("Type your message...")

def run_validation_sync(idea):
    try:
        loop = asyncio.get_event_loop()
        # ✅ Import here so main.py module-level code doesn't run at startup
        import main as validator_main
        result = loop.run_until_complete(validator_main.run_validation(idea))
        return result
    except Exception as e:
        return f"❌ Error: {str(e)}"

if idea:
    if not os.getenv("GOOGLE_API_KEY") or not os.getenv("TAVILY_API_KEY"):
        st.warning("⚠️ Please enter and save both API keys in the sidebar first.")
    else:
        with st.spinner("Validating your startup idea. Please wait..."):
            summary = run_validation_sync(idea)
            st.markdown("---")
            st.markdown(summary)
