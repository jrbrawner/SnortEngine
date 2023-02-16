import subprocess
import tempfile
from fastapi import UploadFile

def get_version():
    """
    snort -V: output version
    Get snort version and return result.
    """
    result = subprocess.run([f'snort -V'],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    return result.stdout

def get_configuration():
    """
    snort -c /usr/local/etc/snort/snort.lua
    Get configuration
    """
    result = subprocess.run([f'snort -c /usr/local/etc/snort/snort.lua'],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    return result.stdout

def testing(pcap_file: UploadFile):

    text = pcap_file.file.read().decode()
    print(text)
    result = subprocess.run([f'cd /snort/pcap && echo {text} > test.pcap && ls'],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    return result.stdout