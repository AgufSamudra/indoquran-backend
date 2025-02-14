from pydantic import BaseModel


class SmartSearch(BaseModel):
    user_input: str
