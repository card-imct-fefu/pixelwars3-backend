from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        if websocket.client_state.CONNECTED:
            try:
                await websocket.send_text(message)
            except Exception:
                pass

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            if connection.client_state.CONNECTED:
                try:
                    await connection.send_text(message)
                except Exception:
                    pass
            elif connection.client_state.DISCONNECTED:
                self.disconnect(connection)

    def get_online(self):
        return len(self.active_connections)


connection_manager = ConnectionManager()
