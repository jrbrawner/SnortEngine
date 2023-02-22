from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import PlainTextResponse
from . import services


router = APIRouter()

@router.get("/version", response_class=PlainTextResponse, tags=['basic'])
def version():
    """Returns version information of the snort instance."""
    result = services.get_version()
    if result is None:
        raise HTTPException(400, 'Error in executing task.')
    return result

@router.post("/snort2lua", response_class=PlainTextResponse)
def testing(rule_string : str):
    result = services.testing(rule_string)
    return result

