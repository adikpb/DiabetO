from contextlib import asynccontextmanager

import flet as ft
import flet_fastapi
from fastapi import FastAPI

from ..backend import main


@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()

ui = FastAPI(lifespan=lifespan)

async def main(page: ft.Page):
    await page.add_async(ft.Text("Hello, Flet!"))

ui.mount("/ui", flet_fastapi.app(main))