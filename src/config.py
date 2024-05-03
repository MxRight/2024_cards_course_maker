from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    FOOTER_NAME: str
    TELEGRAM_URL: str
    GITHUB_URL: str
    SECRET:str

    page_title: str = 'Карточки - конструктор курсов'
    logo_src: str = 'https://starove.ru/wp-content/uploads/2019/05/az-03.jpg'
    footer_text: str = f'Карточки - конструктор курсов для запоминания и обучения, '
    help_page_text: str = '??? please write here :)'

    @property
    def DATABASE_URL_asyncpg(self):
        # postgresql+asyncpg://postgres:postgres@localhost:5432/sa
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
