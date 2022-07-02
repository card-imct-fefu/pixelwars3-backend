import datetime
import uuid

from fastapi import (
    APIRouter,
    Request,
    Response,
    WebSocket,
    WebSocketDisconnect,
)
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pixelwars3.field.connection_manager import connection_manager
from pixelwars3.field.data import CELL_SIZE, FIELD_SIZE, image, players
from pixelwars3.field.schemas import FieldPydantic

router = APIRouter()
templates = Jinja2Templates(directory="templates")


def cooldown(player_id, players, timeout=datetime.timedelta(seconds=3)):
    timestamp = players[player_id]
    timedelta = datetime.datetime.now() - timestamp
    if timedelta < timeout:
        return True, timeout - timedelta
    else:
        return False, timeout - timedelta


def set_player_id(request: Request, response: Response) -> str:
    player_id = request.cookies.get('player_id')
    if not player_id:
        player_id = str(uuid.uuid4())
        players[player_id] = datetime.datetime.now()
    if player_id not in players:
        player_id = str(uuid.uuid4())
        players[player_id] = datetime.datetime.now()
    response.set_cookie(key='player_id', value=player_id)
    return player_id


@router.get("/page", response_class=HTMLResponse)
async def root(request: Request):
    response = templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "image": image,
            "field_size": FIELD_SIZE,
            "cell_size": CELL_SIZE,
            "online": connection_manager.get_online(),
        },
    )
    set_player_id(request, response)
    return response


@router.get("/", response_model=FieldPydantic)
async def get_field(request: Request, response: Response):
    player_id = set_player_id(request, response)
    return FieldPydantic(
        player_id=player_id,
        image=image,
        field_size=FIELD_SIZE,
        cell_size=CELL_SIZE,
        online=connection_manager.get_online(),
    )


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await connection_manager.connect(websocket)
    try:
        await connection_manager.broadcast(
            f"online {connection_manager.get_online()}"
        )
        while True:
            data = await websocket.receive_text()
            index_str, color, player_id = data.split()
            index = int(index_str.replace('p', '')) - 1
            is_cooldown, timedelta = cooldown(player_id, players)
            if is_cooldown:
                msg = f"cooldown {timedelta.total_seconds()}"
                await connection_manager.send_personal_message(msg, websocket)
            else:
                image[index] = color
                players[player_id] = datetime.datetime.now()
                await connection_manager.broadcast(f"{index_str} {color}")
    except WebSocketDisconnect:
        connection_manager.disconnect(websocket)
        try:
            await connection_manager.broadcast(
                f"online {connection_manager.get_online()}"
            )
        except Exception:
            pass
