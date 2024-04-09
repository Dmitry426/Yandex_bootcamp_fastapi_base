import logging

from fastapi import APIRouter

logger = logging.getLogger()
router = APIRouter()


@router.post("/predict_item")
async def predict_item():
    return {"prediction"}


@router.post("/predict_items")
async def predict_items():
    return {"prediction"}
