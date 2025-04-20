# AI News Scraper with CrewAI

An intelligent news scraping and analysis system powered by CrewAI that automatically gathers, processes, and summarizes news articles using multiple AI agents working in collaboration.

## Features

- 🔍 Automated news search and retrieval using Serper.dev API
- 🌐 Web content scraping with Firecrawl
- 🤖 AI-powered content summarization using GPT-4
- 📝 Structured markdown output
- 👥 Multi-agent collaboration using CrewAI framework

## Prerequisites

- Python >=3.10 <3.13
- OpenAI API key
- Serper.dev API key
- Firecrawl API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/codebyshivareddiee/AI_news_scrapper-agents-.git
cd AI_news_scrapper-agents-
```

2. Install UV (Python package manager):
```bash
pip install uv
```

3. Install project dependencies:
```bash
crewai install
```

4. Create a `.env` file in the root directory with your API keys:
```env
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
FIRECRAWL_API_KEY=your_firecrawl_api_key
```

## Project Structure

```
news_scrapper/
├── src/
│   └── news_scrapper/
│       ├── config/
│       │   ├── agents.yaml    # Agent configurations
│       │   └── tasks.yaml     # Task definitions
│       ├── tools/
│       │   └── custom_tool.py # Custom tools for agents
│       ├── crew.py           # Crew setup and coordination
│       └── main.py           # Main execution script
├── knowledge/                # Knowledge base for agents
└── .env                     # Environment variables
```

## Usage

1. Configure your agents in `src/news_scrapper/config/agents.yaml`
2. Define tasks in `src/news_scrapper/config/tasks.yaml`
3. Run the news scraper:
```bash
crewai run
```

The system will:
1. Search for relevant news articles
2. Scrape the content
3. Generate a summarized report in markdown format

## Customization

You can customize the behavior by modifying:
- `agents.yaml`: Define agent roles and capabilities
- `tasks.yaml`: Configure task workflows
- `crew.py`: Add custom logic and tools
- `main.py`: Modify input parameters

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [CrewAI](https://crewai.com) for the multi-agent framework
- [OpenAI](https://openai.com) for GPT models
- [Serper.dev](https://serper.dev) for search capabilities
- [Firecrawl](https://firecrawl.com) for web scraping
