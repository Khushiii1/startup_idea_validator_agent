
# 🏢 Startup Idea Validator Agent

An advanced AI-powered agentic application that validates and analyzes startup ideas through multi-stage research, competitor analysis, and comprehensive reporting. Built with Google ADK, Gemini AI, Tavily, and Streamlit.

## 🚀 Features

- **Multi-Agent Validation**: Clarifies, researches, and analyzes startup ideas using specialized AI agents
- **Market Research**: Estimates market size, segments, and opportunities
- **Competitor Analysis**: Identifies competitors, strengths, weaknesses, and positioning
- **Comprehensive Reports**: Generates markdown-friendly validation reports for easy reading
- **Interactive Dashboard**: Streamlit UI for seamless user experience
- **API Key Management**: Securely manage Gemini and Tavily API keys via sidebar

## 🛠️ Tech Stack

- **Python**: Core programming language
- **Streamlit**: Interactive web dashboard
- **Google ADK**: Agentic workflow and LLM orchestration
- **Gemini AI**: Large language model for research and analysis
- **Tavily**: Web search and data extraction
- **uv**: Fast Python package manager
- **dotenv**: Environment variable management

## 📦 Getting Started

### Prerequisites

- Python 3.9+
- [uv](https://github.com/astral-sh/uv) package manager (used instead of pip)
- [Gemini](https://dub.sh/Nebius) API key
- [Tavily](https://dub.sh/tavily) API key

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
GEMINI_API_KEY="your_gemini_api_key"
TAVILY_API_KEY="your_tavily_api_key"
```

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/startup_idea_validator_agent.git
   cd startup_idea_validator_agent
   ```

2. **Install dependencies using uv:**

   ```bash
   uv sync
   ```

3. **Activate the virtual environment:**

   - **On macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```
   - **On Windows:**
     ```bash
     .venv\Scripts\activate
     ```

## ⚙️ Usage

1. **Run the Streamlit Dashboard:**

   ```bash
   streamlit run app.py
   ```

## 📖 How It Works

1. **Idea Input**: Enter your startup idea in the chat input
2. **Clarification**: The Idea Clarifier agent refines and clarifies your idea
3. **Market Research**: The Market Researcher agent analyzes market size and segments
4. **Competitor Analysis**: The Competitor Analyst agent evaluates competitors and positioning
5. **Report Generation**: The Report Generator agent synthesizes all findings into a markdown-friendly report


