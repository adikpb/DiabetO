import flet as ft
import flet_fastapi

from ..backend.main import *


class MainView(ft.View):
    def __init__(self):
        super().__init__()
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls = [
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[ft.Text("Diabeto", theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM, color="black")],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[ft.TextField(label="Pregnancies")],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[ft.TextField(label="Glucose")],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[ft.TextField(label="Blood Pressure")],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[ft.TextField(label="Skin Thickness")],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[ft.TextField(label="Insulin")],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[ft.TextField(label="BMI")],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[ft.TextField(label="Diabetes Pedigree Function")],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                border_radius=10,
                bgcolor=ft.colors.PRIMARY_CONTAINER,
                expand=True,
                margin=50,
                alignment=ft.alignment.center,
            )
        ]


async def main(page: ft.Page):
    page.views[0] = MainView()
    await page.update_async()


app.mount("/flet-app", flet_fastapi.app(main))
