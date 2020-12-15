import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get('/')
def index():
    return {
        "message": "Hello World",
    }


uvicorn.run(api)
