from fastapi import APIRouter
from app import constants


router = APIRouter()


@router.get("/personas/{persona_id}")
async def get_persona(persona_id: int):
    for persona in constants.predefined_personas:
        if persona.id == persona_id:
            return persona

    return {"error": "Persona not found"}


@router.get("/personas/")
async def list_personas():
    return constants.predefined_personas


@router.get("/personas/constants/")
async def values():
    return {
        "predefined_decision_making_factors": constants.predefined_decision_making_factors,
        "predefined_communication_styles": constants.predefined_communication_styles,
        "predefined_user_experience_expectations": constants.predefined_user_experience_expectations,
    }
