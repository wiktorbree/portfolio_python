import reflex as rx
from reflex import toggle_color_mode
from reflex.components.radix.themes.components.aspect_ratio import aspect_ratio
from portfolio_python.UI.navbar import navbar
from portfolio_python.UI.variables import color_primary, color_text, color_text_light, background, color_surface, trans_time, letter_bold
from rxconfig import config

style = {
    "font-family": "Roboto, sans-serif",
}

class State(rx.State):
    """The app state."""

    ...


def main():
    return rx.box(
        rx.vstack(
            rx.heading(
                "Hi, I'm ",
                rx.text.span("Wiktor", color=color_primary(), letter_spacing=letter_bold,),
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
                rx.text("Get in touch", size="4",),
                background_color=color_primary(),
                border_radius="1rem",
                box_sizing="border-box",
                cursor="pointer",
                height="3.2rem",
                text_align="center",
                transition="all 0.3s ease-in-out",
                padding="2rem 1.5rem 2rem 1.5rem",
                _hover={
                    "background_color": "#2055c9"
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
                rx.Var.range(3),
                lambda i: rx.card(
                    rx.image(src=f"/project{i + 1}.png", width="100%", aspect_ratio="16 / 9", object_fit="cover"),
                    rx.heading(
                        f"Project {i + 1}",
                        size="6",
                        padding="2rem",
                        color=color_text(),
                        letter_spacing=letter_bold,
                    ),
                    rx.text(
                        f"Test description in a project{i + 1}. Lorem ipsum dolor sit amet",
                        padding="0 2rem 0 2rem",
                        color=color_text_light(),
                    ),
                    rx.badge(f"Project{i + 1}"),
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
