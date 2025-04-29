import reflex as rx
from reflex import toggle_color_mode
from reflex.components.radix.themes.components.aspect_ratio import aspect_ratio
from portfolio_python.Components.navbar import navbar
from portfolio_python.Components.variables import color_primary, color_text, color_text_light, background, color_surface, trans_time, letter_bold, hover_primary, btn_color_secondary, btn_color_secondary_hover
import portfolio_python.Components.projects_list as pl
from rxconfig import config

style = {
    "font-family": "Roboto, sans-serif",
    "scroll-behavior": "smooth",
}

class State(rx.State):
    """The app state."""

    ...

project_list = [pl.project_1(), pl.project_2(), pl.project_3()]


def main():
    return rx.box(
        rx.vstack(
            rx.heading(
                "Hi, I'm ",
                rx.text.span("Wiktor", color=color_primary, letter_spacing=letter_bold,),
                size="9",
                font_weight="900",
                color=color_text(),
                letter_spacing=letter_bold,

            ),
            rx.text(
                "Computer Science Student",
                color=color_text_light(),
                size="8",
                weight="bold",
                letter_spacing=letter_bold,
            ),
            rx.text(
                "I create games and apps in Python with a focus on user experience and minimalistic design",
                color=color_text_light(),
                font_size="1.20rem",
                max_width="600px",
            ),
            rx.button(
                rx.text("Get in touch", size="4", color="#f9fafb",),
                background_color=color_primary,
                border_radius="1rem",
                box_sizing="border-box",
                cursor="pointer",
                height="3.2rem",
                text_align="center",
                transition="all 0.3s ease-in-out",
                padding="2rem 1.5rem 2rem 1.5rem",
                _hover={
                    "background_color": f"{hover_primary}"
                },
            ),
            spacing="5",
            justify="center",
            min_height="100vh",
        ),
    )

def projects():
    return rx.box(
        rx.heading("Projects", size="8", weight="bold", align="center", padding="0 0 4rem 0", letter_spacing=letter_bold,),
        rx.grid(
            rx.foreach(
                project_list,
                lambda project: rx.card(
                    project,
                    variant="ghost",
                    background_color=color_surface(),
                    height="45vh",
                    box_shadow="lg",
                    width="100%",
                    margin="0",
                    padding="0",
                    overflow="hidden",
                    border_radius="25px",
                ),
            ),
            columns="3",
            spacing="6",
            width="100%",
        ),
    )

@rx.page(route="/")
def landing() -> rx.Component:

    return rx.box(
        navbar(),
        rx.container(
            main(),
            projects(),
            size="4",
        ),
        background_color=background(),
        transition=trans_time,
    )


app = rx.App(style=style)
app.add_page(landing)
