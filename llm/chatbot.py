# llm/chatbot.py
import ollama

def ask(prompt: str) -> str:
    response = ollama.chat(model='llama3', messages=[
        {'role': 'user', 'content': prompt}
    ])
    return response['message']['content']
