from typing import Tuple, Optional

import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message["content"]


def summarize_text(query_text: str) -> str:
    prompt = f"""Summarize and review it in 50 characters
    ```{query_text}```
    """
    return get_completion(prompt)


def is_sentiment_text(query_text: str) -> Tuple[bool, Optional[str]]:
    prompt = f"""Is there any emotion, If yes please send the emotion else None
    ```{query_text}```
    """
    response = get_completion(prompt)
    if 'None' in response:
        return False, None
    return True, response


def analyze_text(query_text: str) -> str:
    is_sentiment, response = is_sentiment_text(query_text)
    if is_sentiment:
        if len(response) < 50:
            return response
    return summarize_text(query_text)
