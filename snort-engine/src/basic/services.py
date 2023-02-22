import subprocess
from fastapi import UploadFile
import tempfile

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

def testing(rule_string: str):

    temp_file_rules = tempfile.NamedTemporaryFile()
    f = open(temp_file_rules.name, 'w')
    f.write(rule_string)
    f.close()

    conf_path = '/code/snort-engine/src/configuration/snort_config_files'
    result = subprocess.run([f'cd /snort/rules && snort2lua -c {temp_file_rules.name} -r out.rules'],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    
    temp_file_rules.close()
    if result.stderr == "":
        return result.stdout
    else:
        return result.stderr