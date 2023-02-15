from pydantic import BaseSettings

class Settings(BaseSettings):

    SNORT_PATH: str = 'cd /src/snort3/build && src/snort'
    #SNORT_PATH: str = 'src/snort'
    class Config:
        env_file = ".env"


settings = Settings()