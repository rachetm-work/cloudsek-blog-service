from pydantic import BaseModel


class BlogEntry(BaseModel):
    title: str
    content: str
    user_id: str
