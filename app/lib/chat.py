from typing import List, Union

import openai

from app.config import settings
from app.models import Persona


openai.api_key = settings.OPENAI_API_KEY


def chat_completion(model="gpt-3.5-turbo", messages=[], debug=False) -> str:
    print("\n\n".join([message["content"] for message in messages]))

    if debug:
        return "{'0': 'I find the clean design of the page appealing. It looks organized and easy to navigate.', '1': 'I dislike that the pricing is not clearly displayed on the main page. I had to click through to find the price for the lunch menu.', '2': 'I would consider making a purchase on this page. I would be willing to spend around 500 Kč for a meal set because the quality and reliability of the food is important to me.', '3': 'Overall, I have a positive impression of the page. The layout is user-friendly and the content is informative.', '4': 'Yes, I find the design of the page visually appealing. The use of simple colors and clear fonts makes it easy to read.', '5': 'The content on the page is informative, especially the lunch menu with the daily specials.', '6': 'The navigation on the page is intuitive and easy to use. The menu is clearly labeled and I can easily find the information I need.', '7': 'I didn\\'t find any elements on the page that were confusing or hard to understand. The information is presented in a straightforward manner.', '8': 'Yes, the page provides clear and relevant information. I can easily see the dishes available and their prices.', '9': 'The feature that stands out to me is the option to purchase a permanentka, which is a cost-effective way to enjoy multiple meals.', '10': 'I find the rotating banner at the top of the page distracting. It doesn\\'t add much value to the overall user experience.', '11': 'The page does evoke a sense of trust and credibility. The clear presentation of the dishes and their prices gives me confidence in the establishment.', '12': 'I didn\\'t encounter any technical issues or errors on the page. It loaded quickly and all the links worked properly.', '13': 'I find the pricing on the page reasonable. The lunch menu offers a variety of dishes at affordable prices.', '14': 'Compared to similar websites or competitors, this page is on par in terms of design and functionality. However, it could improve by displaying the prices more prominently.', '15': 'I would recommend this page to others because it provides clear information and a convenient way to purchase meals.', '16': 'I think the page could improve by adding more food photos and including customer reviews for each dish. This would help me make a more informed decision.', '17': 'The page aligns with my expectations and needs. It provides the necessary information in a user-friendly manner.', '18': 'I am likely to revisit the page in the future when I'm looking for a place to eat lunch.', '19': 'Yes, I feel that the page effectively communicates its purpose and message. It clearly presents the lunch menu and provides information on how to purchase meals.', '20': 'My user experience from the page is positive. I appreciate the ease of use and the availability of information.', '21': '8'}"

    chat_response = (
        openai.ChatCompletion.create(model=model, messages=messages)
        .choices[0]
        .message.content
    )

    return chat_response


def chat_process_url(
    url,
    website_text: str,
    persona: Persona,
    questions: List[str],
    model="gpt-3.5-turbo",
    debug=True,
) -> str:
    questions_text = "\n".join(questions)
    messages = [
        {
            "role": "system",
            "content": f"You are this person:\n{persona}\n\nI will share with you text from website: {url} and you will answer my questions about it. Return response in json format with keys as indexes of questions (i.e. {{'0': 'answer to question 1', '1': 'answer to question 2', ...}}) and fields only with answer of questions. Never say that you have limited information or that you are not human or that you don't have an access to the internet. Act only like the person I described and make emphasis on your personality, act your age and use as many persona parameters as possible! Be as critical as possible and provide valuable feedback. Make each awnswer maximum 100 words long and never answer in boolean type, only text! Try not to repeat yourself.",
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

    return chat_completion(messages=messages, model=model, debug=debug)
