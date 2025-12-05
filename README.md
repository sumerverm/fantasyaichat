# Fantasy Copilot

A personal NFL fantasy football copilot that pulls league and roster data from the Sleeper API, fetches weekly stats and injury info from an external provider (e.g., MySportsFeeds), and uses the OpenAI API as an LLM "brain" for start/sit and other fantasy questions.

## Setup
1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables:
   ```bash
   cp .env.example .env
   # open .env and fill in your real keys and usernames
   ```

## Running the CLI (placeholder)
Run the upcoming CLI interface (to be implemented) with:
```bash
python -m fantasy_copilot.interfaces.cli_app
```
