import fastapi
import uvicorn
from views import home
from views import weather_api

api = fastapi.FastAPI()


api.include_router(home.router)
api.include_router(weather_api.router)


if __name__ == "__main__":
    uvicorn.run(api)
