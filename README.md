# KALKE-KORBO-

An AI-powered multi-agent productivity and standup assistant that helps users track tasks, generate reports, store memory, and receive proactive insights.

## Features

* Multi-Agent Architecture

  * Collector Agent
  * Critic Agent
  * Writer Agent

* AI-Powered Report Generation

* Long-Term Memory Support

* Reflection & Self-Improvement Workflow

* Proactive Suggestions

* Slack Integration

* Docker Support

* Automated Testing

## Project Structure

```text
.
├── agents/
│   ├── collector.py
│   ├── critic.py
│   └── writer.py
│
├── services/
│   ├── llm_provider.py
│   ├── memory.py
│   ├── proactive.py
│   ├── reflection.py
│   └── report_views.py
│
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── main.py
```

## Installation

### Clone Repository

```bash
git clone https://github.com/ProvaNuran/KALKE-KORBO-.git
cd KALKE-KORBO-
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
API_KEY=your_api_key
MODEL_NAME=your_model
SLACK_WEBHOOK_URL=your_webhook_url
```

## Run the Project

```bash
python main.py
```

## Run Tests

```bash
pytest
```

## Docker

Build:

```bash
docker build -t kalke-korbo .
```

Run:

```bash
docker-compose up
```

## Tech Stack

* Python
* LLM Integration
* Slack API
* Docker
* Pytest

## License

MIT License
