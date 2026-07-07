from pydantic import BaseModel


class Paper(BaseModel):
    title: str
    authors: str
    summary: str
    published: str
    pdf_url: str