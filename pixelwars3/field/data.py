from fastapi import WebSocket

FIELD_SIZE = 50
CELL_SIZE = 8
LOG_SIZE = 100
players: dict[str, WebSocket] = {}
size = FIELD_SIZE
image = ["white" for _ in range(size * size)]
