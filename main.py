from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

llm = ChatOllama(model="qwen2.5:1.5b")

prompts = [
    "Explain what a component is in Angular in simple words.",
    "What is the difference between ngOnInit and the constructor in Angular?",
    "How does dependency injection work in Angular? Give a short example.",
    "What are Angular signals and why were they introduced?",
    "Explain the difference between a Promise and an Observable in Angular.",
]

for p in prompts:
    print(f"Q: {p}")
    print(llm.invoke(p).content)
    print("-" * 40)
