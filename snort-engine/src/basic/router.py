from fastapi import APIRouter
import subprocess
from ..settings import settings

router = APIRouter()
snort_path = settings.SNORT_PATH

@router.get("/version")
def check_version():
    result = subprocess.run([f'{snort_path} -V'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        shell=True,
                        universal_newlines=True)
    
    return result
