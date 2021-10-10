from fastapi import APIRouter

from mlops.app.routes.endpoints import predict

api_router = APIRouter()

# predict endpoint
api_router.include_router(predict.router, tags=["health_check"])
