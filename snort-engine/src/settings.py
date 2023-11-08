from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    config_folder_path = "/code/SnortEngine/snort-engine/src/configuration/snort_config_files"

    class Config:
        env_file = ".env"


settings = Settings()