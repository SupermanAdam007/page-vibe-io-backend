from typing import List
from pydantic import BaseModel


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "app"
    LOG_FORMAT: str = (
        "[%(levelname)s][%(asctime)s][%(funcName)s:%(lineno)s]: %(message)s"
    )
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        LOGGER_NAME: {"handlers": ["default"], "level": LOG_LEVEL},
    }


class Persona(BaseModel):
    id: int
    age: int
    avatar: str
    gender: str
    name: str
    occupation: str
    education_level: int
    income_level: int
    tech_proficiency: int
    user_experience_expectations: dict
    decision_making_factors: List[str]
    communication_style: List[str]

    def __str__(self):
        user_experience_expectations = ", ".join(
            [
                f"{key}: {', '.join(value)}"
                for key, value in self.user_experience_expectations.items()
            ]
        )

        decision_making_factors = ", ".join(self.decision_making_factors)
        communication_style = ", ".join(self.communication_style)

        return f"Age: {self.age}\nGender: {self.gender}\nOccupation: {self.occupation}\nEducation Level: {self.education_level}\nIncome Level: {self.income_level}\nTech Proficiency: {self.tech_proficiency}\nUser Experience Expectations: {user_experience_expectations}\nDecision Making Factors: {decision_making_factors}\nCommunication Style: {communication_style}"


class Question(BaseModel):
    text: str
