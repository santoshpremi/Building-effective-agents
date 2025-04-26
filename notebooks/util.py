import requests
import json
import os
import re

API_KEY = "go to OpenRouter.ai and get your API key free of charge"


def llm_call(prompt: str, system_prompt: str = "", model="deepseek/deepseek-chat-v3-0324:free") -> str:
    """
    Calls the model with the given prompt and returns the response.

    Args:
        prompt (str): The user prompt to send to the model.
        system_prompt (str, optional): Not used in deepseek here but kept for compatibility.
        model (str, optional): The model to use for the call.

    Returns:
        str: The response from the language model.
    """
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional
            "X-Title": "<YOUR_SITE_NAME>",     # Optional
        },
        data=json.dumps({
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            #"max_tokens": 4096,
            #"temperature": 0.1
        })
    )

    result = response.json()
    if 'error' in result:
        raise Exception(f"API Error: {result['error']['message']}")
    
    return result['choices'][0]['message']['content']

def extract_xml(text: str, tag: str) -> str:
    """
    Extracts the content of the specified XML tag from the given text.

    Args:
        text (str): The text containing the XML.
        tag (str): The XML tag to extract content from.

    Returns:
        str: The content of the specified XML tag, or an empty string if the tag is not found.
    """
    match = re.search(f'<{tag}>(.*?)</{tag}>', text, re.DOTALL)
    return match.group(1) if match else ""
