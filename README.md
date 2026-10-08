# Angular Q&A with Local Qwen + LangSmith Tracing

A simple Python project that asks a local AI model (Qwen 2.5) questions about Angular, and tracks every request in LangSmith.

No OpenAI key needed. The model runs fully on your own machine using Ollama.

## What this project does

- Sends a list of Angular questions to a local Qwen model
- Prints the answers in the terminal
- Records each request and answer in LangSmith so you can see the prompt, response, and time taken

## Tech used

| Tool | Purpose |
|---|---|
| Python | Main language |
| LangChain | Connects Python code to the AI model |
| Ollama | Runs the AI model locally |
| Qwen 2.5 (1.5B) | The local AI model |
| LangSmith | Tracks and shows every AI request |

## Prerequisites

- Python 3.9 or later
- [Ollama](https://ollama.com) installed
- A free [LangSmith](https://smith.langchain.com) account and API key

## Setup

**1. Clone the repo**

```bash
git clone https://github.com/<your-username>/angular-qwen-langsmith.git
cd angular-qwen-langsmith
```

**2. Download the Qwen model**

```bash
ollama pull qwen2.5:1.5b
```

**3. Create and activate a virtual environment**

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

**4. Install packages**

```bash
pip install -r requirements.txt
```

**5. Add your LangSmith key**

Copy `.env.example` to a new file named `.env`, then add your key:

```
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your-langsmith-api-key
LANGSMITH_PROJECT=my_first_project
```

The `.env` file is listed in `.gitignore`, so your key is never uploaded to GitHub.

## Run

Make sure Ollama is running, then:

```bash
python main.py
```

The answers print in the terminal.

## View traces in LangSmith

1. Open [smith.langchain.com](https://smith.langchain.com)
2. Go to **Tracing**
3. Open the project named in your `.env` file (`my_first_project`)

Each question shows up as a separate run. Click a run to see the prompt, the answer, and how long it took.

## Project structure

```
angular-qwen-langsmith/
├── main.py            # Sends questions to Qwen
├── requirements.txt   # Python packages
├── .env.example       # Sample settings (copy to .env)
├── .gitignore         # Keeps .env and venv out of Git
└── README.md
```

## Customize

- **Change the questions:** edit the `prompts` list in `main.py`
- **Use a bigger model:** run `ollama pull qwen2.5:7b`, then change the model name in `main.py` for better answers
- **Shorter answers:** add "Answer in 3 lines." to the end of each prompt

## Troubleshooting

| Problem | Fix |
|---|---|
| No traces in LangSmith | Check the project name in `.env` matches the one you opened, and that `LANGSMITH_TRACING=true` |
| 401 or 403 error | Your LangSmith API key is wrong or deleted. Create a new one |
| Connection error to Ollama | Start Ollama with `ollama serve` |
| Model not found | Run `ollama pull qwen2.5:1.5b` |
