import datetime

from pydantic import BaseModel


class Message(BaseModel):
    id: str | None = None
    author: str
    content: str
    created_at: str | None = None
