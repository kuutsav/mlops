from elasticapm.contrib.starlette import make_apm_client, ElasticAPM
from fastapi import FastAPI
from loguru import logger
import uvicorn

from mlops.app.routes.router import api_router


def get_fastapi_application() -> FastAPI:
    application = FastAPI(title="MLOps")
    application.add_middleware(
        ElasticAPM, client=make_apm_client({"SERVICE_NAME": "MLOps Example"})
    )
    application.include_router(api_router)
    return application


app = get_fastapi_application()


if __name__ == "__main__":
    logger.info("*** Starting Prediction Server ***")
    uvicorn.run(app, host="127.0.0.1", port=8010)
