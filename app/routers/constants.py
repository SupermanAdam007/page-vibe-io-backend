from fastapi import APIRouter
from app import constants


router = APIRouter()


@router.get("/constants")
async def values():
    return {
        "predefined_decision_making_factors": constants.predefined_decision_making_factors,
        "predefined_communication_style": constants.predefined_communication_style,
        "predefined_user_experience_expectations": constants.predefined_user_experience_expectations,
        "predefined_personas": constants.predefined_personas,
        "predefined_questions": constants.predefined_questions,
    }
