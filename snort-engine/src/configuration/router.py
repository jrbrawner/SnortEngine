from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import PlainTextResponse
from . import services

router = APIRouter()

@router.get("/configuration", response_class=PlainTextResponse, tags=['configuration'])
def get_configuration():
    """Display all current config files."""
    result = services.get_configuration()
    if result is None:
        raise HTTPException(400, 'Error in executing task.')
    return result

@router.get("/configuration/{name}", response_class=PlainTextResponse, tags=['configuration'])
def get_configuration_name(name: str):
    """Display config file, specified by name"""
    result = services.get_configuration_name(name)
    if result is None:
        raise HTTPException(400, 'Error in reading config file specified by name.')
    return result

@router.post("/configuration", response_class=PlainTextResponse, tags=['configuration'])
def create_configuration(config_name: str, HOME_NET: str, EXTERNAL_NET: str = '!$HOME_NET'):
    result = services.create_configuration(config_name, HOME_NET, EXTERNAL_NET)
    if result is None:
        raise HTTPException(400, 'Error in creating new configuration.')
    return result
