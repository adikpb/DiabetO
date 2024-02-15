import flet as ft
import flet_fastapi
import requests

from ..backend.main import *


class MainView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.dlg = ft.AlertDialog(title=ft.Text("HI"))
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls = [
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text(
                                    "DiabetO",
                                    theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                                    
                                )
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(expand=True),
                                ft.TextField(label="Pregnancies", expand=True),
                                ft.Row(expand=True),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(expand=True),
                                ft.TextField(label="Glucose", expand=True),
                                ft.Row(expand=True),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(expand=True),
                                ft.TextField(label="Blood Pressure", expand=True),
                                ft.Row(expand=True),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(expand=True),
                                ft.TextField(label="Skin Thickness", expand=True),
                                ft.Row(expand=True),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(expand=True),
                                ft.TextField(label="Insulin", expand=True),
                                ft.Row(expand=True),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(expand=True),
                                ft.TextField(label="BMI", expand=True),
                                ft.Row(expand=True),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(expand=True),
                                ft.TextField(
                                    label="Diabetes Pedigree Function", expand=True
                                ),
                                ft.Row(expand=True),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(expand=True),
                                ft.TextField(
                                    label="Age", expand=True
                                ),
                                ft.Row(expand=True),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[
                                ft.Row(expand=True),
                                ft.ElevatedButton(
                                    "Check!",
                                    icon=ft.icons.CHECK,
                                    icon_color="green",
                                    expand=True,
                                    on_click=self.post_req,
                                ),
                                ft.Row(expand=True),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                border_radius=50,
                bgcolor=ft.colors.TERTIARY_CONTAINER,
                expand=True,
                margin=50,
                alignment=ft.alignment.center,
            )
        ]

    async def open_dialog(self, e=None):
        self.page.dialog = self.dlg
        self.dlg.open = True
        await self.page.update_async()

    async def post_req(self, e=None):
        json = {
            "pregnancies": int(self.controls[0].content.controls[1].controls[1].value),
            "glucose": float(self.controls[0].content.controls[2].controls[1].value),
            "bloodpressure": float(self.controls[0].content.controls[3].controls[1].value),
            "skinthickness": float(self.controls[0].content.controls[4].controls[1].value),
            "insulin": float(self.controls[0].content.controls[5].controls[1].value),
            "bmi": float(self.controls[0].content.controls[6].controls[1].value),
            "diabetespedigreefunction": float(self.controls[0].content.controls[7].controls[1].value),
            "age": int(self.controls[0].content.controls[8].controls[1].value),
        }
        while True:
            try:
                response = requests.post("https://diabeto.onrender.com/predict", json=json)
                break
            except:
                pass
        print(response.json()["outcome"])
        self.dlg = ft.AlertDialog(title=ft.Text(value=f'You {"Have" if response.json()["outcome"] else "Don't Have"} Diabetes!'))
        await self.open_dialog()

    


async def main(page: ft.Page):
    page.views[0] = MainView(page)
    await page.update_async()


app.mount("/flet-app", flet_fastapi.app(main))
