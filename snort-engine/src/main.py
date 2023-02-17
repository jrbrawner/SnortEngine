from fastapi import FastAPI
from src.basic.router import router as basic_router
from src.configuration.router import router as configuration_router
from src.pcap.router import router as pcap_router
import subprocess
import os
from src.settings import settings

app = FastAPI()

app.include_router(basic_router)
app.include_router(configuration_router)
app.include_router(pcap_router)

@app.on_event('startup')
def startup_events():
    if os.path.exists('/snort/conf/default_snort.lua') is False:
        'Default config file does not exist, creating now.'
        subprocess.run([f'cp {settings.config_folder_path}/default_snort.lua /snort/conf/'],
                            shell=True,
                            universal_newlines=True)


