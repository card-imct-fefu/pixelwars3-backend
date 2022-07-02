from pydantic import BaseModel, Field

from pixelwars3.field.data import size


class FieldPydantic(BaseModel):
    online: int
    player_id: str
    field_size: int
    cell_size: int
    image: list[str]


class ClearPydantic(BaseModel):
    point_1: int = Field(gt=0, lt=(size * size))
    point_2: int = Field(gt=0, lt=(size * size))
