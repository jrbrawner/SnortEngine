import subprocess
import os
from src.settings import settings

def get_configuration():
    """
    cd /snort/conf && ls\n
    Display all config files and return result.
    """
    result = subprocess.run([f'cd /snort/conf && ls'],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
    return result.stdout

def get_configuration_name(name: str):
    """
    cd /snort/conf && cat {name}\n
    Display config file specified by name.
    """
    if os.path.exists(f'/snort/conf/{name}.lua'):
        result = subprocess.run([f'cd /snort/conf && cat {name}.lua'],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        shell=True,
                        universal_newlines=True)
        return result.stdout
    else:
        raise FileNotFoundError

def create_configuration(config_name: str, HOME_NET: str, EXTERNAL_NET: str):
    """
    Create new configuration file, using default as template.
    """
    if os.path.exists('/snort/conf/default_snort.lua'):
        new_file = ""
        for line in open(f'{settings.config_folder_path}/default_snort.lua').readlines():
            if line.strip() == "HOME_NET = 'any'":
                line = f"HOME_NET = '{HOME_NET}'"
            if line.strip() == "EXTERNAL_NET = 'any'":
                line = f"EXTERNAL_NET = '{EXTERNAL_NET}'"
            new_file += line

        new_config = open(f'/snort/conf/{config_name}.lua', 'w')
        new_config.write(new_file)
        new_config.close()
        return f"New configuration file created named {config_name}."
    else:
        raise FileNotFoundError
    