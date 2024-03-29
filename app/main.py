from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse

from .routers import api
from .dependencies import validate_api_key
from .config import settings


app = FastAPI(title=settings.app_name)

app.include_router(
    router=api.router,
    prefix='/api',
    tags=['api'],
    dependencies=[Depends(validate_api_key)]
)


@app.get('/')
def root():
    return RedirectResponse('/docs', 302)
