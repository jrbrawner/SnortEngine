import subprocess
from fastapi import UploadFile

def get_version():
    """
    snort -V: output version\n
    Get snort version and return result.
    """
    result = subprocess.run([f'snort -V'],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    return result.stdout

def testing(pcap_file: UploadFile):
    pass