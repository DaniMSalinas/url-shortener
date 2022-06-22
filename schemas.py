from pydantic import BaseModel

class URLRequestModel(BaseModel):
    full_url: str
    short_url: str | None = None