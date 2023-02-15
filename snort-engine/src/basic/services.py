import subprocess
from ..settings import settings
from fastapi import File

#This path should correspond to the snort installation location on the docker container
#so that snort commands can be issued easier.
snort_path = settings.SNORT_PATH

def get_version():
    """
    snort -V: output version
    Get snort version and return result.
    """
    result = subprocess.run([f'{snort_path} -V'],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    return result.stdout

def validate_conf():
    """
    snort [-options] -c conf [-T]: validate conf
    Validate configuration file
    """
    result = subprocess.run([f'{snort_path} -c conf'],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    return result.stdout

def testing(pcap_file):
    result = subprocess.run([f'{snort_path} -r {pcap_file}'],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    return result.stdout