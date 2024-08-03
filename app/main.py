from fastapi import FastAPI
import uvicorn

from database import connect_db, disconnect_db
from routers import messages

app = FastAPI()


@app.on_event('startup')
async def startup_db_client():
    await connect_db()


@app.on_event('shutdown')
async def shutdown_db_client():
    await disconnect_db()


app.include_router(messages.router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
