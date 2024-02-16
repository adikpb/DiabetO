import aiohttp
import flet as ft
import flet_fastapi

from ..backend.main import *


class MainView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.session = aiohttp.ClientSession()
        self.dlg = ft.AlertDialog(title=ft.Text("HI"))

        self.gender = ft.Row(
            [
                ft.Text("Gender"),
                ft.SegmentedButton(
                    segments=[
                        ft.Segment(value="1", label=ft.Text("Male")),
                        ft.Segment(value="2", label=ft.Text("Female")),
                        ft.Segment(value="0", label=ft.Text("Rather Not Say")),
                    ],
                    allow_empty_selection=True,
                    expand=True,
                ),
            ],
            expand=True,
        )
        self.age = ft.Row([ft.TextField(label="Age", expand=True)], expand=True)
        self.hypertension = ft.Row(
            [ft.Switch(label="Hypertension", label_position=ft.LabelPosition.LEFT)],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
        )
        self.heart_disease = ft.Row(
            [ft.Switch(label="Heart Disease", label_position=ft.LabelPosition.LEFT)],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
        )
        self.smoking_history = ft.Row(
            [
                ft.Text("Smoking History"),
                ft.SegmentedButton(
                    segments=[
                        ft.Segment(value="0", label=ft.Text("Never")),
                        ft.Segment(value="1", label=ft.Text("Current")),
                        ft.Segment(value="2", label=ft.Text("Former")),
                        ft.Segment(value="3", label=ft.Text("No Info")),
                    ],
                    allow_empty_selection=True,
                    expand=True,
                ),
            ],
            expand=True,
        )
        self.bmi = ft.Row([ft.TextField(label="BMI", expand=True)], expand=True)
        self.HbA1c_level = ft.Row(
            [ft.TextField(label="HbA1c Level", expand=True)], expand=True
        )
        self.blood_glucose_level = ft.Row(
            [
                ft.TextField(
                    label="Blood Glucose Level",
                    input_filter=ft.NumbersOnlyInputFilter(),
                    expand=True,
                )
            ],
            expand=True,
        )

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
                    ]
                    + [
                        ft.Row(
                            controls=[
                                ft.Row(expand=True),
                                i,
                                ft.Row(expand=True),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                        for i in (
                            self.gender,
                            self.age,
                        )
                    ]
                    + [
                        ft.Row(
                            controls=[
                                ft.Row(expand=True),
                                self.hypertension,
                                self.heart_disease,
                                ft.Row(expand=True),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ]
                    + [
                        ft.Row(
                            controls=[
                                ft.Row(expand=True),
                                i,
                                ft.Row(expand=True),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                        for i in (
                            self.smoking_history,
                            self.bmi,
                            self.HbA1c_level,
                            self.blood_glucose_level,
                        )
                    ]
                    + [
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
            "gender": int(list(self.gender.controls[1].selected)[0]),
            "age": float(self.age.controls[0].value),
            "hypertension": int(self.hypertension.controls[0].value),
            "heart_diseases": int(self.heart_disease.controls[0].value),
            "smoking_history": int(list(self.smoking_history.controls[1].selected)[0]),
            "bmi": float(self.bmi.controls[0].value),
            "HbA1c_level": float(self.HbA1c_level.controls[0].value),
            "blood_glucose_level": int(self.blood_glucose_level.controls[0].value),
        }
        print(json)
        self.page.overlay.append(
            ft.Container(
                content=ft.ProgressRing(),
                expand=True,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK,
                opacity=0.60,
            )
        )
        await self.page.update_async()
        async with self.session.post(
            "https://diabeto.onrender.com/predict", json=json
        ) as response:
            response = await response.json()
            if response["outcome"]:
                self.dlg = ft.AlertDialog(title=ft.Text(value="You Have Diabetes!"))
            else:
                self.dlg = ft.AlertDialog(
                    title=ft.Text(value="You Don't Have Diabetes!")
                )
        self.page.overlay.pop()
        await self.page.update_async()
        await self.open_dialog()


async def main(page: ft.Page):
    page.views[0] = MainView(page)
    await page.update_async()


app.mount("/flet-app", flet_fastapi.app(main))
