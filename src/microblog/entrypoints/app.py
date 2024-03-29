import logging

import asyncio
import typer
from fastapi import FastAPI

from ..adapters.router import router
from ..adapters.persistence.db import init_models

logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.include_router(router)
cli = typer.Typer()


@cli.command()
def db_init_modes():
    asyncio.run(init_models())


@app.on_event('startup')
async def startup():
    print('Startup Application')


@app.on_event('shutdown')
async def shutdown():
    print('Shutdown Application')
