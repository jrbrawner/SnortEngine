import subprocess
import tempfile
from fastapi import UploadFile
from scapy.all import rdpcap

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

def read_pcap(pcap_file: UploadFile):
    """
    Have snort read a pcap file and return the result.
    """
    temp_file = tempfile.NamedTemporaryFile()
    temp_file.name = 'test.pcap'
    f = open(temp_file.name, 'wb')
    f.write(pcap_file.file.read())
    f.close()
    
    result = subprocess.run([f'snort -r {temp_file.name}'],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    temp_file.close()

    return result.stdout

def analyze_pcap(pcap_file: UploadFile, rules_file: UploadFile):
    """
    Have snort analyze a pcap file using a provided rules file and return the result.
    """

    test_rule = """
    alert tcp any any -> any any (msg:"TESTING";)
    """
    temp_file_pcap = tempfile.NamedTemporaryFile()
    #temp_file_pcap.name = 'test.pcap'
    f = open(temp_file_pcap.name, 'wb')
    f.write(pcap_file.file.read())
    f.close()

    temp_file_rules = tempfile.NamedTemporaryFile()
    #temp_file_rules.name = 'test.rules'
    f = open(temp_file_rules.name, 'w')
    f.write(rules_file.file.read().decode())
    f.close()

    result = subprocess.run([f'snort -q -c /usr/local/etc/snort/snort.lua -R {temp_file_rules.name} -r {temp_file_pcap.name} -A alert_talos'],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    temp_file_pcap.close()
    temp_file_rules.close()

    return result.stdout