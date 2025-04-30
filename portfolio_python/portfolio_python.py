import reflex as rx
from reflex import toggle_color_mode, mobile_only
from reflex.components.radix.themes.components.aspect_ratio import aspect_ratio
from portfolio_python.Components.navbar import navbar
from portfolio_python.Components.variables import color_primary, color_text, color_text_light, background, color_surface, trans_time, letter_bold, hover_primary, btn_color_secondary, btn_color_secondary_hover
import portfolio_python.Components.projects_list as pl
import portfolio_python.Components.skills_list as skl

from rxconfig import config

style = {
    "font-family": "Roboto, sans-serif",
    "scroll-behavior": "smooth",
}

class State(rx.State):
    """The app state."""

    ...

project_list = [pl.project_1(), pl.project_2(), pl.project_3()]
skills_list = [skl.programming_languages(), skl.tools(), skl.dev_expert(), skl.design(), skl.core_cs()]


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
                on_click=rx.scroll_to("get-in-touch"),
            ),
            spacing="5",
            justify="center",
            min_height="100vh",
        ),
        id="main",
    )

def projects():
    return rx.box(
        rx.heading("Projects", size="8", weight="bold", align="center", padding="0 0 4rem 0", letter_spacing=letter_bold,),
        rx.desktop_only(
            rx.grid(
                rx.foreach(
                    project_list,
                    lambda project: rx.card(
                        project,
                        variant="ghost",
                        background_color=color_surface(),
                        height="28rem",
                        box_shadow="lg",
                        width="100%",
                        margin="0",
                        padding="0",
                        overflow="hidden",
                        border_radius="25px",
                        transition="all 0.3s ease-in-out",
                        _hover={
                            "boxShadow": "0px 10px 20px rgba(0, 0, 0, 0.1)",
                            "transform": "translateY(-4px)",
                        }
                    ),
                ),
                columns="3",
                spacing="6",
                width="100%",
            ),
        ),
        rx.tablet_only(
            rx.vstack(
                rx.foreach(
                    project_list,
                    lambda project: rx.card(
                        project,
                        variant="ghost",
                        background_color=color_surface(),
                        height="31rem",
                        box_shadow="lg",
                        width="28rem",
                        margin="0",
                        padding="0",
                        overflow="hidden",
                        border_radius="25px",
                    )
                ),
                align="center",
            )
        ),
        rx.mobile_only(
            rx.vstack(
                rx.foreach(
                    project_list,
                    lambda project: rx.card(
                        project,
                        variant="ghost",
                        background_color=color_surface(),
                        height="55vh",
                        box_shadow="lg",
                        width="100%",
                        margin="0",
                        padding="0",
                        overflow="hidden",
                        border_radius="25px",
                    )
                ),
                align="center",
            )
        ),
        id="projects",
    )

def skills():
    return rx.box(
        rx.heading("Skills", size="8", weight="bold", align="center", padding="4rem 0 4rem 0", letter_spacing=letter_bold, ),
        rx.desktop_only(
            rx.grid(
                rx.foreach(
                    skills_list,
                    lambda skill: rx.card(
                        skill,
                        align_items="center",
                        variant="ghost",
                        background_color=color_surface(),
                        height="20rem",
                        box_shadow="lg",
                        width="100%",
                        margin="0",
                        padding="0",
                        overflow="hidden",
                        border_radius="25px",
                        transition="all 0.3s ease-in-out",
                        _hover={
                            "boxShadow": "0px 10px 20px rgba(0, 0, 0, 0.1)",
                            "transform": "translateY(-4px)",
                        }
                    )
                ),
                columns="5",
                spacing="6",
                width="100%",
            ),
        ),
        rx.tablet_only(
            rx.grid(
                rx.foreach(
                    skills_list,
                    lambda skill: rx.card(
                        skill,
                        align_items="center",
                        variant="ghost",
                        background_color=color_surface(),
                        height="40vh",
                        box_shadow="lg",
                        width="100%",
                        margin="0",
                        padding="0",
                        overflow="hidden",
                        border_radius="25px",
                        transition="all 0.3s ease-in-out",
                        _hover={
                            "boxShadow": "0px 10px 20px rgba(0, 0, 0, 0.1)",
                            "transform": "translateY(-4px)",
                        }
                    )
                ),
                columns="3",
                rows="2",
                spacing="6",
                width="100%",
            ),
        ),
        mobile_only(
            rx.vstack(
                rx.foreach(
                    skills_list,
                    lambda skill: rx.card(
                        skill,
                        align_items="center",
                        variant="ghost",
                        background_color=color_surface(),
                        height="30vh",
                        box_shadow="lg",
                        width="100%",
                        margin="0",
                        padding="0",
                        overflow="hidden",
                        border_radius="25px",
                        transition="all 0.3s ease-in-out",
                        _hover={
                            "boxShadow": "0px 10px 20px rgba(0, 0, 0, 0.1)",
                            "transform": "translateY(-4px)",
                        }
                    )
                )
            )
        ),
        id="skills",
    )

def get_in_touch():
    return rx.box(
        rx.heading("Get in Touch", size="8", weight="bold", align="center", padding="4rem 0 4rem 0", letter_spacing=letter_bold, ),
        rx.vstack(
            rx.button(
                rx.icon("mail", color=color_primary, margin="0rem 0.75rem 0rem 0rem",),
                rx.text("wiktor@bramerwiktor.pl", size="4", color=color_text(), ),
                background_color=color_surface(),
                border_radius="1rem",
                box_sizing="border-box",
                cursor="pointer",
                height="5rem",
                width="20rem",
                text_align="center",
                align="center",
                transition="all 0.3s ease-in-out",
                padding="2rem 1.5rem 2rem 1.5rem",
                _hover={
                    "filter": "brightness(90%)",
                    "boxShadow": "0px 10px 20px rgba(0, 0, 0, 0.1)",
                    "transform": "translateY(-4px)",
                },
                on_click=rx.redirect("mailto:wiktor@bramerwiktor.pl",),
            ),
            rx.button(
                rx.icon(tag="linkedin", color=color_primary, margin="0rem 0.75rem 0rem 0rem",),
                rx.text("LinkedIn", size="4", color=color_text(),),
                background_color=color_surface(),
                border_radius="1rem",
                box_sizing="border-box",
                cursor="pointer",
                height="5rem",
                width="20rem",
                text_align="center",
                align="center",
                transition="all 0.3s ease-in-out",
                padding="2rem 1.5rem 2rem 1.5rem",
                _hover={
                    "filter": "brightness(90%)",
                    "boxShadow": "0px 10px 20px rgba(0, 0, 0, 0.1)",
                    "transform": "translateY(-4px)",
                },
                on_click=rx.redirect("https://www.linkedin.com/in/wiktor-bramer-4697032ab/", is_external=True),
            ),
            align="center",
            padding_bottom="5rem",
        ),
        id="get-in-touch",
    )

def footer():
    return rx.el.footer(
        rx.hstack(
            rx.icon("github", size=30, stroke_width=2.5, cursor="pointer", on_click=rx.redirect("https://github.com/wiktorbree", is_external=True),),
            rx.icon("linkedin", size=30, stroke_width=2.5, cursor="pointer", on_click=rx.redirect("https://www.linkedin.com/in/wiktor-bramer-4697032ab/", is_external=True)),
            rx.color_mode_cond(
                light=rx.html("""
                    <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="30" height="30" viewBox="0,0,256,256">
                    <g fill="#000000" fill-rule="nonzero" stroke="none" stroke-width="none" stroke-linecap="butt" stroke-linejoin="none" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><path transform="scale(5.12,5.12)" d="M17.93359,6l9.3418,13.61719l11.75391,-13.61719h3.16992l-13.51758,15.66992l15.31836,22.33008h-12.01367l-10,-14.57812l-12.57617,14.57813h-3.17969l14.35156,-16.625l-14.66211,-21.375z" id="strokeMainSVG" stroke="#000000" stroke-width="2" stroke-linejoin="round"></path><g transform="scale(5.12,5.12)" stroke="none" stroke-width="1" stroke-linejoin="miter"><path d="M5.91992,6l14.66211,21.375l-14.35156,16.625h3.17969l12.57617,-14.57812l10,14.57813h12.01367l-15.31836,-22.33008l13.51758,-15.66992h-3.16992l-11.75391,13.61719l-9.3418,-13.61719zM9.7168,8h7.16406l23.32227,34h-7.16406z"></path></g></g>
                    </svg>
                """, cursor="pointer", on_click=rx.redirect("https://x.com/WiktorBree", is_external=True)),
                dark=rx.html("""
                  <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="30" height="30" viewBox="0,0,256,256">
                    <g fill="#ffffff" fill-rule="nonzero" stroke="none" stroke-width="none" stroke-linecap="butt" stroke-linejoin="none" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><path transform="scale(5.12,5.12)" d="M17.93359,6l9.3418,13.61719l11.75391,-13.61719h3.16992l-13.51758,15.66992l15.31836,22.33008h-12.01367l-10,-14.57812l-12.57617,14.57813h-3.17969l14.35156,-16.625l-14.66211,-21.375z" id="strokeMainSVG" stroke="#000000" stroke-width="2" stroke-linejoin="round"></path><g transform="scale(5.12,5.12)" stroke="none" stroke-width="1" stroke-linejoin="miter"><path d="M5.91992,6l14.66211,21.375l-14.35156,16.625h3.17969l12.57617,-14.57812l10,14.57813h12.01367l-15.31836,-22.33008l13.51758,-15.66992h-3.16992l-11.75391,13.61719l-9.3418,-13.61719zM9.7168,8h7.16406l23.32227,34h-7.16406z"></path></g></g>
                    </svg>
                  """, cursor="pointer", on_click=rx.redirect("https://x.com/WiktorBree", is_external=True)),

            ),
            align="center",
            justify="center",
            width="100%",
            gap="4",
        ),
        rx.container(rx.text("© 2025 Wiktor Bramer. All rights reserved.", color=color_text()), size="4",padding_top="2rem"),

        align="center",
        justify="center",
        width="100%",
        padding="2rem 0 2rem 0",
        background_color=color_surface(),
    )

@rx.page(route="/", title="Bramer Wiktor - CS Student")
def landing() -> rx.Component:

    return rx.box(
        navbar(),
        rx.container(
            main(),
            projects(),
            skills(),
            get_in_touch(),
            size="4",
        ),
        footer(),
        background_color=background(),
        transition=trans_time,
    )


app = rx.App(style=style)
app.add_page(landing)
