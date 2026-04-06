from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    openai_api_key: str
    redis_url: str
    supabase_url: str
    supabase_key: str
    supabase_storage_bucket: str
    clerk_secret_key: str
    google_drive_folder_id: str
    google_service_account_json: str
    app_env: str = "development"
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()
