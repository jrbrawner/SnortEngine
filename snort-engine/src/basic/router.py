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

@router.post("/read-pcap", response_class=PlainTextResponse)
def read_pcap(pcap_file: UploadFile):
    result = services.read_pcap(pcap_file)
    if result is None:
        raise HTTPException(400, 'Error in executing task.')
    return result

@router.post("/analyze-pcap", response_class=PlainTextResponse)
def analyze_pcap(pcap_file: UploadFile, rules_file: UploadFile):
    result = services.analyze_pcap(pcap_file, rules_file)
    if result is None:
        raise HTTPException(400, 'Error in executing task.')
    return result

@router.post("/read-pcap-detailed", response_class=PlainTextResponse)
def testing(pcap_file: UploadFile):
    result = services.read_pcap_detailed(pcap_file)
    return result

@router.post("/testing", response_class=PlainTextResponse)
def testing(pcap_file: UploadFile):
    result = services.testing(pcap_file)
    return result

