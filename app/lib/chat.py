from typing import List, Union

import openai

from app.config import settings
from app.models import Persona


openai.api_key = settings.OPENAI_API_KEY


def chat_completion(model="gpt-3.5-turbo", messages=[]):
    print('\n\n'.join([message['content'] for message in messages]))
    return messages
    # chat = openai.ChatCompletion.create(
    #     model=model,
    #     messages=messages
    # ).choices[0].message.content
    #
    # return chat.choices[0].message.content


def chat_process_url(url, website_text: str, persona: Persona, questions: List[str]):
    questions_text = "\n".join(questions)
    messages = [
        {
            "role": "system",
            "content": f"You are this person:\n{persona}\n\nI will share with you text from website: {url} and you will answer my questions about it. Return response in json format with keys as indexes of questions and fields only with answer of questions. Never say that you have limited information or that you are not human or that you don't have an access to the internet. Act only like the person I described and make emphasis on your personality and act your age!",
        },
        {
            "role": "system",
            "content": f"Here are the scraped data from the website: \n```\n{website_text}\n```",
        },
        {
            "role": "system",
            "content": f"Here are the questions: ```\n{questions_text}\n```",
        },
    ]

    return chat_completion(messages=messages)
