from pydantic_settings import BaseSettings, SettingsConfigDict

_base_config = SettingsConfigDict(
    env_file="./.env",
    env_ignore_empty=True,
    extra="ignore",
)

class DbSettings(BaseSettings):

    POSTGRES_PASS: str

    model_config = _base_config

    @property
    def DATABASE_URL(self):
        return f"postgresql://postgres.vqidqzlxdwnstvoioslz:{self.POSTGRES_PASS}@aws-0-ap-south-1.pooler.supabase.com:5432/postgres"

class SecuritySettings(BaseSettings):

    JWT_SECRET: str
    JWT_ALGORITHM: str

    model_config = _base_config

settings = DbSettings()
security_setting = SecuritySettings()