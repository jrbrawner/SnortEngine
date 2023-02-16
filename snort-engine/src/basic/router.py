from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import PlainTextResponse
from . import services


router = APIRouter()

@router.get("/version", response_class=PlainTextResponse)
def version():
    """Returns version information of the snort instance."""
    result = services.get_version()
    if result is None:
        raise HTTPException(400, 'Error in executing task.')
    return result

@router.get("/configuration", response_class=PlainTextResponse)
def get_configuration():
    """Get configuration."""
    result = services.get_configuration()
    if result is None:
        raise HTTPException(400, 'Error in executing task.')
    return result

@router.post("/test-pcap", response_class=PlainTextResponse)
def testing(file: UploadFile):
    result = services.testing(file)
    if result is None:
        raise HTTPException(400, 'Error in executing task.')
    return result

@router.get("/testing", response_class=PlainTextResponse)
def testing():
    result = services.testing()
    return result
