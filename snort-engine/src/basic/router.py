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

@router.get("/test-rule", response_class=PlainTextResponse, tags=['basic'])
def test_rule(rule_string: str):
    result = services.test_rule(rule_string)
    if result is None:
        raise HTTPException(400, 'Error in testing rule.')
    return result

@router.post("/snort2lua/convert-rule", response_class=PlainTextResponse, tags=['basic'])
def convert_rule(rule_string : str):
    result = services.convert_rule(rule_string)
    if result is None:
        raise HTTPException(400, 'Error in converting rule.')
    return result

