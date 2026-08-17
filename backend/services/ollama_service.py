from ollama import chat


MODEL_NAME = "gemma4:12b"


def generate_response(message: str) -> str:
    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response["message"]["content"]