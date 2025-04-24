import reflex as rx
from reflex import toggle_color_mode
from reflex.components.radix.themes.components.aspect_ratio import aspect_ratio
from portfolio_python.UI.navbar import navbar
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...



class Main:
    def __init__(self):
        self.box = rx.box(width="100%")

        self.name = rx.vstack(
            rx.heading(
                    "Hi, I'm ",
                    rx.text.span("Wiktor", color="#2563eb"),
                size="9",
            ),
            rx.text(
                "Computer Science Student",
                color="#6b7280",
                size="8",
                weight="bold",
            ),
            rx.text(
                "I create games and apps in Python with a focus on user experience and minimalistic design",
                color="#6b7280",
                size="4",
                weight="medium",
            ),
            rx.button(
                "Get in touch",
                background_color="#2563eb",
                size="4",
                radius="large",
                _hover={
                    "background_color": "#2055c9"
                },
            ),
            spacing="5",
            justify="center",
            min_height="100vh",
        ),

    def compile_desktop_component(self):
        return rx.desktop_only(
            self.name,
        )

    def compile_mobile_component(self):
        return rx.mobile_and_tablet(
            self.name,
        )

    def build(self):
        self.box.children = [self.compile_desktop_component(), self.compile_mobile_component()]
        return self.box

class Projects:
    def __init__(self):
        self.box = rx.box(width="100%")

        self.projects = rx.box(
            rx.heading("Projects", size="8", weight="bold", align="center", padding="0 0 4rem 0"),
            rx.grid(
            rx.foreach(
                rx.Var.range(3),
                lambda i: rx.card(
                    rx.image(src=f"/project{i+1}.png", width="100%", aspect_ratio="16 / 9", object_fit="cover"),
                    f"Project {i + 1}",
                    variant="ghost",
                    background_color="#212936",
                    height="45vh",
                    box_shadow="lg",
                    width="100%",
                    margin="0",
                    padding="0",
                    overflow="hidden",
                ),
            ),
            columns="3",
            spacing="6",
            width="100%",


        ))

    def compile_desktop_component(self):
        return rx.desktop_only(
            self.projects,
        )

    def compile_mobile_component(self):
        return rx.mobile_and_tablet(
            self.projects,
        )

    def build(self):
        self.box.children = [self.compile_desktop_component(), self.compile_mobile_component()]
        return self.box

@rx.page(route="/")
def landing() -> rx.Component:

    main: object = Main().build()
    projects: object = Projects().build()

    return rx.box(
        navbar(),
        rx.divider(),
        rx.container(
            main,
            projects,
        ),
        background_color=rx.color_mode_cond(
            light="#ffffff",
            dark="#111827",
        )
    )


app = rx.App()
app.add_page(landing)
