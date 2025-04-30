import reflex as rx
from portfolio_python.Components.variables import color_primary, color_text, color_text_light, background, color_surface, trans_time, letter_bold, hover_primary, btn_color_secondary


def project_1():
    return rx.box(
        rx.image(src=f"/project1.png", width="100%", aspect_ratio="16 / 9", object_fit="cover"),
        rx.heading(
            f"Workshop Panel",
            size="6",
            padding="1rem 1.5rem 1rem 1.5rem",
            color=color_text(),
            letter_spacing=letter_bold,
        ),
        rx.text(
            "Web-based panel made in Reflex for managing automotive services.",
            padding="0 1.5rem 0 1.5rem",
            color=color_text_light(),
        ),
        rx.hstack(
            rx.badge(
                rx.text(f"Python", font_size="0.90rem", ),
                variant="solid",
                color="#FFFCF2",
                background_color=color_primary,
                box_sizing="border-box",
                border_radius="0.50rem",
                height="1rem",
                text_align="center",
                padding="1.10rem 0.95rem 1.10rem 0.95rem",

            ),
            rx.badge(
                rx.text(f"Minimalistic", font_size="0.90rem", ),
                variant="solid",
                color="#FFFCF2",
                background_color=color_primary,
                box_sizing="border-box",
                border_radius="0.50rem",
                height="1rem",
                text_align="center",
                padding="1.10rem 0.95rem 1.10rem 0.95rem",

            ),
            rx.badge(
                rx.text(f"Reflex", font_size="0.90rem", ),
                variant="solid",
                color="#FFFCF2",
                background_color=color_primary,
                box_sizing="border-box",
                border_radius="0.50rem",
                height="1rem",
                text_align="center",
                padding="1.10rem 0.95rem 1.10rem 0.95rem",
            ),
            padding="1rem 1.5rem 1rem 1.5rem",
        ),
        rx.hstack(
            rx.button(
                rx.text("View Project", size="4", color="#FFFCF2", weight="bold"),
                background_color=color_primary,
                border_radius="1rem",
                box_sizing="border-box",
                cursor="pointer",
                height="3.2rem",
                text_align="center",
                transition="all 0.3s ease-in-out",
                padding="1rem 1.25rem 1rem 1.25rem",
                _hover={
                    "background_color": f"{hover_primary}"
                },
                on_click=rx.redirect("https://github.com/wiktorbree/workshop_management_panel", is_external=True),
            ),
            rx.button(
                rx.text("Source Code", size="4", color=color_text(), weight="bold"),
                background_color=btn_color_secondary(),
                border_radius="1rem",
                box_sizing="border-box",
                cursor="pointer",
                height="3.2rem",
                text_align="center",
                transition="all 0.3s ease-in-out",
                padding="0.90rem 1.25rem 0.90rem 1.25rem",
                _hover={
                    "filter": "brightness(90%)",
                },
                on_click=rx.redirect("https://github.com/wiktorbree/workshop_management_panel", is_external=True),
            ),
            padding="0rem 1.5rem 0rem 1.5rem",
        ),
    )

def project_2():
    return rx.box(
        rx.image(src=f"/project2.png", width="100%", aspect_ratio="16 / 9", object_fit="cover"),
        rx.heading(
            f"Penguin Invasion",
            size="6",
            padding="1rem 1.5rem 1rem 1.5rem",
            color=color_text(),
            letter_spacing=letter_bold,
        ),
        rx.text(
            f"2D platformer made in Python using PyGame-CE library.",
            padding="0 1.5rem 0 1.5rem",
            color=color_text_light(),
        ),
        rx.hstack(
            rx.badge(
                rx.text(f"Python", font_size="0.90rem", ),
                variant="solid",
                color="#FFFCF2",
                background_color=color_primary,
                box_sizing="border-box",
                border_radius="0.50rem",
                height="1rem",
                text_align="center",
                padding="1.10rem 0.95rem 1.10rem 0.95rem",

            ),
            rx.badge(
                rx.text(f"Pixel Art", font_size="0.90rem", ),
                variant="solid",
                color="#FFFCF2",
                background_color=color_primary,
                box_sizing="border-box",
                border_radius="0.50rem",
                height="1rem",
                text_align="center",
                padding="1.10rem 0.95rem 1.10rem 0.95rem",

            ),
            rx.badge(
                rx.text(f"Game Dev", font_size="0.90rem", ),
                variant="solid",
                color="#FFFCF2",
                background_color=color_primary,
                box_sizing="border-box",
                border_radius="0.50rem",
                height="1rem",
                text_align="center",
                padding="1.10rem 0.95rem 1.10rem 0.95rem",
            ),
            padding="1rem 1.5rem 1rem 1.5rem",
        ),
        rx.hstack(
            rx.button(
                rx.text("View Project", size="4", color="#FFFCF2", weight="bold"),
                background_color=color_primary,
                border_radius="1rem",
                box_sizing="border-box",
                cursor="pointer",
                height="3.2rem",
                text_align="center",
                transition="all 0.3s ease-in-out",
                padding="1rem 1.25rem 1rem 1.25rem",
                _hover={
                    "background_color": f"{hover_primary}"
                },
                on_click=rx.redirect("https://wiktorbree.itch.io/penguin-invasion", is_external=True),
            ),
            rx.button(
                rx.text("Source Code", size="4", color=color_text(), weight="bold"),
                background_color=btn_color_secondary(),
                border_radius="1rem",
                box_sizing="border-box",
                cursor="pointer",
                height="3.2rem",
                text_align="center",
                transition="all 0.3s ease-in-out",
                padding="0.90rem 1.25rem 0.90rem 1.25rem",
                _hover={
                    "filter": "brightness(90%)",
                },
                on_click=rx.redirect("https://github.com/wiktorbree/penguin-invasion", is_external=True),
            ),
            padding="0rem 1.5rem 0rem 1.5rem",
        ),
    )

def project_3():
    return rx.box(
        rx.image(src=f"/project3.png", width="100%", aspect_ratio="16 / 9", object_fit="cover"),
        rx.heading(
            f"Arificial Life",
            size="6",
            padding="1rem 1.5rem 1rem 1.5rem",
            color=color_text(),
            letter_spacing=letter_bold,
        ),
        rx.text(
            f"Simple particle life simulation made in Python using PyGame.",
            padding="0 1.5rem 0 1.5rem",
            color=color_text_light(),
        ),
        rx.hstack(
            rx.badge(
                rx.text(f"Python", font_size="0.90rem", ),
                variant="solid",
                color="#FFFCF2",
                background_color=color_primary,
                box_sizing="border-box",
                border_radius="0.50rem",
                height="1rem",
                text_align="center",
                padding="1.10rem 0.95rem 1.10rem 0.95rem",

            ),
            rx.badge(
                rx.text(f"Minimalistic", font_size="0.90rem", ),
                variant="solid",
                color="#FFFCF2",
                background_color=color_primary,
                box_sizing="border-box",
                border_radius="0.50rem",
                height="1rem",
                text_align="center",
                padding="1.10rem 0.95rem 1.10rem 0.95rem",

            ),
            rx.badge(
                rx.text(f"Simulation", font_size="0.90rem", ),
                variant="solid",
                color="#FFFCF2",
                background_color=color_primary,
                box_sizing="border-box",
                border_radius="0.50rem",
                height="1rem",
                text_align="center",
                padding="1.10rem 0.95rem 1.10rem 0.95rem",
            ),
            padding="1rem 1.5rem 1rem 1.5rem",
        ),
        rx.hstack(
            rx.button(
                rx.text("View Project", size="4", color="#FFFCF2", weight="bold"),
                background_color=color_primary,
                border_radius="1rem",
                box_sizing="border-box",
                cursor="pointer",
                height="3.2rem",
                text_align="center",
                transition="all 0.3s ease-in-out",
                padding="1rem 1.25rem 1rem 1.25rem",
                _hover={
                    "background_color": f"{hover_primary}"
                },
                on_click=rx.redirect("https://github.com/wiktorbree/artificial-life-python", is_external=True),
            ),
            rx.button(
                rx.text("Source Code", size="4", color=color_text(), weight="bold"),
                background_color=btn_color_secondary(),
                border_radius="1rem",
                box_sizing="border-box",
                cursor="pointer",
                height="3.2rem",
                text_align="center",
                transition="all 0.3s ease-in-out",
                padding="0.90rem 1.25rem 0.90rem 1.25rem",
                _hover={
                    "filter": "brightness(90%)",
                },
                on_click=rx.redirect("https://github.com/wiktorbree/artificial-life-python", is_external=True),
            ),
            padding="0rem 1.5rem 0rem 1.5rem",
        ),
    )