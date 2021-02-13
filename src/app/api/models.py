from pydantic import BaseModel


# To validate the payloads for creating and updating notes
class NoteSchema(BaseModel):
    title: str
    description: str


class NoteDB(NoteSchema):
    id: int
