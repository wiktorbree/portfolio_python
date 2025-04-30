import reflex as rx
from portfolio_python.Components.variables import color_primary, color_text, color_text_light, background, color_surface, trans_time, letter_bold, hover_primary, btn_color_secondary, btn_color_secondary_hover

def programming_languages():
    return rx.vstack(
        rx.heading(
            "Programming Languages",
            size="4",
            padding="2rem 1.5rem 1rem 1.5rem",
            color=color_text(),
            letter_spacing=letter_bold,
            align="center",
        ),
        rx.text(
            "Python",
            color=color_text_light(),
            padding="0rem 1.5rem 1rem 1.5rem",
        ),
        rx.text(
            "Swift (Learning)",
            color=color_text_light(),
            padding="0rem 1.5rem 1rem 1.5rem",
        ),
        align="center",
    ),

def tools():
    return rx.vstack(
        rx.heading(
            "Tools & Frameworks",
            size="4",
            padding="2rem 1.5rem 1rem 1.5rem",
            color=color_text(),
            letter_spacing=letter_bold,
            align="center",
        ),
        rx.text(
            "PyGame-CE",
            color=color_text_light(),
            padding="0rem 1.5rem 1rem 1.5rem",
        ),
        rx.text(
            "Git",
            color=color_text_light(),
            padding="0rem 1.5rem 1rem 1.5rem",
        ),
        rx.text(
            "Terminal",
            color=color_text_light(),
            padding="0rem 1.5rem 1rem 1.5rem",
        ),
        align="center",
    ),

def dev_expert():
    return rx.vstack(
        rx.heading(
            "Development Expertise",
            size="4",
            padding="2rem 1.5rem 1rem 1.5rem",
            color=color_text(),
            letter_spacing=letter_bold,
            align="center",
        ),
        rx.text(
            "2D Game Development",
            color=color_text_light(),
            padding="0rem 1.5rem 1rem 1.5rem",
            align="center",
        ),
        rx.text(
            "Web Development (Reflex)",
            color=color_text_light(),
            padding="0rem 1.5rem 1rem 1.5rem",
            align="center",
        ),
        align="center",
    ),

def design():
    return rx.vstack(
        rx.heading(
            "Design & Methodology",
            size="4",
            padding="2rem 1.5rem 1rem 1.5rem",
            color=color_text(),
            letter_spacing=letter_bold,
            align="center",
        ),
        rx.text(
            "UI/UX Design (Learning)",
            color=color_text_light(),
            padding="0rem 1.5rem 1rem 1.5rem",
            align="center",
        ),
        rx.text(
            "Agile Workflow",
            color=color_text_light(),
            padding="0rem 1.5rem 1rem 1.5rem",
            align="center",
        ),
        rx.text(
            "Object-Oriented Programming (OOP)",
            color=color_text_light(),
            padding="0rem 1.5rem 1rem 1.5rem",
            align="center",
        ),
        align="center",
    ),

def core_cs():
    return rx.vstack(
        rx.heading(
            "Core CS",
            size="4",
            padding="2rem 1.5rem 1rem 1.5rem",
            color=color_text(),
            letter_spacing=letter_bold,
            align="center",
        ),
        rx.text(
            "Data Structures",
            color=color_text_light(),
            padding="0rem 1.5rem 1rem 1.5rem",
            align="center",
        ),
        rx.text(
            "Problem-Solving",
            color=color_text_light(),
            padding="0rem 1.5rem 1rem 1.5rem",
            align="center",
        ),
        rx.text(
            "Optimization",
            color=color_text_light(),
            padding="0rem 1.5rem 1rem 1.5rem",
            align="center",
        ),
        align="center",
    ),