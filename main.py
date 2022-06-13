import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from views import home

app = fastapi.FastAPI()

def configure_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)

if __name__ == '__main__':
    configure_routes()
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)
