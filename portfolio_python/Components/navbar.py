import reflex as rx
from pygments.styles.dracula import background
from portfolio_python.Components.variables import color_primary, color_text, color_text_light, color_surface, background, trans_time


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text,
                size="4",
                weight="medium",
                href=url,
                color=color_text(),
                _hover={"color": color_primary,
                        "transition": "all 0.1s ease-in-out",},
        ),
        text_decoration="none",
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Bramer Wiktor",
                        size="5",
                        font_weight="900",
                        letter_spacing="-1px",
                        color=color_text(),
                        position="relative",
                        background_image=f"linear-gradient(to right, {color_primary} 0%, {color_primary} 100%)",
                        background_position="0% 100%",
                        background_repeat="no-repeat",
                        background_size="0% 2px",
                        transition="background-size 0.3s ease-in-out, transform 0.3s ease-in-out",
                        cursor="pointer",
                        _hover={
                            "background_size": "100% 2px",
                            "transform": "translateY(-2px)",
                        },
                        on_click=lambda: rx.call_script("window.scrollTo({ top: 0, behavior: 'smooth' })"),
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("Project", "/#"),
                    navbar_link("Skills", "/#"),
                    navbar_link("Contact", "/#"),
                    rx.color_mode.button(color=color_text()),
                    justify="end",
                    spacing="5",
                    align_items="center",
                ),
                justify="between",
                align_items="center",
                background_color=background(),
                transition=trans_time,
            ),
            padding="1rem 2rem 1rem 2rem",
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Bramer Wiktor",
                        size="5",
                        font_weight="900",
                        letter_spacing="-1px",
                        color=color_text(),
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
                        background_color=background(),
                    ),
                    justify="end",
                    align_items="center",
                ),
                justify="between",
                align_items="center",
            ),
            padding="1rem 2rem 1rem 2rem",
        ),
        rx.divider(),
        width="100%",
        position="fixed",
        background_color=background(),
        transition=trans_time,
    )