from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import PlainTextResponse
from . import services

router = APIRouter()

@router.post("/read-pcap", response_class=PlainTextResponse, tags=['pcap'])
def read_pcap(pcap_file: UploadFile):
    result = services.read_pcap(pcap_file)
    if result is None:
        raise HTTPException(400, 'Error in executing task.')
    return result

@router.post("/read-pcap-detailed", response_class=PlainTextResponse, tags=['pcap'])
def read_pcap_detailed(pcap_file: UploadFile, show_raw_packet_data: bool = False):
    result = services.read_pcap_detailed(pcap_file, show_raw_packet_data)
    if result is None:
        raise HTTPException(400, 'Error in executing task.')
    return result

@router.post("/analyze-pcap", response_class=PlainTextResponse, tags=['pcap'])
def analyze_pcap(pcap_file: UploadFile, rules_file: UploadFile):
    result = services.analyze_pcap(pcap_file, rules_file)
    if result is None:
        raise HTTPException(400, 'Error in executing task.')
    return result
