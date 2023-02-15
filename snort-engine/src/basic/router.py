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

@router.get("/validate-configuration", response_class=PlainTextResponse)
def validate_conf():
    """Validate configuration."""
    result = services.validate_conf()
    if result is None:
        raise HTTPException(400, 'Error in executing task.')
    return result

@router.post("/test-pcap", response_class=PlainTextResponse)
def testing(file: UploadFile):
    print(file.filename)
    result = services.testing(file.file.read())
    if result is None:
        raise HTTPException(400, 'Error in executing task.')
    return result

@router.get("/testing", response_class=PlainTextResponse)
def testing():
    result = services.testing()
    return result
