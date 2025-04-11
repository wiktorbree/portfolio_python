import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", href=url),
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
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Braker Wiktor",
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
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        padding="1rem",
        width="100%",
    )

class Main:
    def __init__(self):
        self.box = rx.box(width="100%")

        self.name = rx.vstack(
            rx.heading("Hi, I'm Wiktor!", size="9"),
            rx.text(
                "Computer Science Student",
                color="grey",
                size="8",
                weight="bold",
            ),
            rx.text(
                "I create games and apps in Python with a focus on user experience and minimalistic design",
                size="4",
            ),
            rx.button(
                "Get in touch"
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

    return rx.container(
        navbar(),
        main,

    )


app = rx.App()
app.add_page(landing)
