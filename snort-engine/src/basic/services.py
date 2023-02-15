import subprocess
from fastapi import File

#This path should correspond to the snort installation location on the docker container
#so that snort commands can be issued easier.

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

def testing(pcap_file):
    result = subprocess.run([f'snort -r {pcap_file}'],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    return result.stdout