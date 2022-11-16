from typing import Optional

from pydantic import BaseModel


class Settings(BaseModel):
    username: str
    password: str
    recent_liked: str
    videos_path: Optional[str] = None
