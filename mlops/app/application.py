import uvicorn
from fastapi import FastAPI
from loguru import logger

from mlops.app.routes.router import api_router


def get_fastapi_application() -> FastAPI:
    application = FastAPI(title="MLOps")
    application.include_router(api_router)
    return application


app = get_fastapi_application()


if __name__ == "__main__":
    logger.info("*** Starting Prediction Server ***")
    uvicorn.run(app, host="127.0.0.1", port=8010)
