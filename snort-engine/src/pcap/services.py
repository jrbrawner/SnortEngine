import subprocess
from fastapi import UploadFile
import tempfile

def read_pcap(pcap_file: UploadFile):
    """
    Have snort read a pcap file and return the result.
    $ snort -r
    """
    temp_file = tempfile.NamedTemporaryFile()
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

def read_pcap_detailed(pcap_file: UploadFile, packet_data: bool):
    """
    Inspect a pcap, packet by packet, and return result.
    $ snort -r a.pcap -L dump
    """
    temp_file_pcap = tempfile.NamedTemporaryFile()
    f = open(temp_file_pcap.name, 'wb')
    f.write(pcap_file.file.read())
    f.close()

    if packet_data is True:
        cmd = f'snort -r {temp_file_pcap.name} -L dump -d'
    if packet_data is False:
        cmd = f'snort -r {temp_file_pcap.name} -L dump'

    result = subprocess.run([cmd],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    temp_file_pcap.close()
    
    return result.stdout

def analyze_pcap(pcap_file: UploadFile, rules_file: UploadFile):
    """
    Have snort analyze a pcap file using a provided rules file, default snort configuration and return the result. Shortened results.
    """
    temp_file_pcap = tempfile.NamedTemporaryFile()
    pcap = pcap_file.file.read()
    f = open(temp_file_pcap.name, 'wb')
    f.write(pcap)
    f.close()
    
    temp_file_rules = tempfile.NamedTemporaryFile()
    rules = rules_file.file.read().decode()
    f = open(temp_file_rules.name, 'w')
    f.write(rules)
    f.close()
    conf_path = '/code/snort-engine/src/configuration/snort_config_files'
    result = subprocess.run([f'snort -c {conf_path}/snort_default_conf.lua -R {temp_file_rules.name} -q -r {temp_file_pcap.name} -A alert_talos'],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    
    temp_file_pcap.close()
    temp_file_rules.close()
    if result.stderr == "":
        return result.stdout
    else:
        return result.stderr
    
def analyze_pcap_detailed(pcap_file: UploadFile, rules_file: UploadFile, packet_data: bool):
    """
    Have snort analyze a pcap file using a provided rules file, default snort configuration and return the result.
    Provides a packet by packet summary.
    """
    temp_file_pcap = tempfile.NamedTemporaryFile()
    pcap = pcap_file.file.read()
    f = open(temp_file_pcap.name, 'wb')
    f.write(pcap)
    f.close()
    
    temp_file_rules = tempfile.NamedTemporaryFile()
    rules = rules_file.file.read().decode()
    f = open(temp_file_rules.name, 'w')
    f.write(rules)
    f.close()
    conf_path = '/code/snort-engine/src/configuration/snort_config_files'

    if packet_data is False:
        cmd = f'snort -c {conf_path}/snort_default_conf.lua -R {temp_file_rules.name} -r {temp_file_pcap.name} -A alert_talos'
    if packet_data is True:
        cmd = f'snort -c {conf_path}/snort_default_conf.lua -R {temp_file_rules.name} -r {temp_file_pcap.name} -A cmg'
    
    result = subprocess.run([cmd],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    
    temp_file_pcap.close()
    temp_file_rules.close()
    if result.stderr == "":
        return result.stdout
    else:
        return result.stderr


def testing(cmd:str):
    """
    Experimental, allows commands to be passed through.
    """
    result = subprocess.run([cmd],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    if result.stderr == "":
        return result.stdout
    else:
        return result.stderr