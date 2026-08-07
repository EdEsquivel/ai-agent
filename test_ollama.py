from ollama import chat

response = chat(
    model="gemma4:12b",
    messages=[
        {
            "role": "user",
            "content": "Explain what FastAPI is in one sentence."
        }
    ]
)

print(response["message"]["content"])