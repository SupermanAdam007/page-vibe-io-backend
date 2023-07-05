from typing import List, Union

import openai

from app.config import settings
from app.models import Persona


openai.api_key = settings.OPENAI_API_KEY


def chat_completion(model="gpt-3.5-turbo", messages=[], debug=False) -> str:
    print("\n\n".join([message["content"] for message in messages]))

    if debug:
        return "Aspects of the page I find appealing are the modern design aesthetics and comprehensive functionality. The website is visually appealing with smooth transitions and clear messaging.###\n\nOne aspect I dislike is the repetitive use of certain elements like multiple scripts and styles. It can make the page feel cluttered and impact performance.###\n\nI would consider making a purchase on this page if the product features and customer reviews align with my needs. The price would also be a factor, but I would be willing to spend more for a high return on investment.###\n\nOverall, my impression of the page is positive. The content is informative and engaging, and the navigation is intuitive and easy to use.###\n\nYes, I find the design of the page visually appealing. It has a modern and visually pleasing layout.###\n\nThe content on the page is informative and engaging. It provides valuable information about the eCommerce platform and its features.###\n\nYes, I find the navigation on the page intuitive and easy to use. The layout and organization of the content make it easy to find what I need.###\n\nThere are some elements on the page, such as the multiple scripts and styles, that can be confusing and hard to understand. It can make the page feel cluttered and overwhelm the user.###\n\nYes, the page provides clear and relevant information about the eCommerce platform, its features, and its benefits for sellers and buyers.###\n\nThe feature that stands out to me is the ability to customize any component of the eCommerce platform using open APIs and SPIs. It offers flexibility and customization options for advanced seller and buyer needs.###\n\nThere isn't anything on the page that I find distracting or unnecessary.###\n\nYes, the page evokes a sense of trust and credibility with its modern design, clear messaging, and emphasis on features like reliable systems and custom domain names.###\n\nI didn't encounter any technical issues or errors on the page.###\n\nThe pricing and value proposition on the page seem reasonable. However, I would need to further evaluate the specific pricing plans and features to make a final judgment.###\n\nCompared to similar websites or competitors, this page stands out with its comprehensive functionality, modern design, and emphasis on customization options for sellers and buyers.###\n\nI would recommend this page to others because of its intuitive navigation, comprehensive features, and visually appealing design.###\n\nOne suggestion for improvement would be to optimize the page's performance by reducing the number of repetitive elements like scripts and styles.###\n\nYes, the page aligns with my expectations and needs as a digital marketer looking for a comprehensive eCommerce platform with customizable features.###\n\nI am very likely to revisit the page in the future to further explore the platform and its offerings.###\n\nYes, I feel the page effectively communicates its purpose and message of being a powerful and customizable eCommerce platform for businesses.###\n\nMy summary of the user experience from the page is positive. The page provides valuable information, has an intuitive design, and offers comprehensive features.###\n\nI would rate the page an 8."

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
            "content": f"You are this person:\n{persona}\n\nI will share with you text from website: {url} and you will answer my questions about it. Make the answer to each question maximum 30 words long and never answer in boolean type, only string. Separate answers with '###' at the end of the answer! Never say that you have limited information or that you are not human or that you don't have an access to the internet. Act only like the person I described and make emphasis on your personality, act your age and use as many persona parameters as possible! Be as critical as possible and provide valuable feedback. Try not to repeat yourself. Remember to end each answer with '###'!",
        },
        {
            "role": "system",
            "content": f"Here are the data from the website: \n```\n{website_text}\n```",
        },
        {
            "role": "system",
            "content": f"Here are the questions: ```\n{questions_text}\n```\nRemember to end each answer with '###'!",
        },
    ]

    return chat_completion(messages=messages, model=model, debug=debug)
