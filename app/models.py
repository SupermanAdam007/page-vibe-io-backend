from typing import List
from pydantic import BaseModel


class Persona(BaseModel):
    id: int
    age: int
    gender: str
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
