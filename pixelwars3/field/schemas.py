from pydantic import BaseModel


class FieldPydantic(BaseModel):
    online: int
    player_id: str
    field_size: int
    cell_size: int
    image: list[str]
