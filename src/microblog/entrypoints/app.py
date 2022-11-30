import asyncio
import typer
from fastapi import FastAPI

from microblog.adapters.orm.db import init_models

app = FastAPI()
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

@app.get("/")
async def root():
    return {'message': 'It works!'}
