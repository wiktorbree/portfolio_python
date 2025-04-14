import reflex as rx
from pygments.styles.dracula import background
from reflex import toggle_color_mode

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", href=url, ),
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Bramer Wiktor",
                        size="7",
                        weight="bold",
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("Project", "/#"),
                    navbar_link("Skills", "/#"),
                    navbar_link("Contact", "/#"),
                    rx.color_mode.button(),
                    justify="end",
                    spacing="5",
                    align_items="center",
                ),
                justify="between",
                align_items="center",
            ),
            padding="1rem 15rem 1rem 15rem",
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Bramer Wiktor",
                        size="6",
                        weight="bold",
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("Project"),
                        rx.menu.item("Skills"),
                        rx.menu.item("Contact"),
                        rx.menu.item(rx.color_mode.button()),
                        background_color=rx.color_mode_cond(
                            light="#f1f1f1",
                            dark="#111827",
                        )
                    ),
                    justify="end",
                    align_items="center",
                ),
                justify="between",
                align_items="center",
            ),
            padding="1rem 2rem 1rem 2rem",
        ),
        width="100%",
    )

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
            min_height="85vh",
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
        pass

@rx.page(route="/")
def landing() -> rx.Component:

    main: object = Main().build()

    return rx.box(
        navbar(),
        rx.divider(),
        rx.container(
            main,
        ),
        background_color=rx.color_mode_cond(
            light="#ffffff",
            dark="#111827",
        )
    )


app = rx.App()
app.add_page(landing)
