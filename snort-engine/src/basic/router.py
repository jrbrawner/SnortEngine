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

@router.post("/testing", response_class=PlainTextResponse)
def testing(pcap_file: UploadFile):
    result = services.testing(pcap_file)
    return result

