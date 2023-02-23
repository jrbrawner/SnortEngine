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

def test_rule(rule_string: str) -> str:
    temp_file_rules = tempfile.NamedTemporaryFile()
    f = open(temp_file_rules.name, 'w')
    f.write(rule_string)
    f.close()

    conf_path = '/code/snort-engine/src/configuration/snort_config_files'
    result = subprocess.run([f'snort -c {conf_path}/snort_default_conf.lua -R {temp_file_rules.name}'],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    
    temp_file_rules.close()
    if result.stderr == "":
        return "Rule loaded successfully."
    else:
        return result.stderr


def convert_rule(rule_string: str):
    """Takes a snort 2 rule, converts it to a snort 3 rule, and returns the result."""
    temp_file_rules = tempfile.NamedTemporaryFile()
    f = open(temp_file_rules.name, 'w')
    f.write(rule_string)
    f.close()

    conf_path = '/code/snort-engine/src/configuration/snort_config_files'
    result = subprocess.run([f'cd /snort/rules && snort2lua -c {temp_file_rules.name} -r out.rules && cat out.rules && rm out.rules'],
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