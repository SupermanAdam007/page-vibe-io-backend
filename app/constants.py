from app.models import Persona

predefined_decision_making_factors = [
    "Price",
    "Product features",
    "Brand reputation",
    "Quality and reliability",
    "Customer reviews",
    "Expert recommendations",
    "Ease of use",
    "Customer service and support",
    "Social proof (testimonials, case studies)",
    "Product demos or trials",
    "Return policy and warranty",
    "Compatibility with existing systems",
    "Scalability and future growth potential",
    "Sustainability and ethical considerations",
    "Delivery options and speed",
    "Customization options",
    "Security and privacy measures",
    "Integration with other tools or platforms",
    "Industry standards and compliance",
    "Innovation and uniqueness",
    "Promotional offers or discounts",
    "Word of mouth referrals",
    "Long-term cost savings",
    "User experience and design",
    "Technical specifications",
    "Past experiences with the brand or product",
]

predefined_communication_style = [
    "In-person",
    "Phone calls",
    "Email",
    "Text messaging",
    "Instant messaging",
    "Video conferencing",
    "Social media",
    "Online chat",
    "Written letters",
    "Voice messages",
    "Video messages",
    "Public speaking",
    "Presentations",
    "Webinars",
    "Podcasts",
    "Blogs",
    "Forums",
    "Newsletters",
    "Collaborative platforms",
    "Non-verbal communication",
]

predefined_user_experience_expectations = {
    "ease_of_use": ["Intuitive", "Simplified", "Effortless"],
    "design_aesthetics": ["Modern", "Clean", "Visually appealing"],
    "functionality": ["Comprehensive", "Robust", "Flexible"],
    "performance": ["Fast", "Responsive", "Reliable"],
    "accessibility": ["Inclusive", "Easy to navigate", "Screen-reader friendly"],
    "personalization": ["Customizable", "Tailored", "Adaptable"],
    "seamlessness": ["Smooth transitions", "Minimal friction", "Integrated"],
    "communication": ["Clear messaging", "Timely notifications", "Effective feedback"],
    "security": ["Trustworthy", "Privacy-focused", "Secure"],
    "support": [
        "Responsive customer service",
        "Knowledgeable support team",
        "Extensive documentation",
    ],
    "innovation": ["Cutting-edge", "Pioneering", "Innovative features"],
    "value_for_money": ["Affordable", "Cost-effective", "High return on investment"],
}


predefined_personas = [
    Persona(
        id=1,
        avatar="/personas/Thinking face-rafiki.png",
        age=25,
        gender="Male",
        name="Adam",
        description="Hey, I'm Adam, a tech-savvy digital marketer who values intuitive design and comprehensive functionality.",
        occupation="Digital Marketer",
        education_level=8,
        income_level=7,
        tech_proficiency=9,
        user_experience_expectations={
            "ease_of_use": ["Intuitive", "Simplified"],
            "design_aesthetics": ["Modern", "Visually appealing"],
            "functionality": ["Comprehensive", "Flexible"],
            "performance": ["Fast", "Responsive"],
            "accessibility": ["Easy to navigate"],
            "personalization": ["Customizable", "Adaptable"],
            "seamlessness": ["Smooth transitions"],
            "communication": ["Clear messaging", "Effective feedback"],
            "security": ["Trustworthy", "Secure"],
            "support": ["Responsive customer service"],
            "innovation": ["Cutting-edge", "Innovative features"],
            "value_for_money": ["Affordable", "High return on investment"],
        },
        decision_making_factors=["Price", "Product features", "Customer reviews"],
        communication_style=["Email", "Phone", "Chat"],
    ),
    Persona(
        id=2,
        avatar="/personas/Judge-cuate.png",
        age=70,
        gender="Female",
        name="Lisa",
        description="Hi, I'm Lisa, a retired individual looking for a clean and trustworthy user experience at an affordable price.",
        occupation="Retired",
        education_level=4,
        income_level=5,
        tech_proficiency=2,
        user_experience_expectations={
            "ease_of_use": ["Simplified"],
            "design_aesthetics": ["Clean"],
            "functionality": ["Robust"],
            "performance": ["Responsive"],
            "accessibility": ["Easy to navigate"],
            "personalization": ["Tailored"],
            "seamlessness": ["Minimal friction"],
            "communication": ["Clear messaging"],
            "security": ["Trustworthy"],
            "support": ["Knowledgeable support team"],
            "innovation": ["Pioneering"],
            "value_for_money": ["Affordable"],
        },
        decision_making_factors=[
            "Brand reputation",
            "Quality and reliability",
            "Customer reviews",
        ],
        communication_style=["In-person", "Phone calls", "Written letters"],
    ),
    Persona(
        id=3,
        avatar="/personas/Programmer-bro.png",
        age=35,
        gender="Male",
        name="Peter",
        description="Hey there, I'm Peter, a software engineer who loves innovation and seamless performance in user interfaces.",
        occupation="Software Engineer",
        education_level=9,
        income_level=9,
        tech_proficiency=10,
        user_experience_expectations={
            "ease_of_use": ["Intuitive"],
            "design_aesthetics": ["Modern"],
            "functionality": ["Comprehensive", "Flexible"],
            "performance": ["Fast", "Responsive"],
            "accessibility": ["Easy to navigate", "Screen-reader friendly"],
            "personalization": ["Customizable", "Tailored"],
            "seamlessness": ["Smooth transitions", "Minimal friction"],
            "communication": ["Clear messaging", "Timely notifications"],
            "security": ["Trustworthy", "Privacy-focused"],
            "support": ["Responsive customer service", "Extensive documentation"],
            "innovation": ["Cutting-edge", "Innovative features"],
            "value_for_money": ["Cost-effective", "High return on investment"],
        },
        decision_making_factors=[
            "Expert recommendations",
            "Productivity Enhancements",
            "Ease of use",
        ],
        communication_style=["Email", "Video conferencing", "Collaborative platforms"],
    ),
    Persona(
        id=4,
        age=30,
        avatar="/personas/Work life balance-amico.png",
        gender="Female",
        name="Isabella",
        description="Hi, I'm Isabella, a homemaker seeking a simple and customizable user experience with clear messaging and reliable support.",
        occupation="Homemaker",
        education_level=6,
        income_level=6,
        tech_proficiency=5,
        user_experience_expectations={
            "ease_of_use": ["Simplified"],
            "design_aesthetics": ["Clean"],
            "functionality": ["Flexible"],
            "performance": ["Responsive"],
            "accessibility": ["Easy to navigate"],
            "personalization": ["Customizable"],
            "seamlessness": ["Smooth transitions"],
            "communication": ["Clear messaging", "Effective feedback"],
            "security": ["Trustworthy"],
            "support": ["Knowledgeable support team"],
            "innovation": ["Innovative features"],
            "value_for_money": ["Affordable"],
        },
        decision_making_factors=[
            "Customer reviews",
            "Affordability",
            "Quality and reliability",
        ],
        communication_style=["Social media", "Online chat", "Blogs"],
    ),
]

predefined_questions = [
    "What score between 1-10 would you rate the page?",
    "What is your summary of your user experience from the page?",
    "What aspects of the page do you find appealing?",
    "What aspects of the page do you dislike or find problematic?",
    "Would you consider making a purchase on this page? If so, how much would you be willing to spend and why?",
    "What are your overall feelings or impressions of the page?",
    "Do you find the design of the page visually appealing?",
    "Is the content on the page informative and engaging?",
    "Do you find the navigation on the page intuitive and easy to use?",
    "Are there any elements on the page that are confusing or hard to understand?",
    "Does the page provide clear and relevant information?",
    "Are there any features or functionalities on the page that stand out to you?",
    "Is there anything on the page that you find distracting or unnecessary?",
    "Does the page evoke a sense of trust or credibility?",
    "Are there any technical issues or errors that you encountered on the page?",
    "Do you find the pricing or value proposition on the page reasonable?",
    "How does the page compare to similar websites or competitors?",
    "Would you recommend this page to others? Why or why not?",
    "Do you have any suggestions or improvements for the page?",
    "Does the page align with your expectations or needs?",
    "How likely are you to revisit the page in the future?",
    "Do you feel the page effectively communicates its purpose or message?",
]
